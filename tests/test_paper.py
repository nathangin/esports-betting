import json
from datetime import datetime, timedelta, timezone

import pandas as pd

from kalshi_fakes import FakeKalshiHttp, market
from esalpha import paper, report
from esalpha.model import Params
from synth import make_history

NOW = datetime(2026, 10, 2, 18, 0, tzinfo=timezone.utc)
EV = "KXCS2GAME-26OCT021445T01T02"        # 2:45 PM EDT = 18:45 UTC, 45 minutes after NOW
LATER = "KXCS2GAME-26OCT021800T03T04"     # 22:00 UTC, four hours out: outside even the late-run window


def _setup(tmp_path):
    make_history(tmp_path, n_days=90, per_day=6)
    # fixed parameters so the test does not depend on what the synthetic fit happens to learn:
    # the win model says 0.82 for team A, the blend averages model and market on the logit scale
    Params(k={"cs2": 32.0, "lol": 32.0}, win_w=[1.5, 0.0, 0.0, 0.0], blend_w=[0.0, 0.5, 0.5],
           meta={"fitted": "2026-10-01T00:00Z"}).save(tmp_path / "params" / "fitted.json")
    open_ms = [market(f"{EV}-T01", "Team 1", "cs2-1", bid=0.44, ask=0.46, opponent="Team 2", new_title=True),
               market(f"{EV}-T02", "Team 2", "cs2-2", bid=0.54, ask=0.56, opponent="Team 1", new_title=True),
               market(f"{LATER}-T03", "Team 3", "cs2-3", bid=0.30, ask=0.32, opponent="Team 4"),
               market(f"{LATER}-T04", "Team 4", "cs2-4", bid=0.68, ask=0.70, opponent="Team 3")]
    return open_ms


def _run(monkeypatch, tmp_path, fake, now):
    monkeypatch.setattr(paper, "Http", lambda *a, **k: fake)
    return paper.run(str(tmp_path), now=now)


