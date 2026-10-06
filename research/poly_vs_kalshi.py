"""Does Polymarket's price for the same esports match add anything to Kalshi's?

Needs ``history/poly`` (``python -m esalpha poly``) and the Kalshi match history and candles.

1. Pair Polymarket moneyline markets with Kalshi match events: same game, start within 3 hours,
   both team names match. The winners must agree (a check on the pairing).
2. At T minutes before the start: Kalshi's mid (both team books) vs Polymarket's last price.
   Log loss of each; how far Kalshi moves toward Polymarket by the start.
3. Walk-forward (each day predicted from earlier days only): Kalshi alone, Kalshi "stretched"
   (y ~ w * logit(q), which captures any favourite-longshot pattern), and Kalshi + Polymarket.
   Bets on Kalshi at the ask with fees when a model says the price is off.

Usage: python research/poly_vs_kalshi.py --state <state dir>
"""
from __future__ import annotations

import argparse
import difflib
import math
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from esalpha.backtest import quotes_at  # noqa: E402
from esalpha.history import normalize_matches, read_table  # noqa: E402
from esalpha.strategy import market_prob  # noqa: E402

STOP = {"esports", "esport", "gaming", "team", "club", "gg", "the", "academy", "e", "sports", "fe", "female"}


def norm(name: str) -> str:
    s = re.sub(r"[^a-z0-9 ]", " ", str(name).lower())
    toks = [t for t in s.split() if t not in STOP]
    return "".join(toks) or re.sub(r"[^a-z0-9]", "", str(name).lower())


def same_team(a: str, b: str) -> float:
    x, y = norm(a), norm(b)
    if not x or not y:
        return 0.0
    if x == y:
        return 1.0
    if min(len(x), len(y)) >= 3 and (x in y or y in x):
        return 0.9
    return difflib.SequenceMatcher(None, x, y).ratio()


def pair(km: pd.DataFrame, pm: pd.DataFrame, max_hours: float = 3.0, min_sim: float = 0.8) -> pd.DataFrame:
    rows = []
    by_game = {g: d for g, d in km.dropna(subset=["start_time"]).groupby("game")}
    for p in pm.itertuples(index=False):
        d = by_game.get(p.game)
        if d is None:
            continue
        near = d[(d["start_time"] - p.start_time).abs() <= pd.Timedelta(hours=max_hours)]
        best = None
        for k in near.itertuples(index=False):
            s_same = min(same_team(k.team_a, p.team_1), same_team(k.team_b, p.team_2))
            s_swap = min(same_team(k.team_a, p.team_2), same_team(k.team_b, p.team_1))
            s, flip = (s_same, False) if s_same >= s_swap else (s_swap, True)
            if s >= min_sim and (best is None or s > best[0]):
                best = (s, k, flip)
        if best is None:
            continue
        s, k, flip = best
        rows.append({"event_ticker": k.event_ticker, "market_id": str(p.market_id), "game": p.game, "sim": s,
                     "flip": flip, "k_start": k.start_time, "k_winner": k.winner, "p_winner": p.winner,
                     "p_team_a": p.team_2 if flip else p.team_1, "ticker_a": k.ticker_a, "ticker_b": k.ticker_b})
    out = pd.DataFrame(rows)
    out = out.sort_values("sim", ascending=False).drop_duplicates("event_ticker").drop_duplicates("market_id")
    known = out["p_winner"].notna() & out["k_winner"].isin(["A", "B"])
    agree = (out["p_winner"] == out["p_team_a"]) == (out["k_winner"] == "A")
    out["winners_agree"] = np.where(known, agree, np.nan)
    return out


def snapshots(pairs, candles, prices, minutes=(60, 15, 5), poly_age=1800) -> pd.DataFrame:
    by_t = {t: g.sort_values("ts")[["ts", "bid", "ask"]].reset_index(drop=True) for t, g in candles.groupby("ticker")}
    ser = {m: (g["ts"].to_numpy(), g["p"].to_numpy()) for m, g in prices.sort_values("ts").groupby("market_id")}
    rows = []
    for r in pairs.itertuples(index=False):
        if r.k_winner not in ("A", "B") or r.winners_agree == 0 or r.market_id not in ser:
            continue
        start = pd.Timestamp(r.k_start)
        t_close = int(start.timestamp())
        q_close = market_prob(*quotes_at(by_t.get(r.ticker_a), t_close, 900), *quotes_at(by_t.get(r.ticker_b), t_close, 900))
        pt, pp = ser[r.market_id]
        for mb in minutes:
            t = int((start - pd.Timedelta(minutes=mb)).timestamp())
            ba, aa = quotes_at(by_t.get(r.ticker_a), t)
            bb, ab = quotes_at(by_t.get(r.ticker_b), t)
            q = market_prob(ba, aa, bb, ab)
            i = int(np.searchsorted(pt, t, side="right")) - 1
            if q is None or i < 0 or t - pt[i] > poly_age:
                continue
            p = 1 - float(pp[i]) if r.flip else float(pp[i])
            rows.append({"event_ticker": r.event_ticker, "game": r.game, "start": start, "mb": mb, "q": q, "p": p,
                         "bid_a": ba, "ask_a": aa, "bid_b": bb, "ask_b": ab, "q_close": q_close,
                         "y": 1 if r.k_winner == "A" else 0})
    return pd.DataFrame(rows)


def logit(p):
    p = np.clip(np.asarray(p, float), 0.01, 0.99)
    return np.log(p / (1 - p))


