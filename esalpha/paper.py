"""One paper-trading pass: settle finished bets, collect new results, look at every esports
match about to start on Kalshi, and place fake-money bets in three books.

Books (each starts with its own fake bankroll):
  blend       the model + market blend fitted by the backtest (the strategy under test)
  model-only  the Elo win model on its own, to show what ignoring the market does
  favourite   1% flat on the market favourite, a no-skill baseline

Each match is decided once, in the first run that finds it 10-70 minutes before its scheduled
start (runs every 15 minutes, so usually 55-70 minutes before; the backtest uses 60). Fills are at the displayed ask (or 1 - bid for
NO), capped at the size shown at that price, with Kalshi's taker fee.

Nothing here places real orders: Kalshi is only read through its public market-data API.
"""

from __future__ import annotations

import json
import logging
import uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import ratings as rt
from .history import build_matches, is_match_series, is_match_title, read_table
from .kalshi import Kalshi, Market, game_of
from .model import Params
from .net import Http
from .strategy import (Rules, default_rules, flat_candidates, flat_rules, match_candidates, market_prob,
                       settle_pnl, size)

log = logging.getLogger(__name__)

BOOKS = ("blend", "model-only", "favourite")
LEDGER_COLS = ["bet_id", "book", "model_version", "placed_at", "event_ticker", "series_ticker", "game", "tournament",
               "start_time", "minutes_to_start", "ticker", "market_team", "backs", "backs_side", "opponent", "side",
               "contracts", "price", "fee", "cost", "prob", "p_model", "q", "p_blend", "ev", "top_size", "status",
               "result", "winner", "settled_at", "pnl"]
TEXT_COLS = ["bet_id", "book", "model_version", "placed_at", "event_ticker", "series_ticker", "game", "tournament",
             "start_time", "ticker", "market_team", "backs", "backs_side", "opponent", "side", "status", "result",
             "winner", "settled_at"]
DEFAULT_CONFIG = {
    "bankroll": 1000.0,
    "lead_minutes": [10, 70],
    "flat_frac": 0.01,
    "rules": {"blend": {}, "model-only": {}, "favourite": {}},
}
MATCH_COLS = ["event_ticker", "series_ticker", "game", "start_time", "open_time", "close_time", "team_a", "team_b",
              "comp_a", "comp_b", "ticker_a", "ticker_b", "winner", "volume", "tournament"]


