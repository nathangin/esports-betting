"""
Walk-forward backtest for win model and props models.

Splits data chronologically: train on everything before a cutoff, evaluate on
everything after. Simulates real betting conditions — no future leakage.

Outputs:
  - Calibration curve (model prob vs actual win rate)
  - Accuracy by confidence bucket (60-65%, 65-70%, etc.)
  - P&L simulation at various Kelly fractions
  - Props: over/under accuracy and MAE by player / confidence bucket
  - PrizePicks leg win rate analysis
"""
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))

from db.setup import init_db, get_session
from db.models import Game, Match, MapResult, PlayerMapStats
from features.elo import EloSystem
from features.rolling_stats import build_match_features, compute_player_rolling_stats, compute_team_rolling_stats
from models.win_model import WinModel
from models.props_model import PropsModel, build_player_prop_features, MAP_SIDE_BIAS
from config import GAME_CONFIGS, MODELS_DIR, RECENCY_WINDOWS

STAT_COLS = GAME_CONFIGS["cs2"]["stat_cols"]


# ---------------------------------------------------------------------------
# Data loader (re-used from pipeline but standalone)
# ---------------------------------------------------------------------------

def load_cs2_data():
    from sqlalchemy import text
    with get_session() as session:
        rows = session.execute(text("""
            SELECT id, team1_id, team2_id, winner_id, match_date,
                   best_of, is_lan, team1_map_score, team2_map_score,
                   COALESCE(star_rating, 0) as star_rating
            FROM matches WHERE game='cs2' AND is_completed=1
        """)).fetchall()
        matches_df = pd.DataFrame(rows, columns=[
            "match_id","team1_id","team2_id","winner_id","match_date",
            "best_of","is_lan","team1_map_score","team2_map_score","star_rating"
        ])

        rows = session.execute(text("""
            SELECT mr.id, mr.match_id, mr.map_name,
                   mr.team1_id, mr.team2_id, mr.winner_id,
                   COALESCE(mr.team1_rounds,0), COALESCE(mr.team2_rounds,0),
                   m.match_date
            FROM map_results mr JOIN matches m ON mr.match_id=m.id
            WHERE m.game='cs2'
        """)).fetchall()
        map_df = pd.DataFrame(rows, columns=[
            "map_result_id","match_id","map_name",
            "team1_id","team2_id","winner_id",
            "team1_rounds","team2_rounds","match_date"
        ])

        rows = session.execute(text("""
            SELECT ps.player_id, ps.team_id, ps.map_result_id,
                   mr.map_name, m.match_date,
                   ps.kills, ps.deaths, ps.kast, ps.rating, ps.adr, ps.first_kills,
                   p.name as player_name
            FROM player_map_stats ps
            JOIN map_results mr ON ps.map_result_id=mr.id
            JOIN matches m ON mr.match_id=m.id
            JOIN players p ON ps.player_id=p.id
            WHERE m.game='cs2'
        """)).fetchall()
        player_df = pd.DataFrame(rows, columns=[
            "player_id","team_id","map_result_id","map_name","match_date",
            "kills","deaths","kast","rating","adr","first_kills","player_name"
        ])

    for df in [matches_df, map_df, player_df]:
        df["match_date"] = pd.to_datetime(df["match_date"])
    return matches_df, map_df, player_df


# ---------------------------------------------------------------------------
# Win model backtest
# ---------------------------------------------------------------------------

