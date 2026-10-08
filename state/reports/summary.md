# Esports paper trading (fake money)

Updated 2026-10-08 11:40 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 62 | 11 | 51 | 13 | -$15.06 | -2.1% | -0.6c (58) | $984.94 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 107 | 18 | 89 | 63 | -$60.17 | -8.7% | -0.6c (102) | $939.83 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

174 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5428 | 0.1813 |
| model | 0.6552 | 0.2312 |
| blend | 0.5403 | 0.1802 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 119 | 0.5644 | 0.6622 |
| lol | 24 | 0.3704 | 0.6283 |
| dota2 | 16 | 0.5946 | 0.6157 |
| r6 | 8 | 0.7369 | 0.7490 |
| ow | 4 | 0.2097 | 0.4720 |
| valorant | 3 | 0.7149 | 0.7980 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-08 11:20 | favourite | dota2 | Aurora | 1win | YES Aurora | 17 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-08 10:50 | favourite | valorant | Team Vitality | Nongshim RedForce | NO Nongshim RedForce | 17 | 0.54 | 0.54 | 0.53 | open | - |
| 2026-10-08 10:50 | model-only | valorant | Nongshim RedForce | Team Vitality | YES Nongshim RedForce | 33 | 0.47 | 0.52 | 0.47 | open | - |
| 2026-10-08 10:50 | favourite | dota2 | Team Synapse | Blasterbl | YES Team Synapse | 17 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-08 10:50 | model-only | dota2 | Team Synapse | Blasterbl | YES Team Synapse | 34 | 0.53 | 0.67 | 0.52 | open | - |
| 2026-10-08 10:50 | favourite | cs2 | Team Nemesis | Sinners | YES Team Nemesis | 17 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-08 10:50 | model-only | cs2 | Team Nemesis | Sinners | YES Team Nemesis | 34 | 0.53 | 0.63 | 0.53 | open | - |
| 2026-10-08 09:50 | favourite | cs2 | Nemiga | Lavked | YES Nemiga | 10 | 0.87 | 0.87 | 0.87 | open | - |
| 2026-10-08 09:50 | model-only | cs2 | Lavked | Nemiga | YES Lavked | 80 | 0.13 | 0.20 | 0.13 | open | - |
| 2026-10-08 09:50 | favourite | cs2 | Noir Verse | Azuolas | YES Noir Verse | 15 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-10-08 09:50 | model-only | cs2 | ENJOY | 6666 | YES ENJOY | 38 | 0.48 | 0.54 | 0.48 | open | - |
| 2026-10-08 09:50 | favourite | cs2 | 6666 | ENJOY | YES 6666 | 17 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-10-08 09:20 | favourite | cs2 | Passion Academy | TheChampionGG | YES Passion Academy | 14 | 0.63 | 0.58 | 0.58 | open | - |
| 2026-10-08 09:20 | favourite | cs2 | MOUZ NXT | RoundsGG | YES MOUZ NXT | 11 | 0.83 | 0.81 | 0.81 | open | - |
| 2026-10-08 09:20 | model-only | cs2 | RoundsGG | MOUZ NXT | NO MOUZ NXT | 90 | 0.20 | 0.40 | 0.19 | open | - |
| 2026-10-08 08:50 | favourite | cs2 | Sangal | OG | NO OG | 16 | 0.57 | 0.58 | 0.58 | open | - |
| 2026-10-08 08:50 | favourite | cs2 | Rebels Gaming | G2 Ares | YES Rebels Gaming | 1 | 0.72 | 0.58 | 0.58 | open | - |
| 2026-10-08 07:50 | model-only | lol | Natus Vincere | JD Gaming | NO JD Gaming | 30 | 0.29 | 0.52 | 0.29 | open | - |
| 2026-10-08 07:50 | model-only | dota2 | LGD Gaming | Team Yandex | YES LGD Gaming | 139 | 0.13 | 0.35 | 0.12 | open | - |
| 2026-10-08 07:50 | favourite | dota2 | Team Yandex | LGD Gaming | YES Team Yandex | 10 | 0.87 | 0.88 | 0.88 | open | - |
| 2026-10-08 07:50 | favourite | cs2 | GamerLegion | 33 | NO 33 | 13 | 0.69 | 0.66 | 0.66 | won | $3.83 |
| 2026-10-08 07:50 | favourite | lol | JD Gaming | Natus Vincere | YES JD Gaming | 12 | 0.73 | 0.71 | 0.71 | open | - |
| 2026-10-08 07:50 | favourite | valorant | 100 Thieves | G2 Esports | YES 100 Thieves | 14 | 0.66 | 0.66 | 0.66 | lost | -$9.46 |
| 2026-10-08 06:50 | favourite | cs2 | EAC Extra | THE UNIT | YES EAC Extra | 12 | 0.76 | 0.75 | 0.75 | lost | -$9.28 |
| 2026-10-08 06:50 | model-only | cs2 | THE UNIT | EAC Extra | YES THE UNIT | 72 | 0.25 | 0.44 | 0.25 | won | $53.05 |

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

