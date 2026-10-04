import numpy as np
import pandas as pd

from esalpha import ratings as rt


def _matches(results):
    t0 = pd.Timestamp("2026-01-01T12:00Z")
    return pd.DataFrame([{"event_ticker": f"E{i}", "game": "cs2", "start_time": t0 + pd.Timedelta(days=i),
                          "comp_a": a, "comp_b": b, "winner": w} for i, (a, b, w) in enumerate(results)])


def test_features_are_pre_match_only():
    base = [("x", "y", "A"), ("x", "z", "A"), ("y", "z", "B"), ("x", "y", "A")]
    f1 = rt.pre_match_features(_matches(base))
    # flipping the LAST result must not change any feature of any match (including the last one)
    f2 = rt.pre_match_features(_matches(base[:-1] + [("x", "y", "B")]))
    cols = ["elo_a", "elo_b", "p_elo", "games_a", "games_b", "form_a", "form_b"]
    pd.testing.assert_frame_equal(f1[cols], f2[cols])
    # first meeting: both teams new, even odds
    assert f1.loc[0, "p_elo"] == 0.5 and f1.loc[0, "games_a"] == 0
    # x won its first two matches, so it is favoured in the rematch
    assert f1.loc[3, "p_elo"] > 0.5 and f1.loc[3, "games_a"] == 2


def test_elo_update_is_zero_sum_for_equal_experience():
    e = rt.Elo(rt.EloConfig(k=32, k_new_boost=0, decay_days=0))
    t = pd.Timestamp("2026-01-01T00:00Z")
    e.update("a", "b", 1.0, t)
    assert abs((e.rating["a"] - 1500) + (e.rating["b"] - 1500)) < 1e-9 and e.rating["a"] == 1516


def test_idle_ratings_decay_toward_the_mean():
    e = rt.Elo(rt.EloConfig(decay_days=120, decay_frac=0.25))
    e.rating["a"], e.last["a"] = 1700.0, pd.Timestamp("2026-01-01T00:00Z")
    assert abs(e._get("a", pd.Timestamp("2026-05-01T00:00Z")) - (1500 + 200 * 0.75)) < 1e-6


def test_fit_logistic_recovers_coefficients():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(20000, 2))
    p = rt.sigmoid(0.3 + 1.2 * X[:, 0] - 0.5 * X[:, 1])
    y = (rng.random(20000) < p).astype(float)
    w = rt.fit_logistic(X, y, l2=0.0)
    assert np.allclose(w, [0.3, 1.2, -0.5], atol=0.06)


def test_tune_k_uses_only_matches_before_cutoff():
    rng = np.random.default_rng(2)
    rows = []
    for i in range(400):
        a, b = rng.choice(10, 2, replace=False)
        rows.append((f"t{a}", f"t{b}", "A" if a < b else "B"))
    m = _matches(rows)
    k, scores = rt.tune_k(m, "cs2", until=m["start_time"].iloc[300])
    assert k in (16, 24, 32, 48, 64) and scores


def test_fit_without_intercept_for_symmetric_features():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(5000, 1))
    y = (rng.random(5000) < rt.sigmoid(0.4 + 1.0 * X[:, 0])).astype(float)
    w = rt.fit_logistic(X, y, l2=0.0, intercept=False)
    assert abs(w[0]) < 1e-6 and 0.7 < w[1] < 1.3