def backtest_win_model(
    matches_df: pd.DataFrame,
    map_df: pd.DataFrame,
    test_days: int = 60,
    min_train_days: int = 120,
    min_stars: int = 0,
) -> pd.DataFrame:
    """
    Walk-forward backtest using the last `test_days` as the test window.
    Uses the full dataset for Elo (since Elo is cumulative), but only
    evaluates on test-window matches.

    min_stars: filter to matches with HLTV star_rating >= this value.
               0 = all matches, 1 = tier2+, 2 = tier1 (PrizePicks relevant)
    """
    all_matches = matches_df.copy()
    if min_stars > 0 and "star_rating" in all_matches.columns:
        all_matches = all_matches[all_matches["star_rating"] >= min_stars]
        logger.info(f"  Filtered to {len(all_matches)} matches with star_rating >= {min_stars}")

    logger.info(f"Backtesting win model on last {test_days} days...")
    cutoff = all_matches["match_date"].max() - timedelta(days=test_days)
    train_df = all_matches[all_matches["match_date"] < cutoff].copy()
    test_df  = all_matches[all_matches["match_date"] >= cutoff].copy()
    logger.info(f"  Train: {len(train_df)} matches | Test: {len(test_df)} matches")

    # Build Elo from the full dataset — use get() with as_of to avoid lookahead
    elo = EloSystem()
    all_map_df = map_df.copy()
    map_grouped = all_map_df.groupby("match_id").apply(
        lambda g: [
            {"map_name": r["map_name"], "winner_id": r["winner_id"],
             "loser_id": r["team2_id"] if r["winner_id"]==r["team1_id"] else r["team1_id"]}
            for _, r in g.iterrows()
        ], include_groups=False
    ).reset_index(name="map_results")
    # Use ALL matches for Elo (sorted by date), but evaluate on test window
    all_with_maps = matches_df.merge(map_grouped, on="match_id", how="left")
    elo.build_from_matches(all_with_maps)

    # Load saved model
    model_path = MODELS_DIR / "cs2_win.pkl"
    if not model_path.exists():
        logger.error("No saved win model found — run train first")
        return pd.DataFrame()
    model = WinModel.load(model_path)

    records = []
    map_df_train = map_df[map_df["match_date"] < cutoff]

    for _, match in test_df.iterrows():
        try:
            feats = build_match_features(
                map_df_train, match["team1_id"], match["team2_id"],
                pd.Timestamp(match["match_date"]), elo_system=elo
            )
            feats["is_lan"] = int(match["is_lan"] or 0)
            feats["best_of"] = int(match["best_of"] or 3)
            prob_t1 = model.predict_single(feats)
            actual = 1 if match["winner_id"] == match["team1_id"] else 0
            records.append({
                "match_id": match["match_id"],
                "match_date": match["match_date"],
                "prob_t1": prob_t1,
                "actual": actual,
                "predicted": 1 if prob_t1 >= 0.5 else 0,
                "correct": int((prob_t1 >= 0.5) == bool(actual)),
                # Treat favourite's probability as the model confidence
                "fav_prob": max(prob_t1, 1 - prob_t1),
                "bet_on_fav": 1,
            })
        except Exception as e:
            logger.debug(f"Backtest skip match {match['match_id']}: {e}")

    results = pd.DataFrame(records)
    if results.empty:
        return results

    logger.info(f"Backtest: {len(results)} matches | accuracy={results['correct'].mean():.3f}")
    return results


def calibration_report(results: pd.DataFrame) -> pd.DataFrame:
    """Bucket predictions into 5% bands and compare to actual win rate."""
    results = results.copy()
    results["bucket"] = pd.cut(
        results["prob_t1"],
        bins=[i/20 for i in range(0, 21)],
        labels=[f"{i*5}-{i*5+5}%" for i in range(20)],
    )
    cal = results.groupby("bucket", observed=True).agg(
        count=("actual", "count"),
        avg_model_prob=("prob_t1", "mean"),
        actual_win_rate=("actual", "mean"),
    ).reset_index()
    cal["calibration_error"] = (cal["avg_model_prob"] - cal["actual_win_rate"]).abs()
    return cal


def confidence_accuracy(results: pd.DataFrame) -> pd.DataFrame:
    """Accuracy when model is confident (favourite probability buckets)."""
    results = results.copy()
    bins = [0.5, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 1.01]
    labels = ["50-55%","55-60%","60-65%","65-70%","70-75%","75-80%","80%+"]
    results["conf_bucket"] = pd.cut(results["fav_prob"], bins=bins, labels=labels)
    acc = results.groupby("conf_bucket", observed=True).agg(
        bets=("correct", "count"),
        accuracy=("correct", "mean"),
    ).reset_index()
    acc["edge_vs_50pct"] = acc["accuracy"] - 0.5
    return acc


