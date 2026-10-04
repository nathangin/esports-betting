"""
Rolling statistics engine — per-player, per-team, per-map.

Supports:
 - Exponentially-decayed weighted averages
 - Fixed windows (last-N)
 - H2H (head-to-head) stats between two specific teams
 - Map-specific breakdowns
"""
import math
from typing import Optional
import pandas as pd
import numpy as np
from loguru import logger

from config import RECENCY_WINDOWS, RECENCY_DECAY


def decay_weights(n: int, decay: float = RECENCY_DECAY) -> np.ndarray:
    """
    Exponential decay weights for n observations, most recent last.
    weights[-1] = 1.0, weights[-2] = decay, etc.
    """
    w = np.array([decay ** i for i in range(n - 1, -1, -1)])
    return w / w.sum()


def weighted_mean(values: pd.Series, decay: float = RECENCY_DECAY) -> float:
    arr = values.dropna().values
    if len(arr) == 0:
        return float("nan")
    w = decay_weights(len(arr), decay)
    return float(np.dot(w, arr))


# ---------------------------------------------------------------------------
# Team rolling stats
# ---------------------------------------------------------------------------

def compute_team_rolling_stats(
    map_results_df: pd.DataFrame,
    team_id: int,
    as_of_date: Optional[pd.Timestamp] = None,
    specific_map: Optional[str] = None,
) -> dict:
    """
    Compute rolling stats for a team from a map-level results DataFrame.

    Required columns: match_date, team1_id, team2_id, winner_id,
                      team1_rounds, team2_rounds, map_name
    """
    df = map_results_df.copy()
    if as_of_date is not None:
        df = df[df["match_date"] < as_of_date]
    if specific_map:
        df = df[df["map_name"] == specific_map]

    # Rows where this team played
    t1_rows = df[df["team1_id"] == team_id].copy()
    t2_rows = df[df["team2_id"] == team_id].copy()

    t1_rows["team_rounds"] = t1_rows["team1_rounds"]
    t1_rows["opp_rounds"] = t1_rows["team2_rounds"]
    t1_rows["won"] = (t1_rows["winner_id"] == team_id).astype(int)

    t2_rows["team_rounds"] = t2_rows["team2_rounds"]
    t2_rows["opp_rounds"] = t2_rows["team1_rounds"]
    t2_rows["won"] = (t2_rows["winner_id"] == team_id).astype(int)

    combined = pd.concat([t1_rows, t2_rows]).sort_values("match_date")

    if len(combined) == 0:
        return _empty_team_stats(team_id)

    stats = {"team_id": team_id, "total_maps": len(combined)}

    # Exponentially-weighted win rate
    stats["ew_win_rate"] = weighted_mean(combined["won"])
    stats["ew_round_diff"] = weighted_mean(combined["team_rounds"] - combined["opp_rounds"])

    # Fixed window stats
    for w in RECENCY_WINDOWS:
        recent = combined.tail(w)
        stats[f"win_rate_last{w}"] = recent["won"].mean()
        stats[f"round_diff_last{w}"] = (recent["team_rounds"] - recent["opp_rounds"]).mean()

    # Map-specific win rate (when specific_map not already filtered)
    if not specific_map:
        for map_name in combined["map_name"].unique():
            map_rows = combined[combined["map_name"] == map_name]
            stats[f"wr_{map_name.replace(' ', '_')}"] = map_rows["won"].mean()

    return stats


def _empty_team_stats(team_id: int) -> dict:
    stats = {"team_id": team_id, "total_maps": 0, "ew_win_rate": 0.5, "ew_round_diff": 0.0}
    for w in RECENCY_WINDOWS:
        stats[f"win_rate_last{w}"] = 0.5
        stats[f"round_diff_last{w}"] = 0.0
    return stats


# ---------------------------------------------------------------------------
# Player rolling stats
# ---------------------------------------------------------------------------

