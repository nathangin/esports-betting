"""
League of Legends pro match data scraper.

Sources:
  1. Leaguepedia (MediaWiki API) — free, comprehensive LoL esports history
  2. Riot Esports API (lolesports.com) — official, requires API key

We use Leaguepedia as the primary source since it has deep historical data.
"""
import time
import re
from datetime import datetime, timedelta
from typing import Optional
from dataclasses import dataclass, field

import requests
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

from config import REQUEST_DELAY, REQUEST_TIMEOUT, MAX_RETRIES

LEAGUEPEDIA_API = "https://lol.fandom.com/api.php"
LOLESPORTS_API = "https://esports-api.lolesports.com/persisted/gw"

HEADERS = {
    "User-Agent": "esports-betting-model/1.0 (research)",
    "x-api-key": "0TvQnueqKa5mxJntVWt0w4LpLfEkrV1Ta8rQBb9Z",  # public LoL esports key
}


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass
class LoLPlayerStats:
    player_name: str
    team_name: str
    role: str
    champion: str
    kills: Optional[int] = None
    deaths: Optional[int] = None
    assists: Optional[int] = None
    cs_total: Optional[int] = None
    cs_per_min: Optional[float] = None
    damage_dealt: Optional[int] = None
    damage_share: Optional[float] = None
    gold_earned: Optional[int] = None
    gold_diff_15: Optional[int] = None
    xp_diff_15: Optional[int] = None
    vision_score: Optional[int] = None
    wards_placed: Optional[int] = None
    wards_cleared: Optional[int] = None
    double_kills: int = 0
    triple_kills: int = 0
    quadra_kills: int = 0
    penta_kills: int = 0

@dataclass
class LoLGameResult:
    game_number: int
    winner_name: str
    loser_name: str
    duration_seconds: Optional[int] = None
    patch: Optional[str] = None
    player_stats: list = field(default_factory=list)
    blue_side: Optional[str] = None
    red_side: Optional[str] = None
    blue_side_won: bool = True

@dataclass
class LoLMatchResult:
    external_id: str
    team1_name: str
    team2_name: str
    winner_name: Optional[str]
    match_date: datetime
    event_name: str
    tournament_stage: Optional[str]
    best_of: int
    team1_games_won: int
    team2_games_won: int
    games: list = field(default_factory=list)
    patch: Optional[str] = None


# ---------------------------------------------------------------------------
# Leaguepedia scraper
# ---------------------------------------------------------------------------

