# Esports paper trading (fake money)

Updated 2026-11-09 13:06 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 629 | 60 | 569 | 202 | -$185.92 | -2.9% | -0.2c (621) | $814.08 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1013 | 89 | 924 | 610 | -$455.43 | -7.7% | -1.6c (1002) | $544.57 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2094 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5848 | 0.2013 |
| model | 0.6515 | 0.2301 |
| blend | 0.5850 | 0.2016 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1335 | 0.5940 | 0.6582 |
| dota2 | 344 | 0.5583 | 0.6392 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 102 | 0.6397 | 0.6752 |
| lol | 95 | 0.5646 | 0.7154 |
| r6 | 77 | 0.5815 | 0.6664 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-09 12:51 | favourite | cs2 | FOKUS | Alliance | NO Alliance | 9 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-11-09 12:51 | model-only | cs2 | FOKUS | Alliance | NO Alliance | 29 | 0.53 | 0.71 | 0.53 | open | - |
| 2026-11-09 12:51 | favourite | cs2 | 9INE | aimclub | YES 9INE | 7 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-11-09 11:51 | favourite | dota2 | Nemiga Gaming | Zenith | YES Nemiga Gaming | 6 | 0.85 | 0.85 | 0.85 | open | - |
| 2026-11-09 11:51 | favourite | dota2 | Xipto Esports | Team Synapse | NO Team Synapse | 8 | 0.61 | 0.60 | 0.60 | open | - |
| 2026-11-09 11:51 | model-only | dota2 | Team Synapse | Xipto Esports | YES Team Synapse | 37 | 0.42 | 0.57 | 0.40 | open | - |
| 2026-11-09 11:51 | favourite | dota2 | Team Lynx | potn9ki | YES Team Lynx | 7 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-11-09 11:51 | model-only | dota2 | potn9ki | Team Lynx | NO Team Lynx | 11 | 0.29 | 0.37 | 0.28 | open | - |
| 2026-11-09 11:51 | favourite | dota2 | Froglings | PlayTime | YES Froglings | 10 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-11-09 11:51 | model-only | dota2 | Froglings | PlayTime | YES Froglings | 30 | 0.51 | 0.58 | 0.51 | open | - |
| 2026-11-09 10:50 | favourite | cs2 | BakS eSports | Leo Team | YES BakS eSports | 8 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-09 10:50 | model-only | cs2 | Leo Team | BakS eSports | NO BakS eSports | 41 | 0.38 | 0.45 | 0.38 | open | - |
| 2026-11-09 10:50 | favourite | cs2 | MASONIC | maybe | YES MASONIC | 9 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-11-09 10:20 | favourite | cs2 | ex-ENCE | Balkan Outlaws | NO Balkan Outlaws | 9 | 0.55 | 0.55 | 0.54 | open | - |
| 2026-11-09 10:20 | model-only | cs2 | Balkan Outlaws | ex-ENCE | YES Balkan Outlaws | 34 | 0.46 | 0.53 | 0.46 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Zero Tenacity | Spirit Academy | NO Spirit Academy | 7 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Spirit Academy | Zero Tenacity | YES Spirit Academy | 31 | 0.36 | 0.41 | 0.34 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Yellow Submarine | Xipto Esports | YES Yellow Submarine | 8 | 0.62 | 0.62 | 0.62 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Xipto Esports | Yellow Submarine | YES Xipto Esports | 25 | 0.38 | 0.49 | 0.38 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Froglings | Team Synapse | YES Froglings | 7 | 0.72 | 0.70 | 0.70 | won | $1.86 |
| 2026-11-09 08:50 | favourite | dota2 | Power Rangers | Nemiga Gaming | NO Nemiga Gaming | 3 | 0.74 | 0.73 | 0.73 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Nemiga Gaming | Power Rangers | NO Power Rangers | 57 | 0.27 | 0.48 | 0.27 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | HULIGANI | Xipto Esports | YES HULIGANI | 9 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Xipto Esports | HULIGANI | NO HULIGANI | 36 | 0.43 | 0.65 | 0.42 | open | - |
| 2026-11-09 07:50 | favourite | cs2 | Walczaki | Noir Verse | YES Walczaki | 9 | 0.59 | 0.59 | 0.59 | lost | -$5.47 |

## Backtest on real Kalshi prices

9155 settled matches from 2026-05-28 to 2026-11-02, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2020 | $9,242.02 | -$992.02 | -10.7% | -18.4% to -3.0% | 33% | -0.7c | 99% |
| always the favourite (1% flat) | 4414 | $17,347.39 | -$838.39 | -4.8% | -7.1% to -2.7% | 67% | -1.7c | 84% |
| always the underdog (1% flat) | 3784 | $8,995.47 | -$985.47 | -11.0% | -16.5% to -4.9% | 31% | -1.3c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8930 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5749 | 0.1968 | 68.9% |
| model | 0.6599 | 0.2340 | 59.6% |
| blend | 0.5747 | 0.1968 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1475 | 0.525 | 0.525 |
| (0.55, 0.6] | 1510 | 0.577 | 0.547 |
| (0.6, 0.65] | 1371 | 0.626 | 0.628 |
| (0.65, 0.7] | 1202 | 0.676 | 0.700 |
| (0.7, 0.75] | 1004 | 0.726 | 0.770 |
| (0.75, 0.8] | 855 | 0.776 | 0.807 |
| (0.8, 0.85] | 729 | 0.826 | 0.823 |
| (0.85, 0.9] | 536 | 0.877 | 0.903 |
| (0.9, 1.0] | 473 | 0.932 | 0.958 |