class State:
    def __init__(self, root: str | Path):
        self.state_root = Path(root)
        self.root = self.state_root / "paper"
        self.root.mkdir(parents=True, exist_ok=True)
        saved = self._json("config.json", {})
        self.config = {**DEFAULT_CONFIG, **saved}
        rules = {b: dict(r) for b, r in DEFAULT_CONFIG["rules"].items()}
        for b, r in (saved.get("rules") or {}).items():
            rules[b] = {**rules.get(b, {}), **r}
        self.config["rules"] = rules
        self.account = self._json("account.json", {})
        for b in BOOKS:
            self.account.setdefault(b, {"start": float(self.config["bankroll"]), "cash": float(self.config["bankroll"])})
        lp = self.root / "ledger.csv"
        self.ledger = pd.read_csv(lp, dtype={c: "object" for c in TEXT_COLS}) if lp.exists() \
            else pd.DataFrame(columns=LEDGER_COLS)
        for c in TEXT_COLS:
            if c in self.ledger:
                self.ledger[c] = self.ledger[c].astype("object")
        self.params = Params.load(self.state_root / "params" / "fitted.json")

    def _json(self, name, default):
        p = self.root / name
        return json.loads(p.read_text()) if p.exists() else default

    def rules(self, book: str) -> Rules:
        base = default_rules().to_dict()
        return Rules.from_dict({**base, **self.config.get("rules", {}).get(book, {})})

    def open_bets(self, book: str | None = None) -> pd.DataFrame:
        o = self.ledger[self.ledger["status"] == "open"]
        return o if book is None else o[o["book"] == book]

    def equity(self, book: str) -> float:
        o = self.open_bets(book)
        return float(self.account[book]["cash"] + (o["cost"].astype(float) + o["fee"].astype(float)).sum())

    def spent_on(self, book: str, day: date) -> float:
        led = self.ledger[self.ledger["book"] == book]
        if led.empty:
            return 0.0
        d = pd.to_datetime(led["placed_at"], utc=True).dt.date == day
        return float((led.loc[d, "cost"].astype(float) + led.loc[d, "fee"].astype(float)).sum())

    def save(self) -> None:
        self.ledger.to_csv(self.root / "ledger.csv", index=False)
        (self.root / "account.json").write_text(json.dumps(self.account, indent=1))
        (self.root / "config.json").write_text(json.dumps(self.config, indent=1))

    # ---- match tables
    def history_matches(self) -> pd.DataFrame:
        m = read_table(self.state_root / "history", "matches")
        return m if len(m) else pd.DataFrame(columns=MATCH_COLS)

    def paper_matches(self) -> pd.DataFrame:
        p = self.root / "matches.parquet"
        return pd.read_parquet(p) if p.exists() else pd.DataFrame(columns=MATCH_COLS)

    def all_matches(self) -> pd.DataFrame:
        frames = [f for f in (self.history_matches(), self.paper_matches()) if len(f)]
        if not frames:
            return pd.DataFrame(columns=MATCH_COLS)
        m = pd.concat([f[MATCH_COLS] for f in frames], ignore_index=True)
        m["game"] = m["series_ticker"].map(game_of)
        m["start_time"] = pd.to_datetime(m["start_time"], utc=True)
        m = m.dropna(subset=["start_time"])
        # later rows (paper results) win over the history copy of the same event
        return m.drop_duplicates("event_ticker", keep="last").sort_values("start_time").reset_index(drop=True)

    def match_series(self) -> list[str]:
        cfg = self.config.get("series")
        if cfg:
            return list(cfg)
        m = self.history_matches()
        return sorted(set(m["series_ticker"].dropna())) if len(m) else []

    def decided(self) -> set[str]:
        d = self.root / "scans"
        if not d.exists():
            return set()
        out = set()
        for p in sorted(d.glob("*.parquet"))[-3:]:
            out |= set(pd.read_parquet(p, columns=["event_ticker"])["event_ticker"])
        return out


# ---------------------------------------------------------------------------
# Settlement and results
# ---------------------------------------------------------------------------

def settle(state: State, k: Kalshi, now: datetime) -> int:
    o = state.open_bets()
    if o.empty:
        return 0
    mk = k.markets_by_ticker(o["ticker"].unique().tolist())
    n = 0
    for idx, b in o.iterrows():
        m = mk.get(b["ticker"])
        if m is None or not m.result:
            continue
        res = m.result
        pnl = settle_pnl(b["side"], int(b["contracts"]), float(b["price"]), float(b["fee"]), res)
        status = "void" if res not in ("yes", "no") else ("won" if res == b["side"] else "lost")
        state.ledger.loc[idx, ["status", "result", "winner", "settled_at", "pnl"]] = \
            [status, res, m.winner_name, now.isoformat(timespec="seconds"), pnl]
        acct = state.account[b["book"]]
        acct["cash"] = round(acct["cash"] + float(b["cost"]) + float(b["fee"]) + pnl, 4)
        n += 1
    return n


def _markets_frame(markets: list[Market]) -> pd.DataFrame:
    rows = [m.to_row() for m in markets if is_match_series(m.series_ticker) and is_match_title(m.title)]
    return pd.DataFrame(rows)


