"""
Proper out-of-sample backtest.

Trains a fresh model on the first 80% of matches (chronologically),
then evaluates on the most recent 20%. Zero data leakage.

Also backtests props models by predicting per-player kill/death lines
against simulated book lines set at the player's rolling mean.

Oct 2026: training features no longer leak (``build_training_dataset`` replays Elo in time
order; it used to hand every training row the final ratings), the AUC printed is the one
measured on the test matches (it was a hard-coded 0.694), and the made-up P&L "at -110" is
gone: there are no real odds in this database. For P&L on real prices run
``python -m esalpha backtest``. Prop lines here are synthetic.
"""
import sys
from pathlib import Path
from datetime import timedelta

import numpy as np
import pandas as pd
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))

from db.setup import init_db
from features.elo import EloSystem
from features.rolling_stats import build_training_dataset, build_match_features, compute_player_rolling_stats, compute_team_rolling_stats
from models.win_model import WinModel
from models.props_model import PropsModel, build_player_prop_features, MAP_SIDE_BIAS
from backtest.backtest import load_cs2_data, calibration_report, confidence_accuracy, oos_metrics, props_by_confidence, prizepicks_simulation
from config import GAME_CONFIGS

STAT_COLS = GAME_CONFIGS["cs2"]["stat_cols"]


def proper_win_backtest(matches_df, map_df, train_pct=0.80):
    """Train on first train_pct of matches, test on the remaining."""
    matches_sorted = matches_df.sort_values("match_date").reset_index(drop=True)
    split_idx = int(len(matches_sorted) * train_pct)
    cutoff_date = matches_sorted.iloc[split_idx]["match_date"]

    train = matches_sorted.iloc[:split_idx].copy()
    test  = matches_sorted.iloc[split_idx:].copy()
    logger.info(f"Train: {len(train)} matches up to {cutoff_date.date()} | Test: {len(test)} matches")

    # Build Elo from training data only
    map_train = map_df[map_df["match_date"] <= cutoff_date].copy()
    map_grouped = map_train.groupby("match_id", group_keys=False).apply(
        lambda g: [
            {"map_name": r["map_name"], "winner_id": r["winner_id"],
             "loser_id": r["team2_id"] if r["winner_id"]==r["team1_id"] else r["team1_id"]}
            for _, r in g.iterrows()
        ]
    ).reset_index(name="map_results")
    enriched_train = train.merge(map_grouped, on="match_id", how="left")
    elo = EloSystem()
    elo.build_from_matches(enriched_train)

    # Build feature matrix (no lookahead — build_training_dataset uses as_of per row)
    logger.info("Building training feature matrix...")
    train_feats = build_training_dataset(train, map_train, elo, target="match_winner")

    # Train fresh model
    model = WinModel("cs2_win_oos")
    model.fit(train_feats, calibrate=True)

    # Predict test set
    logger.info("Predicting test matches...")
    records = []
    for _, match in test.iterrows():
        try:
            feats = build_match_features(
                map_train,
                match["team1_id"], match["team2_id"],
                pd.Timestamp(match["match_date"]),
                elo_system=elo,
            )
            feats["is_lan"]  = int(match.get("is_lan") or 0)
            feats["best_of"] = int(match.get("best_of") or 3)
            prob = model.predict_single(feats)
            actual = 1 if match["winner_id"] == match["team1_id"] else 0
            records.append({
                "match_id":   match["match_id"],
                "match_date": match["match_date"],
                "prob_t1":    prob,
                "actual":     actual,
                "correct":    int((prob >= 0.5) == bool(actual)),
                "fav_prob":   max(prob, 1 - prob),
            })
        except Exception as e:
            logger.debug(f"Skip match {match['match_id']}: {e}")

    return pd.DataFrame(records), model


