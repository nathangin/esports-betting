"""Are Kalshi's esports side markets priced consistently with the match-winner market?

Needs ``history/sides`` (``python -m esalpha sides``) and the Kalshi match history and candles.

A best-of-n match whose favourite has match price q implies a per-map win chance m (maps treated
as independent, m solved from q). The side markets then have "structural" prices:
  BO3 over 2.5 maps = 2m(1-m);  map 1 winner = m (BO3: q = m^2 (3 - 2m); BO5: q = m^3 (10 - 15m + 6m^2)).
The test, walk-forward (each day predicted from earlier days only): does
y ~ logit(structural) [+ logit(side mid)] beat the side market's own mid, and do taker bets on the
gap make money after the spread and fees?

The match format comes from the totals ladder (BO3: 2.5 strike; BO5: 3.5/4.5), which is listed
before the match. Map markets cannot be used for that: the map-4 market is only created once a
match reaches map 4 (a first version of this test that used them found a large "edge" that was
nothing but that look-ahead).

Usage: python research/side_markets.py --state <state dir>
"""
from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from esalpha.backtest import quotes_at  # noqa: E402
from esalpha.history import normalize_matches, read_table  # noqa: E402
from esalpha.strategy import market_prob  # noqa: E402


def match_win(m: float, bo: int) -> float:
    return m * m * (3 - 2 * m) if bo == 3 else m ** 3 * (10 - 15 * m + 6 * m * m)


def per_map(q: float, bo: int) -> float:
    q = min(max(q, 1e-4), 1 - 1e-4)
    return brentq(lambda m: match_win(m, bo) - q, 1e-6, 1 - 1e-6)


def fee(price: float, n: int = 1) -> float:
    return math.ceil(round(0.07 * n * price * (1 - price) * 100, 6)) / 100.0


def build(hist: Path, minutes=(60, 15)) -> pd.DataFrame:
    km = normalize_matches(read_table(hist, "matches")).dropna(subset=["start_time"])
    km["code"] = [e.split("-", 1)[1] for e in km["event_ticker"]]
    km = km[km["winner"].isin(["A", "B"])].drop_duplicates("code").set_index("code")
    mc = read_table(hist, "candles")
    sm = read_table(hist / "sides", "markets")
    sc = read_table(hist / "sides", "candles")
    ladder = sm[sm["kind"] == "total"].groupby("code")["strike"].apply(set)
    fmt = {c: 3 if (2.5 in s and not s & {3.5, 4.5}) else 5 if s & {3.5, 4.5} and 2.5 not in s else None
           for c, s in ladder.items()}
    use = sm[sm["code"].map(fmt).notna() & sm["code"].isin(km.index) & sm["result"].isin(["yes", "no"])
             & (((sm["kind"] == "total") & (sm["strike"] == 2.5)) | ((sm["kind"] == "map") & (sm["map_no"] == 1)))]
    by_t = {k: g.sort_values("ts")[["ts", "bid", "ask"]].reset_index(drop=True) for k, g in mc.groupby("ticker")}
    by_s = {k: g.sort_values("ts")[["ts", "bid", "ask"]].reset_index(drop=True)
            for k, g in sc[sc["ticker"].isin(set(use["ticker"]))].groupby("ticker")}
    rows = []
    for r in use.itertuples(index=False):
        if r.ticker not in by_s:
            continue
        k = km.loc[r.code]
        bo = fmt[r.code]
        a_side = None
        if r.kind == "map":
            if r.competitor not in (k.comp_a, k.comp_b):
                continue
            a_side = r.competitor == k.comp_a
        start = pd.Timestamp(k.start_time)
        close = quotes_at(by_s[r.ticker], int(start.timestamp()), 900)
        for mb in minutes:
            ts = int((start - pd.Timedelta(minutes=mb)).timestamp())
            q = market_prob(*quotes_at(by_t.get(k.ticker_a), ts), *quotes_at(by_t.get(k.ticker_b), ts))
            bid, ask = quotes_at(by_s[r.ticker], ts)
            if q is None or bid is None or ask is None:
                continue
            if r.kind == "total":
                m = per_map(max(q, 1 - q), 3)
                struct = 2 * m * (1 - m)
            else:
                struct = per_map(q if a_side else 1 - q, bo)
            rows.append({"ticker": r.ticker, "code": r.code, "kind": r.kind, "bo": bo, "game": r.game, "mb": mb,
                         "start": start, "struct": struct, "bid": bid, "ask": ask, "mid": (bid + ask) / 2,
                         "close_mid": None if None in close else sum(close) / 2, "y": int(r.result == "yes")})
    return pd.DataFrame(rows)


