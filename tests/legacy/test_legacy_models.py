import numpy as np
import pandas as pd
import pytest

xgb = pytest.importorskip("xgboost")
pytest.importorskip("lightgbm")
pytest.importorskip("optuna")
pytest.importorskip("sklearn")

from models.props_model import PropsModel  # noqa: E402
from models.win_model import WinModel  # noqa: E402


def test_win_model_calibration_is_out_of_fold():
    rng = np.random.default_rng(0)
    n = 1500
    x = rng.normal(size=n)
    y = (rng.random(n) < 1 / (1 + np.exp(-0.8 * x))).astype(int)
    df = pd.DataFrame({"elo_diff_overall": x * 100, "elo_win_prob_t1": 1 / (1 + 10 ** (-x / 4)),
                       "wr_diff_last5": rng.normal(size=n), "label": y,
                       "match_date": pd.date_range("2025-01-01", periods=n, freq="6h")})
    m = WinModel("t").fit(df.iloc[:1200])
    assert m.cal_on_logit and "oof_auc" in m.metrics
    p = m.predict_proba(df.iloc[1200:])
    # calibrated on held-out folds, so new predictions are not wildly overconfident
    assert 0.02 < p.min() and p.max() < 0.98
    # a missing feature is filled with the training median, not 0.5
    assert 0 < m.predict_single({"elo_diff_overall": 50.0}) < 1


def test_props_spread_comes_from_out_of_fold_errors():
    rng = np.random.default_rng(1)
    n = 1200
    ew = rng.normal(18, 3, n)
    kills = rng.normal(ew, 4.0)          # true noise sd = 4
    df = pd.DataFrame({"ew_kills": ew, "kills_last5": ew + rng.normal(0, 1, n), "kills": kills,
                       "match_date": pd.date_range("2025-01-01", periods=n, freq="6h")})
    m = PropsModel("kills").fit(df)
    _, sd = m.predict_expected({"ew_kills": 18.0, "kills_last5": 18.0})
    # in-sample residuals would give well under 4; out-of-fold errors are about the true noise
    assert 3.6 < sd < 5.0