def compute_player_rolling_stats(
    player_stats_df: pd.DataFrame,
    player_id: int,
    stat_cols: list[str],
    as_of_date: Optional[pd.Timestamp] = None,
    specific_map: Optional[str] = None,
) -> dict:
    """
    Rolling stats for a single player.

    Required columns: player_id, match_date, map_name, <stat_cols>
    """
    df = player_stats_df[player_stats_df["player_id"] == player_id].copy()
    if as_of_date is not None:
        df = df[df["match_date"] < as_of_date]
    if specific_map:
        df = df[df["map_name"] == specific_map]

    df = df.sort_values("match_date")

    stats = {"player_id": player_id, "maps_played": len(df)}

    if len(df) == 0:
        for col in stat_cols:
            stats[f"ew_{col}"] = float("nan")
            for w in RECENCY_WINDOWS:
                stats[f"{col}_last{w}"] = float("nan")
        return stats

    for col in stat_cols:
        if col not in df.columns:
            continue
        stats[f"ew_{col}"] = weighted_mean(df[col])
        for w in RECENCY_WINDOWS:
            recent = df[col].tail(w)
            stats[f"{col}_last{w}"] = recent.mean()

    # Trend: compare last5 vs last20 (momentum signal)
    for col in stat_cols:
        if col not in df.columns:
            continue
        l5 = stats.get(f"{col}_last5", float("nan"))
        l20 = stats.get(f"{col}_last20", float("nan"))
        if not math.isnan(l5) and not math.isnan(l20) and l20 != 0:
            stats[f"{col}_trend"] = (l5 - l20) / abs(l20)
        else:
            stats[f"{col}_trend"] = 0.0

    return stats


# ---------------------------------------------------------------------------
# H2H stats
# ---------------------------------------------------------------------------

def compute_h2h_stats(
    map_results_df: pd.DataFrame,
    team1_id: int,
    team2_id: int,
    as_of_date: Optional[pd.Timestamp] = None,
    specific_map: Optional[str] = None,
    lookback_n: int = 10,
) -> dict:
    """H2H win rates and round differentials between two specific teams."""
    df = map_results_df.copy()
    if as_of_date is not None:
        df = df[df["match_date"] < as_of_date]

    h2h = df[
        ((df["team1_id"] == team1_id) & (df["team2_id"] == team2_id)) |
        ((df["team1_id"] == team2_id) & (df["team2_id"] == team1_id))
    ].copy()

    if specific_map:
        h2h = h2h[h2h["map_name"] == specific_map]

    h2h = h2h.sort_values("match_date").tail(lookback_n)

    if len(h2h) == 0:
        return {
            "h2h_maps": 0,
            "h2h_win_rate_t1": 0.5,
            "h2h_round_diff_t1": 0.0,
            "h2h_ew_win_rate_t1": 0.5,
        }

    t1_won = h2h["winner_id"].apply(lambda w: 1 if w == team1_id else 0)
    t1_rounds = h2h.apply(
        lambda r: r["team1_rounds"] if r["team1_id"] == team1_id else r["team2_rounds"],
        axis=1,
    )
    t2_rounds = h2h.apply(
        lambda r: r["team2_rounds"] if r["team1_id"] == team1_id else r["team1_rounds"],
        axis=1,
    )

    return {
        "h2h_maps": len(h2h),
        "h2h_win_rate_t1": t1_won.mean(),
        "h2h_round_diff_t1": (t1_rounds - t2_rounds).mean(),
        "h2h_ew_win_rate_t1": weighted_mean(t1_won),
    }


# ---------------------------------------------------------------------------
# Map pool analysis
# ---------------------------------------------------------------------------

def compute_map_pool_stats(
    map_results_df: pd.DataFrame,
    team_id: int,
    as_of_date: Optional[pd.Timestamp] = None,
) -> dict:
    """Per-map win rates and round differentials for a team."""
    df = map_results_df.copy()
    if as_of_date is not None:
        df = df[df["match_date"] < as_of_date]

    played = df[(df["team1_id"] == team_id) | (df["team2_id"] == team_id)]
    stats: dict = {}

    for map_name in played["map_name"].unique():
        m = played[played["map_name"] == map_name]
        won = m["winner_id"].apply(lambda w: w == team_id)
        t_rounds = m.apply(
            lambda r: r["team1_rounds"] if r["team1_id"] == team_id else r["team2_rounds"],
            axis=1,
        )
        o_rounds = m.apply(
            lambda r: r["team2_rounds"] if r["team1_id"] == team_id else r["team1_rounds"],
            axis=1,
        )
        key = map_name.replace(" ", "_").replace("-", "_")
        stats[f"pool_{key}_wr"] = won.mean()
        stats[f"pool_{key}_rd"] = (t_rounds - o_rounds).mean()
        stats[f"pool_{key}_n"] = len(m)

    return stats


