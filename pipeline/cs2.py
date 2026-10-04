"""
CS2 end-to-end pipeline.

Steps:
  1. scrape()       — pull match history + upcoming matches from HLTV
  2. store()        — persist raw data to SQLite
  3. build_features()— Elo, rolling stats, feature matrix
  4. train()        — fit WinModel + PropsModel (kills, deaths, hs_pct)
  5. predict()      — generate predictions for upcoming matches
  6. edge_report()  — compare to book lines and return flagged edges

Usage:
  from pipeline.cs2 import CS2Pipeline
  pipe = CS2Pipeline()
  pipe.run()                     # full run
  pipe.predict_and_edge(lines)   # just prediction + edge given book lines
"""
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd
from loguru import logger
from sqlalchemy.orm import Session

from config import (
    GAME_CONFIGS, RECENCY_WINDOWS, MODELS_DIR,
    MIN_MATCHES_FOR_PREDICTION, RANDOM_STATE
)
from db.models import (
    Game, Team, Player, Match, MapResult, PlayerMapStats,
    EloRating, UpcomingMatch, Prediction
)
from db.setup import get_session, init_db
from scrapers.hltv import (
    scrape_results, scrape_match, scrape_upcoming_matches,
    ScrapedMatch, ScrapedMapResult
)
from features.elo import EloSystem, pre_match_ratings_from_maps
from features.rolling_stats import (
    build_match_features,
    build_training_dataset,
    compute_player_rolling_stats,
    compute_team_rolling_stats,
    pre_match_team_win_rates,
)
from models.win_model import WinModel
from models.props_model import PropsModel, build_player_prop_features
from betting.edge import BettingLine, SlateAnalyzer


STAT_COLS = GAME_CONFIGS["cs2"]["stat_cols"]
PROP_STATS = GAME_CONFIGS["cs2"]["prop_lines"]


