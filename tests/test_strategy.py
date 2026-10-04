import pytest

from esalpha.strategy import (Rules, default_rules, flat_candidates, flat_rules, market_prob, match_candidates,
                              settle_pnl, size, taker_fee)


def test_taker_fee_rounds_up_to_the_cent():
    assert taker_fee(0.50, 1) == 0.02          # 0.0175 -> 0.02
    assert taker_fee(0.50, 100) == 1.75
    assert taker_fee(0.10, 10) == 0.07         # 0.063 -> 0.07


def test_market_prob_uses_both_team_markets():
    assert market_prob(0.60, 0.62, 0.38, 0.40) == pytest.approx(0.61)
    assert market_prob(None, None, 0.38, 0.40) == pytest.approx(0.61)
    assert market_prob(None, 0.5, None, None) is None


def test_match_candidates_backs_the_cheaper_route():
    a = {"ticker": "E-A", "yes_bid": 0.40, "yes_ask": 0.44}
    b = {"ticker": "E-B", "yes_bid": 0.58, "yes_ask": 0.60}
    # model likes A at 0.55: YES on A costs 0.44, NO on B costs 1 - 0.58 = 0.42 -> buy NO on B
    c = match_candidates("E", 0.55, a, b, default_rules())
    assert len(c) == 1 and c[0]["ticker"] == "E-B" and c[0]["side"] == "no" and c[0]["backs"] == "A"
    assert c[0]["price"] == pytest.approx(0.42)
    # no edge -> no bet
    assert match_candidates("E", 0.43, a, b, default_rules()) == []


def test_flat_baseline_bets_one_percent_on_the_chosen_team():
    a = {"ticker": "E-A", "yes_bid": 0.70, "yes_ask": 0.72}
    b = {"ticker": "E-B", "yes_bid": 0.27, "yes_ask": 0.29}
    rules = default_rules()
    bets = size(flat_candidates("E", True, a, b, rules), 1000, 1000, flat_rules(rules))
    assert len(bets) == 1 and bets[0].extra["backs"] == "A"
    assert bets[0].cost + bets[0].fee <= 10.0 + 1e-9 and bets[0].cost > 9.0


def test_size_respects_caps_and_cash():
    r = Rules(kelly=1.0, max_bet_frac=0.02, max_event_frac=0.02, max_run_frac=1.0)
    c = [{"ticker": "E-A", "event_ticker": "E", "side": "yes", "price": 0.40, "prob": 0.60, "kelly_f": 0.3}]
    bets = size(c, 1000, 1000, r)
    assert bets[0].cost + bets[0].fee <= 20.0 + 1e-9
    assert size(c, 1000, 0.3, r) == []


def test_settle_pnl():
    assert settle_pnl("yes", 10, 0.40, 0.17, "yes") == pytest.approx(10 * 0.6 - 0.17)
    assert settle_pnl("no", 10, 0.40, 0.17, "yes") == pytest.approx(-4.0 - 0.17)
    assert settle_pnl("no", 10, 0.40, 0.17, "void") == 0.0
