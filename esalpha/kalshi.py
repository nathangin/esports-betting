"""Read-only Kalshi client for esports match markets (public market-data endpoints only).

A match is a Kalshi event with one market per team ("Will OpTic Gaming win the OpTic Gaming
vs. Team Heretics match?"). Teams carry a stable competitor id in ``custom_strike``. Markets
open a few hours before the scheduled start (encoded in the event ticker, Eastern time) and
keep trading while the match is played, so a pre-match decision must use pre-start prices.
"""

from __future__ import annotations

import logging
import math
import os
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Iterator
from zoneinfo import ZoneInfo

from .net import Http, HttpError

log = logging.getLogger(__name__)

BASE = os.environ.get("KALSHI_PUBLIC_BASE", "https://api.elections.kalshi.com/trade-api/v2")
ET = ZoneInfo("America/New_York")
_MONTHS = {m: i + 1 for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])}

# series ticker fragments -> game key
GAME_KEYS = [
    ("CSGO", "cs2"), ("CS2", "cs2"), ("LOL", "lol"), ("LEAGUE", "lol"), ("VALORANT", "valorant"),
    ("VCT", "valorant"), ("DOTA", "dota2"), ("COD", "cod"), ("ROCKETLEAGUE", "rl"), ("R6", "r6"),
    ("OVERWATCH", "ow"), ("OW", "ow"), ("PUBG", "pubg"), ("APEX", "apex"), ("MLBB", "mlbb"),
]


def game_of(series_ticker: str) -> str:
    t = (series_ticker or "").upper().removeprefix("KX")
    for frag, key in GAME_KEYS:
        if frag in t:
            return key
    return t.lower()


def _f(x) -> float | None:
    if x is None or x == "":
        return None
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return None if math.isnan(v) else v


def price(m: dict, key: str) -> float | None:
    v = _f(m.get(f"{key}_dollars"))
    if v is not None:
        return v
    v = _f(m.get(key))
    return None if v is None else v / 100.0


def qty(m: dict, key: str) -> float | None:
    v = _f(m.get(f"{key}_fp"))
    return v if v is not None else _f(m.get(key))


def parse_time(s) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


_START_RE = re.compile(r"-(\d{2})([A-Z]{3})(\d{2})(\d{4})")
_RULES_RE = re.compile(r"scheduled for ([A-Z][a-z]{2,8}) (\d{1,2}), (\d{4}) at (\d{1,2}):(\d{2}) ([AP]M) ([A-Z]{2,4})")


def start_from_ticker(event_ticker: str) -> datetime | None:
    """Scheduled start from an event ticker such as KXCODGAME-26AUG091500OGHTCS (Eastern time)."""
    m = _START_RE.search(event_ticker or "")
    if not m or m.group(2) not in _MONTHS:
        return None
    try:
        hh, mm = int(m.group(4)[:2]), int(m.group(4)[2:])
        local = datetime(2000 + int(m.group(1)), _MONTHS[m.group(2)], int(m.group(3)), hh, mm, tzinfo=ET)
    except ValueError:
        return None
    return local.astimezone(timezone.utc)


def start_from_rules(text: str) -> datetime | None:
    m = _RULES_RE.search(text or "")
    if not m:
        return None
    mon = m.group(1)[:3].upper()
    if mon not in _MONTHS:
        return None
    hour = int(m.group(4)) % 12 + (12 if m.group(6) == "PM" else 0)
    try:
        local = datetime(int(m.group(3)), _MONTHS[mon], int(m.group(2)), hour, int(m.group(5)), tzinfo=ET)
    except ValueError:
        return None
    return local.astimezone(timezone.utc)


_TOURNEY_RE = re.compile(r"wins the (.+?): .+? vs\.? .+? (?:[A-Za-z0-9 ]+ )?match", re.I)


@dataclass
class Market:
    ticker: str
    event_ticker: str
    series_ticker: str
    game: str
    team: str                      # yes_sub_title: the team this market pays out on
    competitor: str                # stable competitor id (falls back to the team name)
    title: str
    status: str
    yes_bid: float | None
    yes_ask: float | None
    yes_bid_size: float | None = None
    yes_ask_size: float | None = None
    last_price: float | None = None
    volume: float | None = None
    open_time: datetime | None = None
    close_time: datetime | None = None
    start_time: datetime | None = None
    result: str = ""
    winner_name: str | None = None
    tournament: str | None = None
    raw_keys: list = field(default_factory=list, repr=False)

    @property
    def mid(self) -> float | None:
        if self.yes_bid is not None and self.yes_ask is not None:
            return (self.yes_bid + self.yes_ask) / 2
        return None

    def to_row(self) -> dict:
        d = asdict(self)
        d.pop("raw_keys", None)
        return d


