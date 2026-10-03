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

    args = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    if args.cmd == "probe":
        from . import probe

        rep = probe.run(args.out)
        print(json.dumps({"checks": len(rep["checks"]), "failed": [c["name"] for c in rep["checks"] if not c["ok"]],
                          "http_calls": rep["http_calls"]}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