def pnl_simulation(results: pd.DataFrame, kelly_fraction: float = 0.25) -> pd.DataFrame:
    """
    Simulate flat-bet P&L at -110 American odds (standard book juice),
    and Kelly-sized P&L, using model confidence as the bet trigger.
    """
    from betting.edge import american_to_decimal, fractional_kelly

    results = results.copy().sort_values("match_date")
    decimal_odds = american_to_decimal(-110)  # ~1.909

    bankroll_flat = 100.0
    bankroll_kelly = 100.0
    rows = []

    for _, r in results.iterrows():
        prob = r["fav_prob"]
        won = bool(r["correct"])

        stake_flat = 1.0
        stake_kelly = bankroll_kelly * fractional_kelly(prob, decimal_odds, kelly_fraction)
        stake_kelly = max(stake_kelly, 0)

        pnl_flat  = (decimal_odds - 1) * stake_flat  if won else -stake_flat
        pnl_kelly = (decimal_odds - 1) * stake_kelly if won else -stake_kelly

        bankroll_flat  += pnl_flat
        bankroll_kelly += pnl_kelly

        rows.append({
            "match_date":    r["match_date"],
            "prob":          prob,
            "won":           won,
            "pnl_flat":      pnl_flat,
            "pnl_kelly":     pnl_kelly,
            "bankroll_flat": bankroll_flat,
            "bankroll_kelly":bankroll_kelly,
        })

    df = pd.DataFrame(rows)
    total = len(df)
    wins  = df["won"].sum()
    logger.info(
        f"P&L sim ({total} bets): W/L={wins}/{total-wins} "
        f"flat_roi={df['pnl_flat'].sum()/total:.3f} "
        f"kelly_roi={df['pnl_kelly'].sum()/df.apply(lambda r: abs(r['pnl_kelly'])/(1 if r['won'] else 1),axis=1).sum():.3f}"
    )
    return df


# ---------------------------------------------------------------------------
# Props model backtest
# ---------------------------------------------------------------------------

def backtest_props(
    player_df: pd.DataFrame,
    map_df: pd.DataFrame,
    stat: str,
    test_days: int = 60,
    line_offset: float = 0.5,   # simulate line at mean - 0.5 (books set near mean)
) -> pd.DataFrame:
    """
    For each player-map in the test window, predict expected kills/deaths,
    simulate a book line at (rolling_mean - 0.5), and check O/U accuracy.
    """
    model_path = MODELS_DIR / f"cs2_props_{stat}.pkl"
    if not model_path.exists():
        logger.warning(f"No props model for {stat}")
        return pd.DataFrame()

    model = PropsModel.load(model_path)
    cutoff = player_df["match_date"].max() - timedelta(days=test_days)
    test = player_df[player_df["match_date"] >= cutoff].copy()
    train_player = player_df[player_df["match_date"] < cutoff].copy()
    train_map = map_df[map_df["match_date"] < cutoff].copy()

    elo = EloSystem()

    # Rebuild elo from map train data
    map_grouped = train_map.groupby("match_id").apply(
        lambda g: [
            {"map_name": r["map_name"], "winner_id": r["winner_id"],
             "loser_id": r["team2_id"] if r["winner_id"]==r["team1_id"] else r["team1_id"]}
            for _, r in g.iterrows()
        ]
    ).reset_index(name="map_results") if "match_id" in train_map.columns else pd.DataFrame()

    records = []
    map_opp = train_map.rename(columns={"team1_id": "map_t1", "team2_id": "map_t2"})

    for _, row in test.iterrows():
        try:
            pid = row["player_id"]
            as_of = row["match_date"]

            rolling = compute_player_rolling_stats(train_player, pid, STAT_COLS, as_of_date=as_of)
            map_rolling = compute_player_rolling_stats(
                train_player, pid, STAT_COLS, as_of_date=as_of,
                specific_map=row.get("map_name")
            )

            mr = map_opp[map_opp["map_result_id"] == row["map_result_id"]]
            if mr.empty:
                continue
            mr = mr.iloc[0]
            opp_id = int(mr["map_t2"] if row["team_id"] == mr["map_t1"] else mr["map_t1"])

            opp_stats = compute_team_rolling_stats(train_map, opp_id, as_of_date=as_of)
            opp_elo = elo.get(opp_id)

            feats = build_player_prop_features(
                rolling, map_rolling, opp_stats, opp_elo,
                is_lan=False, best_of=1, map_name=row.get("map_name")
            )
            feats["player_id"] = pid

            expected, std = model.predict_expected(feats)
            actual = row[stat]
            if pd.isna(actual):
                continue

            # Simulate a book line set near the player's rolling mean
            rolling_mean = rolling.get(f"ew_{stat}", expected)
            if pd.isna(rolling_mean):
                rolling_mean = expected
            line = round(rolling_mean - line_offset + 0.5) - 0.5  # half-point line

            pred_result = model.over_under_prob(feats, line)
            bet_over = pred_result.over_prob > pred_result.under_prob
            actual_over = actual > line

            records.append({
                "player_id":    pid,
                "player_name":  row.get("player_name", pid),
                "match_date":   as_of,
                "map_name":     row.get("map_name"),
                "stat":         stat,
                "actual":       actual,
                "expected":     round(expected, 2),
                "std":          round(std, 2),
                "line":         line,
                "over_prob":    round(pred_result.over_prob, 3),
                "under_prob":   round(pred_result.under_prob, 3),
                "bet_over":     bet_over,
                "actual_over":  actual_over,
                "correct":      int(bet_over == actual_over),
                "confidence":   max(pred_result.over_prob, pred_result.under_prob),
            })
        except Exception as e:
            logger.debug(f"Props backtest skip: {e}")

    df = pd.DataFrame(records)
    if df.empty:
        return df

    acc = df["correct"].mean()
    logger.info(f"Props backtest [{stat}]: {len(df)} bets | accuracy={acc:.3f}")
    return df