def test_paper_pass_decides_once_bets_and_settles(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    fake = FakeKalshiHttp(open_markets=open_ms)
    out = _run(monkeypatch, tmp_path, fake, NOW)
    assert out["matches_decided"] == 1 and out["series"] == 2
    scans = pd.read_parquet(tmp_path / "paper" / "scans" / "2026-10-02.parquet")
    row = scans.iloc[0]
    assert row["event_ticker"] == EV and abs(row["q"] - 0.45) < 1e-9 and abs(row["minutes_to_start"] - 45) < 1e-6
    assert abs(row["p_model"] - 0.8176) < 1e-3 and 0.6 < row["p_blend"] < 0.7
    # model-only disagrees with the market by more than max_gap: no bet
    assert str(row["bet_model-only"]).startswith("skip")
    led = pd.read_csv(tmp_path / "paper" / "ledger.csv")
    assert set(led["book"]) == {"blend", "favourite"}
    blend = led[led["book"] == "blend"].iloc[0]
    assert blend["backs"] == "Team 1" and blend["price"] == 0.46
    fav = led[led["book"] == "favourite"].iloc[0]
    assert fav["backs"] == "Team 2" and fav["cost"] + fav["fee"] <= 10.0 + 1e-9
    acct = json.loads((tmp_path / "paper" / "account.json").read_text())
    for b in paper.BOOKS:
        spent = (led.loc[led["book"] == b, "cost"] + led.loc[led["book"] == b, "fee"]).sum()
        assert abs(acct[b]["cash"] + spent - 1000.0) < 1e-6

    # ten minutes later: already decided, nothing new
    out2 = _run(monkeypatch, tmp_path, fake, NOW + timedelta(minutes=10))
    assert out2["matches_decided"] == 0

    # five minutes before the start the market has moved to Team 1 (0.51): that is the closing line
    moved = [dict(open_ms[0], yes_bid_dollars="0.5000", yes_ask_dollars="0.5200"),
             dict(open_ms[1], yes_bid_dollars="0.4800", yes_ask_dollars="0.5000")] + open_ms[2:]
    _run(monkeypatch, tmp_path, FakeKalshiHttp(open_markets=moved), NOW + timedelta(minutes=40))
    closes = pd.read_csv(tmp_path / "paper" / "closes.csv")
    assert list(closes["event_ticker"]) == [EV] and abs(closes["q_close"].iloc[0] - 0.51) < 1e-9
    books = report.book_stats(paper.State(tmp_path))
    assert abs(books["blend"]["avg_clv"] - (0.51 - 0.46)) < 1e-9          # backed Team 1 at 0.46
    assert abs(books["favourite"]["avg_clv"] - (0.49 - 0.56)) < 1e-9      # backed Team 2 at 0.56

    # the match is over: Team 1 won
    settled = [dict(m, status="finalized", result="yes" if m["ticker"].endswith("T01") else "no",
                    expiration_value="Team 1", close_time="2026-10-02T20:30:00Z") for m in open_ms[:2]]
    fake2 = FakeKalshiHttp(open_markets=open_ms[2:], settled_markets=settled)
    out3 = _run(monkeypatch, tmp_path, fake2, NOW + timedelta(hours=4))
    assert out3["settled"] == 2 and out3["results_added"] == 1
    led = pd.read_csv(tmp_path / "paper" / "ledger.csv")
    assert set(led["status"]) == {"won", "lost"}
    assert led.loc[led["book"] == "blend", "status"].iloc[0] == "won"
    st = paper.State(tmp_path)
    assert st.open_bets().empty
    for b in paper.BOOKS:
        assert abs(st.account[b]["cash"] - (1000 + led.loc[led["book"] == b, "pnl"].sum())) < 1e-6
    # the new result feeds the ratings
    assert EV in set(st.all_matches()["event_ticker"])

    rep = report.write(str(tmp_path))
    assert rep["scoring"]["n"] == 1 and rep["books"]["blend"]["won"] == 1
    md = (tmp_path / "reports" / "summary.md").read_text()
    assert "Team 1" in md and "| blend |" in md


def test_trial_end_stops_new_bets_but_keeps_settling(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    monkeypatch.setattr(paper, "Http", lambda *a, **k: FakeKalshiHttp(open_markets=open_ms))
    out = paper.run(str(tmp_path), now=NOW, until="2026-10-01")
    assert "ended" in out["scan"] and "matches_decided" not in out


def test_no_params_means_no_model_bets(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    (tmp_path / "params" / "fitted.json").unlink()
    out = _run(monkeypatch, tmp_path, FakeKalshiHttp(open_markets=open_ms), NOW)
    assert out["bets_placed"]["blend"] == 0 and out["bets_placed"]["model-only"] == 0


def test_decision_window_widens_when_runs_are_late(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    soon = "KXCS2GAME-26OCT021630T05T06"     # 20:30 UTC: 150 minutes after NOW
    open_ms += [market(f"{soon}-T05", "Team 5", "cs2-5", bid=0.48, ask=0.50, new_title=True),
                market(f"{soon}-T06", "Team 6", "cs2-6", bid=0.50, ask=0.52, new_title=True)]
    fake = FakeKalshiHttp(open_markets=open_ms)
    # a run 10 minutes earlier: the normal 10-70 minute window, so only the 18:45 match is decided
    (tmp_path / "paper").mkdir(parents=True, exist_ok=True)
    (tmp_path / "paper" / "runs.jsonl").write_text(json.dumps({"run_at": (NOW - timedelta(minutes=10)).isoformat()}) + "\n")
    out = _run(monkeypatch, tmp_path, fake, NOW)
    assert out["decision_window"] == [10, 70] and out["matches_decided"] == 1
    # the next run comes two hours late: the window widens, so the 20:30 match (20 minutes out)
    # and the 22:00 match (110 minutes out) are both decided now instead of being missed
    out2 = _run(monkeypatch, tmp_path, fake, NOW + timedelta(hours=2, minutes=10))
    assert out2["minutes_since_last_run"] == 130.0 and out2["decision_window"] == [10, 180]
    assert out2["matches_decided"] == 2
    scans = pd.read_parquet(tmp_path / "paper" / "scans" / "2026-10-02.parquet").set_index("event_ticker")
    assert abs(scans.loc[soon, "minutes_to_start"] - 20) < 1e-6 and abs(scans.loc[LATER, "minutes_to_start"] - 110) < 1e-6


def test_closing_lines_backfilled_from_candles_when_runs_are_sparse(tmp_path, monkeypatch):
    open_ms = _setup(tmp_path)
    _run(monkeypatch, tmp_path, FakeKalshiHttp(open_markets=open_ms), NOW)
    start = int(datetime(2026, 10, 2, 18, 45, tzinfo=timezone.utc).timestamp())
    # 1-minute candles: Team 1 drifts from 0.45 to 0.55 by the start (Team 2 mirrors it)
    candles = {f"{EV}-T01": [(start - 600, 0.46, 0.48), (start - 60, 0.54, 0.56)],
               f"{EV}-T02": [(start - 600, 0.52, 0.54), (start - 60, 0.44, 0.46)]}
    # no run near the start; the next one is an hour after it
    out = _run(monkeypatch, tmp_path, FakeKalshiHttp(open_markets=open_ms[2:], candles=candles),
               NOW + timedelta(minutes=105))
    assert out["closes_backfilled"] == 1
    closes = pd.read_csv(tmp_path / "paper" / "closes.csv")
    row = closes.set_index("event_ticker").loc[EV]
    assert row["source"] == "candles" and abs(row["q_close"] - 0.55) < 1e-9
    books = report.book_stats(paper.State(tmp_path))
    assert abs(books["blend"]["avg_clv"] - (0.55 - 0.46)) < 1e-9
    # a later run does not fetch it again
    out2 = _run(monkeypatch, tmp_path, FakeKalshiHttp(open_markets=open_ms[2:], candles=candles),
                NOW + timedelta(minutes=120))
    assert out2["closes_backfilled"] == 0


def test_games_outside_the_trial_are_left_out_and_their_bets_voided(tmp_path, monkeypatch):
    from esalpha.history import read_table, write_table

    open_ms = _setup(tmp_path)
    # Kalshi lists a new KX<GAME>GAME series (e-soccer, Oct 8 2026): it reaches the history...
    hist = tmp_path / "history"
    m = read_table(hist, "matches")
    extra = m.tail(3).copy()
    extra["series_ticker"] = "KXESOCCERGAME"
    extra["game"] = "esoccergame"
    extra["event_ticker"] = ["KXESOCCERGAME-26OCT01" + str(i) for i in range(3)]
    write_table(hist, "matches", pd.concat([m, extra], ignore_index=True), "start_time")
    st = paper.State(tmp_path)
    assert "KXESOCCERGAME" not in st.match_series() and "KXCS2GAME" in st.match_series()
    assert not st.all_matches()["series_ticker"].eq("KXESOCCERGAME").any()

    # ...and bets placed on it before this fix are voided, with the stake given back
    fake = FakeKalshiHttp(open_markets=open_ms)
    _run(monkeypatch, tmp_path, fake, NOW)
    st = paper.State(tmp_path)
    cash0 = {b: st.account[b]["cash"] for b in paper.BOOKS}
    led = st.ledger
    base = led.iloc[0].to_dict()
    lost = {**base, "bet_id": "x1", "book": "favourite", "game": "esoccergame", "status": "lost",
            "cost": 9.7, "fee": 0.01, "pnl": -9.71, "result": "no", "settled_at": "2026-10-09T01:00:00+00:00"}
    won = {**base, "bet_id": "x2", "book": "blend", "game": "ebasketballgame", "status": "won",
           "cost": 4.0, "fee": 0.1, "pnl": 5.9, "result": "yes", "settled_at": "2026-10-09T02:00:00+00:00"}
    opened = {**base, "bet_id": "x3", "book": "model-only", "game": "mlbb", "status": "open",
              "cost": 3.0, "fee": 0.07, "pnl": None, "result": None, "settled_at": None}
    st.ledger = pd.concat([led, pd.DataFrame([lost, won, opened])], ignore_index=True)
    st.account["favourite"]["cash"] = cash0["favourite"] - 9.71       # what placing and settling did
    st.account["blend"]["cash"] = cash0["blend"] + 5.9
    st.account["model-only"]["cash"] = cash0["model-only"] - 3.07
    st.save()
    st = paper.State(tmp_path)
    assert paper.void_out_of_scope(st, NOW) == 3
    for b in paper.BOOKS:
        assert abs(st.account[b]["cash"] - cash0[b]) < 1e-6
    v = st.ledger[st.ledger["bet_id"].isin(["x1", "x2", "x3"])]
    assert set(v["status"]) == {"void"} and set(v["result"]) == {paper.VOID_NOTE} and (v["pnl"] == 0).all()
    assert paper.void_out_of_scope(st, NOW) == 0                      # idempotent
    st.save()
    books = report.book_stats(paper.State(tmp_path))
    assert books["favourite"]["bets"] == 1 and books["favourite"]["void"] == 1


def test_favourite_baseline_skips_empty_order_books():
    from esalpha.strategy import default_rules, flat_candidates

    rules = default_rules()
    a = {"ticker": "A", "yes_bid": 0.10, "yes_ask": 0.85, "bid_size": 5, "ask_size": 5}     # 75c spreads
    b = {"ticker": "B", "yes_bid": 0.15, "yes_ask": 0.90, "bid_size": 5, "ask_size": 5}
    assert flat_candidates("E", True, a, b, rules, max_spread=0.10) == []
    assert flat_candidates("E", True, a, b, rules)                    # the backtest's default keeps them
    a2, b2 = dict(a, yes_bid=0.60, yes_ask=0.62), dict(b, yes_bid=0.38, yes_ask=0.40)
    assert flat_candidates("E", True, a2, b2, rules, max_spread=0.10)