def update_results(state: State, k: Kalshi, now: datetime, series: list[str], days: int = 3) -> int:
    """Add recently settled matches to ``paper/matches.parquet`` so ratings stay current."""
    got = k.settled_markets(series, int((now - timedelta(days=days)).timestamp()))
    # matches we looked at that are still unresolved after 6 hours: ask for them by ticker
    want = []
    d = state.root / "scans"
    if d.exists():
        seen = pd.concat([pd.read_parquet(p, columns=["event_ticker", "ticker_a", "ticker_b", "start_time"])
                          for p in sorted(d.glob("*.parquet"))[-7:]], ignore_index=True)
        known = set(state.paper_matches()["event_ticker"]) | {m.event_ticker for m in got if m.result}
        old = seen[(pd.to_datetime(seen["start_time"], utc=True) < pd.Timestamp(now) - pd.Timedelta(hours=6))
                   & ~seen["event_ticker"].isin(known)]
        want = sorted(set(old["ticker_a"]) | set(old["ticker_b"]))
    if want:
        got += list(k.markets_by_ticker(want).values())
    df = _markets_frame([m for m in got if m.result in ("yes", "no", "void")])
    if df.empty:
        return 0
    new = build_matches(df)
    if new.empty:
        return 0
    new = new[new["winner"].notna()]
    old = state.paper_matches()
    allm = pd.concat([old, new], ignore_index=True) if len(old) else new
    allm = allm.drop_duplicates("event_ticker", keep="last")
    allm.to_parquet(state.root / "matches.parquet", index=False)
    return int(len(new))


def upcoming(markets: list[Market]) -> pd.DataFrame:
    """Two-team match events among open markets, team A = smaller ticker (as in the history)."""
    df = _markets_frame(markets)
    if df.empty:
        return df
    out = []
    for ev, g in df.groupby("event_ticker"):
        g = g.sort_values("ticker")
        if len(g) != 2 or g["competitor"].nunique() != 2 or g["start_time"].isna().any():
            continue
        a, b = g.iloc[0], g.iloc[1]
        out.append({"event_ticker": ev, "series_ticker": a["series_ticker"], "game": a["game"],
                    "start_time": a["start_time"], "open_time": a["open_time"], "close_time": a["close_time"],
                    "team_a": a["team"], "team_b": b["team"], "comp_a": a["competitor"], "comp_b": b["competitor"],
                    "ticker_a": a["ticker"], "ticker_b": b["ticker"], "winner": None,
                    "volume": float((a["volume"] or 0) + (b["volume"] or 0)), "tournament": a["tournament"],
                    "bid_a": a["yes_bid"], "ask_a": a["yes_ask"], "bid_b": b["yes_bid"], "ask_b": b["yes_ask"],
                    "bid_size_a": a["yes_bid_size"], "ask_size_a": a["yes_ask_size"],
                    "bid_size_b": b["yes_bid_size"], "ask_size_b": b["yes_ask_size"]})
    u = pd.DataFrame(out)
    if len(u):
        u["start_time"] = pd.to_datetime(u["start_time"], utc=True)
    return u


# ---------------------------------------------------------------------------
# Scan and bet
# ---------------------------------------------------------------------------

def _nz(x):
    return None if x is None or (isinstance(x, float) and np.isnan(x)) else x


