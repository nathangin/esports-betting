# Esports betting model

Two parts live in this repo:

* **`esalpha/`** (new, Oct 2026): a model for **Kalshi esports match markets** (CS2, League of
  Legends, Valorant, Dota 2, Call of Duty, ...), an honest walk-forward backtest on real Kalshi
  prices, and **fake-money paper trading** that runs by itself on GitHub Actions. It reads
  Kalshi's public market data only: no API key, no orders, no scraping.
* **The original app** (`main.py`, `pipeline/`, `features/`, `models/`, `betting/`, `backtest/`):
  CS2/LoL/Valorant win and player-prop models built from scraped match stats. Several bugs that
  leaked future results into training and testing are now fixed (list below).

> Nothing here is betting advice. All money in this repo is fake.

## Results

**Short version: Kalshi's esports prices are better forecasts than this model, and no strategy
tried here beat them after the bid/ask spread and fees.** The paper trader keeps testing that
live, with fake money.

### Backtest on real Kalshi prices

7,469 settled matches from May 28 to Oct 4 2026 (CS2 3,820, LoL 1,455, Valorant 769, Dota 2 652,
R6 413, Overwatch 216, CoD 88, Rocket League 56). Ratings use all 13,898 Kalshi matches since
Nov 2025.
Every decision is made 60 minutes before the scheduled start at the quoted bid/ask, pays Kalshi's
taker fee and settles on Kalshi's result; ratings, the win model and the blend only ever see
earlier matches (weekly walk-forward refits). Each strategy starts with $1,000.

| Strategy | Bets | ROI | 95% range | Closing-line value | $1,000 became |
|---|---:|---:|---|---:|---:|
| model + market blend | 24 | -0.4% | -35% to +46% | +0.0c | $998 |
| Elo model alone | 1,864 | -10.7% | -19% to -3% | -0.8c | $21 |
| always the favourite (1% flat) | 3,572 | -4.8% | -7.4% to -2.4% | -1.6c | $263 |
| always the underdog (1% flat) | 3,602 | -11.3% | -17% to -5% | -1.3c | $21 |