class CS2Pipeline:
    def __init__(self, days_back: int = 365):
        self.days_back = days_back
        self.elo = EloSystem()
        self.win_model: Optional[WinModel] = None
        self.props_models: dict[str, PropsModel] = {}
        init_db()

    # ------------------------------------------------------------------
    # 1. Scrape & Store
    # ------------------------------------------------------------------

    def scrape_and_store(self, max_pages: int = 20):
        """Scrape HLTV results and store to database."""
        logger.info("Scraping HLTV results...")
        results = scrape_results(max_pages=max_pages, days_back=self.days_back)
        logger.info(f"Found {len(results)} matches on results pages")

        # Track failed IDs in-memory so we don't retry them this run
        failed_ids: set[int] = set()
        new_count = 0
        skip_count = 0

        for r in results:
            hltv_id = r["hltv_id"]
            if hltv_id in failed_ids:
                continue

            with get_session() as session:
                existing = session.query(Match).filter_by(
                    external_id=str(hltv_id), game=Game.cs2
                ).first()
                if existing:
                    skip_count += 1
                    continue

            try:
                # Must pass full URL with slug to avoid 404
                scraped = scrape_match(hltv_id, url=r.get("url"))
                if scraped is None:
                    failed_ids.add(hltv_id)
                    continue
            except Exception as e:
                logger.warning(f"Skipping match {hltv_id} after error: {e}")
                failed_ids.add(hltv_id)
                continue

            try:
                with get_session() as session:
                    self._store_match(session, scraped, star_rating=r.get("star_rating", 0))
                new_count += 1
                if new_count % 10 == 0:
                    logger.info(f"Stored {new_count} new matches... ({skip_count} skipped, {len(failed_ids)} failed)")
            except Exception as e:
                logger.warning(f"Failed to store match {hltv_id}: {e}")
                failed_ids.add(hltv_id)

        logger.info(f"Scrape complete — {new_count} stored, {skip_count} already existed, {len(failed_ids)} failed")

    def scrape_upcoming(self):
        logger.info("Scraping upcoming matches...")
        upcoming_raw = scrape_upcoming_matches()
        with get_session() as session:
            for u in upcoming_raw:
                existing = session.query(UpcomingMatch).filter_by(
                    external_id=str(u["hltv_id"])
                ).first()
                if existing:
                    continue
                t1 = self._get_or_create_team(session, u["team1"])
                t2 = self._get_or_create_team(session, u["team2"])
                um = UpcomingMatch(
                    game=Game.cs2,
                    external_id=str(u["hltv_id"]),
                    team1_id=t1.id,
                    team2_id=t2.id,
                    scheduled_at=u.get("scheduled_at"),
                    event_name=u.get("event"),
                    best_of=u.get("best_of", 3),
                )
                session.add(um)
        logger.info(f"Stored {len(upcoming_raw)} upcoming matches")

    def _get_or_create_team(self, session: Session, name: str, hltv_id: Optional[int] = None) -> Team:
        query = session.query(Team).filter_by(game=Game.cs2, name=name)
        team = query.first()
        if not team:
            team = Team(game=Game.cs2, name=name, hltv_id=hltv_id)
            session.add(team)
            session.flush()
        return team

    def _get_or_create_player(
        self, session: Session, name: str, team_id: int, hltv_id: Optional[int] = None
    ) -> Player:
        query = session.query(Player).filter_by(game=Game.cs2, name=name)
        player = query.first()
        if not player:
            player = Player(
                game=Game.cs2, name=name, team_id=team_id, hltv_id=hltv_id
            )
            session.add(player)
            session.flush()
        elif player.team_id != team_id:
            player.team_id = team_id  # roster move
        return player

    def _store_match(self, session: Session, scraped: ScrapedMatch, star_rating: int = 0):
        t1 = self._get_or_create_team(session, scraped.team1_name)
        t2 = self._get_or_create_team(session, scraped.team2_name)
        winner = None
        if scraped.winner_name:
            winner = t1 if scraped.winner_name == scraped.team1_name else t2

        match = Match(
            game=Game.cs2,
            external_id=str(scraped.hltv_id),
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
            star_rating=star_rating,
        )
        session.add(match)
        session.flush()

        for sm in scraped.maps:
            map_t1 = t1 if sm.team1_name == scraped.team1_name else t2
            map_t2 = t2 if sm.team2_name == scraped.team2_name else t1
            map_winner = (
                map_t1 if sm.winner_name == sm.team1_name else map_t2
            )
            mr = MapResult(
                match_id=match.id,
                map_name=sm.map_name,
                map_order=sm.map_order,
                team1_id=map_t1.id,
                team2_id=map_t2.id,
                winner_id=map_winner.id,
                team1_rounds=sm.team1_rounds,
                team2_rounds=sm.team2_rounds,
                team1_first_half_side="CT" if sm.team1_ct_first else "T",
                team1_first_half_rounds=sm.team1_first_half,
                team2_first_half_rounds=sm.team2_first_half,
                team1_second_half_rounds=sm.team1_second_half,
                team2_second_half_rounds=sm.team2_second_half,
                went_to_ot=sm.went_to_ot,
                team1_ot_rounds=sm.team1_ot,
                team2_ot_rounds=sm.team2_ot,
                is_decider=sm.is_decider,
            )
            session.add(mr)
            session.flush()

            for ps in sm.player_stats:
                player_team = map_t1 if ps.team_name == sm.team1_name else map_t2
                player = self._get_or_create_player(
                    session, ps.player_name, player_team.id, ps.player_hltv_id
                )
                pms = PlayerMapStats(
                    map_result_id=mr.id,
                    player_id=player.id,
                    team_id=player_team.id,
                    is_winner=(player_team.id == map_winner.id),
                    kills=ps.kills,
                    deaths=ps.deaths,
                    assists=ps.assists,
                    hs_count=ps.hs_count,
                    hs_pct=ps.hs_pct,
                    kast=ps.kast,
                    rating=ps.rating,
                    adr=ps.adr,
                    first_kills=ps.first_kills,
                )
                session.add(pms)

    # ------------------------------------------------------------------
    # 2. Load data into DataFrames
    # ------------------------------------------------------------------

    def load_dataframes(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Returns (matches_df, map_results_df, player_stats_df)."""
        from sqlalchemy import text
        with get_session() as session:
            # Matches
            rows = session.execute(text("""
                SELECT id, team1_id, team2_id, winner_id, match_date,
                       best_of, is_lan, team1_map_score, team2_map_score,
                       COALESCE(star_rating, 0) as star_rating
                FROM matches
                WHERE game = 'cs2' AND is_completed = 1
            """)).fetchall()
            matches_df = pd.DataFrame(rows, columns=[
                "match_id", "team1_id", "team2_id", "winner_id", "match_date",
                "best_of", "is_lan", "team1_map_score", "team2_map_score", "star_rating",
            ])
            matches_df["team1_map_score"] = matches_df["team1_map_score"].fillna(0).astype(int)
            matches_df["team2_map_score"] = matches_df["team2_map_score"].fillna(0).astype(int)

            # Map results — join match_date from matches table
            rows = session.execute(text("""
                SELECT mr.id, mr.match_id, mr.map_name,
                       mr.team1_id, mr.team2_id, mr.winner_id,
                       COALESCE(mr.team1_rounds, 0), COALESCE(mr.team2_rounds, 0),
                       m.match_date
                FROM map_results mr
                JOIN matches m ON mr.match_id = m.id
                WHERE m.game = 'cs2'
            """)).fetchall()
            map_df = pd.DataFrame(rows, columns=[
                "map_result_id", "match_id", "map_name",
                "team1_id", "team2_id", "winner_id",
                "team1_rounds", "team2_rounds", "match_date",
            ])

            # Player stats — join map_name and match_date via joins
            rows = session.execute(text("""
                SELECT ps.player_id, ps.team_id, ps.map_result_id,
                       mr.map_name, m.match_date,
                       ps.kills, ps.deaths, ps.assists,
                       ps.hs_pct, ps.kast, ps.rating, ps.adr, ps.first_kills
                FROM player_map_stats ps
                JOIN map_results mr ON ps.map_result_id = mr.id
                JOIN matches m ON mr.match_id = m.id
                WHERE m.game = 'cs2'
            """)).fetchall()
            player_df = pd.DataFrame(rows, columns=[
                "player_id", "team_id", "map_result_id",
                "map_name", "match_date",
                "kills", "deaths", "assists",
                "hs_pct", "kast", "rating", "adr", "first_kills",
            ])

        matches_df["match_date"] = pd.to_datetime(matches_df["match_date"])
        map_df["match_date"] = pd.to_datetime(map_df["match_date"])
        player_df["match_date"] = pd.to_datetime(player_df["match_date"])

        logger.info(
            f"Loaded {len(matches_df)} matches, {len(map_df)} maps, "
            f"{len(player_df)} player-map rows"
        )
        return matches_df, map_df, player_df

    # ------------------------------------------------------------------
    # 3. Build Elo
    # ------------------------------------------------------------------

    def build_elo(self, matches_df: pd.DataFrame, map_df: pd.DataFrame) -> EloSystem:
        """Build Elo ratings from historical data."""
        # Attach map_results list to each match for per-map Elo
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

    # ------------------------------------------------------------------
    # 4. Train
    # ------------------------------------------------------------------

    def train(
        self,
        tune: bool = False,
        n_tune_trials: int = 50,
    ):
        matches_df, map_df, player_df = self.load_dataframes()
        if len(matches_df) < MIN_MATCHES_FOR_PREDICTION:
            logger.warning(f"Not enough data to train ({len(matches_df)} matches)")
            return

        self.build_elo(matches_df, map_df)

        # Win model
        logger.info("Building training dataset for win model...")
        train_df = build_training_dataset(matches_df, map_df, self.elo, target="match_winner")

        self.win_model = WinModel("cs2_win")
        if tune:
            self.win_model.tune(train_df, n_trials=n_tune_trials)
        self.win_model.fit(train_df)
        eval_metrics = self.win_model.walk_forward_eval(train_df)
        logger.info(f"Win model walk-forward: {eval_metrics}")
        self.win_model.save()

        # Props models
        for stat in PROP_STATS:
            if stat not in player_df.columns:
                continue
            logger.info(f"Training props model: {stat}")
            props_df = self._build_props_training_df(player_df, map_df, stat)
            if len(props_df.dropna(subset=[stat])) < 50:
                logger.warning(f"Skipping {stat}: not enough data")
                continue
            pm = PropsModel(stat, game="cs2")
            if tune:
                pm.tune(props_df, n_trials=40)
            pm.fit(props_df)
            pm.walk_forward_eval(props_df)
            pm.save()
            self.props_models[stat] = pm

        logger.info("CS2 training complete")

    def _build_props_training_df(
        self,
        player_df: pd.DataFrame,
        map_df: pd.DataFrame,
        stat: str,
    ) -> pd.DataFrame:
        """
        Vectorized props feature builder — O(n) via pandas groupby+rolling.
        Shift(1) on every stat ensures no lookahead (uses only past matches).
        """
        from config import RECENCY_WINDOWS, RECENCY_DECAY

        df = player_df.sort_values(["player_id", "match_date"]).copy()

        # Pre-compute opponent ids — rename before merge to avoid any suffix ambiguity
        map_opp = map_df[["map_result_id", "team1_id", "team2_id"]].copy()
        map_opp = map_opp.rename(columns={"team1_id": "map_t1", "team2_id": "map_t2"})
        df = df.merge(map_opp, on="map_result_id", how="left")
        df["opp_id"] = df.apply(
            lambda r: r["map_t2"] if r["team_id"] == r["map_t1"] else r["map_t1"],
            axis=1,
        )

        result = df[["player_id", "team_id", "map_result_id", "map_name",
                     "match_date", "opp_id", stat]].copy()

        # Vectorized rolling per player — shift(1) = no current-row lookahead
        grp = df.groupby("player_id")
        for col in STAT_COLS:
            if col not in df.columns:
                continue
            shifted = grp[col].shift(1)          # exclude current row
            # Exponentially-weighted mean
            result[f"ew_{col}"] = (
                grp[col]
                .transform(lambda s: s.shift(1).ewm(span=10, min_periods=1).mean())
            )
            # Fixed windows
            for w in RECENCY_WINDOWS:
                result[f"{col}_last{w}"] = (
                    grp[col].transform(lambda s: s.shift(1).rolling(w, min_periods=1).mean())
                )
            # Momentum: last5 vs last20
            l5  = result.get(f"{col}_last5")
            l20 = result.get(f"{col}_last20")
            if l5 is not None and l20 is not None:
                result[f"{col}_trend"] = (l5 - l20) / (l20.abs().replace(0, 1))

        # Opponent strength as it stood before each match. (This used to read the opponent's
        # final Elo and full-period win rate, i.e. results from after the row being predicted.)
        pre_elo = pre_match_ratings_from_maps(map_df)
        pre_wr = pre_match_team_win_rates(map_df)
        result["opp_elo"] = [
            pre_elo.get(mr, {}).get(oid, 1500.0) if pd.notna(oid) else 1500.0
            for mr, oid in zip(result["map_result_id"], result["opp_id"])
        ]
        result["opp_ew_win_rate"] = [
            pre_wr.get(mr, {}).get(oid, 0.5) if pd.notna(oid) else 0.5
            for mr, oid in zip(result["map_result_id"], result["opp_id"])
        ]

        from models.props_model import MAP_SIDE_BIAS
        result["map_ct_sided"] = result["map_name"].map(
            lambda m: MAP_SIDE_BIAS.get(str(m).lower(), 0) if pd.notna(m) else 0
        )
        result["is_lan"] = 0
        result["best_of"] = 1
        result["is_awper"] = result["is_entry"] = result["is_igl"] = 0

        logger.info(f"Props training df for [{stat}]: {len(result)} rows")
        return result

    # ------------------------------------------------------------------
    # 5. Predict upcoming matches
    # ------------------------------------------------------------------

    def predict_upcoming(self) -> list[dict]:
        if self.win_model is None:
            logger.warning("No win model loaded — call train() first")
            return []

        matches_df, map_df, _ = self.load_dataframes()
        self.build_elo(matches_df, map_df)

        with get_session() as session:
            upcoming = session.query(UpcomingMatch).filter(
                UpcomingMatch.game == Game.cs2,
                UpcomingMatch.scheduled_at >= datetime.utcnow() - timedelta(hours=6),
            ).all()

        with get_session() as session:
            names = {t.id: t.name for t in session.query(Team).filter(Team.game == Game.cs2).all()}

        predictions = []
        for um in upcoming:
            feats = build_match_features(
                map_results_df=map_df,
                team1_id=um.team1_id,
                team2_id=um.team2_id,
                match_date=pd.Timestamp(um.scheduled_at or datetime.utcnow()),
                elo_system=self.elo,
            )
            feats["is_lan"] = int(um.is_lan)
            feats["best_of"] = um.best_of or 3

            p = self.win_model.predict_single(feats)
            predictions.append({
                "upcoming_match_id": um.id,
                "team1_id": um.team1_id,
                "team2_id": um.team2_id,
                "team1_name": names.get(um.team1_id, ""),
                "team2_name": names.get(um.team2_id, ""),
                "scheduled_at": um.scheduled_at,
                "event": um.event_name,
                "team1_win_prob": round(p, 4),
                "team2_win_prob": round(1 - p, 4),
                "features": feats,
            })

        logger.info(f"Generated {len(predictions)} match predictions")
        return predictions

    def predict_player_props(
        self,
        player_id: int,
        opponent_team_id: int,
        map_name: Optional[str],
        is_lan: bool = False,
        best_of: int = 3,
    ) -> dict[str, float]:
        """Predict expected value for each prop stat for a player."""
        _, map_df, player_df = self.load_dataframes()

        rolling = compute_player_rolling_stats(player_df, player_id, STAT_COLS)
        map_rolling = compute_player_rolling_stats(
            player_df, player_id, STAT_COLS, specific_map=map_name
        )
        opp_stats = compute_team_rolling_stats(map_df, opponent_team_id)
        opp_elo = self.elo.get(opponent_team_id, "overall")

        feats = build_player_prop_features(
            rolling, map_rolling, opp_stats, opp_elo, is_lan, best_of, map_name
        )
        feats["player_id"] = player_id

        results = {}
        for stat, model in self.props_models.items():
            expected, std = model.predict_expected(feats)
            results[stat] = {"expected": round(expected, 2), "std": round(std, 2)}

        return results

    # ------------------------------------------------------------------
    # 6. Edge report
    # ------------------------------------------------------------------

    def edge_report(
        self,
        book_lines: list[BettingLine],
        vig_pct: float = 0.05,
    ) -> pd.DataFrame:
        """
        Given a list of BettingLines with American odds,
        attach model probabilities and return edge summary.
        """
        predictions = self.predict_upcoming()

        analyzer = SlateAnalyzer(
            win_model=self.win_model,
            props_models=self.props_models,
        )

        evaluated = []
        for pred in predictions:
            match_lines = [
                l for l in book_lines
                if l.match_id == pred.get("upcoming_match_id")
            ]
            if not match_lines:
                continue
            # (this used to put the numeric team id in team1_name, which crashed on .lower())
            evaluated.extend(
                analyzer.analyze_match_lines(
                    match_lines, pred["features"], vig_pct,
                    team1_name=pred.get("team1_name"), team2_name=pred.get("team2_name"),
                )
            )

        edges = analyzer.get_edges(evaluated)
        logger.info(f"Found {len(edges)} positive-edge lines out of {len(evaluated)} evaluated")
        return analyzer.summary_table(evaluated)

    # ------------------------------------------------------------------
    # Full run
    # ------------------------------------------------------------------

    def run(
        self,
        scrape: bool = True,
        tune: bool = False,
        max_scrape_pages: int = 20,
    ):
        if scrape:
            self.scrape_and_store(max_pages=max_scrape_pages)
            self.scrape_upcoming()
        self.train(tune=tune)
        predictions = self.predict_upcoming()
        return predictions
