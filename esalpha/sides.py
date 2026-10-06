"""Side markets of each esports match: map winner, total maps and spread (handicap).

Kalshi lists them as separate series (KXCS2MAP, KXCS2TOTALMAPS, KXCS2SPREAD, ...) whose
event tickers carry the same match code as the match-winner event:

  KXCODGAME-26AUG091500OGHTCS        match winner (one market per team)
  KXCODMAP-26AUG091500OGHTCS-1       map 1 winner (one market per team)
  KXCODTOTALMAPS-26AUG091500OGHTCS   "over N.5 maps" ladder
  KXCODSPREAD-26AUG091500OGHTCS      "team wins by over N.5 maps"

They are thinner than the match market, so if their prices disagree with what the match
price implies, that is a candidate edge. This module downloads them (read-only, public API)
into ``<state>/history/sides``:

  markets/   one row per settled side market (kind, match code, map number, strike, team, result)
  candles/   1-minute bid/ask around the decision time for side events of priced matches
"""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .history import read_table, write_table
from .kalshi import Kalshi, _f, game_of, parse_time, qty
from .net import Http, HttpError

log = logging.getLogger(__name__)

SIDE_SERIES = re.compile(r"^KX([A-Z0-9]+?)(SPREAD|TOTALMAPS|MAP)$")
KINDS = {"SPREAD": "spread", "TOTALMAPS": "total", "MAP": "map"}
COLS = ["ticker", "event_ticker", "series_ticker", "kind", "game", "code", "map_no", "strike", "team", "competitor",
        "title", "result", "volume", "open_time", "close_time"]


def side_kind(series_ticker: str) -> str | None:
    m = SIDE_SERIES.match(series_ticker or "")
    return KINDS[m.group(2)] if m else None


def side_game(series_ticker: str) -> str:
    """Same game labels as the match series (KXRLSPREAD -> rl, like KXRLGAME)."""
    m = SIDE_SERIES.match(series_ticker or "")
    return game_of(f"KX{m.group(1)}GAME") if m else game_of(series_ticker)


def match_code(event_ticker: str, series_ticker: str) -> tuple[str, int | None]:
    """Match code and map number from a side event ticker (``KXCODMAP-26AUG091500OGHTCS-5``)."""
    parts = (event_ticker or "")[len(series_ticker) + 1:].split("-")
    map_no = int(parts[1]) if side_kind(series_ticker) == "map" and len(parts) > 1 and parts[1].isdigit() else None
    return parts[0], map_no


def parse_side(m: dict, series_ticker: str) -> dict:
    event = m.get("event_ticker") or m.get("ticker", "").rsplit("-", 1)[0]
    code, map_no = match_code(event, series_ticker)
    cs = m.get("custom_strike") or {}
    result = (m.get("result") or "").lower()
    return {"ticker": m.get("ticker"), "event_ticker": event, "series_ticker": series_ticker,
            "kind": side_kind(series_ticker), "game": side_game(series_ticker), "code": code, "map_no": map_no,
            "strike": _f(m.get("floor_strike")), "team": m.get("yes_sub_title") or "",
            "competitor": cs.get("esports_competitor") or cs.get("competitor"), "title": m.get("title") or "",
            "result": result if result in ("yes", "no", "void") else "", "volume": qty(m, "volume"),
            "open_time": parse_time(m.get("open_time")), "close_time": parse_time(m.get("close_time"))}


def fetch_markets(k: Kalshi, hist: Path, manifest: dict, max_pages: int = 40) -> pd.DataFrame:
    p = hist / "series.json"
    series = [s["ticker"] for s in json.loads(p.read_text())] if p.exists() else []
    series = [s for s in series if side_kind(s)]
    rows = []
    for tk in series:
        n0 = len(rows)
        for path, params in (("/markets", {"status": "settled"}), ("/historical/markets", {})):
            try:
                for m in k.iter_markets(path=path, max_pages=max_pages, series_ticker=tk, **params):
                    rows.append(parse_side(m, tk))
            except HttpError as e:
                manifest["errors"].append(f"{tk} {path}: {e}"[:200])
        log.info("%s: %d side markets", tk, len(rows) - n0)
    df = pd.DataFrame(rows, columns=COLS).drop_duplicates("ticker")
    if len(df):
        write_table(hist / "sides", "markets", df.sort_values(["close_time", "ticker"]), "close_time")
    manifest["side_markets"] = {"rows": int(len(df)),
                                "by_series": df.groupby("series_ticker").size().to_dict() if len(df) else {}}
    return df


