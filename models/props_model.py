"""
Player props prediction model.

Predicts per-map stat lines (kills, deaths, HS%, ACS, etc.) for individual players.
Uses LightGBM regression with quantile outputs to estimate over/under probabilities.

For a prop line like "PlayerX kills O/U 18.5":
  - Predict E[kills] and variance
  - P(kills > 18.5) = 1 - CDF(18.5) under a fitted distribution
"""
import pickle
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy import stats
from loguru import logger
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit
import lightgbm as lgb
import optuna
from optuna.samplers import TPESampler

from config import RANDOM_STATE, CV_FOLDS, MODELS_DIR

optuna.logging.set_verbosity(optuna.logging.WARNING)


PLAYER_FEATURE_COLS = [
    # Player recent form
    "ew_kills",
    "ew_deaths",
    "kills_last5",
    "kills_last10",
    "kills_last20",
    "deaths_last5",
    "deaths_last10",
    "ew_rating",
    "ew_adr",
    "ew_kast",
    "ew_hs_pct",
    "kills_trend",
    "deaths_trend",
    # Map-specific form
    "map_ew_kills",
    "map_kills_last5",
    "map_kills_last10",
    "map_ew_rating",
    # Opponent quality
    "opp_elo",
    "opp_ew_win_rate",
    "opp_avg_deaths_allowed",   # how many kills opponents typically get vs this team
    # Match context
    "is_lan",
    "best_of",
    "map_ct_sided",             # 1 = CT-favored map (Inferno, Cache), -1 = T-favored
    # Role
    "is_awper",
    "is_entry",
    "is_igl",
]

# CT/T bias per map (rough historical average, round differential CT - T)
MAP_SIDE_BIAS = {
    "mirage": -1,
    "inferno": 2,
    "nuke": 4,
    "overpass": 1,
    "vertigo": 0,
    "ancient": -1,
    "anubis": 0,
    "dust2": -2,
    "cache": 0,
    "train": 1,
}


@dataclass
class PropPrediction:
    player_id: int
    player_name: str
    stat: str
    expected_value: float
    std_dev: float
    line: float
    over_prob: float
    under_prob: float
    push_prob: float