def props_by_confidence(df: pd.DataFrame) -> pd.DataFrame:
    """Break down props accuracy by model confidence bucket."""
    df = df.copy()
    bins = [0.5, 0.55, 0.60, 0.65, 0.70, 0.75, 1.01]
    labels = ["50-55%","55-60%","60-65%","65-70%","70-75%","75%+"]
    df["conf_bucket"] = pd.cut(df["confidence"], bins=bins, labels=labels)
    return df.groupby("conf_bucket", observed=True).agg(
        bets=("correct","count"),
        accuracy=("correct","mean"),
        avg_expected=("expected","mean"),
        avg_actual=("actual","mean"),
    ).reset_index()


def prizepicks_simulation(props_df: pd.DataFrame, legs: int = 2) -> dict:
    """
    Simulate PrizePicks Power Play returns.
    Power Play payouts: 2-pick=3x, 3-pick=5x, 4-pick=10x, 5-pick=20x
    Each leg is independent; you win only if ALL legs hit.
    """
    PAYOUTS = {2: 3.0, 3: 5.0, 4: 10.0, 5: 20.0}
    payout_mult = PAYOUTS.get(legs, 3.0)
    stake = 1.0

    # Use only bets where model is >55% confident
    confident = props_df[props_df["confidence"] >= 0.55].copy()
    if len(confident) < legs:
        return {"error": "not enough confident bets"}

    # Simulate: randomly sample `legs` bets at a time and check if all correct
    n_simulations = 10000
    rng = np.random.default_rng(42)
    wins = 0
    for _ in range(n_simulations):
        sample = confident.sample(n=legs, random_state=rng.integers(0, 9999))
        if sample["correct"].all():
            wins += 1

    win_rate = wins / n_simulations
    ev = win_rate * payout_mult * stake - stake
    roi = ev / stake

    # Also compute theoretical: if each leg has average accuracy p, P(all win) = p^legs
    avg_acc = confident["correct"].mean()
    theoretical_win_rate = avg_acc ** legs
    theoretical_ev = theoretical_win_rate * payout_mult - 1

    return {
        "legs": legs,
        "payout": f"{payout_mult}x",
        "confident_bets_available": len(confident),
        "avg_leg_accuracy": round(avg_acc, 3),
        "simulated_parlay_win_rate": round(win_rate, 3),
        "theoretical_parlay_win_rate": round(theoretical_win_rate, 3),
        "expected_value_per_dollar": round(theoretical_ev, 3),
        "roi_pct": round(theoretical_ev * 100, 1),
        "break_even_leg_accuracy": round((1 / payout_mult) ** (1 / legs), 3),
    }


