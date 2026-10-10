# Esports paper trading (fake money)

Updated 2026-10-10 20:24 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 107 | 8 | 99 | 24 | -$224.80 | -17.8% | -0.5c (101) | $775.20 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 180 | 10 | 170 | 113 | -$145.02 | -11.2% | -1.1c (179) | $854.98 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1361 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6582 | 0.2342 |
| model | 0.6718 | 0.2395 |
| blend | 0.6599 | 0.2351 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 800 | 0.6931 | 0.6756 |
| cs2 | 263 | 0.5820 | 0.6634 |
| ebasketballgame | 183 | 0.6812 | 0.6808 |
| lol | 33 | 0.4582 | 0.6665 |
| dota2 | 31 | 0.5553 | 0.6402 |
| r6 | 21 | 0.6634 | 0.7190 |
| ow | 13 | 0.4669 | 0.4833 |
| valorant | 12 | 0.6525 | 0.6684 |
| mlbb | 5 | 0.6931 | 0.6964 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-10 19:09 | model-only | cs2 | Wildcard | NRG | NO NRG | 4 | 0.41 | 0.58 | 0.38 | open | - |
| 2026-10-10 15:53 | favourite | cs2 | Spirit | MOUZ | NO MOUZ | 1 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-10 12:38 | model-only | cs2 | Aurora Gaming | Vitality | YES Aurora Gaming | 21 | 0.24 | 0.39 | 0.23 | lost | -$5.31 |
| 2026-10-10 11:53 | model-only | cs2 | PRIVATE | GamerLegion | YES PRIVATE | 19 | 0.32 | 0.51 | 0.32 | won | $12.63 |
| 2026-10-10 11:53 | model-only | cs2 | Just Swing | Kaleido | YES Just Swing | 31 | 0.46 | 0.60 | 0.43 | won | $16.20 |
| 2026-10-10 11:53 | favourite | cs2 | Iberian Soul | Nemiga | NO Nemiga | 3 | 0.81 | 0.81 | 0.81 | won | $0.53 |
| 2026-10-10 10:52 | model-only | valorant | NRG | LOUD | YES NRG | 12 | 0.51 | 0.60 | 0.52 | lost | -$6.33 |
| 2026-10-10 10:52 | model-only | cs2 | LPH Gaming | UNiTY esports | YES LPH Gaming | 43 | 0.24 | 0.33 | 0.23 | lost | -$10.87 |
| 2026-10-10 09:52 | model-only | ow | JD Gaming | Weibo Gaming | YES JD Gaming | 37 | 0.21 | 0.31 | 0.20 | lost | -$8.20 |
| 2026-10-10 09:52 | model-only | cs2 | Saint Sinners | WBT Academy | YES Saint Sinners | 36 | 0.42 | 0.51 | 0.42 | won | $20.26 |
| 2026-10-10 09:47 | favourite | esoccergame | RB Leipzig (Kylian) | Mönchengladbach (Bradley) | YES RB Leipzig (Kylian) | 1 | 0.57 | 0.61 | 0.61 | lost | -$0.59 |
| 2026-10-10 09:22 | model-only | dota2 | Team Spirit | Team Yandex | NO Team Yandex | 39 | 0.38 | 0.47 | 0.38 | lost | -$15.47 |
| 2026-10-10 09:22 | model-only | cs2 | VP.Future 3 | EAC Extra | YES VP.Future 3 | 1 | 0.36 | 0.55 | 0.34 | lost | -$0.38 |
| 2026-10-10 08:52 | favourite | cs2 | FaZe | NAVI Junior | YES FaZe | 9 | 0.89 | 0.89 | 0.89 | won | $0.92 |
| 2026-10-10 08:52 | model-only | cs2 | HOTU | fnatic | YES HOTU | 31 | 0.48 | 0.57 | 0.48 | lost | -$15.43 |
| 2026-10-10 08:52 | favourite | cs2 | fnatic | HOTU | YES fnatic | 15 | 0.52 | 0.52 | 0.52 | won | $6.93 |
| 2026-10-10 08:52 | favourite | cs2 | Black Phoenix | Nexus | YES Black Phoenix | 5 | 0.53 | 0.54 | 0.54 | won | $2.26 |
| 2026-10-10 08:52 | model-only | cs2 | Black Phoenix | Nexus | YES Black Phoenix | 28 | 0.53 | 0.61 | 0.54 | won | $12.67 |
| 2026-10-10 08:52 | model-only | cs2 | PURE | Sangal | NO Sangal | 1 | 0.35 | 0.43 | 0.34 | lost | -$0.37 |
| 2026-10-10 08:22 | favourite | cs2 | KZG | BGNS Orange | YES KZG | 1 | 0.75 | 0.75 | 0.75 | won | $0.23 |
| 2026-10-10 07:52 | favourite | ow | Solus Victorem | HUNENG | YES Solus Victorem | 10 | 0.78 | 0.71 | 0.71 | won | $2.07 |
| 2026-10-10 07:52 | favourite | cs2 | Vitality Academy | Dynamo Eclot Phoenix | NO Dynamo Eclot Phoenix | 10 | 0.76 | 0.75 | 0.75 | won | $2.27 |
| 2026-10-10 07:52 | model-only | cs2 | Dynamo Eclot Phoenix | Vitality Academy | NO Vitality Academy | 1 | 0.26 | 0.42 | 0.25 | lost | -$0.28 |
| 2026-10-10 07:52 | favourite | cs2 | MARKandLARRY | Orgless | YES MARKandLARRY | 14 | 0.55 | 0.54 | 0.54 | won | $6.05 |
| 2026-10-10 07:52 | model-only | cs2 | Orgless | MARKandLARRY | YES Orgless | 32 | 0.48 | 0.58 | 0.46 | lost | -$15.92 |

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

