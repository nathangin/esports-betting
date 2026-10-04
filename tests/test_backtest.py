import json

import numpy as np
import pandas as pd

from esalpha import backtest
from esalpha.model import Params
from esalpha.strategy import default_rules
from synth import make_history


def test_backtest_runs_and_saves_params(tmp_path):
    make_history(tmp_path, n_days=150, per_day=10)
    rep = backtest.run(str(tmp_path))
    assert rep["matches_tested"] > 500
    s = rep["scores"]
    assert s["n"] > 300 and set(s["log_loss"]) == {"market", "model", "blend"}
    # the model learned real team strength: far better than a coin flip
    assert s["log_loss"]["model"] < 0.66
    assert set(rep["results"]) == {name for name, _, _ in backtest.STRATEGIES}
    prm = Params.load(tmp_path / "params" / "fitted.json")
    assert prm.win_w and prm.blend_w and set(prm.k) == {"cs2", "lol"}
    assert (tmp_path / "reports" / "backtest.json").exists()
    json.loads((tmp_path / "reports" / "backtest.json").read_text())


def test_walk_forward_never_sees_the_future(tmp_path):
    truth = make_history(tmp_path, n_days=120, per_day=10)
    hist = tmp_path / "history"
    ev1, info1 = backtest.build_events(hist, 60)
    ev1, _ = backtest.walk_forward(ev1, info1["features"])
    # rewrite every result in the last 30 days, rebuild, and compare earlier predictions
    m = truth["matches"].copy()
    late = m["start_time"] >= m["start_time"].max() - pd.Timedelta(days=30)
    m.loc[late, "winner"] = np.where(m.loc[late, "winner"] == "A", "B", "A")
    m.to_parquet(hist / "matches.parquet", index=False)
    ev2, info2 = backtest.build_events(hist, 60)
    ev2, _ = backtest.walk_forward(ev2, info2["features"])
    cut = m["start_time"].max() - pd.Timedelta(days=30)
    a = ev1[pd.to_datetime(ev1["start_time"], utc=True) < cut].set_index("event_ticker")["p_model"]
    b = ev2[pd.to_datetime(ev2["start_time"], utc=True) < cut].set_index("event_ticker")["p_model"]
    pd.testing.assert_series_equal(a.sort_index(), b.sort_index())


def test_bets_settle_on_the_markets_own_result(tmp_path):
    # one match, A wins; NO on B (backs A) must win, YES on B must lose
    ev = pd.DataFrame([{"event_ticker": "E", "series_ticker": "S", "game": "cs2", "decision_ts": 0,
                        "start_time": pd.Timestamp("2026-01-01T12:00Z"), "close_time": pd.Timestamp("2026-01-01T14:00Z"),
                        "ticker_a": "E-A", "ticker_b": "E-B", "bid_a": 0.40, "ask_a": 0.44, "bid_b": 0.58,
                        "ask_b": 0.60, "q": 0.43, "y": 1, "p": 0.56, "p_model": 0.30}])
    led, s = backtest.simulate(ev, "p", default_rules(), {})
    assert len(led) == 1 and led.iloc[0]["side"] == "no" and led.iloc[0]["ticker"] == "E-B"
    assert led.iloc[0]["result"] == "no" and led.iloc[0]["pnl"] > 0
    led2, _ = backtest.simulate(ev, "p_model", default_rules(), {})
    assert led2.iloc[0]["backs"] == "B" and led2.iloc[0]["pnl"] < 0