# ---------------------------------------------------------------------------
# Full feature matrix builder (team-vs-team for a match)
# ---------------------------------------------------------------------------

def build_match_features(
    map_results_df: pd.DataFrame,
    team1_id: int,
    team2_id: int,
    match_date: pd.Timestamp,
    elo_system=None,               # EloSystem instance
    target_map: Optional[str] = None,
) -> dict:
    """
    Assemble the full feature vector for a team1 vs team2 matchup.
    All stats are computed as_of match_date (no lookahead).
    """
    features: dict = {}

    # --- Elo ---
    if elo_system is not None:
        features["elo_t1_overall"] = elo_system.get(team1_id, "overall")
        features["elo_t2_overall"] = elo_system.get(team2_id, "overall")
        features["elo_diff_overall"] = features["elo_t1_overall"] - features["elo_t2_overall"]
        features["elo_win_prob_t1"] = elo_system.win_probability(team1_id, team2_id)

        if target_map:
            features["elo_t1_map"] = elo_system.get(team1_id, target_map)
            features["elo_t2_map"] = elo_system.get(team2_id, target_map)
            features["elo_diff_map"] = features["elo_t1_map"] - features["elo_t2_map"]
            features["elo_win_prob_t1_map"] = elo_system.win_probability(
                team1_id, team2_id, target_map
            )

    # --- Team rolling stats ---
    t1_stats = compute_team_rolling_stats(map_results_df, team1_id, match_date, target_map)
    t2_stats = compute_team_rolling_stats(map_results_df, team2_id, match_date, target_map)

    for key, val in t1_stats.items():
        if key != "team_id":
            features[f"t1_{key}"] = val
    for key, val in t2_stats.items():
        if key != "team_id":
            features[f"t2_{key}"] = val

    # Differential features
    for w in RECENCY_WINDOWS:
        wr1 = t1_stats.get(f"win_rate_last{w}", 0.5)
        wr2 = t2_stats.get(f"win_rate_last{w}", 0.5)
        features[f"wr_diff_last{w}"] = wr1 - wr2
        rd1 = t1_stats.get(f"round_diff_last{w}", 0.0)
        rd2 = t2_stats.get(f"round_diff_last{w}", 0.0)
        features[f"rd_diff_last{w}"] = rd1 - rd2

    # --- H2H ---
    h2h = compute_h2h_stats(map_results_df, team1_id, team2_id, match_date, target_map)
    features.update(h2h)

    # --- Map pool ---
    if target_map:
        mp1 = compute_map_pool_stats(map_results_df, team1_id, match_date)
        mp2 = compute_map_pool_stats(map_results_df, team2_id, match_date)
        key = target_map.replace(" ", "_").replace("-", "_")
        features[f"t1_pool_wr_{key}"] = mp1.get(f"pool_{key}_wr", 0.5)
        features[f"t2_pool_wr_{key}"] = mp2.get(f"pool_{key}_wr", 0.5)
        features[f"t1_pool_rd_{key}"] = mp1.get(f"pool_{key}_rd", 0.0)
        features[f"t2_pool_rd_{key}"] = mp2.get(f"pool_{key}_rd", 0.0)
        features[f"map_pool_wr_diff"] = (
            features[f"t1_pool_wr_{key}"] - features[f"t2_pool_wr_{key}"]
        )

    return features


