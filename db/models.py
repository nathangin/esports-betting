from datetime import datetime
from sqlalchemy import (
    Column, Integer, Float, String, Boolean, DateTime,
    ForeignKey, UniqueConstraint, Index, Text, Enum
)
from sqlalchemy.orm import DeclarativeBase, relationship
import enum


class Base(DeclarativeBase):
    pass


class Game(enum.Enum):
    cs2 = "cs2"
    lol = "lol"
    valorant = "valorant"


# ---------------------------------------------------------------------------
# Teams & Players
# ---------------------------------------------------------------------------

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    game = Column(Enum(Game), nullable=False)
    name = Column(String(128), nullable=False)
    short_name = Column(String(32))
    region = Column(String(32))
    hltv_id = Column(Integer, unique=True)       # CS2
    vlr_id = Column(Integer, unique=True)        # Valorant
    lol_team_id = Column(String(64), unique=True) # LoL (Riot slug)
    created_at = Column(DateTime, default=datetime.utcnow)

    players = relationship("Player", back_populates="team")
    elo_ratings = relationship("EloRating", back_populates="team")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    game = Column(Enum(Game), nullable=False)
    name = Column(String(128), nullable=False)      # in-game name
    real_name = Column(String(128))
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    role = Column(String(32))                       # entry/awp/support/igl | top/jg/mid/bot/sup | duelist/sentinel/etc
    hltv_id = Column(Integer, unique=True)
    vlr_id = Column(Integer, unique=True)
    riot_id = Column(String(64), unique=True)
    nationality = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    team = relationship("Team", back_populates="players")
    map_stats = relationship("PlayerMapStats", back_populates="player")


# ---------------------------------------------------------------------------
# Matches & Maps
# ---------------------------------------------------------------------------

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    game = Column(Enum(Game), nullable=False)
    external_id = Column(String(64), unique=True)  # hltv/vlr/pandascore id
    team1_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team2_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    winner_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    match_date = Column(DateTime, nullable=False)
    event_name = Column(String(256))
    tournament_stage = Column(String(64))           # groups/playoffs/grand-final
    best_of = Column(Integer, default=3)
    is_lan = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)
    star_rating = Column(Integer, default=0)   # HLTV star rating 0-5 (0=tier3, 3+=tier1)
    team1_map_score = Column(Integer)               # number of maps won
    team2_map_score = Column(Integer)
    patch_version = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)

    team1 = relationship("Team", foreign_keys=[team1_id])
    team2 = relationship("Team", foreign_keys=[team2_id])
    winner = relationship("Team", foreign_keys=[winner_id])
    maps = relationship("MapResult", back_populates="match", order_by="MapResult.map_order")

    __table_args__ = (
        Index("ix_match_date_game", "match_date", "game"),
        Index("ix_match_teams", "team1_id", "team2_id"),
    )


class MapResult(Base):
    __tablename__ = "map_results"

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    map_name = Column(String(64), nullable=False)
    map_order = Column(Integer, default=0)          # 0=map1, 1=map2, etc.
    team1_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team2_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    winner_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    team1_rounds = Column(Integer)
    team2_rounds = Column(Integer)
    # Which side each team started on (CT/T)
    team1_first_half_side = Column(String(2))       # CT or T
    team1_first_half_rounds = Column(Integer)
    team1_second_half_rounds = Column(Integer)
    team2_first_half_rounds = Column(Integer)
    team2_second_half_rounds = Column(Integer)
    # Overtime
    went_to_ot = Column(Boolean, default=False)
    team1_ot_rounds = Column(Integer, default=0)
    team2_ot_rounds = Column(Integer, default=0)
    # Map selection
    picked_by = Column(Integer, ForeignKey("teams.id"), nullable=True)  # team that picked this map
    is_decider = Column(Boolean, default=False)
    duration_minutes = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

    match = relationship("Match", back_populates="maps")
    team1 = relationship("Team", foreign_keys=[team1_id])
    team2 = relationship("Team", foreign_keys=[team2_id])
    winner = relationship("Team", foreign_keys=[winner_id])
    picked_by_team = relationship("Team", foreign_keys=[picked_by])
    player_stats = relationship("PlayerMapStats", back_populates="map_result")

    __table_args__ = (
        UniqueConstraint("match_id", "map_order", name="uq_map_in_match"),
        Index("ix_map_name_game", "map_name"),
    )


# ---------------------------------------------------------------------------
# Player Stats (per map)
# ---------------------------------------------------------------------------

