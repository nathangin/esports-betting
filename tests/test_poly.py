from datetime import datetime, timezone

from esalpha.poly import _time, match_rows


def test_match_rows_keeps_moneyline_markets_only():
    ev = {"id": 1, "title": "Counter-Strike: Vitality vs NAVI (BO3)", "markets": [
        {"id": 11, "question": "Vitality vs NAVI", "outcomes": '["Vitality", "NAVI"]', "clobTokenIds": '["111", "222"]',
         "outcomePrices": '["1", "0"]', "closed": True, "gameStartTime": "2026-10-04 16:30:00+00",
         "sportsMarketType": "moneyline", "volume": "5000"},
        {"id": 12, "question": "Map 1 Winner", "outcomes": '["Vitality", "NAVI"]', "clobTokenIds": '["3", "4"]',
         "outcomePrices": '["0", "1"]', "closed": True, "gameStartTime": "2026-10-04 16:30:00+00",
         "sportsMarketType": "child_moneyline"},
        {"id": 13, "question": "Will it go to 3 maps?", "outcomes": '["Yes", "No"]', "clobTokenIds": '["5", "6"]'}]}
    rows = match_rows(ev, "cs2")
    assert len(rows) == 1
    r = rows[0]
    assert r["team_1"] == "Vitality" and r["winner"] == "Vitality" and r["token_1"] == "111"
    assert r["start_time"] == datetime(2026, 10, 4, 16, 30, tzinfo=timezone.utc)


def test_time_formats():
    assert _time("2026-10-04T16:30:00Z") == datetime(2026, 10, 4, 16, 30, tzinfo=timezone.utc)
    assert _time(None) is None and _time("garbage") is None