def fetch_candles(k: Kalshi, hist: Path, sides: pd.DataFrame, manifest: dict, days: int = 90,
                  minutes: float = 90, before_min: int = 75, after_min: int = 3) -> pd.DataFrame:
    """Candles for the side events (total maps, spread, map 1) of matches that have match
    candles, over [start - before_min, start + after_min]."""
    out_hist = hist / "sides"
    matches = read_table(hist, "matches")
    mc = read_table(hist, "candles")
    if matches.empty or mc.empty or sides.empty:
        return pd.DataFrame()
    matches["start_time"] = pd.to_datetime(matches["start_time"], utc=True)
    priced = set(mc["event_ticker"].unique())
    matches = matches[matches["event_ticker"].isin(priced) & matches["start_time"].notna()]
    matches = matches[matches["start_time"] >= pd.Timestamp(datetime.now(timezone.utc)) - pd.Timedelta(days=days)]
    matches = matches.assign(code=[e.split("-", 1)[1] if "-" in e else e for e in matches["event_ticker"]])
    start_by_code = dict(zip(matches["code"], matches["start_time"]))
    ev = sides[sides["code"].isin(start_by_code) & ((sides["kind"] != "map") | (sides["map_no"] == 1))]
    ev = ev.drop_duplicates("event_ticker")[["event_ticker", "series_ticker", "code"]]
    old = read_table(out_hist, "candles")
    done = set(old["event_ticker"].unique()) if len(old) else set()
    todo = ev[~ev["event_ticker"].isin(done)].copy()
    todo["start"] = todo["code"].map(start_by_code)
    todo = todo.sort_values("start", ascending=False)
    t_end = time.monotonic() + minutes * 60
    rows, n, empty = [], 0, 0

    def save(rows, old):
        new = pd.DataFrame(rows, columns=["event_ticker", "ticker", "ts", "bid", "ask", "price", "volume"])
        df = pd.concat([old, new], ignore_index=True) if len(old) else new
        df = df.drop_duplicates(["ticker", "ts"], keep="last").reset_index(drop=True)
        if len(df):
            write_table(out_hist, "candles", df, "ts")
        return df

    for r in todo.itertuples(index=False):
        if time.monotonic() > t_end:
            manifest["errors"].append(f"side candles stopped by time budget, {len(todo) - n} events left")
            break
        t0 = int((r.start - pd.Timedelta(minutes=before_min)).timestamp())
        t1 = int((r.start + pd.Timedelta(minutes=after_min)).timestamp())
        n += 1
        try:
            got = k.event_candles(r.series_ticker, r.event_ticker, t0, t1, period=1)
        except HttpError as e:
            if e.status not in (400, 404):
                manifest["errors"].append(f"side candles {r.event_ticker}: {e}"[:200])
            got = {}
        if not any(got.values()):
            empty += 1
            continue
        for tkr, cs in got.items():
            for c in cs:
                rows.append({"event_ticker": r.event_ticker, "ticker": tkr, **c})
        if n % 300 == 0:
            log.info("side candles: %d events", n)
            old, rows = save(rows, old), []
    df = save(rows, old)
    manifest["side_candles"] = {"rows": int(len(df)), "events": int(df["event_ticker"].nunique()) if len(df) else 0,
                                "fetched_now": n, "empty": empty, "todo": int(len(todo))}
    return df


def build(state_dir: str, days: int = 90, minutes: float = 90) -> dict:
    hist = Path(state_dir) / "history"
    http = Http(sample_dir=hist / "sides" / "samples")
    k = Kalshi(http)
    manifest: dict = {"started": datetime.now(timezone.utc).isoformat(), "errors": [], "args": {"days": days}}
    sides = fetch_markets(k, hist, manifest)
    fetch_candles(k, hist, sides, manifest, days=days, minutes=minutes)
    manifest["finished"] = datetime.now(timezone.utc).isoformat()
    manifest["http_calls"] = http.calls
    manifest["errors"] = manifest["errors"][:200]
    (hist / "sides").mkdir(parents=True, exist_ok=True)
    (hist / "sides" / "manifest.json").write_text(json.dumps(manifest, indent=1, default=str))
    return manifest
