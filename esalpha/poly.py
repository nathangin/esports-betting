"""Polymarket esports match markets and their pre-match prices (public data, read-only).

Used to test whether another exchange's price adds anything to Kalshi's. Writes into
``<state>/history/poly``:

  matches.parquet   one row per match-winner (moneyline) market: teams, game start, winner
  prices.parquet    1-minute price history of the first team's token around the game start
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .net import Http, HttpError

log = logging.getLogger(__name__)

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
# Polymarket "sports" series ids for esports leagues (from GET /sports, Oct 2026)
SERIES = {"cs2": 10310, "lol": 10311, "valorant": 10369, "dota2": 10309, "r6": 10432, "cod": 10427}


def _json_list(x) -> list:
    if isinstance(x, list):
        return x
    try:
        return json.loads(x or "[]")
    except (TypeError, ValueError):
        return []


def _time(s) -> datetime | None:
    if not s:
        return None
    s = str(s).replace("Z", "+00:00")
    if len(s) >= 3 and (s[-3] in "+-") and s[-2:].isdigit() and ":" not in s[-3:]:
        s = s + ":00"                       # "2026-10-04 16:00:00+00" -> "+00:00"
    try:
        return datetime.fromisoformat(s).astimezone(timezone.utc)
    except ValueError:
        return None


def match_rows(event: dict, game: str) -> list[dict]:
    rows = []
    for m in event.get("markets") or []:
        outcomes = _json_list(m.get("outcomes"))
        tokens = _json_list(m.get("clobTokenIds"))
        smt = (m.get("sportsMarketType") or "").lower()
        if len(outcomes) != 2 or len(tokens) != 2 or {o.lower() for o in outcomes} == {"yes", "no"}:
            continue
        if smt and smt != "moneyline":
            continue
        start = _time(m.get("gameStartTime")) or _time(event.get("startTime"))
        if start is None:
            continue
        prices = [float(p) for p in _json_list(m.get("outcomePrices")) or [] if p not in (None, "")]
        winner = None
        if len(prices) == 2 and m.get("closed"):
            winner = outcomes[0] if prices[0] > 0.99 else outcomes[1] if prices[1] > 0.99 else None
        rows.append({"event_id": str(event.get("id")), "market_id": str(m.get("id")), "game": game,
                     "title": event.get("title") or "", "question": m.get("question") or "",
                     "team_1": outcomes[0], "team_2": outcomes[1], "token_1": tokens[0], "token_2": tokens[1],
                     "start_time": start, "winner": winner, "volume": float(m.get("volume") or 0)})
    return rows


def fetch_matches(http: Http, since: datetime, manifest: dict, max_offset: int = 2000) -> pd.DataFrame:
    rows = []
    for game, sid in SERIES.items():
        n0, offset = len(rows), 0
        while offset < max_offset:
            try:
                evs = http.get_json(f"{GAMMA}/events", {"series_id": sid, "closed": "true", "limit": 100,
                                                         "offset": offset, "order": "endDate", "ascending": "false"},
                                    sample=f"poly_events_{game}")
            except HttpError as e:
                manifest["errors"].append(f"poly events {game} {offset}: {e}"[:200])
                break
            evs = evs if isinstance(evs, list) else evs.get("data", [])
            if not evs:
                break
            for e in evs:
                rows += match_rows(e, game)
            ends = [_time(e.get("endDate")) for e in evs]
            ends = [x for x in ends if x]
            offset += 100
            if ends and max(ends) < since:
                break
        log.info("polymarket %s: %d match markets", game, len(rows) - n0)
    df = pd.DataFrame(rows)
    if len(df):
        df = df.drop_duplicates("market_id")
        df = df[df["start_time"] >= pd.Timestamp(since)]
    manifest["poly_matches"] = {"rows": int(len(df)), "by_game": df.groupby("game").size().to_dict() if len(df) else {}}
    return df


def fetch_prices(http: Http, matches: pd.DataFrame, manifest: dict, minutes: float,
                 before_min: int = 180, after_min: int = 5) -> pd.DataFrame:
    rows, n, empty = [], 0, 0
    t_end = time.monotonic() + minutes * 60
    for r in matches.sort_values("start_time", ascending=False).itertuples(index=False):
        if time.monotonic() > t_end:
            manifest["errors"].append(f"poly prices stopped by time budget at {n} of {len(matches)}")
            break
        t0 = int((r.start_time - pd.Timedelta(minutes=before_min)).timestamp())
        t1 = int((r.start_time + pd.Timedelta(minutes=after_min)).timestamp())
        n += 1
        try:
            js = http.get_json(f"{CLOB}/prices-history", {"market": r.token_1, "startTs": t0, "endTs": t1,
                                                           "fidelity": 1}, sample="poly_prices")
        except HttpError as e:
            manifest["errors"].append(f"poly prices {r.market_id}: {e}"[:200])
            continue
        hist = js.get("history") if isinstance(js, dict) else js
        if not hist:
            empty += 1
            continue
        for h in hist:
            rows.append({"market_id": r.market_id, "ts": int(h.get("t")), "p": float(h.get("p"))})
    df = pd.DataFrame(rows, columns=["market_id", "ts", "p"])
    manifest["poly_prices"] = {"rows": int(len(df)), "markets": int(df["market_id"].nunique()) if len(df) else 0,
                               "fetched": n, "empty": empty}
    return df


def build(state_dir: str, since: str = "2026-08-01", minutes: float = 40) -> dict:
    out = Path(state_dir) / "history" / "poly"
    out.mkdir(parents=True, exist_ok=True)
    http = Http(sample_dir=out / "samples")
    manifest: dict = {"started": datetime.now(timezone.utc).isoformat(), "errors": [], "since": since}
    m = fetch_matches(http, datetime.fromisoformat(since).replace(tzinfo=timezone.utc), manifest)
    if len(m):
        m.to_parquet(out / "matches.parquet", index=False)
        p = fetch_prices(http, m, manifest, minutes)
        p.to_parquet(out / "prices.parquet", index=False)
    manifest["finished"] = datetime.now(timezone.utc).isoformat()
    manifest["http_calls"] = http.calls
    manifest["errors"] = manifest["errors"][:100]
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, default=str))
    return manifest