@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=2, max=10),
)
def _leaguepedia_query(params: dict) -> dict:
    time.sleep(REQUEST_DELAY * 0.5)
    params.setdefault("action", "cargoquery")
    params.setdefault("format", "json")
    resp = requests.get(LEAGUEPEDIA_API, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def scrape_lol_tournaments(
    year: int = 2024,
    leagues: Optional[list[str]] = None,
) -> list[dict]:
    """Fetch tournament list from Leaguepedia."""
    league_filter = ""
    if leagues:
        names = ",".join(f'"{l}"' for l in leagues)
        league_filter = f" AND Tournaments.League IN ({names})"

    params = {
        "tables": "Tournaments",
        "fields": "Tournaments.Name,Tournaments.League,Tournaments.DateStart,Tournaments.Date,Tournaments.Region",
        "where": f"YEAR(Tournaments.DateStart)={year}{league_filter}",
        "limit": "200",
        "offset": "0",
    }
    data = _leaguepedia_query(params)
    return [r["title"] for r in data.get("cargoquery", [])]


def scrape_lol_matches(
    tournament_name: Optional[str] = None,
    days_back: int = 180,
    limit: int = 500,
) -> list[LoLMatchResult]:
    """Fetch match results from Leaguepedia MatchSchedule + ScoreboardGames."""
    cutoff = datetime.utcnow() - timedelta(days=days_back)
    where = f"MS.DateTime_UTC >= '{cutoff.strftime('%Y-%m-%d')}'"
    if tournament_name:
        where += f" AND MS.OverviewPage = '{tournament_name}'"

    params = {
        "tables": "MatchSchedule=MS",
        "fields": (
            "MS.UniqueGame,MS.Team1,MS.Team2,MS.Winner,MS.DateTime_UTC,"
            "MS.BestOf,MS.OverviewPage,MS.Tab,MS.Team1Score,MS.Team2Score"
        ),
        "where": where,
        "order_by": "MS.DateTime_UTC DESC",
        "limit": str(limit),
    }
    data = _leaguepedia_query(params)
    matches = []

    for r in data.get("cargoquery", []):
        t = r["title"]
        try:
            match_date = datetime.strptime(t.get("DateTime UTC", ""), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            match_date = datetime.utcnow()

        if match_date < cutoff:
            continue

        t1_score = int(t.get("Team1Score") or 0)
        t2_score = int(t.get("Team2Score") or 0)
        winner = t.get("Winner", "")
        best_of = int(t.get("BestOf") or 3)

        match = LoLMatchResult(
            external_id=t.get("UniqueGame", ""),
            team1_name=t.get("Team1", ""),
            team2_name=t.get("Team2", ""),
            winner_name=winner or None,
            match_date=match_date,
            event_name=t.get("OverviewPage", ""),
            tournament_stage=t.get("Tab"),
            best_of=best_of,
            team1_games_won=t1_score,
            team2_games_won=t2_score,
        )
        matches.append(match)

    logger.info(f"Found {len(matches)} LoL matches from Leaguepedia")
    return matches


def scrape_lol_game_stats(unique_game: str) -> Optional[LoLGameResult]:
    """Fetch per-game player stats from Leaguepedia ScoreboardPlayers."""
    params = {
        "tables": "ScoreboardGames=SG,ScoreboardPlayers=SP",
        "join_on": "SG.GameId=SP.GameId",
        "fields": (
            "SG.WinTeam,SG.LossTeam,SG.GameId,SG.Gamelength,SG.Patch,"
            "SG.Blue,SG.Red,SG.BlueWin,"
            "SP.Name,SP.Team,SP.Role,SP.Champion,"
            "SP.Kills,SP.Deaths,SP.Assists,SP.CS,SP.CSM,"
            "SP.DamageToChampions,SP.Gold,SP.VisionScore,"
            "SP.WardsPlaced,SP.WardsKilled,"
            "SP.GDPM,SP.GD15,SP.XPD15,"
            "SP.DoubleKills,SP.TripleKills,SP.QuadraKills,SP.PentaKills"
        ),
        "where": f"SG.GameId='{unique_game}'",
        "limit": "15",
    }
    data = _leaguepedia_query(params)
    rows = data.get("cargoquery", [])
    if not rows:
        return None

    first = rows[0]["title"]
    game_len_str = first.get("Gamelength", "0:00")
    try:
        parts = game_len_str.split(":")
        duration_secs = int(parts[0]) * 60 + int(parts[1])
    except (ValueError, IndexError):
        duration_secs = None

    blue_won = first.get("BlueWin", "1") == "1"
    blue_side = first.get("Blue", "")
    red_side = first.get("Red", "")
    winner = first.get("WinTeam", "")
    loser = first.get("LossTeam", "")

    player_stats = []
    for r in rows:
        t = r["title"]
        total_kills = int(t.get("Kills") or 0)
        # Compute damage share after collecting all players on team
        player_stats.append(LoLPlayerStats(
            player_name=t.get("Name", ""),
            team_name=t.get("Team", ""),
            role=t.get("Role", "").lower(),
            champion=t.get("Champion", ""),
            kills=int(t.get("Kills") or 0),
            deaths=int(t.get("Deaths") or 0),
            assists=int(t.get("Assists") or 0),
            cs_total=int(t.get("CS") or 0),
            cs_per_min=float(t.get("CSM") or 0),
            damage_dealt=int(t.get("DamageToChampions") or 0),
            gold_earned=int(t.get("Gold") or 0),
            gold_diff_15=int(t.get("GD15") or 0),
            xp_diff_15=int(t.get("XPD15") or 0),
            vision_score=int(t.get("VisionScore") or 0),
            wards_placed=int(t.get("WardsPlaced") or 0),
            wards_cleared=int(t.get("WardsKilled") or 0),
            double_kills=int(t.get("DoubleKills") or 0),
            triple_kills=int(t.get("TripleKills") or 0),
            quadra_kills=int(t.get("QuadraKills") or 0),
            penta_kills=int(t.get("PentaKills") or 0),
        ))

    # Compute damage share per player
    team_damage: dict[str, int] = {}
    for ps in player_stats:
        team_damage[ps.team_name] = team_damage.get(ps.team_name, 0) + (ps.damage_dealt or 0)
    for ps in player_stats:
        total = team_damage.get(ps.team_name, 1) or 1
        ps.damage_share = (ps.damage_dealt or 0) / total

    return LoLGameResult(
        game_number=1,
        winner_name=winner,
        loser_name=loser,
        duration_seconds=duration_secs,
        patch=first.get("Patch"),
        player_stats=player_stats,
        blue_side=blue_side,
        red_side=red_side,
        blue_side_won=blue_won,
    )


def scrape_lol_matches_with_stats(
    days_back: int = 180,
    tournament_name: Optional[str] = None,
) -> list[LoLMatchResult]:
    """Fetch matches and enrich each with per-game player stats."""
    matches = scrape_lol_matches(tournament_name=tournament_name, days_back=days_back)
    for match in matches:
        if not match.external_id:
            continue
        game = scrape_lol_game_stats(match.external_id)
        if game:
            match.games.append(game)
            match.patch = game.patch
    return matches
