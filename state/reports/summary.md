# Esports paper trading (fake money)

Updated 2026-10-11 16:58 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 125 | 11 | 114 | 31 | -$123.14 | -8.6% | -0.7c (122) | $876.86 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 210 | 11 | 199 | 128 | -$186.35 | -12.4% | -2.0c (209) | $813.65 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1851 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6637 | 0.2367 |
| model | 0.6722 | 0.2399 |
| blend | 0.6657 | 0.2376 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 1146 | 0.6910 | 0.6744 |
| cs2 | 295 | 0.5926 | 0.6676 |
| ebasketballgame | 263 | 0.6845 | 0.6754 |
| lol | 37 | 0.5009 | 0.6991 |
| dota2 | 34 | 0.5809 | 0.6527 |
| ow | 23 | 0.4259 | 0.5014 |
| r6 | 22 | 0.6444 | 0.7203 |
| mlbb | 18 | 0.6203 | 0.7106 |
| valorant | 13 | 0.6397 | 0.6656 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-11 15:53 | model-only | cs2 | antidaun | Saint Sinners | YES antidaun | 8 | 0.19 | 0.43 | 0.18 | open | - |
| 2026-10-11 14:52 | model-only | r6 | Fluxo W7M | Team Liquid | YES Fluxo W7M | 45 | 0.36 | 0.44 | 0.35 | open | - |
| 2026-10-11 13:52 | model-only | cs2 | MOUZ | Vitality | YES MOUZ | 42 | 0.35 | 0.44 | 0.34 | open | - |
| 2026-10-11 12:52 | model-only | cs2 | aimclub | ARGOS | YES aimclub | 30 | 0.47 | 0.54 | 0.47 | won | $15.37 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy Black | Metizport | NO Metizport | 9 | 0.20 | 0.36 | 0.18 | lost | -$1.91 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy | 9INE | YES Spirit Academy | 34 | 0.41 | 0.65 | 0.41 | won | $19.48 |
| 2026-10-11 12:52 | model-only | cs2 | mellren | Bebop | YES mellren | 23 | 0.62 | 0.71 | 0.61 | won | $8.36 |
| 2026-10-11 12:52 | model-only | cs2 | MASONIC | Aurora Young Blood | NO Aurora Young Blood | 33 | 0.43 | 0.55 | 0.42 | lost | -$14.76 |
| 2026-10-11 11:52 | model-only | cs2 | The KnockoutX | Alter Ego | YES The KnockoutX | 22 | 0.24 | 0.40 | 0.23 | lost | -$5.57 |
| 2026-10-11 10:22 | favourite | cs2 | Spirit | Aurora Gaming | NO Aurora Gaming | 1 | 0.68 | 0.68 | 0.68 | lost | -$0.70 |
| 2026-10-11 09:52 | model-only | cs2 | Fire Flux Esports | Gothic | NO Gothic | 27 | 0.53 | 0.60 | 0.52 | won | $12.21 |
| 2026-10-11 09:47 | favourite | esoccergame | RB Leipzig (Kylian) | Mönchengladbach (Bradley) | YES RB Leipzig (Kylian) | 2 | 0.63 | 0.66 | 0.66 | won | $0.70 |
| 2026-10-11 09:21 | favourite | esoccergame | Mönchengladbach (Bradley) | Stuttgart (Frost) | YES Mönchengladbach (Bradley) | 8 | 0.52 | 0.56 | 0.56 | lost | -$4.30 |
| 2026-10-11 09:21 | model-only | cs2 | TheChampionGG | VP.Future 3 | YES TheChampionGG | 37 | 0.39 | 0.45 | 0.39 | lost | -$15.05 |
| 2026-10-11 09:21 | favourite | cs2 | Teletubisie | THE UNIT | YES Teletubisie | 9 | 0.88 | 0.87 | 0.87 | lost | -$7.99 |
| 2026-10-11 09:21 | model-only | cs2 | THE UNIT | Teletubisie | NO Teletubisie | 102 | 0.14 | 0.25 | 0.13 | won | $86.86 |
| 2026-10-11 09:21 | favourite | esoccergame | RB Leipzig (Kylian) | Freiburg (Kevin) | YES RB Leipzig (Kylian) | 15 | 0.55 | 0.59 | 0.59 | lost | -$8.51 |
| 2026-10-11 09:06 | favourite | esoccergame | Freiburg (Kevin) | Mönchengladbach (Bradley) | YES Freiburg (Kevin) | 15 | 0.53 | 0.56 | 0.56 | lost | -$8.22 |
| 2026-10-11 08:51 | favourite | mlbb | ONIC | RRQ Hoshi | YES ONIC | 10 | 0.84 | 0.65 | 0.65 | won | $1.50 |
| 2026-10-11 07:51 | favourite | cs2 | Rooster | Orgless | NO Orgless | 11 | 0.77 | 0.62 | 0.62 | open | - |
| 2026-10-11 07:51 | model-only | valorant | T1 | G2 Esports | NO G2 Esports | 38 | 0.39 | 0.47 | 0.39 | lost | -$15.46 |
| 2026-10-11 07:51 | favourite | ow | HUNENG | SHENGSHI Esports | YES HUNENG | 10 | 0.82 | 0.70 | 0.70 | won | $1.69 |
| 2026-10-11 07:51 | favourite | mlbb | Invictus Gaming | AC Esports | YES Invictus Gaming | 10 | 0.84 | 0.63 | 0.63 | lost | -$8.50 |
| 2026-10-11 07:51 | favourite | lol | Saigon Warriors | MVK Academy | NO MVK Academy | 10 | 0.80 | 0.79 | 0.79 | lost | -$8.12 |
| 2026-10-11 07:51 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 12 | 0.70 | 0.69 | 0.69 | lost | -$8.58 |

## Backtest on real Kalshi prices

7529 settled matches from 2026-05-28 to 2026-10-05, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 1878 | $9,311.87 | -$978.87 | -10.5% | -19.1% to -2.2% | 34% | -0.6c | 98% |
| always the favourite (1% flat) | 3613 | $15,734.92 | -$707.92 | -4.5% | -6.9% to -2.0% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3616 | $8,324.33 | -$978.33 | -11.8% | -17.4% to -5.9% | 32% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7304 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5732 | 0.1960 | 69.2% |
| model | 0.6611 | 0.2345 | 59.4% |
| blend | 0.5729 | 0.1959 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1200 | 0.525 | 0.521 |
| (0.55, 0.6] | 1249 | 0.577 | 0.553 |
| (0.6, 0.65] | 1130 | 0.626 | 0.634 |
| (0.65, 0.7] | 988 | 0.676 | 0.701 |
| (0.7, 0.75] | 838 | 0.726 | 0.773 |
| (0.75, 0.8] | 706 | 0.776 | 0.809 |
| (0.8, 0.85] | 594 | 0.826 | 0.825 |
| (0.85, 0.9] | 443 | 0.877 | 0.905 |
| (0.9, 1.0] | 381 | 0.932 | 0.958 |