class PlayerMapStats(Base):
    """One row per player per map played."""
    __tablename__ = "player_map_stats"

    id = Column(Integer, primary_key=True)
    map_result_id = Column(Integer, ForeignKey("map_results.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    is_winner = Column(Boolean)

    # Universal stats
    kills = Column(Integer)
    deaths = Column(Integer)
    assists = Column(Integer)

    # CS2 / Valorant specific
    hs_count = Column(Integer)
    hs_pct = Column(Float)          # 0.0–1.0
    kast = Column(Float)            # 0.0–1.0
    rating = Column(Float)          # HLTV Rating 2.0 / VLR rating
    adr = Column(Float)             # average damage per round
    first_kills = Column(Integer)   # opening kills
    first_deaths = Column(Integer)
    clutches_won = Column(Integer)
    clutches_attempted = Column(Integer)

    # CS2 specific
    flash_assists = Column(Integer)
    enemies_flashed_per_round = Column(Float)

    # Valorant specific
    acs = Column(Float)             # average combat score
    agent = Column(String(32))

    # LoL specific
    role = Column(String(16))
    champion = Column(String(64))
    cs_total = Column(Integer)
    cs_per_min = Column(Float)
    gold_earned = Column(Integer)
    gold_diff_at_15 = Column(Integer)
    xp_diff_at_15 = Column(Integer)
    damage_dealt_to_champions = Column(Integer)
    damage_share = Column(Float)        # fraction of team damage
    vision_score = Column(Integer)
    wards_placed = Column(Integer)
    wards_cleared = Column(Integer)
    turret_kills = Column(Integer)
    dragon_kills = Column(Integer)
    baron_kills = Column(Integer)
    double_kills = Column(Integer)
    triple_kills = Column(Integer)
    quadra_kills = Column(Integer)
    penta_kills = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    map_result = relationship("MapResult", back_populates="player_stats")
    player = relationship("Player", back_populates="map_stats")
    team = relationship("Team")

    __table_args__ = (
        UniqueConstraint("map_result_id", "player_id", name="uq_player_map"),
        Index("ix_pms_player_date", "player_id"),
    )


# ---------------------------------------------------------------------------
# Elo Ratings (time-series)
# ---------------------------------------------------------------------------

class EloRating(Base):
    """Snapshot of a team's Elo after each match (global + per map)."""
    __tablename__ = "elo_ratings"

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    game = Column(Enum(Game), nullable=False)
    map_name = Column(String(64), default="overall")  # 'overall' or specific map
    rating = Column(Float, nullable=False, default=1500.0)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)
    recorded_at = Column(DateTime, default=datetime.utcnow)

    team = relationship("Team", back_populates="elo_ratings")

    __table_args__ = (
        Index("ix_elo_team_map", "team_id", "map_name"),
        Index("ix_elo_recorded_at", "recorded_at"),
    )


# ---------------------------------------------------------------------------
# Map Pool (veto tendencies)
# ---------------------------------------------------------------------------

class MapVetoStat(Base):
    """Aggregated map pick/ban stats per team (updated after each match)."""
    __tablename__ = "map_veto_stats"

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    game = Column(Enum(Game), nullable=False)
    map_name = Column(String(64), nullable=False)
    times_picked = Column(Integer, default=0)
    times_banned = Column(Integer, default=0)
    times_played = Column(Integer, default=0)
    wins_on_map = Column(Integer, default=0)
    losses_on_map = Column(Integer, default=0)
    avg_rounds_won = Column(Float)
    avg_rounds_lost = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("team_id", "map_name", "game", name="uq_team_map_veto"),
    )


# ---------------------------------------------------------------------------
# Upcoming Matches (for live prediction)
# ---------------------------------------------------------------------------

class UpcomingMatch(Base):
    __tablename__ = "upcoming_matches"

    id = Column(Integer, primary_key=True)
    game = Column(Enum(Game), nullable=False)
    external_id = Column(String(64), unique=True)
    team1_id = Column(Integer, ForeignKey("teams.id"))
    team2_id = Column(Integer, ForeignKey("teams.id"))
    scheduled_at = Column(DateTime)
    event_name = Column(String(256))
    best_of = Column(Integer)
    is_lan = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    team1 = relationship("Team", foreign_keys=[team1_id])
    team2 = relationship("Team", foreign_keys=[team2_id])
    predictions = relationship("Prediction", back_populates="upcoming_match")


# ---------------------------------------------------------------------------
# Predictions & Bet Tracking
# ---------------------------------------------------------------------------

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    upcoming_match_id = Column(Integer, ForeignKey("upcoming_matches.id"), nullable=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=True)  # filled after result
    game = Column(Enum(Game), nullable=False)
    prediction_type = Column(String(64))        # match_winner / map_winner / player_kills_ou / etc.
    subject = Column(String(128))               # team name or "PlayerName kills"
    predicted_value = Column(Float)             # probability or expected value
    line = Column(Float)                        # book line (e.g. 18.5 kills, or 0.6 impl. prob)
    book_odds = Column(Float)                   # American or decimal odds
    implied_prob = Column(Float)
    model_prob = Column(Float)
    edge = Column(Float)                        # model_prob - implied_prob
    kelly_fraction = Column(Float)
    model_version = Column(String(32))
    features_snapshot = Column(Text)            # JSON blob of key features used
    created_at = Column(DateTime, default=datetime.utcnow)
    # filled after match completes
    actual_value = Column(Float)
    correct = Column(Boolean)

    upcoming_match = relationship("UpcomingMatch", back_populates="predictions")
