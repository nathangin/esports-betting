"""Fake Kalshi responses for the esalpha tests (field names copied from real responses)."""

def market(ticker, team, comp, *, status="active", bid=None, ask=None, result="", open_time="2026-10-02T16:00:00Z",
           close_time="2026-10-03T16:00:00Z", bid_size=500.0, ask_size=500.0, opponent="Other", new_title=False):
    """A market object shaped like Kalshi's (field names copied from a real response).
    ``new_title``: the short title format Kalshi uses since August 2026 ("A wins")."""
    event = ticker.rsplit("-", 1)[0]
    return {
        "ticker": ticker, "event_ticker": event,
        "title": f"{team} wins" if new_title else f"Will {team} win the {team} vs. {opponent} match?",
        "yes_sub_title": team, "no_sub_title": team, "custom_strike": {"esports_competitor": comp},
        "status": status, "result": result, "expiration_value": team if result == "yes" else "",
        "yes_bid_dollars": "0.0000" if bid is None else f"{bid:.4f}",
        "yes_ask_dollars": "1.0000" if ask is None else f"{ask:.4f}",
        "yes_bid_size_fp": f"{bid_size:.2f}", "yes_ask_size_fp": f"{ask_size:.2f}",
        "volume_fp": "1000.00", "open_time": open_time, "close_time": close_time,
        "rules_primary": f"If {team} wins the Test Cup: {team} vs. {opponent} Counter-Strike match originally "
                         "scheduled for Oct 2, 2026 at 3:00 PM EDT, then the market resolves to Yes.",
    }


class FakeKalshiHttp:
    """Serves Kalshi's public market endpoints from in-memory market objects."""

    def __init__(self, open_markets=(), settled_markets=()):
        self.open = {m["ticker"]: m for m in open_markets}
        self.settled = {m["ticker"]: m for m in settled_markets}
        self.calls = 0
        self.urls = []
        self.sample_dir = None

    def save_sample(self, *a, **k):
        pass

    def get_json(self, url, params=None, headers=None, sample=None):
        self.calls += 1
        params = dict(params or {})
        self.urls.append((url, params))
        assert "api.elections.kalshi.com" in url, url
        allm = {**self.open, **self.settled}
        if url.endswith("/markets"):
            if params.get("tickers"):
                want = params["tickers"].split(",")
                return {"markets": [allm[t] for t in want if t in allm], "cursor": ""}
            series = params.get("series_ticker")
            src = self.settled if params.get("status") == "settled" else self.open
            return {"markets": [m for m in src.values() if m["ticker"].startswith(series + "-")], "cursor": ""}
        if "/markets/" in url:
            t = url.rsplit("/", 1)[1]
            return {"market": allm[t]}
        raise AssertionError(f"unexpected Kalshi path {url}")
