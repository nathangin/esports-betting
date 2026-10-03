"""Tests for the original app (pipeline/, features/, models/, betting/). They need its
lighter dependencies (loguru, python-dotenv); model tests skip if xgboost/lightgbm are missing."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
pytest.importorskip("loguru")
pytest.importorskip("dotenv")
