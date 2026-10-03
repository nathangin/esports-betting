"""
Valorant pipeline.

Key differences vs CS2:
  - ACS (Average Combat Score) is the primary player performance metric
  - Agent matters (duelists get more kills; controllers/sentinels fewer)
  - Max 25 rounds per half (not 16) with 2-round OT
  - Attack-first vs defense-first choice at round 1
  - Map pool rotates seasonally (act patches)

Data source: VLR.gg
"""
from datetime import datetime, timedelta
from typing import Optional
from pathlib import Path

import pandas as pd
from loguru import logger

from config import GAME_CONFIGS, MODELS_DIR, MIN_MATCHES_FOR_PREDICTION
from db.models import Game, Team, Player, Match, MapResult, PlayerMapStats, UpcomingMatch
from db.setup import get_session, init_db
from scrapers.vlr import (
    scrape_vlr_all_results, scrape_vlr_match, scrape_vlr_upcoming,
    VlrMatch, VlrMapResult, VlrPlayerStats
)
from features.elo import EloSystem, pre_match_ratings_from_maps
from features.rolling_stats import (
    build_training_dataset, compute_player_rolling_stats,
    compute_team_rolling_stats, build_match_features
)
from models.win_model import WinModel
from models.props_model import PropsModel, build_player_prop_features

STAT_COLS = GAME_CONFIGS["valorant"]["stat_cols"]
PROP_STATS = GAME_CONFIGS["valorant"]["prop_lines"]

# Agent role classification (determines expected stat profile)
AGENT_ROLES = {
    # Duelists — high kill output
    "jett": "duelist", "reyna": "duelist", "neon": "duelist",
    "yoru": "duelist", "iso": "duelist", "phoenix": "duelist",
    # Initiators — mid-range kills + support
    "sova": "initiator", "breach": "initiator", "fade": "initiator",
    "kayo": "initiator", "skye": "initiator", "gekko": "initiator",
    # Controllers — lower kills, more utility
    "brimstone": "controller", "omen": "controller", "viper": "controller",
    "astra": "controller", "harbor": "controller", "clove": "controller",
    # Sentinels — lowest kills typically
    "killjoy": "sentinel", "cypher": "sentinel", "sage": "sentinel",
    "chamber": "sentinel", "deadlock": "sentinel",
}


