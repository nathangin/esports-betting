"""Team ratings from match results, computed strictly in time order.

Every match gets the ratings as they stood *before* it was played (no look-ahead: the old
app used each team's final rating as a training feature). Ratings are kept per game and
keyed by Kalshi's stable competitor id.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class EloConfig:
    k: float = 32.0             # base update size (400-point scale)
    k_new_boost: float = 2.0    # newer teams move faster: K * (1 + boost / (1 + games))
    initial: float = 1500.0
    decay_days: float = 120.0   # ratings drift back toward the mean when a team is idle
    decay_frac: float = 0.25    # share of the gap closed after decay_days idle


@dataclass
class Elo:
    cfg: EloConfig = field(default_factory=EloConfig)
    rating: dict = field(default_factory=dict)
    games: dict = field(default_factory=dict)
    last: dict = field(default_factory=dict)

    def _get(self, team: str, when: pd.Timestamp) -> float:
        r = self.rating.get(team, self.cfg.initial)
        last = self.last.get(team)
        if last is not None and self.cfg.decay_days > 0:
            idle = (when - last).total_seconds() / 86400.0
            if idle > 0:
                keep = (1 - self.cfg.decay_frac) ** (idle / self.cfg.decay_days)
                r = self.cfg.initial + (r - self.cfg.initial) * keep
        return r

    def expected(self, a: str, b: str, when: pd.Timestamp) -> float:
        ra, rb = self._get(a, when), self._get(b, when)
        return 1.0 / (1.0 + 10 ** ((rb - ra) / 400.0))

    def snapshot(self, a: str, b: str, when: pd.Timestamp) -> dict:
        ra, rb = self._get(a, when), self._get(b, when)
        return {"elo_a": ra, "elo_b": rb, "elo_diff": ra - rb, "games_a": self.games.get(a, 0),
                "games_b": self.games.get(b, 0), "p_elo": 1.0 / (1.0 + 10 ** ((rb - ra) / 400.0))}

    def update(self, a: str, b: str, score_a: float, when: pd.Timestamp) -> None:
        ra, rb = self._get(a, when), self._get(b, when)
        ea = 1.0 / (1.0 + 10 ** ((rb - ra) / 400.0))
        ka = self.cfg.k * (1 + self.cfg.k_new_boost / (1 + self.games.get(a, 0)))
        kb = self.cfg.k * (1 + self.cfg.k_new_boost / (1 + self.games.get(b, 0)))
        self.rating[a] = ra + ka * (score_a - ea)
        self.rating[b] = rb + kb * ((1 - score_a) - (1 - ea))
        for t in (a, b):
            self.games[t] = self.games.get(t, 0) + 1
            self.last[t] = when


def pre_match_features(matches: pd.DataFrame, cfgs: dict[str, EloConfig] | None = None,
                       form_n: int = 5) -> pd.DataFrame:
    """For every match (sorted by start time), ratings and form as of just before it.

    matches: event_ticker, game, start_time, comp_a, comp_b, winner ('A'/'B'/None)
    """
    cfgs = cfgs or {}
    m = matches.sort_values("start_time").reset_index(drop=True)
    elos: dict[str, Elo] = {}
    resid: dict[tuple, list] = {}
    rows = []
    for r in m.itertuples(index=False):
        g = r.game
        elo = elos.setdefault(g, Elo(cfgs.get(g, cfgs.get("default", EloConfig()))))
        when = pd.Timestamp(r.start_time)
        snap = elo.snapshot(r.comp_a, r.comp_b, when)
        fa = resid.get((g, r.comp_a), [])[-form_n:]
        fb = resid.get((g, r.comp_b), [])[-form_n:]
        snap["form_a"] = float(np.mean(fa)) if fa else 0.0
        snap["form_b"] = float(np.mean(fb)) if fb else 0.0
        snap["event_ticker"] = r.event_ticker
        rows.append(snap)
        if r.winner in ("A", "B"):
            s = 1.0 if r.winner == "A" else 0.0
            exp = snap["p_elo"]
            resid.setdefault((g, r.comp_a), []).append(s - exp)
            resid.setdefault((g, r.comp_b), []).append((1 - s) - (1 - exp))
            elo.update(r.comp_a, r.comp_b, s, when)
    feats = pd.DataFrame(rows)
    return m.merge(feats, on="event_ticker", how="left")


def tune_k(matches: pd.DataFrame, game: str, grid=(16, 24, 32, 48, 64), until=None) -> tuple[float, dict]:
    """Pick K for one game by the log loss of its pre-match Elo probabilities (matches before ``until``)."""
    g = matches[(matches["game"] == game) & matches["winner"].isin(["A", "B"])]
    if until is not None:
        g = g[pd.to_datetime(g["start_time"], utc=True) < pd.Timestamp(until)]
    if len(g) < 100:
        return 32.0, {}
    scores = {}
    for k in grid:
        f = pre_match_features(g, {game: EloConfig(k=float(k))})
        warm = f[(f["games_a"] >= 3) & (f["games_b"] >= 3)]
        if len(warm) < 50:
            continue
        p = warm["p_elo"].clip(1e-4, 1 - 1e-4).to_numpy()
        y = (warm["winner"] == "A").to_numpy()
        scores[k] = float(-np.mean(np.where(y, np.log(p), np.log(1 - p))))
    if not scores:
        return 32.0, {}
    best = min(scores, key=scores.get)
    return float(best), scores


def logit(p):
    p = np.clip(np.asarray(p, dtype=float), 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.asarray(z, dtype=float)))


def model_matrix(f: pd.DataFrame) -> np.ndarray:
    """Features for the calibrated win model (team A's view)."""
    n_min = np.minimum(f["games_a"].to_numpy(), f["games_b"].to_numpy())
    z = logit(f["p_elo"].to_numpy())
    return np.column_stack([
        z,
        z / (1.0 + n_min),                       # trust Elo less when a team is new
        f["form_a"].to_numpy() - f["form_b"].to_numpy(),
    ])


def fit_logistic(X: np.ndarray, y: np.ndarray, l2: float = 1.0, intercept: bool = True) -> np.ndarray:
    """Plain L2-regularised logistic regression (Newton steps); weights are returned intercept
    first. With ``intercept=False`` the intercept is held at 0: right when the features are
    antisymmetric in the two teams and which team is "A" is arbitrary (smaller ticker)."""
    Xb = np.column_stack([np.ones(len(X)), X])
    w = np.zeros(Xb.shape[1])
    lam = np.full(Xb.shape[1], l2)
    lam[0] = 0.0 if intercept else 1e12
    for _ in range(50):
        p = sigmoid(Xb @ w)
        g = Xb.T @ (p - y) + lam * w
        H = (Xb * (p * (1 - p))[:, None]).T @ Xb + np.diag(lam) + 1e-9 * np.eye(len(w))
        step = np.linalg.solve(H, g)
        w -= step
        if np.max(np.abs(step)) < 1e-8:
            break
    return w


def predict_logistic(w: np.ndarray, X: np.ndarray) -> np.ndarray:
    return sigmoid(np.column_stack([np.ones(len(X)), X]) @ w)


def log_loss(p, y) -> float:
    p = np.clip(np.asarray(p, dtype=float), 1e-6, 1 - 1e-6)
    y = np.asarray(y, dtype=float)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def brier(p, y) -> float:
    return float(np.mean((np.asarray(p, dtype=float) - np.asarray(y, dtype=float)) ** 2))


def binom_se(n: int, p: float) -> float:
    return math.sqrt(max(p * (1 - p), 1e-9) / max(n, 1))
