"""Download the esports history: every settled Kalshi esports match, plus pre-match price
candles for recent matches (for the fake-money backtest).

Writes into ``<state>/history``:
  series.json        all esports series Kalshi lists, with fee settings
  markets/           one row per settled market (team, competitor id, result, times)
  matches/           one row per two-team match event (team A/B, winner, scheduled start)
  candles/           1-minute bid/ask candles for the last hours before each recent match
  manifest.json      counts and any errors

Tables are stored as monthly parquet shards (``matches/2026-09.parquet``) and a shard is only
rewritten when its rows change, so the daily refresh adds little to the state branch.
"""

from __future__ import annotations

import json
import logging
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from .kalshi import Kalshi, parse_market
from .net import Http, HttpError

log = logging.getLogger(__name__)

MATCH_TITLE = re.compile(r"^Will (.+?) win the (.+?) vs\.? (.+?) match\??$", re.I)
MARKET_COLS = ["ticker", "event_ticker", "series_ticker", "game", "team", "competitor", "title", "status",
               "result", "winner_name", "volume", "last_price", "open_time", "close_time", "start_time", "tournament"]


def write_table(hist: Path, name: str, df: pd.DataFrame, time_col: str) -> None:
    """Save ``df`` as monthly shards ``<hist>/<name>/YYYY-MM.parquet`` (by ``time_col``)."""
    d = hist / name
    d.mkdir(parents=True, exist_ok=True)
    t = df[time_col]
    t = pd.to_datetime(t, unit="s", utc=True) if pd.api.types.is_numeric_dtype(t) else pd.to_datetime(t, utc=True)
    month = t.dt.strftime("%Y-%m").fillna("unknown")
    for mo, g in df.groupby(month, sort=True):
        g = g.reset_index(drop=True)
        path = d / f"{mo}.parquet"
        if path.exists():
            try:
                if pd.read_parquet(path).equals(g):
                    continue
            except Exception:  # noqa: BLE001 - unreadable shard: rewrite it
                pass
        g.to_parquet(path, index=False)
    legacy = hist / f"{name}.parquet"
    if legacy.exists():
        legacy.unlink()


def read_table(hist: Path, name: str) -> pd.DataFrame:
    """All shards of a history table (also reads an older single-file ``<name>.parquet``)."""
    hist = Path(hist)
    frames = [pd.read_parquet(p) for p in sorted((hist / name).glob("*.parquet"))] if (hist / name).is_dir() else []
    legacy = hist / f"{name}.parquet"
    if legacy.exists():
        frames.append(pd.read_parquet(legacy))
    frames = [f for f in frames if len(f)]
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def fetch_series(k: Kalshi, hist: Path, manifest: dict) -> list[dict]:
    series = k.esports_series()
    keep = [{"ticker": s.get("ticker"), "title": s.get("title"), "fee_type": s.get("fee_type"),
             "fee_multiplier": s.get("fee_multiplier"), "frequency": s.get("frequency")} for s in series]
    (hist / "series.json").write_text(json.dumps(keep, indent=1))
    manifest["series"] = len(keep)
    return keep


def fetch_markets(k: Kalshi, series: list[dict], hist: Path, manifest: dict, max_hist_pages: int = 30) -> pd.DataFrame:
    rows = []
    for s in series:
        tk = s["ticker"]
        n0 = len(rows)
        for path, params, pages in (("/markets", {"status": "settled"}, 40), ("/historical/markets", {}, max_hist_pages)):
            try:
                for m in k.iter_markets(path=path, max_pages=pages, series_ticker=tk, **params):
                    if not MATCH_TITLE.match((m.get("title") or "").strip()):
                        continue
                    mk = parse_market(m, tk).to_row()
                    rows.append({c: mk.get(c) for c in MARKET_COLS})
            except HttpError as e:
                manifest["errors"].append(f"{tk} {path}: {e}"[:200])
        if len(rows) > n0:
            log.info("%s: %d match markets", tk, len(rows) - n0)
    df = pd.DataFrame(rows, columns=MARKET_COLS).drop_duplicates("ticker")
    write_table(hist, "markets", df.sort_values(["close_time", "ticker"]), "close_time")
    manifest["markets"] = {"rows": int(len(df)), "events": int(df["event_ticker"].nunique()),
                           "by_game": df.groupby("game")["event_ticker"].nunique().to_dict()}
    return df


