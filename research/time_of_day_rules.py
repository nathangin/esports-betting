"""Esports: every simple rule by game / start hour / weekday / minutes before start / favourite
or underdog / price band / liquidity / tournament, on real Kalshi prices, picked on one period and
checked on the other. Each rule backs one team per match at most, as a 10-contract taker order at
the cheaper of YES-on-it (ask) or NO-on-the-other (1 - bid), with Kalshi's fee.

Usage: python research/time_of_day_rules.py --state <state dir>
"""
import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from esalpha.history import normalize_matches, read_table  # noqa: E402

N = 10
MINUTES = (240, 120, 60, 30, 15, 5)


def fee_pc(p):
    return np.ceil(np.round(0.07 * N * p * (1 - p) * 100, 6)) / 100.0 / N


def quotes(c: pd.DataFrame, ts: np.ndarray, max_age=3600):
    t = c["ts"].to_numpy()
    i = np.searchsorted(t, ts, side="right") - 1
    ok = (i >= 0)
    bid = np.full(len(ts), np.nan)
    ask = np.full(len(ts), np.nan)
    vol = np.zeros(len(ts))
    cumv = np.cumsum(np.nan_to_num(c["volume"].to_numpy()))
    for k in np.where(ok)[0]:
        if ts[k] - t[i[k]] <= max_age:
            bid[k], ask[k] = c["bid"].iat[i[k]], c["ask"].iat[i[k]]
        vol[k] = cumv[i[k]]
    return bid, ask, vol


