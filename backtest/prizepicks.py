"""
PrizePicks live line scraper + edge finder.

PrizePicks exposes an unofficial JSON API used by their web app.
Endpoints don't require auth for reading public projections.

Usage:
  python backtest/prizepicks.py              # print today's esports lines
  python backtest/prizepicks.py --edge       # compare to model, show edges
"""
import sys
import time
import argparse
from pathlib import Path
from typing import Optional

import requests
import pandas as pd
from loguru import logger

sys.path.insert(0, str(Path(__file__).parent.parent))

PP_API = "https://api.prizepicks.com"
PP_HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://app.prizepicks.com/",
    "x-device-id": "esports-model",
}

# PrizePicks league IDs for esports
ESPORTS_LEAGUES = {
    "CS2":       "esports-cs2",       # may vary — discover via /leagues
    "LOL":       "esports-lol",
    "VALORANT":  "esports-valorant",
}

STAT_MAP = {
    # PrizePicks stat name -> our model stat name
    "Kills":         "kills",
    "Deaths":        "deaths",
    "Assists":       "assists",
    "Headshots":     "hs_count",
    "Headshot %":    "hs_pct",
    "Rating":        "rating",
    "ADR":           "adr",
    "ACS":           "acs",
    "KDA":           None,   # not modeled directly
}