def proper_props_backtest(player_df, map_df, matches_df, stat, train_pct=0.80):
    """Train props model on first train_pct, test on rest."""
    sorted_df = player_df.sort_values("match_date").reset_index(drop=True)
    split_idx = int(len(sorted_df) * train_pct)
    cutoff_date = sorted_df.iloc[split_idx]["match_date"]

    train_p = sorted_df.iloc[:split_idx].copy()
    test_p  = sorted_df.iloc[split_idx:].copy()
    train_m = map_df[map_df["match_date"] <= cutoff_date].copy()
    train_matches = matches_df[matches_df["match_date"] <= cutoff_date].copy()

    logger.info(f"Props [{stat}] train: {len(train_p)} | test: {len(test_p)}")
    if len(train_p.dropna(subset=[stat])) < 50:
        logger.warning(f"Not enough data to train props [{stat}]")
        return pd.DataFrame()

    # Build props training features vectorized
    from pipeline.cs2 import CS2Pipeline
    pipe = CS2Pipeline.__new__(CS2Pipeline)
    pipe.elo = EloSystem()
    map_grouped = train_m.groupby("match_id", group_keys=False).apply(
        lambda g: [
            {"map_name": r["map_name"], "winner_id": r["winner_id"],
             "loser_id": r["team2_id"] if r["winner_id"]==r["team1_id"] else r["team1_id"]}
            for _, r in g.iterrows()
        ]
    ).reset_index(name="map_results")
    enriched = train_matches.merge(map_grouped, on="match_id", how="left")
    pipe.elo.build_from_matches(enriched)

    train_feats = pipe._build_props_training_df(train_p, train_m, stat)
    model = PropsModel(stat, game="cs2")
    model.fit(train_feats)

    # Evaluate on test set
    map_opp = train_m.rename(columns={"team1_id": "map_t1", "team2_id": "map_t2"})
    records = []
    for _, row in test_p.iterrows():
        if pd.isna(row.get(stat)):
            continue
        try:
            pid = row["player_id"]
            as_of = row["match_date"]
            rolling = compute_player_rolling_stats(train_p, pid, STAT_COLS, as_of_date=as_of)
            map_rolling = compute_player_rolling_stats(train_p, pid, STAT_COLS, as_of_date=as_of, specific_map=row.get("map_name"))
            mr = map_opp[map_opp["map_result_id"] == row["map_result_id"]]
            if mr.empty:
                continue
            mr = mr.iloc[0]
            opp_id = int(mr["map_t2"] if row["team_id"] == mr["map_t1"] else mr["map_t1"])
            opp_stats = compute_team_rolling_stats(train_m, opp_id, as_of_date=as_of)
            opp_elo = pipe.elo.get(opp_id)

            feats = build_player_prop_features(rolling, map_rolling, opp_stats, opp_elo, is_lan=False, best_of=1, map_name=row.get("map_name"))
            feats["player_id"] = pid

            expected, std = model.predict_expected(feats)
            actual = float(row[stat])
            rolling_mean = rolling.get(f"ew_{stat}", expected)
            if pd.isna(rolling_mean):
                rolling_mean = expected
            line = round(float(rolling_mean) - 0.5 + 0.5) - 0.5

            pred = model.over_under_prob(feats, line)
            bet_over = pred.over_prob > pred.under_prob
            actual_over = actual > line

            records.append({
                "player_name":  row.get("player_name", pid),
                "match_date":   as_of,
                "map_name":     row.get("map_name"),
                "stat":         stat,
                "actual":       actual,
                "expected":     round(expected, 2),
                "line":         line,
                "over_prob":    round(pred.over_prob, 3),
                "under_prob":   round(pred.under_prob, 3),
                "bet_over":     bet_over,
                "actual_over":  actual_over,
                "correct":      int(bet_over == actual_over),
                "confidence":   max(pred.over_prob, pred.under_prob),
            })
        except Exception as e:
            logger.debug(f"Props skip: {e}")

    return pd.DataFrame(records)


