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
    p.add_argument("--kalshi-coverage", action="store_true", help="only check which Kalshi endpoints list which markets")

    p = sub.add_parser("history", help="download settled esports matches and pre-match price candles")
    p.add_argument("--state", default="state")
    p.add_argument("--days", type=int, default=150, help="days of recent matches to fetch candles for")
    p.add_argument("--hours-before", type=float, default=6.0, help="hours of candles before each start")
    p.add_argument("--minutes", type=float, default=90, help="time budget for candles")

    p = sub.add_parser("backtest", help="walk-forward fake-money backtest on real Kalshi prices; refits the model")
    p.add_argument("--state", default="state")
    p.add_argument("--minutes-before", type=float, default=60.0, help="decide this long before the scheduled start")
    p.add_argument("--name", default="backtest")
    p.add_argument("--no-save-params", action="store_true", help="do not overwrite state/params/fitted.json")

    p = sub.add_parser("paper", help="one paper-trading pass (settle, scan upcoming matches, fake bets)")
    p.add_argument("--state", default="state")
    p.add_argument("--until", default=None, help="last day (YYYY-MM-DD) of the paper trial")

    p = sub.add_parser("paper-loop", help="repeat paper passes for hours (one long GitHub Actions job)")
    p.add_argument("--state", default="state")
    p.add_argument("--until", default=None, help="last day (YYYY-MM-DD) of the paper trial")
    p.add_argument("--minutes", type=float, default=330.0, help="how long to keep going")
    p.add_argument("--every", type=float, default=5.0, help="minutes between passes")
    p.add_argument("--commit-cmd", default=None, help="command that saves the state; the message is appended")
    p.add_argument("--commit-every", type=float, default=30.0, help="save at least this often (minutes)")

    p = sub.add_parser("report", help="write state/reports/summary.md from the paper ledger and backtest")
    p.add_argument("--state", default="state")

    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    if args.cmd == "probe":
        from . import probe

        if args.kalshi_coverage:
            rep = probe.run_kalshi(args.out)
            print(json.dumps(rep, indent=1, default=str)[:20000])
        else:
            rep = probe.run(args.out)
            print(json.dumps({"checks": len(rep["checks"]), "failed": [c["name"] for c in rep["checks"] if not c["ok"]],
                              "http_calls": rep["http_calls"]}, indent=1))
    elif args.cmd == "history":
        from . import history

        man = history.build(args.state, days=args.days, hours_before=args.hours_before, minutes=args.minutes)
        print(json.dumps({k: v for k, v in man.items() if k != "errors"}, indent=1, default=str))
        print(f"{len(man['errors'])} errors", *man["errors"][:20], sep="\n  ")
    elif args.cmd == "backtest":
        from . import backtest

        rep = backtest.run(args.state, minutes_before=args.minutes_before, name=args.name,
                           save_params=not args.no_save_params)
        print(json.dumps({k: rep[k] for k in ("decision", "matches_all", "matches_priced", "matches_tested", "period",
                                              "by_game", "scores", "results", "params") if k in rep},
                         indent=1, default=str))
    elif args.cmd == "paper":
        from . import paper

        print(json.dumps(paper.run(args.state, until=args.until), indent=1, default=str))
    elif args.cmd == "paper-loop":
        from . import loop

        out = loop.run_loop(args.state, until=args.until, minutes=args.minutes, every=args.every,
                            commit_cmd=args.commit_cmd, commit_every=args.commit_every)
        print(json.dumps(out))
    elif args.cmd == "report":
        from . import report

        rep = report.write(args.state)
        print(json.dumps(rep.get("books", {}), indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