def parse_market(m: dict, series_ticker: str | None = None) -> Market:
    ticker = m.get("ticker", "")
    event = m.get("event_ticker") or ticker.rsplit("-", 1)[0]
    series = series_ticker or event.split("-", 1)[0]
    cs = m.get("custom_strike") or {}
    team = m.get("yes_sub_title") or ""
    comp = cs.get("esports_competitor") or cs.get("competitor") or team
    bid, ask = price(m, "yes_bid"), price(m, "yes_ask")
    if bid is not None and bid <= 0:
        bid = None
    if ask is not None and ask >= 1.0:
        ask = None
    rules = m.get("rules_primary") or ""
    tm = _TOURNEY_RE.search(rules)
    result = (m.get("result") or "").lower()
    return Market(
        ticker=ticker, event_ticker=event, series_ticker=series, game=game_of(series), team=team,
        competitor=str(comp), title=m.get("title") or "", status=(m.get("status") or "").lower(),
        yes_bid=bid, yes_ask=ask, yes_bid_size=qty(m, "yes_bid_size"), yes_ask_size=qty(m, "yes_ask_size"),
        last_price=price(m, "last_price"), volume=qty(m, "volume"),
        open_time=parse_time(m.get("open_time")), close_time=parse_time(m.get("close_time")),
        start_time=start_from_ticker(event) or start_from_rules(rules),
        result=result if result in ("yes", "no", "void") else "", winner_name=m.get("expiration_value") or None,
        tournament=tm.group(1).strip() if tm else None, raw_keys=sorted(m.keys()))


def parse_candles(rows) -> list[dict]:
    out = []
    for c in rows or []:
        def ohlc(name, fld="close"):
            d = c.get(name) or {}
            v = _f(d.get(f"{fld}_dollars"))
            if v is not None:
                return v
            v = _f(d.get(fld))
            return None if v is None else v / 100.0
        bid, ask = ohlc("yes_bid"), ohlc("yes_ask")
        out.append({"ts": int(c.get("end_period_ts") or 0), "bid": bid if bid and bid > 0 else None,
                    "ask": ask if ask is not None and ask < 1.0 else None, "price": ohlc("price"),
                    "volume": qty(c, "volume")})
    return out


class Kalshi:
    def __init__(self, http: Http | None = None, base: str = BASE):
        self.http = http or Http()
        self.base = base.rstrip("/")

    def get(self, path: str, params: dict | None = None, sample: str | None = None):
        return self.http.get_json(self.base + path, params=params, sample=sample)

    def esports_series(self) -> list[dict]:
        rows = self.get("/series", {"category": "Sports"}, sample="series_sports").get("series") or []
        return [s for s in rows if "Esports" in (s.get("tags") or [])]

    def iter_markets(self, path: str = "/markets", page_size: int = 1000, max_pages: int = 50,
                     **params) -> Iterator[dict]:
        params = {k: v for k, v in params.items() if v is not None}
        params["limit"] = page_size
        cursor, pages = None, 0
        while pages < max_pages:
            if cursor:
                params["cursor"] = cursor
            js = self.get(path, params, sample="markets_page")
            rows = js.get("markets") or []
            pages += 1
            yield from rows
            cursor = js.get("cursor")
            if not cursor or not rows:
                break

    def markets(self, **params) -> list[Market]:
        out = []
        for m in self.iter_markets(**params):
            try:
                out.append(parse_market(m))
            except Exception as e:  # noqa: BLE001
                log.warning("could not parse market %s: %s", m.get("ticker"), e)
        return out

    def markets_by_ticker(self, tickers: list[str]) -> dict[str, Market]:
        out: dict[str, Market] = {}
        tickers = list(dict.fromkeys(tickers))
        for i in range(0, len(tickers), 50):
            chunk = tickers[i:i + 50]
            try:
                for m in self.markets(tickers=",".join(chunk), page_size=200, max_pages=2):
                    out[m.ticker] = m
            except HttpError as e:
                log.warning("batch lookup failed (%s)", e)
            for t in chunk:
                if t not in out:
                    try:
                        out[t] = parse_market(self.get(f"/markets/{t}").get("market") or {})
                    except HttpError as e:
                        log.warning("market %s: %s", t, e)
        return out

    def event_candles(self, series: str, event: str, start_ts: int, end_ts: int, period: int = 60) -> dict[str, list]:
        js = self.get(f"/series/{series}/events/{event}/candlesticks",
                      {"start_ts": int(start_ts), "end_ts": int(end_ts), "period_interval": period},
                      sample="event_candles")
        return {t: parse_candles(cs) for t, cs in zip(js.get("market_tickers") or [], js.get("market_candlesticks") or [])}

    def market_candles(self, series: str, ticker: str, start_ts: int, end_ts: int, period: int = 60) -> list[dict]:
        params = {"start_ts": int(start_ts), "end_ts": int(end_ts), "period_interval": period}
        for path in (f"/series/{series}/markets/{ticker}/candlesticks", f"/historical/markets/{ticker}/candlesticks"):
            try:
                rows = parse_candles(self.get(path, params, sample="market_candles").get("candlesticks"))
                if rows:
                    return rows
            except HttpError as e:
                if e.status not in (400, 404):
                    raise
        return []