def logit(p):
    p = np.clip(np.asarray(p, float), 0.005, 0.995)
    return np.log(p / (1 - p))


def fit(x, y, l2=1e-3):
    w = np.zeros(x.shape[1])
    for _ in range(100):
        pr = 1 / (1 + np.exp(-(x @ w)))
        step = np.linalg.solve(-(x * (pr * (1 - pr))[:, None]).T @ x - l2 * np.eye(x.shape[1]), x.T @ (y - pr) - l2 * w)
        w -= step
        if np.abs(step).max() < 1e-10:
            break
    return w


def ll(p, y):
    p = np.clip(np.asarray(p, float), 0.01, 0.99)
    return float(-np.mean(np.where(np.asarray(y) == 1, np.log(p), np.log(1 - p))))


FEATS = {"struct": lambda d: np.c_[np.ones(len(d)), logit(d["struct"])],
         "struct_mid": lambda d: np.c_[np.ones(len(d)), logit(d["struct"]), logit(d["mid"])]}


def walk(d: pd.DataFrame, burn_days: int = 14, min_train: int = 150) -> pd.DataFrame:
    d = d.sort_values("start").copy()
    d["day"] = d["start"].dt.floor("D")
    parts = []
    for day in sorted(d["day"].unique()):
        tr, te = d[d["day"] < day], d[d["day"] == day].copy()
        if len(tr) < min_train or (day - d["day"].min()).days < burn_days:
            continue
        for name, f in FEATS.items():
            te["p_" + name] = 1 / (1 + np.exp(-(f(te) @ fit(f(tr), tr["y"].to_numpy().astype(float)))))
        parts.append(te)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def bets(d: pd.DataFrame, col: str, thr: float, max_spread: float = 0.10, n: int = 10) -> pd.DataFrame:
    out = []
    for r in d.itertuples(index=False):
        if r.ask - r.bid > max_spread:
            continue
        p = getattr(r, col)
        best = None
        for side, price, prob in (("yes", r.ask, p), ("no", 1 - r.bid, 1 - p)):
            if 0.05 <= price <= 0.95:
                ev = prob - price - 0.07 * price * (1 - price)
                if ev >= thr and (best is None or ev > best[0]):
                    best = (ev, side, price)
        if best is None:
            continue
        ev, side, price = best
        won = (r.y == 1) == (side == "yes")
        f = fee(price, n)
        out.append({"start": r.start, "side": side, "price": price, "won": won,
                    "pnl": n * ((1 - price) if won else -price) - f, "outlay": n * price + f})
    return pd.DataFrame(out)


def summary(b: pd.DataFrame) -> str:
    if b.empty:
        return "no bets"
    day = pd.to_datetime(b["start"]).dt.floor("D")
    by = b.groupby(day).agg(p=("pnl", "sum"), o=("outlay", "sum"))
    rng = np.random.default_rng(0)
    boot = [by["p"].to_numpy()[i].sum() / by["o"].to_numpy()[i].sum()
            for i in (rng.integers(0, len(by), len(by)) for _ in range(2000))]
    return (f"bets {len(b):4d}  ROI {b['pnl'].sum() / b['outlay'].sum():+.3f} "
            f"[{np.percentile(boot, 2.5):+.3f}, {np.percentile(boot, 97.5):+.3f}]  hit {b['won'].mean():.3f}  "
            f"avg price {b['price'].mean():.2f}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    a = ap.parse_args()
    df = build(Path(a.state) / "history")
    print(f"{len(df)} side-market snapshots, {df['code'].nunique()} matches")
    for (kind, mb), d in df.groupby(["kind", "mb"]):
        wf = walk(d)
        if wf.empty:
            continue
        print(f"\n{kind} T-{mb}: {len(d)} markets ({len(wf)} walk-forward); outcome rate {wf['y'].mean():.3f}, "
              f"side mid {wf['mid'].mean():.3f}, structural {wf['struct'].mean():.3f}, "
              f"median spread {np.median(wf['ask'] - wf['bid']):.3f}")
        print(f"  log loss: side mid {ll(wf['mid'], wf['y']):.4f}  structural {ll(wf['struct'], wf['y']):.4f}  "
              f"structural refit {ll(wf['p_struct'], wf['y']):.4f}  structural + mid {ll(wf['p_struct_mid'], wf['y']):.4f}")
        for col in ("p_struct", "p_struct_mid"):
            for thr in (0.0, 0.02, 0.04):
                print(f"    {col:10s} ev >= {thr:.2f}: {summary(bets(wf, col, thr))}")


if __name__ == "__main__":
    main()