Forecast quality on the same matches (log loss, lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| Kalshi price 60 min before | **0.573** | 0.196 | 69.1% |
| Elo win model | 0.662 | 0.235 | 59.3% |
| model + market blend | **0.573** | 0.196 | |

What this means:

* **The market is far ahead of a results-only model**, in every game (CS2 0.591 vs 0.674,
  LoL 0.547 vs 0.643, Valorant 0.612 vs 0.696, Dota 2 0.548 vs 0.656). It knows rosters,
  stand-ins, map pools and form that match results alone do not show.
* **The fitted blend puts all its weight on the market** (weights -0.06 on the model, 1.13 on the
  market), so it almost never finds a bet: 24 in four months, too few to say anything.
* **Closing-line value is zero or negative for every strategy**: on average the bets were placed
  at prices no better than where the market stood at the start. That is the signature of no
  information edge.
* **The favourite-longshot pattern is real but not bettable as a taker**: at mid prices,
  favourites at 70-80c won about 4 points more often than priced, but the price you can actually
  buy at averaged 2.5c above that mid and the fee adds about 1.3c, so backing favourites at the
  ask still lost about 2% at 60, 30 and 10 minutes before the start.
* Also tried and rejected (no out-of-sample gain over the market): team ratings learned from
  earlier matches' closing prices, recalibrating the market price, deciding 120/30/10 minutes
  before the start, stricter edge thresholds.

The same lesson as the Kalshi weather project: only trust an edge that survives a walk-forward
test against the market's own price, and judge live results by closing-line value before P&L.

### Paper trading

Running on GitHub Actions every 15 minutes from Oct 4 2026 (new bets stop after Nov 15). The
live report, with every bet, is
[`state/reports/summary.md`](../../blob/paper-trading/state/reports/summary.md) on the
`paper-trading` branch.

### The original app

Its reported accuracy was inflated by look-ahead: every training row carried the teams' final
Elo ratings, which already include that match's result, and the "out-of-sample" backtest
reused models trained on the test period. The fixes are listed below; with them the app's
numbers can be trusted, but there are still no real prices in its database to say whether
its edges would have paid.

## How esalpha works

**Market.** Each Kalshi esports match is an event with one market per team in a
`KX<GAME>GAME` series ("Will OpTic Gaming win the OpTic Gaming vs. Team Heretics match?", or
since August 2026 just "OpTic Gaming wins"). A team is identified by a stable
competitor id (`custom_strike.esports_competitor`), the scheduled start is encoded in the event
ticker in Eastern time (`KXCODGAME-26AUG091500OGHTCS` = Aug 9 2026, 3:00 PM ET), markets open
about two hours before the start, keep trading during the match and close as soon as a
winner is declared. The winner's name is in `expiration_value`.

**Model.**
1. Per-game Elo on every settled Kalshi match, keyed by competitor id, with faster updates
   for teams with few games and a slow drift back to the mean for idle teams. K is tuned per
   game on matches *before* the backtest period. Every match only sees ratings from
   earlier matches.
2. A logistic win model on the Elo probability, its reliability (fewer games, less trust) and
   recent form (results versus expectation), refitted weekly on earlier results.
3. A **model + market blend**: a logistic regression of the result on the model's and the
   market's log-odds, refitted weekly on earlier priced matches. This is the probability the
   strategy bets on. The market is usually the better forecaster, so the blend leans on it
   and only moves away where the model has historically added information.

**Bets.** Backing team A can be done by buying YES on A or NO on B; the cheaper route is used.
A bet needs at least 3c of expected profit per contract after Kalshi's taker fee
(`ceil(0.07 * C * P * (1 - P))`) and 5% expected return, is skipped if the bid/ask spread is over
6c or the price is outside 10-90c, and is sized at quarter Kelly with a 2% cap per match and
25% of the bankroll per day. Matches where model and market disagree by more than 25 points
are skipped: that is usually news (a stand-in, a roster change) the model has not seen.

**Backtest.** Decisions are made 60 minutes before the scheduled start, at the last 1-minute
bid/ask before that moment, and settle on Kalshi's recorded result. Nothing in a decision uses
information from after it.

**Paper trading.** `.github/workflows/es-paper.yml` runs every 15 minutes: it settles finished
bets, adds new results to the ratings, and decides once on every match that starts in the next
10-70 minutes, in three fake $1,000 books:

| Book | What it does |
|---|---|
| `blend` | the strategy under test (model + market blend) |
| `model-only` | the Elo win model alone, to show what ignoring the market does |
| `favourite` | 1% flat on the market favourite, a no-skill baseline |

Fills are at the displayed ask (or 1 - bid for NO), capped at the size shown at that price.
State (ledger, every scanned match, fitted parameters, reports) lives on the
[`paper-trading`](../../tree/paper-trading) branch; the running report is
[`state/reports/summary.md`](../../blob/paper-trading/state/reports/summary.md). New bets stop
on the date in `PAPER_UNTIL` (es-paper.yml); open bets keep settling after that.

`.github/workflows/es-data.yml` refreshes the match history and price candles daily and reruns
the backtest (which also refits the parameters the paper trader uses) every Monday.

## Commands

```bash
pip install -e ".[dev]"
python -m esalpha history  --state state          # settled matches + 1-minute pre-match candles
python -m esalpha backtest --state state          # walk-forward backtest, writes params/fitted.json
python -m esalpha paper    --state state          # one paper-trading pass
python -m esalpha report   --state state          # state/reports/summary.md
python -m esalpha probe                           # check the data sources, save raw samples
python -m pytest -q
```

## Fixes to the original app

| Where | Problem | Fix |
|---|---|---|
| `features/rolling_stats.build_training_dataset` | every training row got the teams' **final** Elo, which already contains that match and all later ones; the model looked much better in training than it can be live | Elo is replayed in time order; each row sees ratings from before the match |
| `pipeline/*._build_props_*` | opponent Elo (and, for CS2, opponent win rate) came from the whole period | pre-match values from a time-ordered replay |
| `models/win_model.WinModel.fit` | Platt scaling fitted on the model's own training predictions (in-sample), so probabilities stayed overconfident | fitted on out-of-fold, time-ordered predictions; missing features use training medians instead of 0.5 |
| `models/props_model.PropsModel.fit` | over/under spread learned from in-sample residuals (too small), and a mean absolute error used as a standard deviation | out-of-fold residuals, scaled by sqrt(pi/2) |
| `betting/edge.fractional_kelly` | capped at 25% of bankroll per bet | quarter Kelly with a separate 2% per-bet cap (`MAX_STAKE_FRACTION`) |
| `betting/edge.SlateAnalyzer` | edge report passed a numeric team id as the team name (crash), an empty name matched every line, and `"o" in description` priced most unders as overs | lines are matched by team name, ambiguous lines are skipped, over/under parsed explicitly, two-way vig removal when both sides are known |
| `backtest/backtest.py` | Elo built from all matches including the test window, saved models trained on the test window, P&L assumed every favourite was available at -110, hard-coded AUC 0.6937 | fresh models trained before the cutoff, measured log loss/Brier/AUC, no fictional P&L |
| `backtest/proper_backtest.py` | leaky training features, hard-coded "CV AUC 0.694", P&L at -110 | same fixes |
| props backtests | lines are synthetic (the player's own average) | labelled as such; accuracy against them is not evidence of an edge |

Tests for these fixes are in `tests/legacy/`.

**A caution about the scrapers.** `scrapers/hltv.py` drives a browser to get past HLTV's
Cloudflare protection and `backtest/prizepicks.py` calls PrizePicks' private app API with a
browser user agent. Both sites' terms restrict automated access, so check them before running
these. esalpha does not use either.

## Original app usage

```bash
pip install -r requirements.txt
python main.py cs2 run          # scrape + train + predict
python main.py cs2 train        # train only
python main.py cs2 predict      # predict upcoming matches
python main.py cs2 edge --lines lines.json
python main.py lol run
python main.py valorant run
python backtest/proper_backtest.py
```
