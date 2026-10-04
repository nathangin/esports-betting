"""
Elo rating system — global and per-map.

Expected score: E_A = 1 / (1 + 10^((R_B - R_A) / 400))
Update:         R_A' = R_A + K * (S_A - E_A)

We maintain separate Elo tables:
  - overall: tracks map-score results (e.g. 2-0 counts as +2)
  - per map_name: tracks win/loss on that specific map
"""
import math
from collections import defaultdict
from datetime import datetime
from typing import Optional
import pandas as pd
from loguru import logger

from config import ELO_K_FACTOR, ELO_MAP_K_FACTOR, ELO_START


class EloSystem:
    def __init__(
        self,
        k_overall: float = ELO_K_FACTOR,
        k_map: float = ELO_MAP_K_FACTOR,
        initial: float = ELO_START,
    ):
        self.k_overall = k_overall
        self.k_map = k_map
        self.initial = initial
        # {team_id: {map_name: rating}}  (map_name='overall' for global)
        self._ratings: dict[int, dict[str, float]] = defaultdict(
            lambda: defaultdict(lambda: self.initial)
        )
        # history: list of (match_id, team_id, map_name, old, new, date)
        self._history: list[tuple] = []

    def get(self, team_id: int, map_name: str = "overall") -> float:
        return self._ratings[team_id][map_name]

    def expected(self, r_a: float, r_b: float) -> float:
        return 1.0 / (1.0 + math.pow(10, (r_b - r_a) / 400.0))

    def update_match(
        self,
        match_id: int,
        team1_id: int,
        team2_id: int,
        team1_maps_won: int,
        team2_maps_won: int,
        match_date: datetime,
        map_results: Optional[list[dict]] = None,
    ):
        """
        Update overall Elo based on match result (map count).
        Optionally update per-map Elo for each map played.
        map_results: list of {map_name, winner_id, loser_id}
        """
        # --- Overall Elo ---
        total_maps = team1_maps_won + team2_maps_won
        if total_maps == 0:
            return

        r1 = self.get(team1_id)
        r2 = self.get(team2_id)
        e1 = self.expected(r1, r2)
        s1 = team1_maps_won / total_maps   # fractional score (0.0–1.0)

        new_r1 = r1 + self.k_overall * (s1 - e1)
        new_r2 = r2 + self.k_overall * ((1 - s1) - (1 - e1))

        self._history.append((match_id, team1_id, "overall", r1, new_r1, match_date))
        self._history.append((match_id, team2_id, "overall", r2, new_r2, match_date))

        self._ratings[team1_id]["overall"] = new_r1
        self._ratings[team2_id]["overall"] = new_r2

        # --- Per-map Elo ---
        if map_results:
            for m in map_results:
                map_name = m["map_name"]
                winner_id = m["winner_id"]
                loser_id = m["loser_id"]

                rw = self.get(winner_id, map_name)
                rl = self.get(loser_id, map_name)
                ew = self.expected(rw, rl)

                new_rw = rw + self.k_map * (1.0 - ew)
                new_rl = rl + self.k_map * (0.0 - (1 - ew))

                self._history.append((match_id, winner_id, map_name, rw, new_rw, match_date))
                self._history.append((match_id, loser_id, map_name, rl, new_rl, match_date))

                self._ratings[winner_id][map_name] = new_rw
                self._ratings[loser_id][map_name] = new_rl

    def get_all_ratings(self, as_of: Optional[datetime] = None) -> dict[int, dict[str, float]]:
        """Returns current ratings. If as_of is given, only matches played strictly before it
        count (a match on the as_of timestamp itself must not see its own result)."""
        if as_of is None:
            return dict(self._ratings)

        # Replay from scratch up to as_of
        snapshot = EloSystem(self.k_overall, self.k_map, self.initial)
        for match_id, team_id, map_name, old, new, date in self._history:
            if date < as_of:
                snapshot._ratings[team_id][map_name] = new
        return dict(snapshot._ratings)

    def fresh(self) -> "EloSystem":
        """An empty system with the same settings (for replaying matches in time order)."""
        return EloSystem(self.k_overall, self.k_map, self.initial)

    def to_dataframe(self) -> pd.DataFrame:
        rows = []
        for match_id, team_id, map_name, old_r, new_r, date in self._history:
            rows.append({
                "match_id": match_id,
                "team_id": team_id,
                "map_name": map_name,
                "old_rating": old_r,
                "new_rating": new_r,
                "date": date,
            })
        return pd.DataFrame(rows)

    def build_from_matches(self, matches_df: pd.DataFrame) -> "EloSystem":
        """
        Bulk-build Elo from a sorted DataFrame of matches.
        Required columns: match_id, team1_id, team2_id, team1_map_score,
                          team2_map_score, match_date
        Optional: map_results (list of dicts per row)
        """
        matches_df = matches_df.sort_values("match_date")
        for _, row in matches_df.iterrows():
            map_results = row.get("map_results", None)
            self.update_match(
                match_id=row["match_id"],
                team1_id=row["team1_id"],
                team2_id=row["team2_id"],
                team1_maps_won=int(row["team1_map_score"]),
                team2_maps_won=int(row["team2_map_score"]),
                match_date=row["match_date"],
                map_results=map_results if isinstance(map_results, list) else None,
            )
        logger.info(f"Elo built from {len(matches_df)} matches, {len(self._ratings)} teams rated")
        return self

    def win_probability(self, team1_id: int, team2_id: int, map_name: str = "overall") -> float:
        """Returns P(team1 wins)."""
        r1 = self.get(team1_id, map_name)
        r2 = self.get(team2_id, map_name)
        return self.expected(r1, r2)


def pre_match_ratings_from_maps(
    map_df: pd.DataFrame, k: float = ELO_K_FACTOR, initial: float = ELO_START
) -> dict:
    """{map_result_id: {team_id: overall Elo before that map's match}}.

    Replays matches (maps won per team) in time order, so a training row for a map only
    sees results from earlier matches. Used for the opponent-strength feature of the props
    models, which previously read each opponent's *final* rating (look-ahead).
    """
    out: dict = {}
    if map_df is None or map_df.empty:
        return out
    elo = EloSystem(k_overall=k, initial=initial)
    df = map_df.dropna(subset=["match_id"]).sort_values("match_date", kind="stable")
    order = df.drop_duplicates("match_id")["match_id"].tolist()
    groups = {mid: g for mid, g in df.groupby("match_id", sort=False)}
    for mid in order:
        g = groups[mid]
        teams = list(dict.fromkeys(list(g["team1_id"]) + list(g["team2_id"])))
        if len(teams) != 2:
            continue
        ta, tb = teams
        pre = {ta: elo.get(ta), tb: elo.get(tb)}
        for mr in g["map_result_id"]:
            out[mr] = pre
        wins_a = int((g["winner_id"] == ta).sum())
        wins_b = int((g["winner_id"] == tb).sum())
        elo.update_match(mid, ta, tb, wins_a, wins_b, g["match_date"].iloc[0])
    return out
