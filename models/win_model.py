"""
Match/map winner prediction model.

Architecture:
  - XGBoost classifier trained on historical match features
  - Platt scaling (LogisticRegression) for calibration
  - Optuna hyperparameter tuning
  - Walk-forward validation (no future leakage)
"""
import json
import pickle
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
from loguru import logger
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, brier_score_loss, log_loss, roc_auc_score
)
from sklearn.model_selection import TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
import optuna
from optuna.samplers import TPESampler

from config import RANDOM_STATE, CV_FOLDS, MODELS_DIR, MIN_MATCHES_FOR_PREDICTION

optuna.logging.set_verbosity(optuna.logging.WARNING)


FEATURE_COLS_CORE = [
    "elo_diff_overall",
    "elo_win_prob_t1",
    "t1_ew_win_rate",
    "t2_ew_win_rate",
    "wr_diff_last5",
    "wr_diff_last10",
    "wr_diff_last20",
    "rd_diff_last5",
    "rd_diff_last10",
    "t1_total_maps",
    "t2_total_maps",
    "h2h_ew_win_rate_t1",
    "h2h_maps",
    "is_lan",
    "best_of",
]

MAP_FEATURE_COLS = [
    "elo_diff_map",
    "elo_win_prob_t1_map",
    "map_pool_wr_diff",
    "t1_pool_wr",
    "t2_pool_wr",
    "t1_pool_rd",
    "t2_pool_rd",
]