class PropsModel:
    """
    Regression model for a single player stat (e.g. 'kills').
    Train a separate instance per stat (kills, deaths, hs_pct, etc.).
    """

    def __init__(self, stat: str, game: str = "cs2"):
        self.stat = stat
        self.game = game
        self.model: Optional[lgb.LGBMRegressor] = None
        self.std_model: Optional[lgb.LGBMRegressor] = None  # predicts residual std
        self.feature_cols: list[str] = []
        self.best_params: dict = {}
        self.metrics: dict = {}

    # ------------------------------------------------------------------
    # Data preparation
    # ------------------------------------------------------------------

    def _select_features(self, df: pd.DataFrame) -> list[str]:
        return [c for c in PLAYER_FEATURE_COLS if c in df.columns]

    def _prepare(self, df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        X = df[self.feature_cols].fillna(0).values
        y = df[self.stat].values.astype(float)
        return X, y

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def tune(self, df: pd.DataFrame, n_trials: int = 40) -> dict:
        df = df.dropna(subset=[self.stat])
        self.feature_cols = self._select_features(df)
        X, y = self._prepare(df)
        tscv = TimeSeriesSplit(n_splits=CV_FOLDS)

        def objective(trial):
            params = {
                "num_leaves": trial.suggest_int("num_leaves", 20, 100),
                "max_depth": trial.suggest_int("max_depth", 3, 8),
                "learning_rate": trial.suggest_float("lr", 0.01, 0.2, log=True),
                "n_estimators": trial.suggest_int("n_estimators", 100, 500),
                "min_child_samples": trial.suggest_int("min_child_samples", 5, 30),
                "subsample": trial.suggest_float("subsample", 0.6, 1.0),
                "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
                "reg_alpha": trial.suggest_float("reg_alpha", 0, 1),
                "reg_lambda": trial.suggest_float("reg_lambda", 0, 2),
                "random_state": RANDOM_STATE,
                "verbose": -1,
            }
            maes = []
            for train_idx, val_idx in tscv.split(X):
                m = lgb.LGBMRegressor(**params)
                m.fit(X[train_idx], y[train_idx])
                preds = m.predict(X[val_idx])
                maes.append(mean_absolute_error(y[val_idx], preds))
            return np.mean(maes)

        study = optuna.create_study(direction="minimize", sampler=TPESampler(seed=RANDOM_STATE))
        study.optimize(objective, n_trials=n_trials, show_progress_bar=False)
        self.best_params = {k: v for k, v in study.best_params.items() if k != "lr"}
        self.best_params["learning_rate"] = study.best_params.get("lr", 0.05)
        logger.info(f"[{self.stat}] Best MAE: {study.best_value:.3f}")
        return self.best_params

    def fit(self, df: pd.DataFrame) -> "PropsModel":
        df = df.dropna(subset=[self.stat]).sort_values("match_date")
        self.feature_cols = self._select_features(df)
        X, y = self._prepare(df)

        params = {**self.best_params, "random_state": RANDOM_STATE, "verbose": -1}
        if not params.get("n_estimators"):
            params.update({"n_estimators": 300, "max_depth": 5, "learning_rate": 0.05})

        self.model = lgb.LGBMRegressor(**params)
        self.model.fit(X, y)

        # Spread model, fitted on out-of-fold absolute residuals (each fold's model only saw
        # earlier rows). In-sample residuals of a boosted model are much smaller than the
        # errors it makes on new matches, which made every over/under look more certain
        # than it was. sqrt(pi/2) turns a mean absolute error into a normal standard deviation.
        oof = np.full(len(y), np.nan)
        for train_idx, val_idx in TimeSeriesSplit(n_splits=CV_FOLDS).split(X):
            m = lgb.LGBMRegressor(**params)
            m.fit(X[train_idx], y[train_idx])
            oof[val_idx] = np.abs(y[val_idx] - m.predict(X[val_idx]))
        ok = ~np.isnan(oof)
        self.std_model = lgb.LGBMRegressor(**{**params, "n_estimators": 100})
        self.std_model.fit(X[ok], oof[ok] * np.sqrt(np.pi / 2))
        self.metrics["oof_mae"] = float(np.nanmean(oof))

        preds = self.model.predict(X)
        self.metrics["train_mae"] = mean_absolute_error(y, preds)
        self.metrics["train_rmse"] = np.sqrt(mean_squared_error(y, preds))
        logger.info(f"[{self.stat}] Train MAE={self.metrics['train_mae']:.3f} RMSE={self.metrics['train_rmse']:.3f}")
        return self

    def walk_forward_eval(self, df: pd.DataFrame, n_splits: int = CV_FOLDS) -> dict:
        df = df.dropna(subset=[self.stat]).sort_values("match_date").reset_index(drop=True)
        self.feature_cols = self._select_features(df)
        X, y = self._prepare(df)
        tscv = TimeSeriesSplit(n_splits=n_splits)

        all_preds, all_true = [], []
        for train_idx, val_idx in tscv.split(X):
            m = lgb.LGBMRegressor(
                **{**self.best_params, "random_state": RANDOM_STATE, "verbose": -1}
            )
            m.fit(X[train_idx], y[train_idx])
            all_preds.extend(m.predict(X[val_idx]))
            all_true.extend(y[val_idx])

        metrics = {
            "cv_mae": mean_absolute_error(all_true, all_preds),
            "cv_rmse": np.sqrt(mean_squared_error(all_true, all_preds)),
        }
        self.metrics.update(metrics)
        logger.info(f"[{self.stat}] Walk-forward: {metrics}")
        return metrics

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def predict_expected(self, feature_dict: dict) -> tuple[float, float]:
        """Returns (expected_value, predicted_std_dev)."""
        df = pd.DataFrame([feature_dict])
        for col in self.feature_cols:
            if col not in df.columns:
                df[col] = 0
        X = df[self.feature_cols].values
        expected = float(self.model.predict(X)[0])
        std = float(self.std_model.predict(X)[0]) if self.std_model else expected * 0.25
        std = max(std, 0.5)  # floor
        return expected, std

    def over_under_prob(
        self, feature_dict: dict, line: float
    ) -> PropPrediction:
        """
        Compute P(stat > line) and P(stat < line) using a normal approximation.
        For kill counts, a negative-binomial would be more accurate but
        normal is a reasonable first approximation.
        """
        expected, std = self.predict_expected(feature_dict)

        # Normal CDF
        z = (line - expected) / std
        under_prob = float(stats.norm.cdf(z))
        over_prob = 1.0 - under_prob

        # Half-point push buffer (most books use .5 lines so push = 0)
        push_prob = 0.0
        if line == int(line):
            # exact integer line — estimate push probability at that point
            push_prob = float(stats.norm.pdf(z) / std)
            over_prob = (1.0 - under_prob - push_prob)

        player_id = int(feature_dict.get("player_id", 0))
        player_name = str(feature_dict.get("player_name", ""))

        return PropPrediction(
            player_id=player_id,
            player_name=player_name,
            stat=self.stat,
            expected_value=expected,
            std_dev=std,
            line=line,
            over_prob=over_prob,
            under_prob=under_prob,
            push_prob=push_prob,
        )

    def feature_importance(self) -> pd.DataFrame:
        if self.model is None:
            raise RuntimeError("Model not trained")
        imp = self.model.feature_importances_
        return (
            pd.DataFrame({"feature": self.feature_cols, "importance": imp})
            .sort_values("importance", ascending=False)
            .reset_index(drop=True)
        )

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, path: Optional[Path] = None):
        path = path or MODELS_DIR / f"{self.game}_props_{self.stat}.pkl"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self, f)
        logger.info(f"Props model [{self.stat}] saved to {path}")

    @classmethod
    def load(cls, path: Path) -> "PropsModel":
        with open(path, "rb") as f:
            return pickle.load(f)


