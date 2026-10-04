"""Synthetic esports history in the same layout ``esalpha history`` writes (for tests)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

GAMES = {"cs2": "KXCS2GAME", "lol": "KXLOLGAME"}


def make_history(root: Path, n_days: int = 200, per_day: int = 12, teams: int = 40, seed: int = 0,
                 market_noise: float = 0.35, priced_from_day: int = 60) -> dict:
    """Matches between teams with hidden strengths; the market sees the strengths with noise.

    Returns the hidden truth so tests can check that the model learns something.
    """
    rng = np.random.default_rng(seed)
    hist = root / "history"
    hist.mkdir(parents=True, exist_ok=True)
    t0 = pd.Timestamp("2026-03-01T12:00Z")
    rows, candles = [], []
    strengths = {g: rng.normal(0, 1.0, teams) for g in GAMES}
    for d in range(n_days):
        for j in range(per_day):
            g = list(GAMES)[j % len(GAMES)]
            series = GAMES[g]
            a, b = rng.choice(teams, 2, replace=False)
            sa, sb = strengths[g][a], strengths[g][b]
            p_true = 1 / (1 + np.exp(-(sa - sb)))
            y = rng.random() < p_true
            start = t0 + pd.Timedelta(days=d, hours=int(j * 1.5))
            code = start.tz_convert("America/New_York").strftime("%y%b%d%H%M").upper()
            ev = f"{series}-{code}T{a:02d}T{b:02d}"
            ta, tb = f"{ev}-T{a:02d}", f"{ev}-T{b:02d}"
            rows.append({"event_ticker": ev, "series_ticker": series, "game": g, "start_time": start,
                         "open_time": start - pd.Timedelta(hours=2), "close_time": start + pd.Timedelta(hours=2),
                         "team_a": f"Team {a}", "team_b": f"Team {b}", "comp_a": f"{g}-{a}", "comp_b": f"{g}-{b}",
                         "ticker_a": ta, "ticker_b": tb, "winner": "A" if y else "B", "volume": 1000.0,
                         "tournament": "Test Cup"})
            if d >= priced_from_day:
                z = (sa - sb) + rng.normal(0, market_noise)
                q = float(np.clip(1 / (1 + np.exp(-z)), 0.03, 0.97))
                for k in range(0, 121, 5):
                    ts = int((start - pd.Timedelta(minutes=120 - k)).timestamp())
                    mid = round(q, 2)
                    candles.append({"event_ticker": ev, "ticker": ta, "ts": ts, "bid": max(mid - 0.01, 0.01),
                                    "ask": min(mid + 0.01, 0.99), "price": mid, "volume": 10.0})
                    candles.append({"event_ticker": ev, "ticker": tb, "ts": ts, "bid": max(1 - mid - 0.01, 0.01),
                                    "ask": min(1 - mid + 0.01, 0.99), "price": 1 - mid, "volume": 10.0})
    m = pd.DataFrame(rows)
    m.to_parquet(hist / "matches.parquet", index=False)
    pd.DataFrame(candles).to_parquet(hist / "candles.parquet", index=False)
    (hist / "series.json").write_text(json.dumps([{"ticker": s, "title": g, "fee_type": "quadratic",
                                                   "fee_multiplier": 1} for g, s in GAMES.items()]))
    return {"strengths": strengths, "matches": m}