def scan(state: State, k: Kalshi, now: datetime, series: list[str]) -> tuple[list[dict], list[dict]]:
    up = upcoming(k.open_markets(series))
    if up.empty:
        return [], []
    lo, hi = state.config.get("lead_minutes", [10, 70])
    up["minutes_to_start"] = (up["start_time"] - pd.Timestamp(now)).dt.total_seconds() / 60.0
    decided = state.decided()
    # matches already under way that this trader never decided on (late runs, late markets)
    state.missed = int(((up["minutes_to_start"] < lo) & ~up["event_ticker"].isin(decided)).sum())
    record_closes(state, up[up["event_ticker"].isin(decided)], now)
    todo = up[(up["minutes_to_start"] >= lo) & (up["minutes_to_start"] <= hi) & ~up["event_ticker"].isin(decided)]
    if todo.empty:
        return [], []
    params = state.params
    hist = state.all_matches()
    hist = hist[~hist["event_ticker"].isin(todo["event_ticker"])]
    frame = pd.concat([hist, todo[MATCH_COLS]], ignore_index=True)
    feats = rt.pre_match_features(frame, params.elo_configs())
    feats = feats[feats["event_ticker"].isin(todo["event_ticker"])].set_index("event_ticker")
    run_at = now.isoformat(timespec="seconds")
    day = now.date()
    budget = {b: max(state.rules(b).max_run_frac * state.equity(b) - state.spent_on(b, day), 0.0) for b in BOOKS}
    scans, placed = [], []
    for r in todo.sort_values("start_time").itertuples(index=False):
        q = market_prob(_nz(r.bid_a), _nz(r.ask_a), _nz(r.bid_b), _nz(r.ask_b))
        if q is None:
            log.info("%s: no two-sided quotes yet", r.event_ticker)
            continue
        f = feats.loc[[r.event_ticker]]
        p_model = float(params.p_model(f)[0])
        pb = params.p_blend(p_model, q)
        p_blend = None if pb is None else float(pb[0])
        fr = f.iloc[0]
        row = {"run_at": run_at, "event_ticker": r.event_ticker, "series_ticker": r.series_ticker, "game": r.game,
               "tournament": r.tournament, "start_time": r.start_time.isoformat(),
               "minutes_to_start": round(float(r.minutes_to_start), 1), "team_a": r.team_a, "team_b": r.team_b,
               "comp_a": r.comp_a, "comp_b": r.comp_b, "ticker_a": r.ticker_a, "ticker_b": r.ticker_b,
               "bid_a": _nz(r.bid_a), "ask_a": _nz(r.ask_a), "bid_b": _nz(r.bid_b), "ask_b": _nz(r.ask_b),
               "volume": r.volume, "q": round(q, 4), "p_elo": round(float(fr["p_elo"]), 4),
               "p_model": round(p_model, 4), "p_blend": None if p_blend is None else round(p_blend, 4),
               "elo_a": round(float(fr["elo_a"]), 1), "elo_b": round(float(fr["elo_b"]), 1),
               "games_a": int(fr["games_a"]), "games_b": int(fr["games_b"]), "model_version": params.version}
        a = {"ticker": r.ticker_a, "yes_bid": _nz(r.bid_a), "yes_ask": _nz(r.ask_a),
             "bid_size": _nz(r.bid_size_a), "ask_size": _nz(r.ask_size_a)}
        b = {"ticker": r.ticker_b, "yes_bid": _nz(r.bid_b), "yes_ask": _nz(r.ask_b),
             "bid_size": _nz(r.bid_size_b), "ask_size": _nz(r.ask_size_b)}
        for book in BOOKS:
            rules = state.rules(book)
            eq, cash = state.equity(book), state.account[book]["cash"]
            if book == "favourite":
                cands = flat_candidates(r.event_ticker, q >= 0.5, a, b, rules)
                bets = size(cands, eq, cash, flat_rules(rules, state.config.get("flat_frac", 0.01)),
                            run_budget=budget[book])
            else:
                prob = p_blend if book == "blend" else p_model
                if prob is None or not state.params.win_w:
                    row[f"bet_{book}"] = "no params" if not state.params.win_w else "no blend"
                    continue
                if abs(prob - q) > rules.max_gap:
                    row[f"bet_{book}"] = f"skip: model/market gap {abs(prob - q):.2f}"
                    continue
                bets = size(match_candidates(r.event_ticker, prob, a, b, rules), eq, cash, rules,
                            run_budget=budget[book])
            for bt in bets:
                rec = _record(state, book, now, r, bt, p_model, q, p_blend)
                placed.append(rec)
                budget[book] -= bt.outlay
                row[f"bet_{book}"] = f"{bt.side.upper()} {rec['market_team']} x{bt.contracts} @ {bt.price:.2f}"
        scans.append(row)
    return scans, placed


def record_closes(state: State, up: pd.DataFrame, now: datetime, window=(-10.0, 15.0)) -> int:
    """Snapshot the market near the scheduled start of matches already decided on: the
    closing line used to score bets (closing-line value). Keeps the snapshot nearest the start."""
    near = up[(up["minutes_to_start"] >= window[0]) & (up["minutes_to_start"] < window[1])]
    rows = []
    for r in near.itertuples(index=False):
        q = market_prob(_nz(r.bid_a), _nz(r.ask_a), _nz(r.bid_b), _nz(r.ask_b))
        if q is not None:
            rows.append({"event_ticker": r.event_ticker, "at": now.isoformat(timespec="seconds"),
                         "minutes_to_start": round(float(r.minutes_to_start), 1), "q_close": round(q, 4)})
    if not rows:
        return 0
    path = state.root / "closes.csv"
    old = pd.read_csv(path) if path.exists() else None
    df = pd.concat([old, pd.DataFrame(rows)], ignore_index=True) if old is not None else pd.DataFrame(rows)
    df = df.assign(dist=df["minutes_to_start"].abs()).sort_values("dist").drop_duplicates("event_ticker")
    df.drop(columns="dist").sort_values("at").to_csv(path, index=False)
    return len(rows)


