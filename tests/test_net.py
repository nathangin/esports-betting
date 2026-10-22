import pytest
import requests

from esalpha import net


class _Resp:
    status_code = 200
    url = "https://example.test/x"


class _Session:
    def __init__(self, fail_times):
        self.fail_times, self.calls = fail_times, 0

    def get(self, url, params=None, headers=None, timeout=None):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise requests.exceptions.ChunkedEncodingError("Response ended prematurely")
        return _Resp()


def test_a_download_cut_off_midway_is_retried(monkeypatch):
    monkeypatch.setattr(net.time, "sleep", lambda s: None)
    h = net.Http()
    h.session = _Session(fail_times=2)
    assert h.get("https://example.test/x").status_code == 200 and h.session.calls == 3


def test_a_download_that_keeps_failing_becomes_an_http_error(monkeypatch):
    monkeypatch.setattr(net.time, "sleep", lambda s: None)
    h = net.Http()
    h.session = _Session(fail_times=99)
    with pytest.raises(net.HttpError) as e:
        h.get("https://example.test/x")
    assert e.value.status == 0 and "ChunkedEncodingError" in str(e.value) and h.session.calls == 3