def fetch_leagues() -> list[dict]:
    resp = requests.get(f"{PP_API}/leagues", headers=PP_HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", [])


def fetch_projections(league_id: Optional[str] = None, per_page: int = 250) -> list[dict]:
    """Fetch all active projections, optionally filtered by league."""
    params = {
        "per_page": per_page,
        "single_stat": "true",
        "in_game": "false",
    }
    if league_id:
        params["league_id"] = league_id

    resp = requests.get(
        f"{PP_API}/projections",
        headers=PP_HEADERS,
        params=params,
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json()


def parse_projections(raw: dict) -> pd.DataFrame:
    """
    Parse PrizePicks API response into a flat DataFrame.
    The API uses JSON:API format with a `data` array and `included` sideloads.
    """
    projections = raw.get("data", [])
    included = {
        item["type"] + ":" + item["id"]: item
        for item in raw.get("included", [])
    }

    rows = []
    for proj in projections:
        attrs = proj.get("attributes", {})
        rels = proj.get("relationships", {})

        # Resolve player from included
        player_rel = rels.get("new_player", {}).get("data", {})
        player_key = f"new_player:{player_rel.get('id', '')}"
        player = included.get(player_key, {}).get("attributes", {})

        # Resolve league
        league_rel = rels.get("league", {}).get("data", {})
        league_key = f"league:{league_rel.get('id', '')}"
        league = included.get(league_key, {}).get("attributes", {})

        stat_type = attrs.get("stat_type", "")
        line = attrs.get("line_score")
        if line is None:
            continue

        rows.append({
            "projection_id": proj["id"],
            "player_name":   player.get("name", ""),
            "team_name":     player.get("team", ""),
            "position":      player.get("position", ""),
            "league":        league.get("name", ""),
            "stat":          stat_type,
            "model_stat":    STAT_MAP.get(stat_type),
            "line":          float(line),
            "start_time":    attrs.get("start_time"),
            "description":   attrs.get("description", ""),
            "status":        attrs.get("status", ""),
            "game_id":       attrs.get("game_id"),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        df = df[df["status"] == "pre_game"].copy()
    return df


def get_esports_lines(games: list[str] = None) -> pd.DataFrame:
    """
    Fetch all live esports lines from PrizePicks.
    games: list of ['CS2', 'LOL', 'VALORANT'] or None for all
    """
    logger.info("Fetching PrizePicks projections...")
    try:
        raw = fetch_projections()
        all_lines = parse_projections(raw)
    except Exception as e:
        logger.error(f"Failed to fetch PrizePicks lines: {e}")
        return pd.DataFrame()

    if all_lines.empty:
        return all_lines

    # Filter to esports games
    esports_keywords = ["CS", "League", "Valorant", "Counter", "CSGO", "CS2", "LOL", "LoL"]
    mask = all_lines["league"].apply(
        lambda l: any(kw.lower() in str(l).lower() for kw in esports_keywords)
    )
    esports = all_lines[mask].copy()

    if games:
        game_mask = esports["league"].apply(
            lambda l: any(g.lower() in str(l).lower() for g in games)
        )
        esports = esports[game_mask]

    logger.info(f"Found {len(esports)} esports prop lines")
    return esports


# ---------------------------------------------------------------------------
# Edge finder: compare PrizePicks lines to model predictions
# ---------------------------------------------------------------------------

def find_edges(
    lines_df: pd.DataFrame,
    min_confidence: float = 0.56,
    game: str = "cs2",
) -> pd.DataFrame:
    """
    For each PrizePicks line, look up the player in our DB and compute
    the model's predicted probability. Flag lines with edge.
    """
    from db.setup import init_db, get_session
    from sqlalchemy import text
    from models.props_model import PropsModel
    from features.rolling_stats import compute_player_rolling_stats, compute_team_rolling_stats
    from features.elo import EloSystem

    init_db()

    # Load recent player stats for rolling features
    with get_session() as session:
        rows = session.execute(text(f"""
            SELECT ps.player_id, ps.team_id, ps.map_result_id,
                   mr.map_name, m.match_date,
                   ps.kills, ps.deaths, ps.kast, ps.rating, ps.adr, ps.first_kills,
                   p.name as player_name
            FROM player_map_stats ps
            JOIN map_results mr ON ps.map_result_id=mr.id
            JOIN matches m ON mr.match_id=m.id
            JOIN players p ON ps.player_id=p.id
            WHERE m.game='{game}'
            ORDER BY m.match_date DESC
            LIMIT 50000
        """)).fetchall()
        player_df = pd.DataFrame(rows, columns=[
            "player_id","team_id","map_result_id","map_name","match_date",
            "kills","deaths","kast","rating","adr","first_kills","player_name"
        ])

        map_rows = session.execute(text(f"""
            SELECT mr.id, mr.match_id, mr.map_name, mr.team1_id, mr.team2_id,
                   mr.winner_id, m.match_date
            FROM map_results mr JOIN matches m ON mr.match_id=m.id
            WHERE m.game='{game}'
        """)).fetchall()
        map_df = pd.DataFrame(map_rows, columns=[
            "map_result_id","match_id","map_name","team1_id","team2_id","winner_id","match_date"
        ])

    player_df["match_date"] = pd.to_datetime(player_df["match_date"])
    map_df["match_date"] = pd.to_datetime(map_df["match_date"])

    # Build name -> player_id index (case-insensitive)
    name_index = player_df.groupby("player_name")["player_id"].first().to_dict()
    name_index_lower = {k.lower(): v for k, v in name_index.items()}

    elo = EloSystem()
    stat_cols = ["kills", "deaths", "kast", "rating", "adr", "first_kills"]

    edges = []
    for _, line in lines_df.iterrows():
        stat = line.get("model_stat")
        if not stat:
            continue

        model_path = Path(f"data/models_saved/{game}_props_{stat}.pkl")
        if not model_path.exists():
            continue

        model = PropsModel.load(model_path)

        # Find player in DB
        pname = str(line["player_name"]).lower().strip()
        player_id = name_index_lower.get(pname)
        if player_id is None:
            # Try partial match on last word (handle "TeamTag Player" format)
            parts = pname.split()
            for part in parts:
                if len(part) > 2:
                    matches = [pid for name, pid in name_index_lower.items() if part in name]
                    if len(matches) == 1:
                        player_id = matches[0]
                        break
        if player_id is None:
            logger.debug(f"Player not found in DB: {line['player_name']}")
            continue

        # Compute rolling features
        rolling = compute_player_rolling_stats(player_df, player_id, stat_cols)
        map_rolling = compute_player_rolling_stats(player_df, player_id, stat_cols)

        # Get most recent opponent (approximate — ideally from schedule)
        recent = player_df[player_df["player_id"] == player_id].sort_values("match_date")
        if recent.empty:
            continue

        last_team_id = int(recent.iloc[-1]["team_id"])
        last_map_row = map_df[map_df["map_result_id"] == int(recent.iloc[-1]["map_result_id"])]
        if last_map_row.empty:
            continue
        lmr = last_map_row.iloc[0]
        opp_id = int(lmr["team2_id"] if lmr["team1_id"] == last_team_id else lmr["team1_id"])

        opp_stats = compute_team_rolling_stats(map_df, opp_id)
        opp_elo = elo.get(opp_id)

        feats = build_player_prop_features(
            rolling, map_rolling, opp_stats, opp_elo,
            is_lan=False, best_of=3
        )
        feats["player_id"] = player_id

        try:
            pred = model.over_under_prob(feats, float(line["line"]))
        except Exception as e:
            logger.debug(f"Prediction error for {line['player_name']}: {e}")
            continue

        best_side = "OVER" if pred.over_prob > pred.under_prob else "UNDER"
        best_prob = max(pred.over_prob, pred.under_prob)

        edges.append({
            "player":       line["player_name"],
            "team":         line["team_name"],
            "league":       line["league"],
            "stat":         line["stat"],
            "line":         line["line"],
            "expected":     round(pred.expected_value, 2),
            "std":          round(pred.std_dev, 2),
            "over_prob":    round(pred.over_prob, 3),
            "under_prob":   round(pred.under_prob, 3),
            "best_side":    best_side,
            "confidence":   round(best_prob, 3),
            "edge_vs_50":   round(best_prob - 0.5, 3),
            "flag":         best_prob >= min_confidence,
        })

    result = pd.DataFrame(edges)
    if not result.empty:
        result = result.sort_values("confidence", ascending=False)
    return result


def build_player_prop_features(rolling, map_rolling, opp_stats, opp_elo, **kwargs):
    from models.props_model import build_player_prop_features as _build
    return _build(rolling, map_rolling, opp_stats, opp_elo, **kwargs)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--edge", action="store_true", help="Show model edge vs PrizePicks lines")
    parser.add_argument("--min-conf", type=float, default=0.56, help="Min confidence to flag (default 0.56)")
    parser.add_argument("--game", type=str, default="cs2", choices=["cs2","lol","valorant"])
    args = parser.parse_args()

    lines = get_esports_lines()
    if lines.empty:
        print("No esports lines found on PrizePicks right now.")
        sys.exit(0)

    print(f"\nLive PrizePicks Esports Lines ({len(lines)} props):")
    print(lines[["player_name","team_name","league","stat","line"]].to_string(index=False))

    if args.edge:
        print("\nComputing model edge...")
        edges = find_edges(lines, min_confidence=args.min_conf, game=args.game)
        if edges.empty:
            print("No players matched in DB or no models loaded.")
        else:
            flagged = edges[edges["flag"]]
            print(f"\nFlagged edges ({len(flagged)} of {len(edges)} lines >= {args.min_conf:.0%} confidence):")
            if not flagged.empty:
                print(flagged[[
                    "player","stat","line","expected","best_side","confidence","edge_vs_50"
                ]].to_string(index=False))
            else:
                print("No edges above threshold found today.")

            print(f"\nAll lines with model probabilities:")
            print(edges[[
                "player","stat","line","expected","over_prob","under_prob","best_side","confidence"
            ]].to_string(index=False))