class ValorantPipeline:
    def __init__(self, days_back: int = 365):
        self.days_back = days_back
        self.elo = EloSystem()
        self.win_model: Optional[WinModel] = None
        self.props_models: dict[str, PropsModel] = {}  # {stat: model}
        init_db()

    # ------------------------------------------------------------------
    # 1. Scrape & Store
    # ------------------------------------------------------------------

    def scrape_and_store(self, max_pages: int = 15):
        logger.info("Scraping VLR.gg results...")
        raw_results = scrape_vlr_all_results(max_pages=max_pages, days_back=self.days_back)
        logger.info(f"Found {len(raw_results)} matches on VLR results pages")

        with get_session() as session:
            new_count = 0
            for r in raw_results:
                existing = session.query(Match).filter_by(
                    external_id=str(r["vlr_id"]), game=Game.valorant
                ).first()
                if existing:
                    continue

                scraped = scrape_vlr_match(r["vlr_id"])
                if scraped is None:
                    continue

                self._store_match(session, scraped)
                new_count += 1
                if new_count % 10 == 0:
                    session.commit()
                    logger.info(f"Stored {new_count} Valorant matches...")

            session.commit()
        logger.info(f"Valorant scrape complete — {new_count} new matches stored")

    def scrape_upcoming(self):
        upcoming_raw = scrape_vlr_upcoming()
        with get_session() as session:
            for u in upcoming_raw:
                existing = session.query(UpcomingMatch).filter_by(
                    external_id=str(u["vlr_id"])
                ).first()
                if existing:
                    continue
                t1 = self._get_or_create_team(session, u["team1"])
                t2 = self._get_or_create_team(session, u["team2"])
                um = UpcomingMatch(
                    game=Game.valorant,
                    external_id=str(u["vlr_id"]),
                    team1_id=t1.id,
                    team2_id=t2.id,
                    scheduled_at=u.get("scheduled_at"),
                    event_name=u.get("event"),
                    best_of=3,
                )
                session.add(um)

    def _get_or_create_team(self, session, name: str) -> Team:
        t = session.query(Team).filter_by(game=Game.valorant, name=name).first()
        if not t:
            t = Team(game=Game.valorant, name=name)
            session.add(t)
            session.flush()
        return t

    def _get_or_create_player(self, session, name: str, team_id: int) -> Player:
        p = session.query(Player).filter_by(game=Game.valorant, name=name).first()
        if not p:
            p = Player(game=Game.valorant, name=name, team_id=team_id)
            session.add(p)
            session.flush()
        elif p.team_id != team_id:
            p.team_id = team_id
        return p

    def _store_match(self, session, scraped: VlrMatch):
        t1 = self._get_or_create_team(session, scraped.team1_name)
        t2 = self._get_or_create_team(session, scraped.team2_name)
        winner = None
        if scraped.winner_name == scraped.team1_name:
            winner = t1
        elif scraped.winner_name == scraped.team2_name:
            winner = t2

        match = Match(
            game=Game.valorant,
            external_id=str(scraped.vlr_id),
            team1_id=t1.id,
            team2_id=t2.id,
            winner_id=winner.id if winner else None,
            match_date=scraped.match_date,
            event_name=scraped.event_name,
            tournament_stage=scraped.tournament_stage,
            best_of=scraped.best_of,
            is_lan=scraped.is_lan,
            is_completed=True,
            team1_map_score=scraped.team1_map_score,
            team2_map_score=scraped.team2_map_score,
        )
        session.add(match)
        session.flush()

        for sm in scraped.maps:
            map_t1 = t1 if sm.team1_name == scraped.team1_name else t2
            map_t2 = t2 if sm.team2_name == scraped.team2_name else t1
            map_winner = map_t1 if sm.winner_name == sm.team1_name else map_t2

            mr = MapResult(
                match_id=match.id,
                map_name=sm.map_name,
                map_order=sm.map_order,
                team1_id=map_t1.id,
                team2_id=map_t2.id,
                winner_id=map_winner.id,
                team1_rounds=sm.team1_rounds,
                team2_rounds=sm.team2_rounds,
                team1_first_half_rounds=sm.team1_first_half,
                team2_first_half_rounds=sm.team2_first_half,
                team1_second_half_rounds=sm.team1_second_half,
                team2_second_half_rounds=sm.team2_second_half,
                went_to_ot=sm.went_to_ot,
                team1_ot_rounds=sm.team1_ot,
                team2_ot_rounds=sm.team2_ot,
            )
            session.add(mr)
            session.flush()

            for ps in sm.player_stats:
                player_team = map_t1 if ps.team_name == sm.team1_name else map_t2
                player = self._get_or_create_player(session, ps.player_name, player_team.id)
                agent_role = AGENT_ROLES.get(ps.agent.lower(), "unknown") if ps.agent else None
                pms = PlayerMapStats(
                    map_result_id=mr.id,
                    player_id=player.id,
                    team_id=player_team.id,
                    is_winner=(player_team.id == map_winner.id),
                    kills=ps.kills,
                    deaths=ps.deaths,
                    assists=ps.assists,
                    acs=ps.acs,
                    kast=ps.kast,
                    adr=ps.adr,
                    hs_pct=ps.hs_pct,
                    first_kills=ps.first_kills,
                    first_deaths=ps.first_deaths,
                    agent=ps.agent,
                    role=agent_role,
                )
                session.add(pms)

    # ------------------------------------------------------------------
    # 2. Load DataFrames
    # ------------------------------------------------------------------

    def load_dataframes(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        with get_session() as session:
            matches = session.query(Match).filter_by(game=Game.valorant, is_completed=True).all()
            map_results = (
                session.query(MapResult)
                .join(Match, MapResult.match_id == Match.id)
                .filter(Match.game == Game.valorant)
                .all()
            )
            player_stats = (
                session.query(PlayerMapStats)
                .join(MapResult)
                .join(Match, MapResult.match_id == Match.id)
                .filter(Match.game == Game.valorant)
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
        } for m in matches])

        map_df = pd.DataFrame([{
            "map_result_id": mr.id,
            "match_id": mr.match_id,
            "map_name": mr.map_name,
            "team1_id": mr.team1_id,
            "team2_id": mr.team2_id,
            "winner_id": mr.winner_id,
            "team1_rounds": mr.team1_rounds or 0,
            "team2_rounds": mr.team2_rounds or 0,
            "match_date": mr.match.match_date if mr.match else None,
        } for mr in map_results])

        player_df = pd.DataFrame([{
            "player_id": ps.player_id,
            "team_id": ps.team_id,
            "map_result_id": ps.map_result_id,
            "map_name": ps.map_result.map_name if ps.map_result else None,
            "match_date": ps.map_result.match.match_date if ps.map_result and ps.map_result.match else None,
            "agent": ps.agent,
            "agent_role": ps.role,
            "kills": ps.kills,
            "deaths": ps.deaths,
            "assists": ps.assists,
            "acs": ps.acs,
            "hs_pct": ps.hs_pct,
            "kast": ps.kast,
            "adr": ps.adr,
            "first_kills": ps.first_kills,
            "first_deaths": ps.first_deaths,
        } for ps in player_stats])

        return matches_df, map_df, player_df

    # ------------------------------------------------------------------
    # 3-4. Build Elo & Train
    # ------------------------------------------------------------------

    def build_elo(self, matches_df: pd.DataFrame, map_df: pd.DataFrame) -> EloSystem:
        map_grouped = map_df.groupby("match_id").apply(
            lambda g: [
                {"map_name": row["map_name"], "winner_id": row["winner_id"],
                 "loser_id": row["team2_id"] if row["winner_id"] == row["team1_id"] else row["team1_id"]}
                for _, row in g.iterrows()
            ]
        ).reset_index(name="map_results")
        enriched = matches_df.merge(map_grouped, on="match_id", how="left")
        self.elo = EloSystem()
        self.elo.build_from_matches(enriched)
        return self.elo

    def train(self, tune: bool = False):
        matches_df, map_df, player_df = self.load_dataframes()
        if len(matches_df) < MIN_MATCHES_FOR_PREDICTION:
            logger.warning("Not enough Valorant data to train")
            return

        self.build_elo(matches_df, map_df)

        train_df = build_training_dataset(matches_df, map_df, self.elo, target="match_winner")
        self.win_model = WinModel("valorant_win")
        if tune:
            self.win_model.tune(train_df)
        self.win_model.fit(train_df)
        self.win_model.walk_forward_eval(train_df)
        self.win_model.save()

        # Props models — split by agent role to capture different kill distributions
        for stat in PROP_STATS:
            if stat not in player_df.columns:
                continue
            for agent_role in ["duelist", "initiator", "controller", "sentinel"]:
                role_df = player_df[player_df["agent_role"] == agent_role]
                if len(role_df.dropna(subset=[stat])) < 30:
                    continue
                pm = PropsModel(f"{stat}_{agent_role}", game="valorant")
                props_df = self._build_props_df(role_df, map_df, stat)
                if tune:
                    pm.tune(props_df, n_trials=30)
                pm.fit(props_df)
                pm.save(MODELS_DIR / f"valorant_props_{agent_role}_{stat}.pkl")
                self.props_models[f"{agent_role}_{stat}"] = pm

        logger.info("Valorant training complete")

    def _build_props_df(
        self, player_df: pd.DataFrame, map_df: pd.DataFrame, stat: str
    ) -> pd.DataFrame:
        rows = []
        # opponent Elo as it stood before each match (the final ratings would leak results)
        pre_elo = pre_match_ratings_from_maps(map_df)
        for _, row in player_df.sort_values("match_date").iterrows():
            as_of = pd.Timestamp(row["match_date"])
            pid = row["player_id"]

            rolling = compute_player_rolling_stats(player_df, pid, STAT_COLS, as_of_date=as_of)
            map_rolling = compute_player_rolling_stats(
                player_df, pid, STAT_COLS, as_of_date=as_of,
                specific_map=row.get("map_name"),
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
                is_lan=False, best_of=1, map_name=row.get("map_name"),
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
        best_of: int = 3,
        is_lan: bool = True,
        target_map: Optional[str] = None,
    ) -> dict:
        _, map_df, _ = self.load_dataframes()
        feats = build_match_features(
            map_df, team1_id, team2_id,
            pd.Timestamp(scheduled_at or datetime.utcnow()),
            elo_system=self.elo,
            target_map=target_map,
        )
        feats["is_lan"] = int(is_lan)
        feats["best_of"] = best_of

        p = self.win_model.predict_single(feats) if self.win_model else 0.5
        return {
            "team1_win_prob": round(p, 4),
            "team2_win_prob": round(1 - p, 4),
            "features": feats,
        }

    def predict_player_props(
        self,
        player_id: int,
        agent: str,
        opponent_team_id: int,
        map_name: Optional[str] = None,
        is_lan: bool = True,
        best_of: int = 3,
    ) -> dict:
        _, map_df, player_df = self.load_dataframes()
        agent_role = AGENT_ROLES.get(agent.lower(), "unknown")

        rolling = compute_player_rolling_stats(player_df, player_id, STAT_COLS)
        map_rolling = compute_player_rolling_stats(
            player_df, player_id, STAT_COLS, specific_map=map_name
        )
        opp_stats = compute_team_rolling_stats(map_df, opponent_team_id)
        opp_elo = self.elo.get(opponent_team_id)

        feats = build_player_prop_features(
            rolling, map_rolling, opp_stats, opp_elo, is_lan, best_of, map_name=map_name
        )
        feats["player_id"] = player_id

        results = {}
        for stat in PROP_STATS:
            model_key = f"{agent_role}_{stat}"
            model = self.props_models.get(model_key)
            if model:
                expected, std = model.predict_expected(feats)
                results[stat] = {"expected": round(expected, 2), "std": round(std, 2)}

        return results

    def run(self, scrape: bool = True, tune: bool = False, max_pages: int = 15):
        if scrape:
            self.scrape_and_store(max_pages=max_pages)
            self.scrape_upcoming()
        self.train(tune=tune)
        logger.info("Valorant pipeline complete")