def build(H: Path) -> pd.DataFrame:
    m = normalize_matches(read_table(H, "matches"))
    m = m[m["winner"].isin(["A", "B"]) & ~m["start_estimated"]].dropna(subset=["start_time"])
    c = read_table(H, "candles")
    by = {t: g.sort_values("ts").reset_index(drop=True) for t, g in c.groupby("ticker")}
    rows = []
    for r in m.itertuples(index=False):
        ca, cb = by.get(r.ticker_a), by.get(r.ticker_b)
        if ca is None or cb is None:
            continue
        start = pd.Timestamp(r.start_time)
        ts = np.array([int((start - pd.Timedelta(minutes=mb)).timestamp()) for mb in MINUTES])
        ba, aa, va = quotes(ca, ts)
        bb, ab, vb = quotes(cb, ts)
        for k, mb in enumerate(MINUTES):
            if np.isnan([ba[k], aa[k], bb[k], ab[k]]).any():
                continue
            q = ((ba[k] + aa[k]) / 2 + 1 - (bb[k] + ab[k]) / 2) / 2
            for team, won, p_yes, p_no, prob in (("A", r.winner == "A", aa[k], 1 - bb[k], q),
                                                  ("B", r.winner == "B", ab[k], 1 - ba[k], 1 - q)):
                price = min(p_yes, p_no)
                rows.append({"event": r.event_ticker, "game": r.game, "start": start, "mb": mb, "team": team,
                             "q": prob, "price": price, "won": int(won), "vol_pre": va[k] + vb[k],
                             "tournament": r.tournament or "", "spread": min(aa[k] - ba[k], ab[k] - bb[k])})
    df = pd.DataFrame(rows)
    df = df[df["price"].between(0.02, 0.98)]
    f = fee_pc(df["price"].to_numpy())
    df["pnl"] = df["won"] - df["price"] - f
    df["outlay"] = df["price"] + f
    et = df["start"].dt.tz_convert("America/New_York")
    df["hour_et"] = et.dt.hour
    df["hblock"] = (et.dt.hour // 6 * 6).map(lambda h: f"{h:02d}-{h + 5:02d} ET")
    df["weekend"] = np.where(et.dt.dayofweek >= 5, "weekend", "weekday")
    df["date"] = et.dt.date
    df["fav"] = np.where(df["q"] > 0.5, "favourite", "underdog")
    df["band"] = pd.cut(df["price"], [0.0, 0.2, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0]).astype(str)
    # liquidity: contracts traded before the decision, terciles within each game and decision time
    df["liq"] = df.groupby(["game", "mb"])["vol_pre"].transform(
        lambda v: pd.qcut(v.rank(method="first"), 3, labels=["thin", "medium", "busy"])).astype(str)
    top = df.drop_duplicates("event")["tournament"].value_counts()
    df["tour"] = np.where(df["tournament"].isin(top[top >= 40].index), df["tournament"], "other")
    return df


def score(b, keys):
    g = b.groupby(keys + ["date"], observed=True).agg(p=("pnl", "sum"), o=("outlay", "sum"), n=("pnl", "size")).reset_index()
    t = g.groupby(keys, observed=True).agg(p=("p", "sum"), o=("o", "sum"), n=("n", "sum"))
    t["roi"] = t["p"] / t["o"]
    g = g.merge(t["roi"].reset_index(), on=keys)
    g["r"] = g["p"] - g["o"] * g["roi"]
    t["t"] = t["p"] / g.groupby(keys, observed=True)["r"].apply(lambda r: math.sqrt((r ** 2).sum()) if len(r) > 1 else np.nan)
    return t


FAMILIES = {
    "minutes before x game x fav/dog x price": (None, ["mb", "game", "fav", "band"]),
    "start hour block x game x fav/dog x price": (60, ["hblock", "game", "fav", "band"]),
    "start hour x fav/dog": (60, ["hour_et", "fav"]),
    "start hour x game x fav/dog": (60, ["hour_et", "game", "fav"]),
    "weekday/weekend x game x fav/dog x price": (60, ["weekend", "game", "fav", "band"]),
    "liquidity x game x fav/dog x price": (60, ["liq", "game", "fav", "band"]),
    "tournament x fav/dog": (60, ["tour", "fav"]),
    "tournament x fav/dog x price": (60, ["tour", "fav", "band"]),
}


def run(b, split, min_n=40, min_roi=0.05, min_t=2.0):
    a, h = b[b["date"] < split], b[b["date"] >= split]
    print(f"period A: {a['date'].min()} to {a['date'].max()} ({a['event'].nunique()} matches); "
          f"period B: {h['date'].min()} to {h['date'].max()} ({h['event'].nunique()} matches)")
    rows = []
    for fam, (mb, keys) in FAMILIES.items():
        aa, hh = (a, h) if mb is None else (a[a["mb"] == mb], h[h["mb"] == mb])
        j = score(aa, keys).join(score(hh, keys), lsuffix="_a", rsuffix="_b", how="outer")
        j["family"] = fam
        j["rule"] = [" | ".join(map(str, k if isinstance(k, tuple) else (k,))) for k in j.index]
        rows.append(j.reset_index(drop=True))
    r = pd.concat(rows, ignore_index=True)
    for fold, (x, y) in {"pick on A, check on B": ("a", "b"), "pick on B, check on A": ("b", "a")}.items():
        sel = r[(r[f"n_{x}"] >= min_n) & (r[f"roi_{x}"] >= min_roi) & (r[f"t_{x}"] >= min_t)]
        tested = sel[sel[f"n_{y}"] >= 10]
        print(f"{fold}: {int((r[f'n_{x}'] >= min_n).sum())} rules with {min_n}+ bets; {len(sel)} made {min_roi:.0%}+ "
              f"with t >= {min_t}; {(tested[f'roi_{y}'] > 0).sum()} of {len(tested)} made money in the other period; "
              f"pooled ROI there {tested[f'p_{y}'].sum() / max(tested[f'o_{y}'].sum(), 1e-9):+.3f} on {int(tested[f'n_{y}'].sum())} bets")
    return r


def tables(b: pd.DataFrame, split) -> None:
    b = b.assign(period=np.where(b["date"] < split, "A", "B"))
    x = b[b["mb"] == 60]
    for keys, lab, d in ((["hblock", "fav"], "60 min before, by start time (ET)", x),
                         (["game", "fav"], "60 min before, by game", x),
                         (["mb"], "favourites, by minutes before the start", b[b["fav"] == "favourite"])):
        t = d.groupby(keys + ["period"]).agg(p=("pnl", "sum"), o=("outlay", "sum"))
        t = (t["p"] / t["o"]).unstack("period")
        print(f"\n{lab}: ROI A / B")
        print("  " + "  ".join(f"{' '.join(map(str, k)) if isinstance(k, tuple) else k}: {r['A']:+.1%}/{r['B']:+.1%}"
                              for k, r in t.iterrows()))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    b = build(Path(ap.parse_args().state) / "history")
    print(f"{len(b)} candidate bets, {b['event'].nunique()} matches, {b['date'].min()} to {b['date'].max()}")
    days = sorted(b["date"].unique())
    split = days[len(days) * 6 // 10]
    run(b, split)
    tables(b, split)