def fit(x, y, iters=100):
    w = np.zeros(x.shape[1])
    for _ in range(iters):
        pr = 1 / (1 + np.exp(-(x @ w)))
        step = np.linalg.solve(-(x * (pr * (1 - pr))[:, None]).T @ x - 1e-6 * np.eye(x.shape[1]), x.T @ (y - pr))
        w -= step
        if np.abs(step).max() < 1e-9:
            break
    return w


def losses(p, y):
    p = np.clip(np.asarray(p, float), 0.01, 0.99)
    return -np.where(np.asarray(y) == 1, np.log(p), np.log(1 - p))


def fee(price: float, n: int = 1) -> float:
    return math.ceil(round(0.07 * n * price * (1 - price) * 100, 6)) / 100.0


def walk_forward(g: pd.DataFrame, burn_days: int = 14) -> pd.DataFrame:
    g = g.sort_values("start").copy()
    g["day"] = g["start"].dt.floor("D")
    parts = []
    for d in sorted(g["day"].unique())[burn_days:]:
        tr, te = g[g["day"] < d], g[g["day"] == d].copy()
        y = tr["y"].to_numpy()
        w1 = fit(np.c_[logit(tr["q"])], y)
        w2 = fit(np.c_[logit(tr["q"]), logit(tr["p"])], y)
        te["stretched"] = 1 / (1 + np.exp(-(logit(te["q"]) * w1[0])))
        te["with_poly"] = 1 / (1 + np.exp(-(np.c_[logit(te["q"]), logit(te["p"])] @ w2)))
        parts.append(te)
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def bets(s: pd.DataFrame, col: str, min_edge: float, max_spread: float = 0.05, n: int = 10) -> pd.DataFrame:
    """Back whichever team the probability favours over Kalshi's ask (YES on it or NO on the
    other team, whichever is cheaper), fee-aware, one bet per match."""
    out = []
    for r in s.itertuples(index=False):
        pa = getattr(r, col)
        opts = []
        for backs, prob, routes in (("A", pa, ((r.ask_a, r.bid_a), (_inv(r.bid_b), _inv(r.ask_b)))),
                                    ("B", 1 - pa, ((r.ask_b, r.bid_b), (_inv(r.bid_a), _inv(r.ask_a))))):
            for price, other in routes:
                if price is None or other is None or abs(price - other) > max_spread or not (0.05 <= price <= 0.95):
                    continue
                ev = prob - price - 0.07 * price * (1 - price)
                if ev >= min_edge:
                    opts.append((ev, backs, price))
        if not opts:
            continue
        ev, backs, price = max(opts)
        won = (r.y == 1) == (backs == "A")
        f = fee(price, n)
        qc = None if r.q_close is None or pd.isna(r.q_close) else (r.q_close if backs == "A" else 1 - r.q_close)
        out.append({"start": r.start, "price": price, "won": won, "pnl": n * ((1 - price) if won else -price) - f,
                    "outlay": n * price + f, "clv": None if qc is None else qc - price})
    return pd.DataFrame(out)


def _inv(x):
    return None if x is None or pd.isna(x) else 1 - float(x)


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
            f"avg price {b['price'].mean():.2f}  CLV {b['clv'].dropna().mean():+.4f}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    ap.add_argument("--since", default="2026-07-25")
    a = ap.parse_args()
    hist = Path(a.state) / "history"
    km = normalize_matches(read_table(hist, "matches"))
    km = km[km["start_time"] >= pd.Timestamp(a.since, tz="UTC")]
    pm = pd.read_parquet(hist / "poly" / "matches.parquet")
    pm["start_time"] = pd.to_datetime(pm["start_time"], utc=True)
    prices = pd.read_parquet(hist / "poly" / "prices.parquet")
    prices["market_id"] = prices["market_id"].astype(str)
    pairs = pair(km, pm)
    print(f"Kalshi matches since {a.since}: {len(km)}; Polymarket match markets: {len(pm)}; paired: {len(pairs)}; "
          f"winners agree on {pairs['winners_agree'].mean():.4f} of the settled pairs")
    candles = read_table(hist, "candles")
    s = snapshots(pairs, candles[candles["event_ticker"].isin(set(pairs["event_ticker"]))], prices)
    for mb, g in s.groupby("mb"):
        h = g.dropna(subset=["q_close"])
        x, dy = (h["p"] - h["q"]).to_numpy(), (h["q_close"] - h["q"]).to_numpy()
        print(f"\nT-{mb}: {len(g)} matches; mean |Polymarket - Kalshi| {np.abs(g['p'] - g['q']).mean():.3f}; "
              f"log loss Kalshi {losses(g['q'], g['y']).mean():.4f}, Polymarket {losses(g['p'], g['y']).mean():.4f}; "
              f"by the start Kalshi moves {float((x * dy).sum() / (x * x).sum()):.0%} of the way to Polymarket")
        wf = walk_forward(g)
        if wf.empty:
            continue
        lq, ls, lp = losses(wf["q"], wf["y"]), losses(wf["stretched"], wf["y"]), losses(wf["with_poly"], wf["y"])
        print(f"  walk-forward ({len(wf)} matches): log loss Kalshi {lq.mean():.4f}, stretched {ls.mean():.4f}, "
              f"Kalshi + Polymarket {lp.mean():.4f} (gain over stretched {ls.mean() - lp.mean():+.4f})")
        for col in ("stretched", "with_poly"):
            for thr in (0.0, 0.01, 0.02):
                print(f"    {col:10s} edge >= {thr:.2f}: {summary(bets(wf, col, thr))}")


if __name__ == "__main__":
    main()