class WinModel:
    """
    Binary classifier: P(team1 wins the match).
    Can also be used for map-level prediction by passing map features.
    """

    def __init__(self, model_name: str = "cs2_win"):
        self.model_name = model_name
        self.model: Optional[xgb.XGBClassifier] = None
        self.calibrator: Optional[LogisticRegression] = None
        self.feature_cols: list[str] = []
        self.best_params: dict = {}
        self.metrics: dict = {}

    # ------------------------------------------------------------------
    # Training
    # ------------------------------------------------------------------

    def _select_features(self, df: pd.DataFrame) -> list[str]:
        candidates = FEATURE_COLS_CORE + MAP_FEATURE_COLS
        return [c for c in candidates if c in df.columns]

    def _prepare(self, df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        X = df[self.feature_cols].fillna(df[self.feature_cols].median()).values
        y = df["label"].values.astype(int)
        return X, y

    def tune(self, df: pd.DataFrame, n_trials: int = 50) -> dict:
        """Optuna hyperparameter search with time-series CV."""
        self.feature_cols = self._select_features(df)
        X, y = self._prepare(df)
        tscv = TimeSeriesSplit(n_splits=CV_FOLDS)

        def objective(trial):
            params = {
                "n_estimators": trial.suggest_int("n_estimators", 100, 600),
                "max_depth": trial.suggest_int("max_depth", 3, 8),
                "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
                "subsample": trial.suggest_float("subsample", 0.5, 1.0),
                "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
                "min_child_weight": trial.suggest_int("min_child_weight", 1, 10),
                "gamma": trial.suggest_float("gamma", 0, 5),
                "reg_alpha": trial.suggest_float("reg_alpha", 0, 2),
                "reg_lambda": trial.suggest_float("reg_lambda", 0.5, 3),
                "random_state": RANDOM_STATE,
                "eval_metric": "logloss",
                "use_label_encoder": False,
            }
            scores = []
            for train_idx, val_idx in tscv.split(X):
                clf = xgb.XGBClassifier(**params)
                clf.fit(X[train_idx], y[train_idx], verbose=False)
                probs = clf.predict_proba(X[val_idx])[:, 1]
                scores.append(log_loss(y[val_idx], probs))
            return np.mean(scores)

        study = optuna.create_study(
            direction="minimize",
            sampler=TPESampler(seed=RANDOM_STATE),
        )
        study.optimize(objective, n_trials=n_trials, show_progress_bar=False)
        self.best_params = study.best_params
        logger.info(f"Best log-loss: {study.best_value:.4f} | params: {self.best_params}")
        return self.best_params

    def fit(self, df: pd.DataFrame, calibrate: bool = True) -> "WinModel":
        """Train on full dataset (after tuning)."""
        self.feature_cols = self._select_features(df)
        X, y = self._prepare(df)

        params = {**self.best_params, "random_state": RANDOM_STATE}
        if not params:
            params = {
                "n_estimators": 300,
                "max_depth": 5,
                "learning_rate": 0.05,
                "subsample": 0.8,
                "colsample_bytree": 0.8,
                "random_state": RANDOM_STATE,
            }

        self.model = xgb.XGBClassifier(**params)
        self.model.fit(X, y)

        if calibrate:
            raw_probs = self.model.predict_proba(X)[:, 1]
            self.calibrator = LogisticRegression()
            self.calibrator.fit(raw_probs.reshape(-1, 1), y)
            logger.info("Platt scaling calibration fitted")

        train_probs = self.predict_proba(df)
        self.metrics["train_logloss"] = log_loss(y, train_probs)
        self.metrics["train_auc"] = roc_auc_score(y, train_probs)
        self.metrics["train_brier"] = brier_score_loss(y, train_probs)
        logger.info(f"Train metrics: {self.metrics}")
        return self

    def walk_forward_eval(self, df: pd.DataFrame, n_splits: int = CV_FOLDS) -> dict:
        """Walk-forward (time-series) evaluation — no future leakage."""
        self.feature_cols = self._select_features(df)
        df_sorted = df.sort_values("match_date").reset_index(drop=True)
        X, y = self._prepare(df_sorted)
        tscv = TimeSeriesSplit(n_splits=n_splits)

        all_probs, all_labels = [], []
        for fold, (train_idx, val_idx) in enumerate(tscv.split(X)):
            clf = xgb.XGBClassifier(
                **{**self.best_params, "random_state": RANDOM_STATE}
            )
            clf.fit(X[train_idx], y[train_idx])
            probs = clf.predict_proba(X[val_idx])[:, 1]
            all_probs.extend(probs)
            all_labels.extend(y[val_idx])

        metrics = {
            "cv_log_loss": log_loss(all_labels, all_probs),
            "cv_auc": roc_auc_score(all_labels, all_probs),
            "cv_brier": brier_score_loss(all_labels, all_probs),
            "cv_accuracy": accuracy_score(all_labels, [1 if p > 0.5 else 0 for p in all_probs]),
        }
        self.metrics.update(metrics)
        logger.info(f"Walk-forward eval: {metrics}")
        return metrics

    # ------------------------------------------------------------------
    # Inference
    # ------------------------------------------------------------------

    def predict_proba(self, df: pd.DataFrame) -> np.ndarray:
        """Return P(team1 wins) for each row."""
        X = df[self.feature_cols].fillna(df[self.feature_cols].median()).values
        raw = self.model.predict_proba(X)[:, 1]
        if self.calibrator is not None:
            return self.calibrator.predict_proba(raw.reshape(-1, 1))[:, 1]
        return raw

    def predict_single(self, feature_dict: dict) -> float:
        """Predict a single match. Returns P(team1 wins)."""
        df = pd.DataFrame([feature_dict])
        for col in self.feature_cols:
            if col not in df.columns:
                df[col] = 0.5
        return float(self.predict_proba(df)[0])

    def feature_importance(self) -> pd.DataFrame:
        if self.model is None:
            raise RuntimeError("Model not trained yet")
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
        path = path or MODELS_DIR / f"{self.model_name}.pkl"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "wb") as f:
            pickle.dump(self, f)
        logger.info(f"Model saved to {path}")

    @classmethod
    def load(cls, path: Path) -> "WinModel":
        with open(path, "rb") as f:
            return pickle.load(f)
