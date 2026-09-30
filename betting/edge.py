"""
Betting edge detection and position sizing.

Workflow:
  1. Convert book odds → implied probability (accounting for vig)
  2. Compare implied probability to model probability
  3. Flag bets where edge >= threshold
  4. Size using fractional Kelly criterion
"""
from dataclasses import dataclass, field
from typing import Optional
import pandas as pd
import numpy as np
from loguru import logger

from config import MIN_EDGE_THRESHOLD, MAX_KELLY_FRACTION


# ---------------------------------------------------------------------------
# Odds conversion utilities
# ---------------------------------------------------------------------------

def american_to_decimal(american: float) -> float:
    """Convert American odds to decimal odds."""
    if american > 0:
        return (american / 100) + 1
    else:
        return (100 / abs(american)) + 1


def decimal_to_implied(decimal: float) -> float:
    """Decimal odds → raw implied probability (includes vig)."""
    return 1.0 / decimal


def american_to_implied(american: float) -> float:
    return decimal_to_implied(american_to_decimal(american))


def remove_vig_two_way(implied_a: float, implied_b: float) -> tuple[float, float]:
    """
    Remove bookmaker vig from a two-outcome market.
    Returns (fair_prob_a, fair_prob_b) that sum to 1.0.
    """
    total = implied_a + implied_b
    return implied_a / total, implied_b / total


def remove_vig_one_side(implied: float, vig_pct: float = 0.05) -> float:
    """
    Remove estimated vig from a single side.
    vig_pct: estimated total overround (e.g. 0.05 = 5%).
    """
    return implied / (1 + vig_pct)


def implied_to_american(prob: float) -> float:
    """Fair probability → American odds (no vig)."""
    if prob >= 0.5:
        return -(prob / (1 - prob)) * 100
    else:
        return ((1 - prob) / prob) * 100


# ---------------------------------------------------------------------------
# Edge and Kelly
# ---------------------------------------------------------------------------

def edge(model_prob: float, implied_prob: float) -> float:
    """Simple edge: model_prob - implied_prob (fair, vig-removed)."""
    return model_prob - implied_prob


def kelly_fraction(model_prob: float, decimal_odds: float) -> float:
    """
    Full Kelly fraction: f = (bp - q) / b
    b = decimal_odds - 1 (net profit per unit)
    p = model probability of winning
    q = 1 - p
    """
    b = decimal_odds - 1
    p = model_prob
    q = 1 - p
    if b <= 0:
        return 0.0
    f = (b * p - q) / b
    return max(f, 0.0)


def fractional_kelly(model_prob: float, decimal_odds: float, fraction: float = MAX_KELLY_FRACTION) -> float:
    """Capped fractional Kelly — reduces variance."""
    full = kelly_fraction(model_prob, decimal_odds)
    return min(full * fraction, fraction)


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass
class BettingLine:
    """Represents a single book line for a bet."""
    match_id: Optional[int]
    game: str
    bet_type: str                   # match_winner / map_winner / kills_ou / etc.
    description: str                # e.g. "Team A ML" or "PlayerX kills O18.5"
    subject: str                    # team name / player name
    # Book side
    american_odds: float
    line_value: Optional[float] = None  # e.g. 18.5 for props, None for ML
    # Model
    model_prob: Optional[float] = None
    # Computed
    decimal_odds: float = field(init=False)
    implied_prob: float = field(init=False)
    fair_prob: Optional[float] = None
    edge_value: Optional[float] = None
    kelly: Optional[float] = None
    flag: bool = False

    def __post_init__(self):
        self.decimal_odds = american_to_decimal(self.american_odds)
        self.implied_prob = american_to_implied(self.american_odds)

    def evaluate(self, vig_pct: float = 0.05) -> "BettingLine":
        """Compute edge and Kelly given model_prob."""
        if self.model_prob is None:
            return self
        self.fair_prob = remove_vig_one_side(self.implied_prob, vig_pct)
        self.edge_value = edge(self.model_prob, self.fair_prob)
        self.kelly = fractional_kelly(self.model_prob, self.decimal_odds)
        self.flag = self.edge_value >= MIN_EDGE_THRESHOLD
        return self


# ---------------------------------------------------------------------------
# Slate analyzer
# ---------------------------------------------------------------------------