def build_matches(markets: pd.DataFrame) -> pd.DataFrame:
    """One row per event with exactly two team markets; team A is the market with the smaller ticker."""
    out = []
    for ev, g in markets.groupby("event_ticker"):
        g = g.sort_values("ticker")
        if len(g) != 2 or g["competitor"].nunique() != 2:
            continue
        a, b = g.iloc[0], g.iloc[1]
        res = (a["result"], b["result"])
        winner = "A" if res == ("yes", "no") else "B" if res == ("no", "yes") else None
        start = a["start_time"] if pd.notna(a["start_time"]) else b["start_time"]
        out.append({"event_ticker": ev, "series_ticker": a["series_ticker"], "game": a["game"],
                    "start_time": start, "open_time": min(a["open_time"], b["open_time"]),
                    "close_time": max(a["close_time"], b["close_time"]),
                    "team_a": a["team"], "team_b": b["team"], "comp_a": a["competitor"], "comp_b": b["competitor"],
                    "ticker_a": a["ticker"], "ticker_b": b["ticker"], "winner": winner,
                    "volume": float((a["volume"] or 0) + (b["volume"] or 0)), "tournament": a["tournament"]})
    df = pd.DataFrame(out)
    if len(df):
        df = df.sort_values("start_time").reset_index(drop=True)
    return df


def fetch_candles(k: Kalshi, hist: Path, matches: pd.DataFrame, days: int, hours_before: float,
                  manifest: dict, minutes: float) -> pd.DataFrame:
    """1-minute candles for the ``hours_before`` hours up to each match's scheduled start."""
    old = read_table(hist, "candles")
    old = old if len(old) else None
    done = set(old["event_ticker"].unique()) if old is not None else set()
    t_end = time.monotonic() + minutes * 60
    cutoff = pd.Timestamp(datetime.now(timezone.utc) - timedelta(days=days))
    todo = matches[(pd.to_datetime(matches["start_time"], utc=True) >= cutoff) & matches["winner"].notna()
                   & ~matches["event_ticker"].isin(done)].sort_values("start_time", ascending=False)
    rows, n, empty = [], 0, 0
    for r in todo.itertuples():
        if time.monotonic() > t_end:
            manifest["errors"].append(f"candles stopped by time budget, {len(todo) - n} events left")
            break
        start = pd.Timestamp(r.start_time)
        t0 = int((max(start - pd.Timedelta(hours=hours_before), pd.Timestamp(r.open_time))).timestamp())
        t1 = int((start + pd.Timedelta(minutes=5)).timestamp())
        if t1 <= t0:
            continue
        got = {}
        try:
            got = k.event_candles(r.series_ticker, r.event_ticker, t0, t1, period=1)
        except HttpError as e:
            if e.status not in (400, 404):
                manifest["errors"].append(f"candles {r.event_ticker}: {e}"[:200])
        if not got:
            for tkr in (r.ticker_a, r.ticker_b):
                got[tkr] = k.market_candles(r.series_ticker, tkr, t0, t1, period=1)
        n += 1
        if not any(got.values()):
            empty += 1
            continue
        for tkr, cs in got.items():
            for c in cs:
                rows.append({"event_ticker": r.event_ticker, "ticker": tkr, **c})
        if n % 250 == 0:
            log.info("candles: %d events", n)
            old, rows = _save(old, rows, hist), []
    df = _save(old, rows, hist)
    manifest["candles"] = {"rows": int(len(df)), "events": int(df["event_ticker"].nunique()) if len(df) else 0,
                           "fetched_now": n, "empty": empty}
    return df


def _save(old, rows, hist: Path) -> pd.DataFrame:
    new = pd.DataFrame(rows, columns=["event_ticker", "ticker", "ts", "bid", "ask", "price", "volume"])
    df = pd.concat([old, new], ignore_index=True) if old is not None and len(new) else (old if old is not None else new)
    df = df.drop_duplicates(["ticker", "ts"], keep="last").reset_index(drop=True)
    if len(df):
        write_table(hist, "candles", df, "ts")
    return df


def build(state_dir: str, days: int = 150, hours_before: float = 6.0, minutes: float = 90) -> dict:
    hist = Path(state_dir) / "history"
    hist.mkdir(parents=True, exist_ok=True)
    http = Http(sample_dir=hist / "samples")
    k = Kalshi(http)
    manifest: dict = {"started": datetime.now(timezone.utc).isoformat(), "errors": [],
                      "args": {"days": days, "hours_before": hours_before}}
    t0 = time.time()
    series = fetch_series(k, hist, manifest)
    markets = fetch_markets(k, series, hist, manifest)
    log.info("markets done (%.0fs)", time.time() - t0)
    matches = build_matches(markets)
    if len(matches):
        write_table(hist, "matches", matches, "start_time")
    manifest["matches"] = {"rows": int(len(matches)),
                           "by_game": matches.groupby("game").size().to_dict() if len(matches) else {},
                           "first": str(matches["start_time"].min()) if len(matches) else None,
                           "last": str(matches["start_time"].max()) if len(matches) else None,
                           "decided": int(matches["winner"].notna().sum()) if len(matches) else 0}
    if len(matches):
        fetch_candles(k, hist, matches, days, hours_before, manifest, minutes)
    log.info("candles done (%.0fs)", time.time() - t0)
    manifest["finished"] = datetime.now(timezone.utc).isoformat()
    manifest["http_calls"] = http.calls
    manifest["errors"] = manifest["errors"][:200]
    (hist / "manifest.json").write_text(json.dumps(manifest, indent=1, default=str))
    return manifest
