# Esports betting model — notes for Claude

Two parts: the original scraped-stats app (`main.py`, `pipeline/`, `features/`, `models/`,
`betting/`, `backtest/`) and `esalpha/` (Kalshi esports match markets, walk-forward backtest,
fake-money paper trading on GitHub Actions). See README.md for results.

## Rules
- Paper trading only. esalpha reads Kalshi's public market data; never add order placement or
  use API keys without the user's explicit confirmation.
- Do not run or extend the HLTV (Cloudflare-evading browser) or PrizePicks (private app API)
  scrapers; their sites' terms restrict automated access.
- State (history, params, ledger, reports) lives on the `paper-trading` branch, written only
  by the workflows (`scripts/state_branch.sh`).
- GitHub starts this repo's scheduled runs only ~3 times a day, so `es-paper.yml` runs
  `esalpha paper-loop`: one job does a pass every 5 minutes for up to 5.5 hours and saves state
  as it goes; the next scheduled run waits in the concurrency queue and takes over.

## Kalshi esports facts (verified Oct 2026)
- Match-winner series are `KX<GAME>GAME`: KXCS2GAME, KXLOLGAME, KXVALORANTGAME, KXDOTA2GAME,
  KXR6GAME, KXOWGAME, KXCODGAME, KXRLGAME (older: KXCSGOGAME). `KXDOTA2GAME3WAY` has draws.
- One event per match, one market per team; team id in `custom_strike.esports_competitor`;
  scheduled start in the event ticker in Eastern time (`-26AUG091500...` = Aug 9 2026 3:00 PM ET);
  markets open ~2h before the start, trade in-play, close when a winner is declared;
  `expiration_value` is the winner's name; statuses come back as `finalized`.
- Titles changed in early August 2026 from "Will A win the A vs. B match?" to "A wins" (R6 still
  uses the old form). Detect matches by series + two-market structure, not by title alone.
- Markets settled before `GET /historical/cutoff` (`market_settled_ts`, 2026-08-05 when checked)
  are only in `/historical/markets`; later ones in `/markets?status=settled`.
- Prices are dollar strings: `yes_bid_dollars` on live endpoints, but the historical
  candlestick endpoint uses bare names (`"close": "0.9000"`). A decimal string is dollars.
- `/events?series_ticker=...` returned HTTP 400 for these series; use `/markets`.
- Taker fee `ceil(0.07 * C * P * (1 - P))` (all match series quadratic, multiplier 1).
- Side markets share the match code: `KX<G>MAP-<code>-<n>` (map n winner, one market per team) and
  `KX<G>TOTALMAPS-<code>` ("over N.5 maps" ladder: BO3 2.5; BO5 3.5 and 4.5). Map 1-3 markets are
  listed before the match, map 4+ only once the match gets there: never infer best-of from map
  markets (look-ahead); use the totals ladder.
- Polymarket esports: gamma `/events?series_id=` (cs2 10310, lol 10311, valorant 10369, dota2
  10309, r6 10432, cod 10427), moneyline markets, CLOB `/prices-history?market=<token>`.

## What the data says
- At 60 minutes before the start the market's log loss is ~0.573; the Elo model's ~0.662. The
  model + market blend is no better than the market, and bets lose after spread and fees.
  Closing-line value of every strategy tried was zero or negative. Treat any new "edge" with
  suspicion until it shows positive closing-line value out of sample.
- Also no edge (Oct 2026, `research/`): Polymarket's price (same accuracy as Kalshi, 1-2c apart,
  nothing left after costs); side markets (less accurate than the match price implies, but 5-10c
  spreads and almost no volume, so bets lose); favourites (good Sep-Oct, bad May-Aug, negative CLV).
- Time-of-day / game / weekday / timing / liquidity / tournament rules (Oct 2026,
  `research/time_of_day_rules.py`): no persistence beyond luck (27 of 432 rules made money in both
  periods vs ~21 by chance). Underdogs lose 6-20% everywhere; only LoL favourites at 90c+ made ~+3%
  in both periods (~185 bets in 5 months).
- The original app's training leaked future results (final Elo in training rows); fixed in Oct 2026.

## Commands
`python -m esalpha history|backtest|paper|report|sides|poly|probe [--kalshi-coverage] --state <dir>`;
`python research/poly_vs_kalshi.py|side_markets.py|time_of_day_rules.py --state <dir>`;
`python -m pytest -q` (tests/legacy covers the original app).