def _record(state: State, book: str, now: datetime, r, bt, p_model, q, p_blend) -> dict:
    is_a = bt.ticker == r.ticker_a
    market_team = r.team_a if is_a else r.team_b
    backs = bt.extra.get("backs")
    backs_team = r.team_a if backs == "A" else r.team_b
    prob = bt.prob
    if book == "favourite":   # flat bets carry no model view; record the market's probability instead
        prob = q if backs == "A" else 1 - q
    rec = {"bet_id": uuid.uuid4().hex[:12], "book": book, "model_version": state.params.version,
           "placed_at": now.isoformat(timespec="seconds"), "event_ticker": r.event_ticker,
           "series_ticker": r.series_ticker, "game": r.game, "tournament": r.tournament,
           "start_time": r.start_time.isoformat(), "minutes_to_start": round(float(r.minutes_to_start), 1),
           "ticker": bt.ticker, "market_team": market_team, "backs": backs_team, "backs_side": backs,
           "opponent": r.team_b if backs == "A" else r.team_a, "side": bt.side, "contracts": bt.contracts,
           "price": bt.price, "fee": bt.fee, "cost": bt.cost, "prob": round(float(prob), 4),
           "p_model": round(p_model, 4), "q": round(q, 4), "p_blend": None if p_blend is None else round(p_blend, 4),
           "ev": round(bt.ev, 4), "top_size": bt.extra.get("max_size"), "status": "open", "result": None,
           "winner": None, "settled_at": None, "pnl": None}
    state.ledger = pd.concat([state.ledger, pd.DataFrame([rec])], ignore_index=True) if len(state.ledger) \
        else pd.DataFrame([rec], columns=LEDGER_COLS)
    for c in TEXT_COLS:
        state.ledger[c] = state.ledger[c].astype("object")
    acct = state.account[book]
    acct["cash"] = round(acct["cash"] - bt.cost - bt.fee, 4)
    return rec


# ---------------------------------------------------------------------------

def run(state_dir: str, now: datetime | None = None, until: str | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    state = State(state_dir)
    summary: dict = {"run_at": now.isoformat(timespec="seconds"), "params": state.params.version}
    http = Http(sample_dir=state.root / "samples")
    k = Kalshi(http)
    summary["settled"] = settle(state, k, now)
    series = state.match_series()
    summary["series"] = len(series)
    if not series:
        summary["skipped"] = "no match series known yet; run `esalpha history` first"
    else:
        summary["results_added"] = update_results(state, k, now, series)
        if until and now.date() > date.fromisoformat(until):
            summary["scan"] = f"paper trial ended {until}; settling only"
        else:
            scans, placed = scan(state, k, now, series)
            summary["matches_decided"] = len(scans)
            summary["open_matches_missed"] = getattr(state, "missed", 0)
            summary["bets_placed"] = {b: sum(1 for p in placed if p["book"] == b) for b in BOOKS}
            if scans:
                sp = state.root / "scans" / f"{now:%Y-%m-%d}.parquet"
                sp.parent.mkdir(parents=True, exist_ok=True)
                new = pd.DataFrame(scans)
                old = pd.read_parquet(sp) if sp.exists() else None
                (pd.concat([old, new], ignore_index=True) if old is not None else new).to_parquet(sp, index=False)
    state.save()
    summary["http_calls"] = http.calls
    summary["equity"] = {b: round(state.equity(b), 2) for b in BOOKS}
    with (state.root / "runs.jsonl").open("a") as fh:
        fh.write(json.dumps(summary, default=str) + "\n")
    return summary
