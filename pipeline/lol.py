"""
League of Legends pipeline.

Key differences vs CS2:
  - No map picks/bans — match = series of games on Summoner's Rift
  - Role matters enormously: ADC kills ≠ support kills
  - Side selection (blue/red) is a significant advantage (~53% blue winrate)
  - Patch version shifts meta — data older than 2-3 patches is less relevant
  - Gold/XP differentials at 15 min are strong early-game indicators

Data source: Leaguepedia MediaWiki API (free, no key needed)
"""
from datetime import datetime, timedelta
from typing import Optional
from pathlib import Path

import pandas as pd
import numpy as np
from loguru import logger

from config import GAME_CONFIGS, MODELS_DIR, MIN_MATCHES_FOR_PREDICTION, RECENCY_WINDOWS
from db.models import Game, Team, Player, Match, MapResult, PlayerMapStats, UpcomingMatch
from db.setup import get_session, init_db
from scrapers.lol import (
    scrape_lol_matches_with_stats, scrape_lol_tournaments,
    LoLMatchResult, LoLGameResult, LoLPlayerStats
)
from features.elo import EloSystem, pre_match_ratings_from_maps
from features.rolling_stats import (
    build_training_dataset, compute_player_rolling_stats,
    compute_team_rolling_stats, compute_h2h_stats,
    build_match_features
)
from models.win_model import WinModel
from models.props_model import PropsModel, build_player_prop_features

STAT_COLS = GAME_CONFIGS["lol"]["stat_cols"]
PROP_STATS = GAME_CONFIGS["lol"]["prop_lines"]
ROLES = GAME_CONFIGS["lol"]["roles"]

# Blue-side win bonus (Elo adjustment)
BLUE_SIDE_WIN_RATE = 0.528
BLUE_SIDE_LOGIT = np.log(BLUE_SIDE_WIN_RATE / (1 - BLUE_SIDE_WIN_RATE))