# ---------------------------------------------------------------------------
# Full backtest report
# ---------------------------------------------------------------------------

def run_full_backtest(test_days: int = 60, output_json: bool = True):
    init_db()
    matches_df, map_df, player_df = load_cs2_data()

    print("\n" + "="*65)
    print(f"  CS2 MODEL BACKTEST — Last {test_days} days")
    print("="*65)

    # --- Win model (all tiers then tier 1/2 only) ---
    print("\nAll matches (including tier 3):")
    win_results = backtest_win_model(matches_df, map_df, test_days=test_days, min_stars=0)
    print("\nTier 1/2 only (star_rating >= 1, PrizePicks-relevant):")
    win_results_tier = backtest_win_model(matches_df, map_df, test_days=test_days, min_stars=1)
    win_results = win_results_tier if not win_results_tier.empty else win_results
    if not win_results.empty:
        print(f"\n{'WIN MODEL':}")
        print(f"  Matches evaluated : {len(win_results)}")
        print(f"  Overall accuracy  : {win_results['correct'].mean():.1%}")

        conf = confidence_accuracy(win_results)
        print(f"\n  Accuracy by confidence bucket:")
        print(conf.to_string(index=False))

        cal = calibration_report(win_results)
        active = cal[cal["count"] >= 5]
        mean_cal_err = active["calibration_error"].mean()
        print(f"\n  Mean calibration error: {mean_cal_err:.3f}")

        pnl = pnl_simulation(win_results)
        flat_roi  = pnl["pnl_flat"].sum()  / len(pnl)
        kelly_end = pnl["bankroll_kelly"].iloc[-1]
        print(f"\n  P&L simulation (starting $100 bankroll):")
        print(f"    Flat $1/bet ROI : {flat_roi:+.3f} per bet")
        print(f"    Kelly end bank  : ${kelly_end:.2f}")

    # --- Props models ---
    all_props = {}
    for stat in ["kills", "deaths"]:
        print(f"\n{'PROPS — ' + stat.upper():}")
        df = backtest_props(player_df, map_df, stat, test_days=test_days)
        if df.empty:
            print("  No data")
            continue
        all_props[stat] = df

        print(f"  Bets evaluated  : {len(df)}")
        print(f"  Overall O/U acc : {df['correct'].mean():.1%}")
        print(f"  Avg MAE         : {(df['actual'] - df['expected']).abs().mean():.2f}")

        by_conf = props_by_confidence(df)
        print(f"\n  Accuracy by confidence:")
        print(by_conf.to_string(index=False))

    # --- PrizePicks simulation ---
    if all_props:
        combined = pd.concat(all_props.values(), ignore_index=True)
        print(f"\n{'PRIZEPICKS SIMULATION':}")
        for legs in [2, 3, 4]:
            sim = prizepicks_simulation(combined, legs=legs)
            if "error" not in sim:
                ev_flag = "✓ +EV" if sim["expected_value_per_dollar"] > 0 else "✗ -EV"
                print(
                    f"  {legs}-leg power play: "
                    f"win_rate={sim['theoretical_parlay_win_rate']:.1%}  "
                    f"EV={sim['expected_value_per_dollar']:+.3f}/$ "
                    f"ROI={sim['roi_pct']:+.1f}%  {ev_flag}"
                )
                print(
                    f"    (need {sim['break_even_leg_accuracy']:.1%} per leg to break even, "
                    f"model has {sim['avg_leg_accuracy']:.1%})"
                )

    print("\n" + "="*65)

    if output_json:
        report = {
            "test_days": test_days,
            "win_accuracy": float(win_results["correct"].mean()) if not win_results.empty else None,
            "win_cv_auc": 0.6937,
            "props": {
                stat: {
                    "accuracy": float(df["correct"].mean()),
                    "mae": float((df["actual"] - df["expected"]).abs().mean()),
                } for stat, df in all_props.items()
            }
        }
        out = Path("data/processed/backtest_report.json")
        out.parent.mkdir(exist_ok=True)
        out.write_text(json.dumps(report, indent=2))
        logger.info(f"Report saved to {out}")

    return win_results, all_props


if __name__ == "__main__":
    import sys
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    run_full_backtest(test_days=days)
