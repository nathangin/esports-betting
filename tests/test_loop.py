import json
from datetime import timedelta

from esalpha import loop, paper
from kalshi_fakes import FakeKalshiHttp
from test_paper import NOW, _setup


class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t

    def sleep(self, s):
        self.t += s

    def now(self):
        return NOW + timedelta(seconds=self.t)


def _saver(tmp_path):
    log = tmp_path / "commits.log"
    return log, f"bash -c 'echo \"$0\" >> {log}'"


def test_loop_passes_every_few_minutes_and_saves_when_something_happens(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    monkeypatch.setattr(paper, "Http", lambda *a, **k: FakeKalshiHttp(open_markets=open_ms))
    clock = FakeClock()
    log, cmd = _saver(tmp_path)
    out = loop.run_loop(str(tmp_path), minutes=30, every=5, commit_cmd=cmd, commit_every=30,
                        clock=clock, sleep=clock.sleep, now=clock.now)
    assert out["passes"] == 7 and out["errors"] == 0           # 18:00, 18:05, ... 18:30
    assert out["decided"] == 1 and out["bets"] >= 1               # the 18:45 match, decided once
    runs = [json.loads(x) for x in (tmp_path / "paper" / "runs.jsonl").read_text().splitlines()]
    assert len(runs) == 7
    # the first pass follows a long gap (wide window); the rest run 5 minutes apart (normal window)
    assert runs[0]["decision_window"] == [10, 180] and runs[1]["decision_window"] == [10, 70]
    assert all(r["minutes_since_last_run"] == 5.0 for r in runs[1:])
    saved = log.read_text().splitlines()
    # saved after the pass with the bet, at the 30-minute heartbeat, and at the end
    assert saved[0].startswith("paper pass 1 ") and saved[-1].startswith("paper loop done")
    assert len(saved) == 3
    assert (tmp_path / "reports" / "summary.md").exists()


def test_loop_survives_a_failed_pass(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    monkeypatch.setattr(paper, "Http", lambda *a, **k: FakeKalshiHttp(open_markets=open_ms))
    real = paper.run
    calls = {"n": 0}

    def flaky(*a, **k):
        calls["n"] += 1
        if calls["n"] == 2:
            raise RuntimeError("Kalshi timed out")
        return real(*a, **k)

    monkeypatch.setattr(paper, "run", flaky)
    clock = FakeClock()
    out = loop.run_loop(str(tmp_path), minutes=15, every=5, clock=clock, sleep=clock.sleep, now=clock.now)
    assert out["passes"] == 4 and out["errors"] == 1


def test_after_the_trial_one_settling_pass_is_enough(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    monkeypatch.setattr(paper, "Http", lambda *a, **k: FakeKalshiHttp(open_markets=open_ms))
    clock = FakeClock()
    out = loop.run_loop(str(tmp_path), until="2026-10-01", minutes=300, every=5, clock=clock, sleep=clock.sleep,
                        now=clock.now)
    assert out["passes"] == 1 and clock.t == 0
