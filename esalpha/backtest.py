"""Fake-money backtest of esports match betting on real Kalshi prices.

For every settled match with price history, the decision is made ``minutes_before`` the
scheduled start using the last 1-minute bid/ask before that moment. Team ratings come only
from earlier matches; the win model and the model+market blend are refitted weekly on
earlier weeks only. Bets fill at the ask (or 1 - bid for NO) with Kalshi's taker fee and
settle on Kalshi's result.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import ratings as rt
from .history import read_table
from .kalshi import game_of
from .model import Params
from .strategy import Rules, default_rules, flat_candidates, flat_rules, match_candidates, market_prob, settle_pnl, size

log = logging.getLogger(__name__)


def fee_rates(hist: Path) -> dict[str, float]:
    p = hist / "series.json"
    if not p.exists():
        return {}
    out = {}
    for s in json.loads(p.read_text()):
        mult = s.get("fee_multiplier")
        out[s["ticker"]] = 0.07 * float(mult) if mult not in (None, "") else 0.07
    return out


def quotes_at(c: pd.DataFrame | None, ts: int, max_age: int = 3600) -> tuple[float | None, float | None]:
    if c is None or c.empty:
        return None, None
    i = int(np.searchsorted(c["ts"].to_numpy(), ts, side="right")) - 1
    if i < 0:
        return None, None
    row = c.iloc[i]
    if ts - int(row["ts"]) > max_age:
        return None, None
    bid = None if pd.isna(row["bid"]) else float(row["bid"])
    ask = None if pd.isna(row["ask"]) else float(row["ask"])
    return bid, ask


def build_events(hist: Path, minutes_before: float = 60.0, tune_until=None) -> tuple[pd.DataFrame, dict]:
    matches = read_table(hist, "matches")
    matches["game"] = matches["series_ticker"].map(game_of)        # labels follow the current code
    matches["start_time"] = pd.to_datetime(matches["start_time"], utc=True)
    matches = matches.dropna(subset=["start_time"])
    candles = read_table(hist, "candles")
    by_ticker = {t: g.sort_values("ts")[["ts", "bid", "ask"]].reset_index(drop=True) for t, g in candles.groupby("ticker")}
    priced_events = set(candles["event_ticker"].unique())
    first_priced = matches.loc[matches["event_ticker"].isin(priced_events), "start_time"].min()
    tune_until = tune_until or first_priced
    cfgs, tuning = {}, {}
    for g in matches["game"].unique():
        k, scores = rt.tune_k(matches, g, until=tune_until)
        cfgs[g] = rt.EloConfig(k=k)
        tuning[g] = {"k": k, "scores": scores}
    f = rt.pre_match_features(matches, cfgs)
    rows = []
    for r in f.itertuples(index=False):
        if r.event_ticker not in priced_events or r.winner not in ("A", "B"):
            continue
        t = int((pd.Timestamp(r.start_time) - pd.Timedelta(minutes=minutes_before)).timestamp())
        ba, aa = quotes_at(by_ticker.get(r.ticker_a), t)
        bb, ab = quotes_at(by_ticker.get(r.ticker_b), t)
        q = market_prob(ba, aa, bb, ab)
        if q is None:
            continue
        rows.append({**r._asdict(), "decision_ts": t, "bid_a": ba, "ask_a": aa, "bid_b": bb, "ask_b": ab, "q": q,
                     "y": 1 if r.winner == "A" else 0})
    ev = pd.DataFrame(rows)
    return ev, {"elo": tuning, "all_matches": int(len(f)), "features": f}


def walk_forward(ev: pd.DataFrame, feats: pd.DataFrame, burn_in_days: int = 21) -> tuple[pd.DataFrame, list]:
    """Weekly refits: calibrated win model (on all earlier results) and model+market blend
    (on earlier priced matches)."""
    ev = ev.sort_values("decision_ts").reset_index(drop=True)
    ev["p_model"] = np.nan
    ev["p"] = np.nan
    start = pd.to_datetime(ev["start_time"], utc=True)
    first = start.min().normalize() + pd.Timedelta(days=burn_in_days)
    weeks = pd.date_range(first, start.max() + pd.Timedelta(days=7), freq="7D")
    hist_res = feats[feats["winner"].isin(["A", "B"])].copy()
    hist_res["start_time"] = pd.to_datetime(hist_res["start_time"], utc=True)
    log_rows = []
    for w0, w1 in zip(weeks[:-1], weeks[1:]):
        sel = (start >= w0) & (start < w1)
        if not sel.any():
            continue
        train = hist_res[hist_res["start_time"] < w0]
        if len(train) < 200:
            continue
        wm = rt.fit_logistic(rt.model_matrix(train), (train["winner"] == "A").to_numpy().astype(float), l2=1.0)
        ev.loc[sel, "p_model"] = rt.predict_logistic(wm, rt.model_matrix(ev.loc[sel]))
        past = ev[(start < w0) & ev["p_model"].notna()]
        blend = None
        if len(past) >= 150:
            Xb = np.column_stack([rt.logit(past["p_model"]), rt.logit(past["q"])])
            blend = rt.fit_logistic(Xb, past["y"].to_numpy().astype(float), l2=0.5)
            Xn = np.column_stack([rt.logit(ev.loc[sel, "p_model"]), rt.logit(ev.loc[sel, "q"])])
            ev.loc[sel, "p"] = rt.predict_logistic(blend, Xn)
        log_rows.append({"from": str(w0.date()), "train_results": int(len(train)), "blend_fit_on": int(len(past)),
                         "model_w": [round(float(x), 3) for x in wm],
                         "blend_w": None if blend is None else [round(float(x), 3) for x in blend]})
    return ev, log_rows


def simulate(ev: pd.DataFrame, prob_col: str, rules: Rules, fees: dict, bankroll: float = 1000.0,
             strategy: str = "model") -> tuple[pd.DataFrame, dict]:
    cash, open_bets, ledger, curve = bankroll, [], [], []
    day_budget: dict = {}
    for r in ev.sort_values("decision_ts").itertuples(index=False):
        now = pd.Timestamp(r.decision_ts, unit="s", tz="UTC")
        still = []
        for b in open_bets:
            if b["settle_ts"] <= now:
                pnl = settle_pnl(b["side"], b["contracts"], b["price"], b["fee"], b["result"])
                cash += b["cost"] + b["fee"] + pnl
                b["pnl"] = pnl
                ledger.append(b)
            else:
                still.append(b)
        open_bets = still
        equity = cash + sum(b["cost"] + b["fee"] for b in open_bets)
        curve.append(equity)
        day = now.date()
        budget = day_budget.setdefault(day, rules.max_run_frac * equity)
        rl = Rules(**{**rules.to_dict(), "sides": tuple(rules.sides), "fee_rate": fees.get(r.series_ticker, 0.07)})
        a = {"ticker": r.ticker_a, "yes_bid": r.bid_a, "yes_ask": r.ask_a}
        b_ = {"ticker": r.ticker_b, "yes_bid": r.bid_b, "yes_ask": r.ask_b}
        if strategy in ("favourite", "underdog"):
            fav_a = r.q >= 0.5
            backs_a = fav_a if strategy == "favourite" else not fav_a
            cands = flat_candidates(r.event_ticker, backs_a, a, b_, rl)
            sized = size(cands, equity, cash, flat_rules(rl), run_budget=budget)
        else:
            p_a = getattr(r, prob_col)
            if p_a is None or pd.isna(p_a):
                continue
            if abs(p_a - r.q) > rl.max_gap:
                continue
            cands = match_candidates(r.event_ticker, float(p_a), a, b_, rl)
            sized = size(cands, equity, cash, rl, run_budget=budget)
        for bt in sized:
            backs = bt.extra.get("backs")
            winner_ticker = r.ticker_a if r.y == 1 else r.ticker_b
            result = "yes" if bt.ticker == winner_ticker else "no"     # the market's own result
            rec = {"strategy": strategy, "event_ticker": r.event_ticker, "game": r.game, "start_time": r.start_time,
                   "ticker": bt.ticker, "side": bt.side, "backs": backs, "price": bt.price, "contracts": bt.contracts,
                   "cost": bt.cost, "fee": bt.fee, "prob": bt.prob, "q": r.q, "result": result,
                   "settle_ts": pd.Timestamp(r.close_time) if pd.notna(r.close_time) else now + pd.Timedelta(hours=6)}
            cash -= bt.cost + bt.fee
            day_budget[day] -= bt.cost + bt.fee
            open_bets.append(rec)
    for b in open_bets:
        pnl = settle_pnl(b["side"], b["contracts"], b["price"], b["fee"], b["result"])
        cash += b["cost"] + b["fee"] + pnl
        b["pnl"] = pnl
        ledger.append(b)
    led = pd.DataFrame(ledger)
    return led, summarize(led, bankroll, cash, curve)


def summarize(led: pd.DataFrame, start: float, end_cash: float, curve) -> dict:
    if led.empty:
        return {"bets": 0, "start": start, "end": round(end_cash, 2), "pnl": 0.0}
    outlay = (led["cost"] + led["fee"]).sum()
    led = led.assign(day=pd.to_datetime(led["start_time"], utc=True).dt.date)
    pnl_d = led.groupby("day")["pnl"].sum()
    out_d = led.assign(o=led["cost"] + led["fee"]).groupby("day")["o"].sum()
    rng = np.random.default_rng(0)
    days = pnl_d.index.to_numpy()
    boot = [pnl_d.loc[pick].sum() / max(out_d.loc[pick].sum(), 1e-9)
            for pick in (rng.choice(days, len(days), replace=True) for _ in range(2000))]
    eq = np.array(curve) if curve else np.array([start])
    peak = np.maximum.accumulate(eq)
    won = (led["pnl"] > 0).mean()
    return {"bets": int(len(led)), "days": int(len(pnl_d)), "start": start, "end": round(end_cash, 2),
            "pnl": round(float(led["pnl"].sum()), 2), "outlay": round(float(outlay), 2),
            "roi": float(led["pnl"].sum() / outlay), "roi_ci95": [float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))],
            "hit_rate": float(won), "avg_price": float(led["price"].mean()), "fees": round(float(led["fee"].sum()), 2),
            "max_drawdown": float(np.max((peak - eq) / peak)) if len(eq) else 0.0,
            "by_game": led.assign(o=led["cost"] + led["fee"]).groupby("game").agg(
                bets=("pnl", "size"), pnl=("pnl", "sum"), outlay=("o", "sum")).round(2).reset_index().to_dict("records")}


def calibration_table(ev: pd.DataFrame, col: str) -> list[dict]:
    d = ev.dropna(subset=[col])
    fav = np.where(d[col] >= 0.5, d[col], 1 - d[col])
    won = np.where(d[col] >= 0.5, d["y"], 1 - d["y"])
    bins = pd.cut(fav, [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 1.0], include_lowest=True)
    t = pd.DataFrame({"bin": bins, "p": fav, "won": won}).groupby("bin", observed=True).agg(
        n=("won", "size"), mean_p=("p", "mean"), won=("won", "mean"))
    return [{"favourite_prob": str(i), "n": int(r["n"]), "mean_p": round(float(r["mean_p"]), 3),
             "won": round(float(r["won"]), 3)} for i, r in t.iterrows()]


def final_params(ev: pd.DataFrame, feats: pd.DataFrame, k: dict, minutes_before: float) -> Params:
    """What the paper trader uses: the win model fitted on every result so far and the blend
    fitted on every priced match (with out-of-sample model probabilities)."""
    res = feats[feats["winner"].isin(["A", "B"])]
    win_w = rt.fit_logistic(rt.model_matrix(res), (res["winner"] == "A").to_numpy().astype(float), l2=1.0)
    past = ev.dropna(subset=["p_model"])
    blend_w = None
    if len(past) >= 150:
        Xb = np.column_stack([rt.logit(past["p_model"]), rt.logit(past["q"])])
        blend_w = rt.fit_logistic(Xb, past["y"].to_numpy().astype(float), l2=0.5)
    return Params(k={g: float(v) for g, v in k.items()},
                  win_w=[float(x) for x in win_w], blend_w=None if blend_w is None else [float(x) for x in blend_w],
                  meta={"fitted": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"), "results": int(len(res)),
                        "priced_matches": int(len(past)), "decision_minutes_before": minutes_before,
                        "last_match": str(pd.to_datetime(res["start_time"], utc=True).max())})


def run(state_dir: str, minutes_before: float = 60.0, rules: Rules | None = None, name: str = "backtest",
        save_params: bool = True) -> dict:
    state = Path(state_dir)
    hist = state / "history"
    rules = rules or default_rules()
    ev, info = build_events(hist, minutes_before)
    if ev.empty:
        raise RuntimeError("no priced matches; run `esalpha history` first")
    ev, wf = walk_forward(ev, info["features"])
    fees = fee_rates(hist)
    test = ev[ev["p_model"].notna()]
    scored = test.dropna(subset=["p"])
    rep = {"generated": datetime.now(timezone.utc).isoformat(), "decision": f"{minutes_before:g} min before scheduled start",
           "matches_all": info["all_matches"], "matches_priced": int(len(ev)), "matches_tested": int(len(test)),
           "period": [str(pd.to_datetime(test["start_time"]).min()), str(pd.to_datetime(test["start_time"]).max())],
           "by_game": test.groupby("game").size().to_dict(), "elo_tuning": info["elo"], "walk_forward": wf,
           "scores": score_table(scored), "scores_by_game": {g: score_table(d) for g, d in scored.groupby("game")},
           "market_calibration": calibration_table(test, "q"), "model_calibration": calibration_table(test, "p_model"),
           "rules": rules.to_dict(), "results": {}}
    ledgers = []
    for label, col, strat in STRATEGIES:
        led, summ = simulate(test, col, rules, fees, strategy=strat)
        rep["results"][label] = summ
        if len(led):
            ledgers.append(led.assign(book=label))
    if save_params:
        prm = final_params(ev, info["features"], {g: v["k"] for g, v in info["elo"].items()}, minutes_before)
        prm.save(state / "params" / "fitted.json")
        rep["params"] = {"fitted": prm.meta["fitted"], "win_w": prm.win_w, "blend_w": prm.blend_w}
    out = state / "reports"
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{name}.json").write_text(json.dumps(rep, indent=1, default=str))
    if ledgers:
        pd.concat(ledgers).to_csv(out / f"{name}_bets.csv", index=False)
    return rep


STRATEGIES = [("model + market blend", "p", "model"), ("model only", "p_model", "model"),
              ("always the favourite (1% flat)", None, "favourite"),
              ("always the underdog (1% flat)", None, "underdog")]


def score_table(d: pd.DataFrame) -> dict:
    """Log loss / Brier of market, model and blend on the same matches (lower is better)."""
    if d.empty:
        return {"n": 0}
    y = d["y"]
    return {"n": int(len(d)),
            "log_loss": {"market": rt.log_loss(d["q"], y), "model": rt.log_loss(d["p_model"], y),
                         "blend": rt.log_loss(d["p"], y)},
            "brier": {"market": rt.brier(d["q"], y), "model": rt.brier(d["p_model"], y), "blend": rt.brier(d["p"], y)},
            "accuracy": {"market": float(((d["q"] >= 0.5) == (y == 1)).mean()),
                         "model": float(((d["p_model"] >= 0.5) == (y == 1)).mean())}}