def pre_match_team_win_rates(map_results_df: pd.DataFrame, decay: float = RECENCY_DECAY) -> dict:
    """{map_result_id: {team_id: decay-weighted map win rate before that map's match}}.

    Same weighting as ``compute_team_rolling_stats(...)["ew_win_rate"]`` (what the live
    prediction uses), but computed for every historical map from earlier matches only.
    Teams with no history get 0.5.
    """
    out: dict = {}
    if map_results_df is None or map_results_df.empty:
        return out
    df = map_results_df.dropna(subset=["match_id"]).sort_values("match_date", kind="stable")
    acc: dict = {}   # team -> [weighted wins, weight]
    for mid, g in df.groupby("match_id", sort=False):
        teams = list(dict.fromkeys(list(g["team1_id"]) + list(g["team2_id"])))
        pre = {t: (acc[t][0] / acc[t][1] if t in acc and acc[t][1] > 0 else 0.5) for t in teams}
        for mr in g["map_result_id"]:
            out[mr] = pre
        for r in g.itertuples(index=False):       # maps of this match enter afterwards
            for t in (r.team1_id, r.team2_id):
                num, den = acc.get(t, [0.0, 0.0])
                acc[t] = [num * decay + float(r.winner_id == t), den * decay + 1.0]
    return out


def _map_results_by_match(map_results_df: pd.DataFrame) -> dict:
    """{match_id: [{map_name, winner_id, loser_id}, ...]} for per-map Elo updates."""
    out: dict = {}
    if map_results_df is None or map_results_df.empty or "match_id" not in map_results_df.columns:
        return out
    for r in map_results_df.itertuples(index=False):
        if pd.isna(r.winner_id):
            continue
        loser = r.team2_id if r.winner_id == r.team1_id else r.team1_id
        out.setdefault(r.match_id, []).append({"map_name": r.map_name, "winner_id": r.winner_id, "loser_id": loser})
    return out


def build_training_dataset(
    matches_df: pd.DataFrame,
    map_results_df: pd.DataFrame,
    elo_system,
    target: str = "match_winner",   # match_winner | map_winner | round_total
) -> pd.DataFrame:
    """
    Build the full historical feature + label dataset for model training.
    Each row is one match (or map) with features computed as_of match_date.

    Elo features are taken from a replay of the matches in time order: each row sees the
    ratings as they stood *before* that match. (Earlier versions passed the final, fully
    built ratings into every row, so each training row already contained its own result
    and every later one: the model looked far better in training than it could be live.)
    ``elo_system`` only supplies the K factors and starting rating.
    """
    rows = []
    matches_sorted = matches_df.sort_values("match_date", kind="stable")
    replay = elo_system.fresh() if elo_system is not None and hasattr(elo_system, "fresh") else None
    maps_by_match = _map_results_by_match(map_results_df)

    for _, match in matches_sorted.iterrows():
        try:
            feats = build_match_features(
                map_results_df=map_results_df,
                team1_id=match["team1_id"],
                team2_id=match["team2_id"],
                match_date=pd.Timestamp(match["match_date"]),
                elo_system=replay,
            )
            feats["match_id"] = match["match_id"]
            feats["match_date"] = match["match_date"]
            feats["is_lan"] = int(match.get("is_lan", False) or 0)
            feats["best_of"] = match.get("best_of", 3)

            if target == "match_winner":
                feats["label"] = 1 if match["winner_id"] == match["team1_id"] else 0
            elif target == "team1_map_score":
                feats["label"] = match["team1_map_score"]

            rows.append(feats)
        except Exception as e:
            logger.debug(f"Error building features for match {match.get('match_id')}: {e}")
        finally:
            # only now does this match's result enter the ratings
            if replay is not None:
                s1 = match.get("team1_map_score")
                s2 = match.get("team2_map_score")
                if pd.isna(s1) or pd.isna(s2) or (s1 + s2) == 0:
                    if pd.notna(match.get("winner_id")):
                        s1, s2 = (1, 0) if match["winner_id"] == match["team1_id"] else (0, 1)
                    else:
                        s1 = s2 = 0
                replay.update_match(
                    match_id=match["match_id"], team1_id=match["team1_id"], team2_id=match["team2_id"],
                    team1_maps_won=int(s1), team2_maps_won=int(s2), match_date=match["match_date"],
                    map_results=maps_by_match.get(match["match_id"]),
                )

    df = pd.DataFrame(rows)
    logger.info(f"Training dataset: {len(df)} rows, {len(df.columns)} features")
    return df
