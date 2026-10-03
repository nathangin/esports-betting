"""Command line: ``python -m esalpha <command>``."""

from __future__ import annotations

import argparse
import json
import logging
import sys


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="esalpha", description="Esports match-market model and paper trader")
    ap.add_argument("-v", "--verbose", action="store_true")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("probe", help="check market and results sources and save raw samples")
    p.add_argument("--out", default="state/probe")

    p = sub.add_parser("history", help="download settled esports matches and pre-match price candles")
    p.add_argument("--state", default="state")
    p.add_argument("--days", type=int, default=150, help="days of recent matches to fetch candles for")
    p.add_argument("--hours-before", type=float, default=6.0, help="hours of candles before each start")
    p.add_argument("--minutes", type=float, default=90, help="time budget for candles")

    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    if args.cmd == "probe":
        from . import probe

        rep = probe.run(args.out)
        print(json.dumps({"checks": len(rep["checks"]), "failed": [c["name"] for c in rep["checks"] if not c["ok"]],
                          "http_calls": rep["http_calls"]}, indent=1))
    elif args.cmd == "history":
        from . import history

        man = history.build(args.state, days=args.days, hours_before=args.hours_before, minutes=args.minutes)
        print(json.dumps({k: v for k, v in man.items() if k != "errors"}, indent=1, default=str))
        print(f"{len(man['errors'])} errors", *man["errors"][:20], sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
