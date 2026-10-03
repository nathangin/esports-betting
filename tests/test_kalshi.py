from datetime import datetime, timezone

from esalpha.history import MATCH_TITLE, build_matches
from esalpha.kalshi import game_of, parse_candles, parse_market, start_from_rules, start_from_ticker

import pandas as pd


def test_parse_real_settled_match(fixture):
    ms = [parse_market(m) for m in fixture("kalshi_codgame_settled.json")["markets"]]
    og = next(m for m in ms if m.ticker.endswith("-OG"))
    assert og.series_ticker == "KXCODGAME" and og.game == "cod"
    assert og.team == "OpTic Gaming" and og.competitor == "f0ccadd8-0367-473e-8e56-8f1e600f14d2"
    assert og.result == "yes" and og.winner_name == "OpTic Gaming"
    # 3:00 PM EDT on Aug 9 2026, from the ticker and from the rules text
    assert og.start_time == datetime(2026, 8, 9, 19, 0, tzinfo=timezone.utc)
    assert og.tournament == "Esports World Cup 2026"
    # settled markets show a 0/1 book: those quotes are dropped rather than read as prices
    assert og.yes_bid is None and og.yes_ask is None
    assert MATCH_TITLE.match(og.title)


def test_build_matches_from_real_pair(fixture):
    rows = [parse_market(m).to_row() for m in fixture("kalshi_codgame_settled.json")["markets"]]
    m = build_matches(pd.DataFrame(rows))
    assert len(m) == 1
    r = m.iloc[0]
    # team A is the market with the smaller ticker (-HTCS < -OG), and OpTic won
    assert r["ticker_a"].endswith("-HTCS") and r["winner"] == "B"


def test_start_time_parsers():
    assert start_from_ticker("KXLOLGAME-26JAN051030T1GEN") == datetime(2026, 1, 5, 15, 30, tzinfo=timezone.utc)  # EST
    assert start_from_ticker("KXLOLGAME-NOTATICKER") is None
    assert start_from_rules("match originally scheduled for Oct 2, 2026 at 9:05 AM EDT") == \
        datetime(2026, 10, 2, 13, 5, tzinfo=timezone.utc)
    assert game_of("KXCS2GAME") == "cs2" and game_of("KXVALORANTGAME") == "valorant" and game_of("KXLOLGAME") == "lol"


def test_parse_candles_dollar_fields():
    rows = [{"end_period_ts": 100, "yes_bid": {"close_dollars": "0.4500"}, "yes_ask": {"close_dollars": "0.4700"},
             "price": {"close_dollars": "0.4600"}, "volume_fp": "12.00"},
            {"end_period_ts": 160, "yes_bid": {"close": 0}, "yes_ask": {"close": 100}, "price": {}, "volume": 0}]
    c = parse_candles(rows)
    assert c[0] == {"ts": 100, "bid": 0.45, "ask": 0.47, "price": 0.46, "volume": 12.0}
    assert c[1]["bid"] is None and c[1]["ask"] is None


def test_history_tables_are_monthly_shards(tmp_path):
    from esalpha.history import read_table, write_table

    df = pd.DataFrame({"event_ticker": ["A", "B", "C"], "ts": [1756684800, 1759276800, 1759363200],
                       "bid": [0.4, 0.5, 0.6]})                     # 2025-09-01, 2025-10-01, 2025-10-02
    (tmp_path / "candles.parquet").write_bytes(b"")                 # an old single-file table is replaced
    write_table(tmp_path, "candles", df, "ts")
    assert sorted(p.name for p in (tmp_path / "candles").iterdir()) == ["2025-09.parquet", "2025-10.parquet"]
    assert not (tmp_path / "candles.parquet").exists()
    before = (tmp_path / "candles" / "2025-09.parquet").stat().st_mtime_ns
    write_table(tmp_path, "candles", pd.concat([df, df.iloc[[2]].assign(event_ticker="D", ts=1759370000)],
                                               ignore_index=True), "ts")
    assert (tmp_path / "candles" / "2025-09.parquet").stat().st_mtime_ns == before   # untouched month
    out = read_table(tmp_path, "candles")
    assert list(out["event_ticker"]) == ["A", "B", "C", "D"]
