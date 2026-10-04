"""Plain-markdown report of the paper trial and the latest backtest (state/reports/summary.md)."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import ratings as rt
from .paper import BOOKS, State

BOOK_NOTES = {
    "blend": "model + market blend (the strategy under test)",
    "model-only": "Elo win model alone (control: ignores the market)",
    "favourite": "1% flat on the market favourite (no-skill baseline)",
}


def _money(x) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-"
    return f"-${abs(x):,.2f}" if x < 0 else f"${x:,.2f}"


def _pct(x, digits=1) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-"
    return f"{100 * x:+.{digits}f}%"


def _closes(state: State) -> dict:
    p = state.root / "closes.csv"
    if not p.exists():
        return {}
    c = pd.read_csv(p)
    return dict(zip(c["event_ticker"], c["q_close"]))


def book_stats(state: State) -> dict:
    led = state.ledger.copy()
    closes = _closes(state)
    if len(led) and "backs_side" in led:
        # closing-line value: the market's probability, near the start, of the team the bet backs,
        # minus the price paid
        qc = led["event_ticker"].map(closes).astype(float)
        side_close = np.where(led["backs_side"] == "A", qc, 1 - qc)
        led["clv"] = side_close - led["price"].astype(float)
    else:
        led["clv"] = np.nan
    out = {}
    for b in BOOKS:
        lb = led[led["book"] == b]
        done = lb[lb["status"].isin(["won", "lost"])]
        outlay = float((done["cost"].astype(float) + done["fee"].astype(float)).sum()) if len(done) else 0.0
        pnl = float(done["pnl"].astype(float).sum()) if len(done) else 0.0
        out[b] = {"start": state.account[b]["start"], "equity": round(state.equity(b), 2),
                  "cash": round(state.account[b]["cash"], 2), "bets": int(len(lb)),
                  "open": int((lb["status"] == "open").sum()), "settled": int(len(done)),
                  "won": int((done["status"] == "won").sum()), "void": int((lb["status"] == "void").sum()),
                  "pnl": round(pnl, 2), "outlay": round(outlay, 2), "roi": pnl / outlay if outlay else None,
                  "fees": round(float(lb["fee"].astype(float).sum()), 2) if len(lb) else 0.0,
                  "avg_clv": float(lb["clv"].mean()) if len(lb) and lb["clv"].notna().any() else None,
                  "clv_n": int(lb["clv"].notna().sum()) if len(lb) else 0}
    return out


def scoring(state: State) -> dict:
    """How good were the probabilities on every match the trader looked at (bet or not)?"""
    d = state.root / "scans"
    files = sorted(d.glob("*.parquet")) if d.exists() else []
    if not files:
        return {"n": 0}
    s = pd.concat([pd.read_parquet(p) for p in files], ignore_index=True).drop_duplicates("event_ticker", keep="first")
    res = state.all_matches()[["event_ticker", "winner"]]
    s = s.merge(res, on="event_ticker", how="inner")
    s = s[s["winner"].isin(["A", "B"])]
    if s.empty:
        return {"n": 0, "scanned": int(len(files))}
    y = (s["winner"] == "A").astype(float)
    out = {"n": int(len(s)), "log_loss": {"market": rt.log_loss(s["q"], y), "model": rt.log_loss(s["p_model"], y)},
           "brier": {"market": rt.brier(s["q"], y), "model": rt.brier(s["p_model"], y)}}
    sb = s.dropna(subset=["p_blend"])
    if len(sb):
        yb = (sb["winner"] == "A").astype(float)
        out["log_loss"]["blend"] = rt.log_loss(sb["p_blend"], yb)
        out["brier"]["blend"] = rt.brier(sb["p_blend"], yb)
        out["log_loss"]["market (same matches)"] = rt.log_loss(sb["q"], yb)
        out["n_blend"] = int(len(sb))
    out["by_game"] = {g: {"n": int(len(x)), "market": rt.log_loss(x["q"], (x["winner"] == "A").astype(float)),
                          "model": rt.log_loss(x["p_model"], (x["winner"] == "A").astype(float))}
                      for g, x in s.groupby("game")}
    return out


def write(state_dir: str) -> dict:
    state = State(state_dir)
    books = book_stats(state)
    sc = scoring(state)
    bt_path = state.state_root / "reports" / "backtest.json"
    bt = json.loads(bt_path.read_text()) if bt_path.exists() else None
    now = datetime.now(timezone.utc)
    L = [f"# Esports paper trading (fake money)", "",
         f"Updated {now:%Y-%m-%d %H:%M} UTC. Model fitted {state.params.version}. Every bet below is simulated: "
         "the trader only reads Kalshi's public market data and never places orders.", "",
         "## Books", "",
         "| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |",
         "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for b, s in books.items():
        clv = "-" if s.get("avg_clv") is None else f"{100 * s['avg_clv']:+.1f}c ({s['clv_n']})"
        L.append(f"| {b} | {BOOK_NOTES[b]} | {s['bets']} | {s['open']} | {s['settled']} | {s['won']} | "
                 f"{_money(s['pnl'])} | {_pct(s['roi'])} | {clv} | {_money(s['equity'])} |")
    L += ["", "Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. "
          "Closing-line value is the market's probability of the backed team near the start minus the price "
          "paid (bets with a snapshot); it shows skill long before P&L can.", ""]
    L += ["## Forecast scoring on the matches the trader looked at", ""]
    if sc.get("n"):
        L += [f"{sc['n']} finished matches. Lower is better; the market line is the bar to beat.", "",
              "| Forecast | Log loss | Brier |", "|---|---:|---:|"]
        for k in ("market", "model", "blend"):
            if k in sc["log_loss"]:
                L.append(f"| {k} | {sc['log_loss'][k]:.4f} | {sc['brier'][k]:.4f} |")
        if sc.get("by_game"):
            L += ["", "| Game | Matches | Market log loss | Model log loss |", "|---|---:|---:|---:|"]
            for g, x in sorted(sc["by_game"].items(), key=lambda kv: -kv[1]["n"]):
                L.append(f"| {g} | {x['n']} | {x['market']:.4f} | {x['model']:.4f} |")
    else:
        L.append("No finished matches yet.")
    L.append("")
    led = state.ledger
    if len(led):
        L += ["## Latest bets", "", "| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |",
              "|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|"]
        for _, r in led.sort_values("placed_at", ascending=False).head(25).iterrows():
            L.append(f"| {str(r['placed_at'])[:16].replace('T', ' ')} | {r['book']} | {r['game']} | {r['backs']} | "
                     f"{r['opponent']} | {str(r['side']).upper()} {r['market_team']} | {int(r['contracts'])} | "
                     f"{float(r['price']):.2f} | {float(r['prob']):.2f} | {float(r['q']):.2f} | {r['status']} | "
                     f"{_money(None if pd.isna(r['pnl']) else float(r['pnl']))} |")
        L.append("")
    if bt:
        L += backtest_section(bt)
    out = state.state_root / "reports"
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.md").write_text("\n".join(L) + "\n")
    rep = {"generated": now.isoformat(), "books": books, "scoring": sc}
    (out / "summary.json").write_text(json.dumps(rep, indent=1, default=str))
    return rep


def backtest_section(bt: dict) -> list[str]:
    L = ["## Backtest on real Kalshi prices", "",
         f"{bt['matches_tested']} settled matches from {bt['period'][0][:10]} to {bt['period'][1][:10]}, "
         f"decided {bt['decision']} at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model "
         "and the blend only ever use earlier matches (weekly walk-forward refits).", "",
         "| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |",
         "|---|---:|---:|---:|---:|---|---:|---:|---:|"]
    for name, r in bt["results"].items():
        if not r.get("bets"):
            L.append(f"| {name} | 0 | - | - | - | - | - | - | - |")
            continue
        ci = r.get("roi_ci95") or [None, None]
        clv = r.get("avg_clv")
        L.append(f"| {name} | {r['bets']} | {_money(r['outlay'])} | {_money(r['pnl'])} | {_pct(r['roi'])} | "
                 f"{_pct(ci[0])} to {_pct(ci[1])} | {100 * r['hit_rate']:.0f}% | "
                 f"{'-' if clv is None or clv != clv else f'{100 * clv:+.1f}c'} | {100 * r['max_drawdown']:.0f}% |")
    L += ["", "Closing-line value: the market's probability at the scheduled start of the side bought, minus the "
          "price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in "
          "by the start."]
    s = bt.get("scores") or {}
    if s.get("n"):
        L += ["", f"Forecast quality on the same {s['n']} matches (lower is better):", "",
              "| Forecast | Log loss | Brier | Picks the winner |", "|---|---:|---:|---:|"]
        for k in ("market", "model", "blend"):
            acc = s.get("accuracy", {}).get(k)
            L.append(f"| {k} | {s['log_loss'][k]:.4f} | {s['brier'][k]:.4f} | "
                     f"{'-' if acc is None else f'{100 * acc:.1f}%'} |")
    if bt.get("market_calibration"):
        L += ["", "Is the market's favourite priced right?", "",
              "| Market favourite at | Matches | Average price | Won |", "|---|---:|---:|---:|"]
        for c in bt["market_calibration"]:
            L.append(f"| {c['favourite_prob']} | {c['n']} | {c['mean_p']:.3f} | {c['won']:.3f} |")
    L.append("")
    return L
