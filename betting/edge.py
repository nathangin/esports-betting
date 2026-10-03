"""
Betting edge detection and position sizing.

Workflow:
  1. Convert book odds → implied probability (accounting for vig)
  2. Compare implied probability to model probability
  3. Flag bets where edge >= threshold
  4. Size using fractional Kelly criterion
"""
import re
from dataclasses import dataclass, field
from typing import Optional
import pandas as pd
import numpy as np
from loguru import logger

from config import MIN_EDGE_THRESHOLD, MAX_KELLY_FRACTION, MAX_STAKE_FRACTION


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


def fractional_kelly(
    model_prob: float,
    decimal_odds: float,
    fraction: float = MAX_KELLY_FRACTION,
    max_stake: float = MAX_STAKE_FRACTION,
) -> float:
    """Fractional Kelly stake as a share of bankroll, capped per bet.

    ``fraction`` scales full Kelly (0.25 = quarter Kelly); ``max_stake`` caps any single
    bet. (The cap used to be ``fraction`` itself, i.e. up to 25% of the bankroll on one
    match whenever the model was confident.)
    """
    full = kelly_fraction(model_prob, decimal_odds)
    return min(full * fraction, max_stake)


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

    def evaluate(self, vig_pct: float = 0.05, fair_prob: Optional[float] = None) -> "BettingLine":
        """Compute edge and Kelly given model_prob.

        Pass ``fair_prob`` when both sides of the market are known (``remove_vig_two_way``);
        otherwise the vig is estimated from ``vig_pct``."""
        if self.model_prob is None:
            return self
        self.fair_prob = fair_prob if fair_prob is not None else remove_vig_one_side(self.implied_prob, vig_pct)
        self.edge_value = edge(self.model_prob, self.fair_prob)
        self.kelly = fractional_kelly(self.model_prob, self.decimal_odds)
        self.flag = self.edge_value >= MIN_EDGE_THRESHOLD
        return self


# ---------------------------------------------------------------------------
# Line matching helpers
# ---------------------------------------------------------------------------

def _which_team(line: "BettingLine", names: dict[int, str]) -> Optional[int]:
    """1 or 2 for the team a match-winner line is on, None if unclear."""
    subj = (line.subject or "").strip().casefold()
    for side, name in names.items():
        if name and subj == name.casefold():
            return side
    desc = (line.description or "").casefold()
    if desc.startswith("team1") or desc.startswith("team 1"):
        return 1
    if desc.startswith("team2") or desc.startswith("team 2"):
        return 2
    hits = [side for side, name in names.items() if name and name.casefold() in desc]
    return hits[0] if len(hits) == 1 else None


_OVER = re.compile(r"(?:\bover\b|\bo\s*\d)", re.I)
_UNDER = re.compile(r"(?:\bunder\b|\bu\s*\d)", re.I)


def prop_direction(line: "BettingLine") -> Optional[bool]:
    """True for an over, False for an under, None if the line does not say.

    (This used to test ``"o" in description``, which is true for almost any player name,
    so unders were priced as overs.)"""
    bt = (line.bet_type or "").lower()
    if bt.endswith("_over") or bt == "over":
        return True
    if bt.endswith("_under") or bt == "under":
        return False
    desc = re.sub(r"\bo\s*/\s*u\b", " ", line.description or "", flags=re.I)   # "O/U 18.5" says neither
    over, under = bool(_OVER.search(desc)), bool(_UNDER.search(desc))
    if over != under:
        return over
    return None


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
        team1_name: Optional[str] = None,
        team2_name: Optional[str] = None,
    ) -> list[BettingLine]:
        """Assign model probs to match-winner lines and evaluate.

        Each line is matched to a team by its ``subject`` (or, failing that, its
        description). Lines that name neither team, or both, are left unpriced instead of
        being given team 1's probability. When both teams' lines are present the vig is
        removed from the pair.
        """
        if self.win_model is None:
            return lines

        team1_win_prob = self.win_model.predict_single(match_features)
        names = {
            1: str(team1_name if team1_name is not None else match_features.get("team1_name", "") or "").strip(),
            2: str(team2_name if team2_name is not None else match_features.get("team2_name", "") or "").strip(),
        }

        side_of: dict[int, int] = {}
        for i, line in enumerate(lines):
            if line.bet_type != "match_winner":
                continue
            side = _which_team(line, names)
            if side is None:
                logger.warning(f"Line '{line.description}' does not name either team; skipped")
                continue
            side_of[i] = side

        fair = {}
        by_side = {s: i for i, s in side_of.items()}
        if len(by_side) == 2:
            f1, f2 = remove_vig_two_way(lines[by_side[1]].implied_prob, lines[by_side[2]].implied_prob)
            fair = {by_side[1]: f1, by_side[2]: f2}

        for i, side in side_of.items():
            line = lines[i]
            line.model_prob = team1_win_prob if side == 1 else 1.0 - team1_win_prob
            line.evaluate(vig_pct, fair_prob=fair.get(i))

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
            is_over = prop_direction(line)
            if is_over is None:
                logger.warning(f"Prop '{line.description}': cannot tell over from under; skipped")
                continue

            model = self.props_models[stat]
            pred = model.over_under_prob(player_features, line.line_value)
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