def run_proper_backtest():
    init_db()
    matches_df, map_df, player_df = load_cs2_data()

    print("\n" + "="*65)
    print("  CS2 PROPER OUT-OF-SAMPLE BACKTEST (80/20 split)")
    print("="*65)

    # Win model
    win_results, model = proper_win_backtest(matches_df, map_df, train_pct=0.80)
    if win_results.empty:
        print("No win results")
        return

    n = len(win_results)
    acc = win_results["correct"].mean()
    print(f"\nWIN MODEL — {n} test matches")
    print(f"  Accuracy        : {acc:.1%}")

    conf = confidence_accuracy(win_results)
    print(f"\n  Accuracy by confidence (only bet here if accuracy > book's implied):")
    print(conf.to_string(index=False))

    cal = calibration_report(win_results)
    active = cal[cal["count"] >= 3]
    print(f"\n  Mean calibration error: {active['calibration_error'].mean():.3f}")
    print(f"  (0.00 = perfect, 0.50 = random)")

    m = oos_metrics(win_results)
    print(f"\n  Out-of-sample log loss: {m['log_loss']:.4f} (coin flip {m['coin_flip_log_loss']:.4f}), "
          f"Brier {m['brier']:.4f}, AUC {m['auc'] if m['auc'] is None else round(m['auc'], 3)}")
    print("  No P&L: the database has no real odds, and accuracy alone does not say whether a")
    print("  bet beats its price. Real-price backtest: `python -m esalpha backtest`.")

    # Props
    all_props = {}
    for stat in ["kills", "deaths"]:
        print(f"\nPROPS — {stat.upper()}")
        df = proper_props_backtest(player_df, map_df, matches_df, stat, train_pct=0.80)
        if df.empty:
            print("  No data")
            continue
        all_props[stat] = df
        ou_acc = df["correct"].mean()
        mae = (df["actual"] - df["expected"]).abs().mean()
        print(f"  O/U accuracy vs synthetic lines: {ou_acc:.1%}  MAE: {mae:.2f}")
        by_conf = props_by_confidence(df)
        print(f"\n  By confidence bucket:")
        print(by_conf.to_string(index=False))

    # PrizePicks power play simulation
    if all_props:
        combined = pd.concat(all_props.values(), ignore_index=True)
        print(f"\nPRIZEPICKS SIMULATION (synthetic lines, confident legs >= 55%; not a real result)")
        for legs in [2, 3, 4]:
            sim = prizepicks_simulation(combined, legs=legs)
            if "error" not in sim:
                ev_flag = "+EV" if sim["expected_value_per_dollar"] > 0 else "-EV"
                print(
                    f"  {legs}-pick Power Play: "
                    f"win_rate={sim['theoretical_parlay_win_rate']:.1%}  "
                    f"EV={sim['expected_value_per_dollar']:+.3f}/$  "
                    f"ROI={sim['roi_pct']:+.1f}%  [{ev_flag}]"
                )
                print(f"    Need {sim['break_even_leg_accuracy']:.1%}/leg to break even, "
                      f"model has {sim['avg_leg_accuracy']:.1%}/leg")

    print("\n" + "="*65)
    print("\nSUMMARY FOR BETTING:")
    print(f"  Win model OOS accuracy : {acc:.1%}")
    print(f"  Win model OOS AUC      : {m['auc'] if m['auc'] is None else round(m['auc'], 3)}")
    best_bucket = conf.loc[conf["accuracy"].idxmax()]
    print(f"  Best confidence bucket : {best_bucket['conf_bucket']} ({best_bucket['accuracy']:.1%} acc, {int(best_bucket['bets'])} bets)")
    if all_props:
        for stat, df in all_props.items():
            confident = df[df["confidence"] >= 0.56]
            print(f"  Props [{stat}] at 56%+ conf: {len(confident)} bets, {confident['correct'].mean():.1%} O/U accuracy")
    print("="*65)


if __name__ == "__main__":
    run_proper_backtest()
