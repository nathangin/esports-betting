import json
import sys
from pathlib import Path

import pytest

FIX = Path(__file__).parent / "fixtures"
sys.path.insert(0, str(Path(__file__).parent))


def load(name):
    return json.loads((FIX / name).read_text())


@pytest.fixture
def fixture():
    return load
