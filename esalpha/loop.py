"""Keep one paper-trading job open for hours, doing a pass every few minutes.

GitHub starts this repo's scheduled runs only a few times a day, hours apart, so a single
pass per run misses most matches. One job can run for up to six hours: this loop repeats the
normal pass (settle, results, decide on matches about to start, report) every ``every``
minutes until ``minutes`` have passed, and saves the state as it goes so nothing is lost if
the job is stopped. The next scheduled run waits in the queue and takes over when this one
ends.
"""

from __future__ import annotations

import json
import logging
import shlex
import subprocess
import time
from datetime import datetime, timezone
from typing import Callable

from . import paper, report

log = logging.getLogger(__name__)


def _active(summary: dict) -> bool:
    """Did this pass change anything worth saving right away?"""
    bets = summary.get("bets_placed") or {}
    return bool(summary.get("matches_decided") or summary.get("settled") or summary.get("closes_backfilled")
                or any(bets.values()) or summary.get("error"))


def run_loop(state_dir: str, until: str | None = None, minutes: float = 330.0, every: float = 5.0,
             commit_cmd: str | None = None, commit_every: float = 30.0,
             clock: Callable[[], float] = time.time, sleep: Callable[[float], None] = time.sleep,
             now: Callable[[], datetime] | None = None) -> dict:
    """Run paper passes until ``minutes`` are used up. Returns counts for the job log.

    commit_cmd: shell command that saves the state (gets the commit message appended); run
    after a pass that placed, decided or settled anything, and at least every ``commit_every``
    minutes otherwise, and once at the end.
    """
    now = now or (lambda: datetime.now(timezone.utc))
    end = clock() + minutes * 60.0
    last_commit = clock()
    out = {"passes": 0, "errors": 0, "commits": 0, "decided": 0, "bets": 0, "settled": 0}

    def commit(msg: str) -> None:
        if not commit_cmd:
            return
        cmd = shlex.split(commit_cmd) + [msg]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            log.warning("saving state failed (%s): %s", res.returncode, (res.stderr or res.stdout)[-500:])
        else:
            out["commits"] += 1

    while True:
        started = clock()
        try:
            summary = paper.run(state_dir, now=now(), until=until)
            report.write(state_dir)
        except Exception as e:  # noqa: BLE001 - one failed pass must not end the job
            log.exception("paper pass failed")
            summary = {"error": f"{type(e).__name__}: {e}"[:300]}
            out["errors"] += 1
        out["passes"] += 1
        out["decided"] += int(summary.get("matches_decided") or 0)
        out["bets"] += sum((summary.get("bets_placed") or {}).values())
        out["settled"] += int(summary.get("settled") or 0)
        print(json.dumps({"pass": out["passes"], **summary}, default=str), flush=True)
        if _active(summary) or clock() - last_commit >= commit_every * 60.0:
            commit(f"paper pass {out['passes']} {summary.get('run_at', '')}".strip())
            last_commit = clock()
        if summary.get("scan", "").startswith("paper trial ended"):
            break                     # after the trial only settling is left: one pass is enough
        if clock() + every * 60.0 > end:
            break
        sleep(max(0.0, every * 60.0 - (clock() - started)))
    commit(f"paper loop done after {out['passes']} passes")
    return out