# ---------------------------------------------------------------------------
# Props feature builder (player-level, requires rolling stats already computed)
# ---------------------------------------------------------------------------

def build_player_prop_features(
    player_rolling: dict,          # output of rolling_stats.compute_player_rolling_stats
    map_player_rolling: dict,      # same but map-specific
    opponent_team_stats: dict,     # output of rolling_stats.compute_team_rolling_stats
    opponent_elo: float,
    is_lan: bool,
    best_of: int,
    map_name: Optional[str] = None,
    player_role: Optional[str] = None,
) -> dict:
    feats = {}

    for key, val in player_rolling.items():
        if key != "player_id":
            feats[key] = val

    for key, val in map_player_rolling.items():
        if key not in ("player_id", "maps_played"):
            feats[f"map_{key}"] = val

    feats["opp_elo"] = opponent_elo
    feats["opp_ew_win_rate"] = opponent_team_stats.get("ew_win_rate", 0.5)

    # Opponent defense quality: average deaths they allow (= opp kills)
    feats["opp_avg_deaths_allowed"] = opponent_team_stats.get("ew_round_diff", 0.0)

    feats["is_lan"] = int(is_lan)
    feats["best_of"] = best_of

    if map_name:
        from models.props_model import MAP_SIDE_BIAS
        feats["map_ct_sided"] = MAP_SIDE_BIAS.get(map_name.lower(), 0)

    if player_role:
        feats["is_awper"] = int(player_role.lower() in ("awper", "awp"))
        feats["is_entry"] = int(player_role.lower() in ("entry", "entry fragger"))
        feats["is_igl"] = int(player_role.lower() == "igl")
    else:
        feats["is_awper"] = feats["is_entry"] = feats["is_igl"] = 0

    return feats
