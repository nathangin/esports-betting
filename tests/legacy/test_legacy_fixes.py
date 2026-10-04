import numpy as np
import pandas as pd
import pytest

from betting.edge import BettingLine, SlateAnalyzer, fractional_kelly, prop_direction
from features.elo import EloSystem, pre_match_ratings_from_maps
from features.rolling_stats import build_training_dataset, pre_match_team_win_rates


def _league(n=60, seed=0):
    rng = np.random.default_rng(seed)
    strength = rng.normal(0, 1, 8)
    matches, maps = [], []
    t0 = pd.Timestamp("2026-01-01")
    for i in range(n):
        a, b = (int(x) for x in rng.choice(8, 2, replace=False))
        p = 1 / (1 + np.exp(-(strength[a] - strength[b])))
        w = a if rng.random() < p else b
        d = t0 + pd.Timedelta(days=i)
        matches.append({"match_id": i, "team1_id": a, "team2_id": b, "winner_id": w, "match_date": d,
                        "best_of": 1, "is_lan": False, "team1_map_score": int(w == a), "team2_map_score": int(w == b)})
        maps.append({"map_result_id": 1000 + i, "match_id": i, "map_name": "mirage", "team1_id": a, "team2_id": b,
                     "winner_id": w, "team1_rounds": 13 if w == a else 7, "team2_rounds": 13 if w == b else 7,
                     "match_date": d})
    return pd.DataFrame(matches), pd.DataFrame(maps)


def test_training_rows_only_see_earlier_results():
    m, mp = _league()
    f1 = build_training_dataset(m, mp, EloSystem())
    # flip the last result: no feature of any row may change (labels of course do)
    m2, mp2 = m.copy(), mp.copy()
    last = m2.index[-1]
    a, b, w = m2.loc[last, ["team1_id", "team2_id", "winner_id"]]
    loser = b if w == a else a
    m2.loc[last, ["winner_id", "team1_map_score", "team2_map_score"]] = [loser, int(loser == a), int(loser == b)]
    mp2.loc[mp2.index[-1], "winner_id"] = loser
    f2 = build_training_dataset(m2, mp2, EloSystem())
    cols = ["elo_t1_overall", "elo_t2_overall", "elo_diff_overall", "elo_win_prob_t1", "t1_ew_win_rate"]
    pd.testing.assert_frame_equal(f1[cols], f2[cols])
    # the very first match is played between two unrated teams
    assert f1.loc[0, "elo_diff_overall"] == 0


def test_pre_match_helpers_exclude_the_match_itself():
    m, mp = _league(20)
    elo = pre_match_ratings_from_maps(mp)
    wr = pre_match_team_win_rates(mp)
    first = mp.iloc[0]
    assert elo[first["map_result_id"]] == {first["team1_id"]: 1500.0, first["team2_id"]: 1500.0}
    assert wr[first["map_result_id"]] == {first["team1_id"]: 0.5, first["team2_id"]: 0.5}


def test_kelly_is_capped_per_bet():
    assert fractional_kelly(0.9, 2.0) == pytest.approx(0.02)       # quarter Kelly would be 0.2
    assert fractional_kelly(0.52, 2.0) == pytest.approx(0.25 * 0.04)
    assert fractional_kelly(0.4, 2.0) == 0.0


class _Fixed:
    def predict_single(self, feats):
        return 0.6


def test_match_lines_are_matched_by_team_name():
    lines = [BettingLine(1, "cs2", "match_winner", "Vitality ML", "Vitality", -150),
             BettingLine(1, "cs2", "match_winner", "Spirit ML", "Spirit", 130),
             BettingLine(1, "cs2", "match_winner", "Some other team ML", "Other", 200)]
    out = SlateAnalyzer(win_model=_Fixed()).analyze_match_lines(lines, {}, team1_name="Spirit", team2_name="Vitality")
    assert out[0].model_prob == pytest.approx(0.4) and out[1].model_prob == pytest.approx(0.6)
    assert out[2].model_prob is None
    # two-way vig removal: the pair's fair probabilities add up to one
    assert out[0].fair_prob + out[1].fair_prob == pytest.approx(1.0)
    # numeric ids no longer crash (the old edge_report put an int in team1_name)
    SlateAnalyzer(win_model=_Fixed()).analyze_match_lines(lines[:1], {"team1_name": 17})


def test_prop_direction():
    def line(desc, bt="kills_ou"):
        return BettingLine(None, "cs2", bt, desc, "x", -110, line_value=18.5)
    assert prop_direction(line("donk kills O18.5")) is True
    assert prop_direction(line("donk kills U18.5")) is False
    assert prop_direction(line("ropz kills under 18.5")) is False
    assert prop_direction(line("ropz kills O/U 18.5")) is None      # used to count as an over
    assert prop_direction(line("anything", bt="kills_over")) is True
