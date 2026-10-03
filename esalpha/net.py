"""HTTP helper: one session, retries with backoff, polite per-host pacing, optional raw samples."""

from __future__ import annotations

import json
import logging
import os
import threading
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

log = logging.getLogger(__name__)

DEFAULT_UA = os.environ.get(
    "ES_USER_AGENT", "esalpha-paper-trader (github.com/nathangin/esports-betting)")

# Minimum seconds between requests to the same host.
HOST_INTERVAL = {
    "api.elections.kalshi.com": 0.12,
    "gamma-api.polymarket.com": 0.15,
    "clob.polymarket.com": 0.15,
    "lol.fandom.com": 1.0,
    "liquipedia.net": 2.1,     # Liquipedia API terms: at most one request every 2 seconds
    "www.vlr.gg": 1.5,
}
DEFAULT_INTERVAL = 0.1


class HttpError(RuntimeError):
    def __init__(self, url: str, status: int, body: str):
        super().__init__(f"HTTP {status} for {url}: {body[:300]}")
        self.url, self.status, self.body = url, status, body


class Http:
    def __init__(self, user_agent: str = DEFAULT_UA, timeout: float = 30.0, retries: int = 4,
                 sample_dir: str | os.PathLike | None = None):
        self.timeout = timeout
        self.session = requests.Session()
        retry = Retry(total=retries, connect=retries, read=retries, status=retries,
                      backoff_factor=1.5, status_forcelist=(429, 500, 502, 503, 504),
                      allowed_methods=frozenset(["GET"]), respect_retry_after_header=True,
                      raise_on_status=False)
        adapter = HTTPAdapter(max_retries=retry, pool_maxsize=8)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
        self.session.headers.update({"User-Agent": user_agent, "Accept": "application/json"})
        self._last: dict[str, float] = {}
        self._lock = threading.Lock()
        self.sample_dir = Path(sample_dir) if sample_dir else None
        self._sampled: set[str] = set()
        self.calls = 0

    def _pace(self, host: str) -> None:
        gap = HOST_INTERVAL.get(host, DEFAULT_INTERVAL)
        with self._lock:
            wait = self._last.get(host, 0.0) + gap - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            self._last[host] = time.monotonic()

    def get(self, url: str, params: dict | None = None, headers: dict | None = None) -> requests.Response:
        host = urlparse(url).netloc
        self._pace(host)
        self.calls += 1
        return self.session.get(url, params=params, headers=headers, timeout=self.timeout)

    def get_json(self, url: str, params: dict | None = None, headers: dict | None = None,
                 sample: str | None = None) -> Any:
        resp = self.get(url, params=params, headers=headers)
        if resp.status_code >= 400:
            raise HttpError(resp.url, resp.status_code, resp.text)
        data = resp.json()
        if sample:
            self.save_sample(sample, {"url": resp.url, "status": resp.status_code, "body": data})
        return data

    def save_sample(self, name: str, payload: Any, max_chars: int = 200_000) -> None:
        """Keep the first raw response of each kind, so parsers can be checked against reality."""
        if not self.sample_dir or name in self._sampled:
            return
        self._sampled.add(name)
        self.sample_dir.mkdir(parents=True, exist_ok=True)
        text = json.dumps(payload, indent=1, default=str)
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... (truncated)"
        (self.sample_dir / f"{name}.json").write_text(text)
