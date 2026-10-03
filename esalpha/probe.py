"""Endpoint probe for the esports paper trader: which market and results sources answer,
and what their data looks like. Read-only; writes raw samples plus a summary."""

from __future__ import annotations

import json
import re
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

from .net import Http

KALSHI = "https://api.elections.kalshi.com/trade-api/v2"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
ESPORT_WORDS = re.compile(r"counter[- ]?strike|\bcs2\b|\bcsgo\b|cs:go|league of legends|\blol\b|valorant|dota|"
                          r"esport|e-sport|overwatch|rocket league|rainbow|call of duty", re.I)


def run(out_dir: str) -> dict:
    out = Path(out_dir)
    http = Http(sample_dir=out / "samples")
    report: dict = {"started": datetime.now(timezone.utc).isoformat(), "checks": []}

    def check(name, fn):
        t0 = time.time()
        try:
            res = fn()
            report["checks"].append({"name": name, "ok": True, "secs": round(time.time() - t0, 2), "result": res})
            return res
        except Exception as e:  # noqa: BLE001 - a probe records failures and moves on
            report["checks"].append({"name": name, "ok": False, "secs": round(time.time() - t0, 2),
                                     "error": f"{type(e).__name__}: {e}"[:600], "trace": traceback.format_exc()[-1200:]})
            return None

    # ---------------- Kalshi ----------------
    def kalshi_series():
        found = []
        for cat in ("Sports", "Esports", "E-Sports"):
            try:
                rows = http.get_json(f"{KALSHI}/series", {"category": cat}, sample=f"kalshi_series_{cat}").get("series") or []
            except Exception as e:  # noqa: BLE001
                found.append({"category": cat, "error": str(e)[:150]})
                continue
            hits = [{"ticker": s.get("ticker"), "title": s.get("title"), "tags": s.get("tags")}
                    for s in rows if ESPORT_WORDS.search(" ".join([s.get("title") or "", s.get("ticker") or "",
                                                                   " ".join(s.get("tags") or [])]))]
            found.append({"category": cat, "n_series": len(rows), "esports": hits[:60]})
        return found
    ks = check("kalshi esports series", kalshi_series)
    tickers = [h["ticker"] for c in (ks or []) for h in c.get("esports", [])][:8]
    if tickers:
        def kalshi_markets():
            res = {}
            for tk in tickers:
                js = http.get_json(f"{KALSHI}/markets", {"series_ticker": tk, "limit": 20}, sample=f"kalshi_mk_{tk}")
                ms = js.get("markets") or []
                res[tk] = {"n": len(ms), "examples": [{k: m.get(k) for k in ("ticker", "title", "yes_sub_title", "status",
                                                                             "yes_bid_dollars", "yes_ask_dollars", "result",
                                                                             "volume_fp", "close_time")} for m in ms[:4]]}
            return res
        check("kalshi esports markets", kalshi_markets)

    # ---------------- Polymarket ----------------
    def pm_sports():
        js = http.get_json(f"{GAMMA}/sports", sample="pm_sports")
        rows = js if isinstance(js, list) else js.get("data", [])
        return [r for r in rows if ESPORT_WORDS.search(json.dumps(r))][:40] or rows[:5]
    check("polymarket /sports", pm_sports)

    def pm_tags():
        rows = http.get_json(f"{GAMMA}/tags", {"limit": 1000}, sample="pm_tags")
        rows = rows if isinstance(rows, list) else rows.get("data", [])
        return [{"id": t.get("id"), "label": t.get("label"), "slug": t.get("slug")} for t in rows
                if ESPORT_WORDS.search(f"{t.get('label')} {t.get('slug')}")][:60]
    tags = check("polymarket esports tags", pm_tags) or []

    open_token = closed_token = None
    for slug in ["esports", "counter-strike", "cs2", "league-of-legends", "valorant", "dota-2"]:
        def pm_events(slug=slug, closed=False):
            js = http.get_json(f"{GAMMA}/events", {"tag_slug": slug, "closed": str(closed).lower(), "limit": 50},
                               sample=f"pm_events_{slug}_{'closed' if closed else 'open'}")
            rows = js if isinstance(js, list) else js.get("data", [])
            ex = []
            for e in rows[:6]:
                mks = e.get("markets") or []
                ex.append({"title": e.get("title"), "slug": e.get("slug"), "start": e.get("startDate"),
                           "end": e.get("endDate"), "closed": e.get("closed"), "n_markets": len(mks),
                           "markets": [{k: m.get(k) for k in ("question", "outcomes", "outcomePrices", "clobTokenIds",
                                                              "volume", "liquidity", "closed", "gameStartTime",
                                                              "sportsMarketType", "bestBid", "bestAsk", "spread",
                                                              "umaResolutionStatus", "feeType", "takerBaseFee")}
                                       for m in mks[:3]]})
            return {"n": len(rows), "examples": ex}
        r1 = check(f"polymarket events tag={slug} open", pm_events)
        r2 = check(f"polymarket events tag={slug} closed", lambda slug=slug: pm_events(slug, True))
        for r, which in ((r1, "open"), (r2, "closed")):
            for e in (r or {}).get("examples", []):
                for m in e.get("markets", []):
                    try:
                        toks = json.loads(m.get("clobTokenIds") or "[]")
                    except (TypeError, ValueError):
                        toks = []
                    if toks:
                        if which == "open" and open_token is None:
                            open_token = toks[0]
                        if which == "closed" and closed_token is None:
                            closed_token = toks[0]

    if closed_token:
        check("polymarket price history (closed market)", lambda: _hist(http.get_json(
            f"{CLOB}/prices-history", {"market": closed_token, "interval": "max", "fidelity": 60}, sample="pm_hist_closed")))
    if open_token:
        check("polymarket price history (open market)", lambda: _hist(http.get_json(
            f"{CLOB}/prices-history", {"market": open_token, "interval": "1w", "fidelity": 60}, sample="pm_hist_open")))
        check("polymarket order book", lambda: _book(http.get_json(f"{CLOB}/book", {"token_id": open_token},
                                                                   sample="pm_book")))

    def pm_closed_depth():
        n, offset, oldest = 0, 0, None
        while offset < 3000:
            js = http.get_json(f"{GAMMA}/events", {"tag_slug": "esports", "closed": "true", "limit": 500,
                                                   "offset": offset, "order": "endDate", "ascending": "false"})
            rows = js if isinstance(js, list) else js.get("data", [])
            if not rows:
                break
            n += len(rows)
            oldest = rows[-1].get("endDate")
            offset += len(rows)
        return {"closed_events_seen": n, "oldest_end": oldest}
    check("polymarket closed esports depth", pm_closed_depth)

    # ---------------- Results sources ----------------
    check("leaguepedia cargo", lambda: _short(http.get_json("https://lol.fandom.com/api.php", {
        "action": "cargoquery", "tables": "ScoreboardGames", "fields": "Team1,Team2,WinTeam,DateTime_UTC,Tournament",
        "order_by": "DateTime_UTC DESC", "limit": 5, "format": "json"}, sample="leaguepedia")))
    check("liquipedia api (cs)", lambda: _short(http.get_json("https://liquipedia.net/counterstrike/api.php", {
        "action": "query", "list": "search", "srsearch": "Major", "srlimit": 3, "format": "json"},
        headers={"Accept-Encoding": "gzip"}, sample="liquipedia")))

    def plain(url):
        r = http.get(url, headers={"Accept": "text/html"})
        return {"status": r.status_code, "bytes": len(r.text), "head": r.text[:300]}
    check("vlr.gg results page (honest UA)", lambda: plain("https://www.vlr.gg/matches/results"))
    check("hltv results page (honest UA)", lambda: plain("https://www.hltv.org/results"))

    report["finished"] = datetime.now(timezone.utc).isoformat()
    report["http_calls"] = http.calls
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(report, indent=1, default=str))
    lines = [f"# Probe {report['started']}", ""] + [
        f"- {'OK ' if c['ok'] else 'ERR'} {c['name']} ({c['secs']}s)" + ("" if c["ok"] else f"\n    {c['error']}")
        for c in report["checks"]]
    (out / "summary.md").write_text("\n".join(lines) + "\n")
    return report


def _hist(js):
    h = js.get("history") or []
    return {"n": len(h), "first": h[0] if h else None, "last": h[-1] if h else None, "keys": sorted(js.keys())}


def _book(js):
    return {"keys": sorted(js.keys()), "bids": (js.get("bids") or [])[-3:], "asks": (js.get("asks") or [])[-3:],
            "tick_size": js.get("tick_size"), "min_order_size": js.get("min_order_size")}


def _short(js):
    return json.dumps(js)[:1500]
