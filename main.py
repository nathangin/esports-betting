"""
Esports betting model — entry point.

Usage examples:

  # Full CS2 pipeline (scrape + train + predict)
  python main.py cs2 run

  # CS2 train only (no scrape)
  python main.py cs2 train

  # CS2 predict upcoming matches
  python main.py cs2 predict

  # LoL full pipeline
  python main.py lol run

  # Valorant full pipeline
  python main.py valorant run

  # Edge report given book lines (JSON file)
  python main.py cs2 edge --lines lines.json

  # Tune hyperparameters (slow — run once, then use saved params)
  python main.py cs2 train --tune
"""
import argparse
import json
import sys
from pathlib import Path

from loguru import logger
from db.setup import init_db


def main():
    parser = argparse.ArgumentParser(description="Esports Betting Model")
    parser.add_argument("game", choices=["cs2", "lol", "valorant"])
    parser.add_argument("command", choices=["run", "scrape", "train", "predict", "edge"])
    parser.add_argument("--tune", action="store_true", help="Run Optuna hyperparameter tuning")
    parser.add_argument("--lines", type=str, help="Path to JSON file with book lines for edge report")
    parser.add_argument("--pages", type=int, default=20, help="Max pages to scrape")
    parser.add_argument("--days", type=int, default=365, help="Days of history to collect")
    args = parser.parse_args()

    init_db()

    if args.game == "cs2":
        from pipeline.cs2 import CS2Pipeline
        pipe = CS2Pipeline(days_back=args.days)

        if args.command == "run":
            results = pipe.run(scrape=True, tune=args.tune, max_scrape_pages=args.pages)
            _print_predictions(results)

        elif args.command == "scrape":
            pipe.scrape_and_store(max_pages=args.pages)
            pipe.scrape_upcoming()

        elif args.command == "train":
            matches_df, map_df, _ = pipe.load_dataframes()
            pipe.build_elo(matches_df, map_df)
            pipe.train(tune=args.tune)

        elif args.command == "predict":
            matches_df, map_df, _ = pipe.load_dataframes()
            pipe.build_elo(matches_df, map_df)
            # Load saved win model
            model_path = Path("data/models_saved/cs2_win.pkl")
            if model_path.exists():
                from models.win_model import WinModel
                pipe.win_model = WinModel.load(model_path)
            preds = pipe.predict_upcoming()
            _print_predictions(preds)

        elif args.command == "edge":
            if not args.lines:
                logger.error("--lines <file.json> required for edge command")
                sys.exit(1)
            lines = _load_lines(args.lines)
            matches_df, map_df, _ = pipe.load_dataframes()
            pipe.build_elo(matches_df, map_df)
            from models.win_model import WinModel
            model_path = Path("data/models_saved/cs2_win.pkl")
            if model_path.exists():
                pipe.win_model = WinModel.load(model_path)
            report = pipe.edge_report(lines)
            print(report.to_string(index=False))

    elif args.game == "lol":
        from pipeline.lol import LoLPipeline
        pipe = LoLPipeline(days_back=args.days)

        if args.command == "run":
            pipe.run(scrape=True, tune=args.tune)
        elif args.command == "scrape":
            pipe.scrape_and_store()
        elif args.command == "train":
            matches_df, map_df, _ = pipe.load_dataframes()
            pipe.build_elo(matches_df)
            pipe.train(tune=args.tune)
        elif args.command == "predict":
            logger.info("LoL predict: query upcoming matches from DB and call predict_match()")

    elif args.game == "valorant":
        from pipeline.valorant import ValorantPipeline
        pipe = ValorantPipeline(days_back=args.days)

        if args.command == "run":
            pipe.run(scrape=True, tune=args.tune, max_pages=args.pages)
        elif args.command == "scrape":
            pipe.scrape_and_store(max_pages=args.pages)
            pipe.scrape_upcoming()
        elif args.command == "train":
            matches_df, map_df, _ = pipe.load_dataframes()
            pipe.build_elo(matches_df, map_df)
            pipe.train(tune=args.tune)
        elif args.command == "predict":
            logger.info("Valorant predict: query upcoming matches from DB and call predict_match()")


def _print_predictions(predictions: list[dict]):
    if not predictions:
        print("No predictions available.")
        return
    print(f"\n{'='*60}")
    print(f"{'UPCOMING MATCH PREDICTIONS':^60}")
    print(f"{'='*60}")
    for p in predictions:
        print(
            f"  Match {p.get('upcoming_match_id', '?'):>4} | "
            f"T1 win: {p['team1_win_prob']:.1%} | "
            f"T2 win: {p['team2_win_prob']:.1%} | "
            f"{p.get('event', '')}"
        )
    print(f"{'='*60}\n")


def _load_lines(path: str) -> list:
    """Load betting lines from a JSON file."""
    from betting.edge import BettingLine
    with open(path) as f:
        raw = json.load(f)
    lines = []
    for r in raw:
        lines.append(BettingLine(
            match_id=r.get("match_id"),
            game=r.get("game", "cs2"),
            bet_type=r.get("bet_type", "match_winner"),
            description=r.get("description", ""),
            subject=r.get("subject", ""),
            american_odds=float(r["american_odds"]),
            line_value=r.get("line_value"),
        ))
    return lines


if __name__ == "__main__":
    main()