class SlateAnalyzer:
    """
    Takes a list of BettingLines for upcoming matches,
    applies model probabilities, and returns flagged edges.
    """

    def __init__(self, win_model=None, props_models: Optional[dict] = None):
        self.win_model = win_model
        self.props_models = props_models or {}   # {stat: PropsModel}

    def analyze_match_lines(
        self,
        lines: list[BettingLine],
        match_features: dict,
        vig_pct: float = 0.05,
    ) -> list[BettingLine]:
        """Assign model probs to match-winner lines and evaluate."""
        if self.win_model is None:
            return lines

        team1_win_prob = self.win_model.predict_single(match_features)
        team2_win_prob = 1.0 - team1_win_prob

        for line in lines:
            if line.bet_type == "match_winner":
                if "team1" in line.description.lower() or match_features.get("team1_name", "").lower() in line.description.lower():
                    line.model_prob = team1_win_prob
                else:
                    line.model_prob = team2_win_prob
                line.evaluate(vig_pct)

        return lines

    def analyze_prop_lines(
        self,
        lines: list[BettingLine],
        player_features: dict,
        vig_pct: float = 0.05,
    ) -> list[BettingLine]:
        """Assign model probs to player prop lines and evaluate."""
        for line in lines:
            stat = line.bet_type.replace("_ou", "").replace("_over", "").replace("_under", "")
            if stat not in self.props_models or line.line_value is None:
                continue

            model = self.props_models[stat]
            pred = model.over_under_prob(player_features, line.line_value)

            is_over = "over" in line.bet_type.lower() or "o" in line.description.lower()
            line.model_prob = pred.over_prob if is_over else pred.under_prob
            line.evaluate(vig_pct)

        return lines

    def get_edges(
        self,
        lines: list[BettingLine],
        min_edge: float = MIN_EDGE_THRESHOLD,
    ) -> list[BettingLine]:
        """Return only lines with positive edge above threshold."""
        return [l for l in lines if l.flag and l.edge_value is not None and l.edge_value >= min_edge]

    def summary_table(self, lines: list[BettingLine]) -> pd.DataFrame:
        rows = []
        for l in lines:
            rows.append({
                "game": l.game,
                "type": l.bet_type,
                "description": l.description,
                "american_odds": l.american_odds,
                "implied_prob": round(l.implied_prob, 3) if l.implied_prob else None,
                "fair_prob": round(l.fair_prob, 3) if l.fair_prob else None,
                "model_prob": round(l.model_prob, 3) if l.model_prob else None,
                "edge": round(l.edge_value, 3) if l.edge_value else None,
                "kelly_pct": round((l.kelly or 0) * 100, 2),
                "flag": l.flag,
            })
        return pd.DataFrame(rows).sort_values("edge", ascending=False, na_position="last")


# ---------------------------------------------------------------------------
# Expected Value tracker (for backtesting / live performance)
# ---------------------------------------------------------------------------

class BetTracker:
    def __init__(self):
        self._bets: list[dict] = []

    def record(
        self,
        line: BettingLine,
        stake_units: float,
        outcome: Optional[bool] = None,  # True=win, False=loss, None=pending
    ):
        self._bets.append({
            "description": line.description,
            "american_odds": line.american_odds,
            "decimal_odds": line.decimal_odds,
            "model_prob": line.model_prob,
            "edge": line.edge_value,
            "kelly": line.kelly,
            "stake": stake_units,
            "outcome": outcome,
            "pnl": (stake_units * (line.decimal_odds - 1)) if outcome else (-stake_units if outcome is False else None),
        })

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self._bets)

    def roi(self) -> float:
        df = self.to_dataframe().dropna(subset=["pnl"])
        if df.empty:
            return 0.0
        return df["pnl"].sum() / df["stake"].sum()

    def summary(self) -> dict:
        df = self.to_dataframe()
        settled = df.dropna(subset=["pnl"])
        return {
            "total_bets": len(df),
            "settled": len(settled),
            "wins": int((settled["outcome"] == True).sum()),
            "total_staked": settled["stake"].sum(),
            "total_pnl": settled["pnl"].sum(),
            "roi": self.roi(),
            "avg_edge": df["edge"].mean(),
            "avg_kelly": df["kelly"].mean(),
        }