class LoLPipeline:
    def __init__(self, days_back: int = 365):
        self.days_back = days_back
        self.elo = EloSystem()
        self.win_model: Optional[WinModel] = None
        self.props_models: dict[str, dict[str, PropsModel]] = {}  # {role: {stat: model}}
        init_db()

    # ------------------------------------------------------------------
    # 1. Scrape & Store
    # ------------------------------------------------------------------

    def scrape_and_store(
        self,
        tournaments: Optional[list[str]] = None,
    ):
        """Fetch LoL matches from Leaguepedia and store to DB."""
        logger.info("Scraping LoL matches from Leaguepedia...")
        all_matches = []
        if tournaments:
            for t in tournaments:
                logger.info(f"Fetching tournament: {t}")
                all_matches.extend(
                    scrape_lol_matches_with_stats(
                        days_back=self.days_back, tournament_name=t
                    )
                )
        else:
            all_matches = scrape_lol_matches_with_stats(days_back=self.days_back)

        with get_session() as session:
            new_count = 0
            for match in all_matches:
                existing = session.query(Match).filter_by(
                    external_id=match.external_id, game=Game.lol
                ).first()
                if existing:
                    continue
                self._store_lol_match(session, match)
                new_count += 1
                if new_count % 20 == 0:
                    session.commit()
            session.commit()
        logger.info(f"Stored {new_count} new LoL matches")

    def _get_or_create_team(self, session, name: str) -> Team:
        t = session.query(Team).filter_by(game=Game.lol, name=name).first()
        if not t:
            t = Team(game=Game.lol, name=name)
            session.add(t)
            session.flush()
        return t

    def _get_or_create_player(self, session, name: str, team_id: int, role: str) -> Player:
        p = session.query(Player).filter_by(game=Game.lol, name=name).first()
        if not p:
            p = Player(game=Game.lol, name=name, team_id=team_id, role=role)
            session.add(p)
            session.flush()
        elif p.team_id != team_id:
            p.team_id = team_id
        return p

    def _store_lol_match(self, session, match: LoLMatchResult):
        t1 = self._get_or_create_team(session, match.team1_name)
        t2 = self._get_or_create_team(session, match.team2_name)
        winner = None
        if match.winner_name == match.team1_name:
            winner = t1
        elif match.winner_name == match.team2_name:
            winner = t2

        db_match = Match(
            game=Game.lol,
            external_id=match.external_id,
            team1_id=t1.id,
            team2_id=t2.id,
            winner_id=winner.id if winner else None,
            match_date=match.match_date,
            event_name=match.event_name,
            tournament_stage=match.tournament_stage,
            best_of=match.best_of,
            is_completed=True,
            team1_map_score=match.team1_games_won,
            team2_map_score=match.team2_games_won,
            patch_version=match.patch,
        )
        session.add(db_match)
        session.flush()

        for game_num, game in enumerate(match.games):
            game_t1 = t1 if game.blue_side == match.team1_name else t2
            game_t2 = t2 if game.blue_side == match.team1_name else t1
            game_winner = self._get_or_create_team(session, game.winner_name)
            game_loser = self._get_or_create_team(session, game.loser_name)

            mr = MapResult(
                match_id=db_match.id,
                map_name="summoners_rift",
                map_order=game_num,
                team1_id=game_t1.id,
                team2_id=game_t2.id,
                winner_id=game_winner.id,
                duration_minutes=game.duration_seconds // 60 if game.duration_seconds else None,
            )
            session.add(mr)
            session.flush()

            for ps in game.player_stats:
                player_team = self._get_or_create_team(session, ps.team_name)
                player = self._get_or_create_player(session, ps.player_name, player_team.id, ps.role)
                pms = PlayerMapStats(
                    map_result_id=mr.id,
                    player_id=player.id,
                    team_id=player_team.id,
                    is_winner=(player_team.id == game_winner.id),
                    kills=ps.kills,
                    deaths=ps.deaths,
                    assists=ps.assists,
                    role=ps.role,
                    champion=ps.champion,
                    cs_total=ps.cs_total,
                    cs_per_min=ps.cs_per_min,
                    damage_dealt_to_champions=ps.damage_dealt,
                    damage_share=ps.damage_share,
                    gold_earned=ps.gold_earned,
                    gold_diff_at_15=ps.gold_diff_15,
                    xp_diff_at_15=ps.xp_diff_15,
                    vision_score=ps.vision_score,
                    wards_placed=ps.wards_placed,
                    wards_cleared=ps.wards_cleared,
                    double_kills=ps.double_kills,
                    triple_kills=ps.triple_kills,
                    quadra_kills=ps.quadra_kills,
                    penta_kills=ps.penta_kills,
                )
                session.add(pms)

    # ------------------------------------------------------------------
    # 2. Load DataFrames
    # ------------------------------------------------------------------

    def load_dataframes(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        with get_session() as session:
            matches = session.query(Match).filter_by(game=Game.lol, is_completed=True).all()
            map_results = (
                session.query(MapResult)
                .join(Match, MapResult.match_id == Match.id)
                .filter(Match.game == Game.lol)
                .all()
            )
            player_stats = (
                session.query(PlayerMapStats)
                .join(MapResult)
                .join(Match, MapResult.match_id == Match.id)
                .filter(Match.game == Game.lol)
                .all()
            )

        matches_df = pd.DataFrame([{
            "match_id": m.id,
            "team1_id": m.team1_id,
            "team2_id": m.team2_id,
            "winner_id": m.winner_id,
            "match_date": m.match_date,
            "best_of": m.best_of,
            "is_lan": m.is_lan,
            "team1_map_score": m.team1_map_score or 0,
            "team2_map_score": m.team2_map_score or 0,
            "patch_version": m.patch_version,
        } for m in matches])

        map_df = pd.DataFrame([{
            "map_result_id": mr.id,
            "match_id": mr.match_id,
            "map_name": mr.map_name,
            "team1_id": mr.team1_id,
            "team2_id": mr.team2_id,
            "winner_id": mr.winner_id,
            "team1_rounds": 1,
            "team2_rounds": 0,
            "match_date": mr.match.match_date if mr.match else None,
            "duration_minutes": mr.duration_minutes,
        } for mr in map_results])

        player_df = pd.DataFrame([{
            "player_id": ps.player_id,
            "team_id": ps.team_id,
            "map_result_id": ps.map_result_id,
            "map_name": "summoners_rift",
            "match_date": ps.map_result.match.match_date if ps.map_result and ps.map_result.match else None,
            "role": ps.role,
            "champion": ps.champion,
            "kills": ps.kills,
            "deaths": ps.deaths,
            "assists": ps.assists,
            "cs_per_min": ps.cs_per_min,
            "damage_share": ps.damage_share,
            "gold_diff_15": ps.gold_diff_at_15,
            "vision_score": ps.vision_score,
        } for ps in player_stats])

        return matches_df, map_df, player_df

    # ------------------------------------------------------------------
    # 3-4. Build Elo & Train
    # ------------------------------------------------------------------

    def build_elo(self, matches_df: pd.DataFrame) -> EloSystem:
        self.elo = EloSystem()
        self.elo.build_from_matches(matches_df)
        return self.elo

    def train(self, tune: bool = False):
        matches_df, map_df, player_df = self.load_dataframes()
        if len(matches_df) < MIN_MATCHES_FOR_PREDICTION:
            logger.warning("Not enough LoL data to train")
            return

        self.build_elo(matches_df)

        # Win model — add blue-side feature to training data
        train_df = build_training_dataset(matches_df, map_df, self.elo, target="match_winner")
        # LoL-specific: patch recency weighting (last 2 patches = full weight)
        if "patch_version" in matches_df.columns:
            train_df = train_df.merge(
                matches_df[["match_id", "patch_version"]], on="match_id", how="left"
            )

        self.win_model = WinModel("lol_win")
        if tune:
            self.win_model.tune(train_df, n_trials=50)
        self.win_model.fit(train_df)
        self.win_model.walk_forward_eval(train_df)
        self.win_model.save()

        # Props models — train per-role to capture role stat distributions
        for role in ROLES:
            role_df = player_df[player_df["role"] == role]
            if len(role_df) < 50:
                continue
            self.props_models[role] = {}
            for stat in PROP_STATS:
                if stat not in role_df.columns:
                    continue
                pm = PropsModel(stat, game="lol")
                props_df = self._build_props_df(role_df, map_df, stat, role)
                if len(props_df.dropna(subset=[stat])) < 30:
                    continue
                if tune:
                    pm.tune(props_df, n_trials=30)
                pm.fit(props_df)
                pm.save(MODELS_DIR / f"lol_props_{role}_{stat}.pkl")
                self.props_models[role][stat] = pm
                logger.info(f"LoL props model trained: {role}/{stat}")

        logger.info("LoL training complete")

    def _build_props_df(
        self,
        player_df: pd.DataFrame,
        map_df: pd.DataFrame,
        stat: str,
        role: str,
    ) -> pd.DataFrame:
        rows = []
        # opponent Elo as it stood before each match (the final ratings would leak results)
        pre_elo = pre_match_ratings_from_maps(map_df)
        for _, row in player_df.sort_values("match_date").iterrows():
            as_of = pd.Timestamp(row["match_date"])
            pid = row["player_id"]

            rolling = compute_player_rolling_stats(player_df, pid, STAT_COLS, as_of_date=as_of)
            map_rolling = compute_player_rolling_stats(
                player_df, pid, STAT_COLS, as_of_date=as_of, specific_map="summoners_rift"
            )
            map_row = map_df[map_df["map_result_id"] == row["map_result_id"]]
            if map_row.empty:
                continue
            opp_id = (
                map_row.iloc[0]["team2_id"]
                if map_row.iloc[0]["team1_id"] == row["team_id"]
                else map_row.iloc[0]["team1_id"]
            )
            opp_stats = compute_team_rolling_stats(map_df, opp_id, as_of_date=as_of)
            opp_elo = pre_elo.get(row["map_result_id"], {}).get(opp_id, 1500.0)

            feats = build_player_prop_features(
                rolling, map_rolling, opp_stats, opp_elo,
                is_lan=False, best_of=1, player_role=role
            )
            feats["player_id"] = pid
            feats["match_date"] = row["match_date"]
            feats[stat] = row.get(stat)
            rows.append(feats)

        return pd.DataFrame(rows)

    # ------------------------------------------------------------------
    # 5. Predict
    # ------------------------------------------------------------------

    def predict_match(
        self,
        team1_id: int,
        team2_id: int,
        scheduled_at: Optional[datetime] = None,
        blue_side_team: Optional[int] = None,
        best_of: int = 3,
    ) -> dict:
        _, map_df, _ = self.load_dataframes()
        feats = build_match_features(
            map_df, team1_id, team2_id,
            pd.Timestamp(scheduled_at or datetime.utcnow()),
            elo_system=self.elo,
        )
        feats["is_lan"] = 1
        feats["best_of"] = best_of

        # Blue side advantage
        if blue_side_team == team1_id:
            feats["blue_side_t1"] = 1
        elif blue_side_team == team2_id:
            feats["blue_side_t1"] = 0
        else:
            feats["blue_side_t1"] = 0.5  # unknown

        p = self.win_model.predict_single(feats) if self.win_model else 0.5
        return {
            "team1_win_prob": round(p, 4),
            "team2_win_prob": round(1 - p, 4),
            "features": feats,
        }

    def predict_player_props(
        self,
        player_id: int,
        role: str,
        opponent_team_id: int,
        is_lan: bool = True,
        best_of: int = 3,
    ) -> dict:
        _, map_df, player_df = self.load_dataframes()
        rolling = compute_player_rolling_stats(player_df, player_id, STAT_COLS)
        map_rolling = compute_player_rolling_stats(
            player_df, player_id, STAT_COLS, specific_map="summoners_rift"
        )
        opp_stats = compute_team_rolling_stats(map_df, opponent_team_id)
        opp_elo = self.elo.get(opponent_team_id)

        feats = build_player_prop_features(
            rolling, map_rolling, opp_stats, opp_elo, is_lan, best_of, player_role=role
        )
        feats["player_id"] = player_id

        results = {}
        role_models = self.props_models.get(role, {})
        for stat, model in role_models.items():
            expected, std = model.predict_expected(feats)
            results[stat] = {"expected": round(expected, 2), "std": round(std, 2)}

        return results

    def run(self, scrape: bool = True, tune: bool = False):
        if scrape:
            self.scrape_and_store()
        self.train(tune=tune)
        logger.info("LoL pipeline complete")
