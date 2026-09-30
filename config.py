from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = DATA_DIR / "models_saved"

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/data/esports.db")

# PandaScore API (optional — higher quality, paid)
PANDASCORE_TOKEN = os.getenv("PANDASCORE_TOKEN", "")

# Riot API (for LoL)
RIOT_API_KEY = os.getenv("RIOT_API_KEY", "")

# Scraper settings
HLTV_BASE = "https://www.hltv.org"
VLR_BASE = "https://www.vlr.gg"
REQUEST_DELAY = 2.5          # seconds between HLTV requests (be polite)
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Elo settings
ELO_K_FACTOR = 32
ELO_START = 1500
ELO_MAP_K_FACTOR = 24        # per-map Elo is noisier, lower K

# Rolling window sizes
RECENCY_WINDOWS = [5, 10, 20]   # matches to look back
RECENCY_DECAY = 0.92            # exponential decay weight per match (most recent = 1.0)

# Model settings
RANDOM_STATE = 42
CV_FOLDS = 5
MIN_MATCHES_FOR_PREDICTION = 5  # minimum team history before predicting

# Betting
MAX_KELLY_FRACTION = 0.25       # fractional Kelly cap (25% of full Kelly)
MIN_EDGE_THRESHOLD = 0.03       # minimum edge to flag a bet (3%)

GAME_CONFIGS = {
    "cs2": {
        "stat_cols": ["kills", "deaths", "assists", "hs_pct", "kast", "rating", "adr", "first_kills"],
        "prop_lines": ["kills", "deaths", "hs_pct"],
        "max_rounds": 30,
        "overtimes": True,
    },
    "lol": {
        "stat_cols": ["kills", "deaths", "assists", "cs_per_min", "damage_share", "vision_score", "gold_diff_15"],
        "prop_lines": ["kills", "deaths", "assists"],
        "roles": ["top", "jungle", "mid", "bot", "support"],
    },
    "valorant": {
        "stat_cols": ["kills", "deaths", "assists", "acs", "hs_pct", "kast", "adr", "first_kills"],
        "prop_lines": ["kills", "deaths", "acs"],
        "max_rounds": 25,
        "overtime_rounds": 2,
    },
}
