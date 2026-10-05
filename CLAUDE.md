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

## What the data says
- At 60 minutes before the start the market's log loss is ~0.573; the Elo model's ~0.662. The
  model + market blend is no better than the market, and bets lose after spread and fees.
  Closing-line value of every strategy tried was zero or negative. Treat any new "edge" with
  suspicion until it shows positive closing-line value out of sample.
- The original app's training leaked future results (final Elo in training rows); fixed in Oct 2026.

## Commands
`python -m esalpha history|backtest|paper|report|probe [--kalshi-coverage] --state <dir>`;
`python -m pytest -q` (tests/legacy covers the original app).
