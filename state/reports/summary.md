# Esports paper trading (fake money)

Updated 2026-10-08 07:50 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 56 | 8 | 48 | 12 | -$39.86 | -6.0% | -0.5c (53) | $960.14 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 96 | 12 | 84 | 61 | -$36.61 | -5.6% | -0.5c (91) | $963.39 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

168 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5434 | 0.1811 |
| model | 0.6498 | 0.2287 |
| blend | 0.5412 | 0.1801 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 115 | 0.5666 | 0.6594 |
| lol | 23 | 0.3830 | 0.6273 |
| dota2 | 16 | 0.5946 | 0.6157 |
| r6 | 8 | 0.7369 | 0.7490 |
| ow | 4 | 0.2097 | 0.4720 |
| valorant | 2 | 0.5402 | 0.5937 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-08 07:50 | favourite | valorant | 100 Thieves | G2 Esports | YES 100 Thieves | 14 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-10-08 07:50 | favourite | lol | JD Gaming | Natus Vincere | YES JD Gaming | 12 | 0.73 | 0.71 | 0.71 | open | - |
| 2026-10-08 07:50 | model-only | lol | Natus Vincere | JD Gaming | NO JD Gaming | 30 | 0.29 | 0.52 | 0.29 | open | - |
| 2026-10-08 07:50 | favourite | dota2 | Team Yandex | LGD Gaming | YES Team Yandex | 10 | 0.87 | 0.88 | 0.88 | open | - |
| 2026-10-08 07:50 | model-only | dota2 | LGD Gaming | Team Yandex | YES LGD Gaming | 139 | 0.13 | 0.35 | 0.12 | open | - |
| 2026-10-08 07:50 | favourite | cs2 | GamerLegion | 33 | NO 33 | 13 | 0.69 | 0.66 | 0.66 | open | - |
| 2026-10-08 06:50 | model-only | cs2 | SINQU Rehti | Sokerorg | YES SINQU Rehti | 100 | 0.18 | 0.37 | 0.17 | open | - |
| 2026-10-08 06:50 | favourite | cs2 | ex-Zero Tenacity | Acend | NO Acend | 15 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-08 06:50 | model-only | cs2 | Fortress | Lavked | YES Fortress | 180 | 0.10 | 0.31 | 0.09 | open | - |
| 2026-10-08 06:50 | favourite | cs2 | ILLYRIANS | los kogutos | YES ILLYRIANS | 1 | 0.52 | 0.54 | 0.54 | open | - |
| 2026-10-08 06:50 | model-only | cs2 | ex-Zero Tenacity | Acend | NO Acend | 15 | 0.59 | 0.66 | 0.58 | open | - |
| 2026-10-08 06:50 | favourite | cs2 | Sokerorg | SINQU Rehti | NO SINQU Rehti | 11 | 0.85 | 0.83 | 0.83 | open | - |
| 2026-10-08 06:50 | favourite | cs2 | EAC Extra | THE UNIT | YES EAC Extra | 12 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-10-08 06:50 | model-only | cs2 | THE UNIT | EAC Extra | YES THE UNIT | 72 | 0.25 | 0.44 | 0.25 | open | - |
| 2026-10-08 01:54 | favourite | dota2 | Direborn | InterActive Philippines | YES Direborn | 17 | 0.55 | 0.54 | 0.54 | lost | -$9.65 |
| 2026-10-07 12:51 | favourite | cs2 | megoshort | Azuolas | YES megoshort | 4 | 0.57 | 0.53 | 0.53 | won | $1.65 |
| 2026-10-07 12:21 | favourite | cs2 | Vitality Academy | Royal Foxes Esports | NO Royal Foxes Esports | 3 | 0.78 | 0.77 | 0.77 | won | $0.62 |
| 2026-10-07 10:51 | favourite | cs2 | Acend | Sashi Esport | YES Acend | 7 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-07 10:51 | favourite | cs2 | Spirit | M80 | YES Spirit | 11 | 0.86 | 0.86 | 0.86 | won | $1.44 |
| 2026-10-07 08:46 | model-only | cs2 | Falcons Force | OG | YES Falcons Force | 66 | 0.29 | 0.43 | 0.28 | won | $45.90 |
| 2026-10-07 08:46 | model-only | cs2 | SINQU | G2 Ares | NO G2 Ares | 79 | 0.24 | 0.39 | 0.23 | lost | -$19.97 |
| 2026-10-07 08:46 | favourite | cs2 | PURE | Orion Wanderers | NO Orion Wanderers | 10 | 0.86 | 0.85 | 0.85 | won | $1.31 |
| 2026-10-07 08:46 | favourite | cs2 | OG | Falcons Force | NO Falcons Force | 12 | 0.73 | 0.72 | 0.72 | lost | -$8.93 |
| 2026-10-07 08:46 | model-only | cs2 | Falcons Force | G2 Ares | YES Falcons Force | 34 | 0.46 | 0.51 | 0.45 | lost | -$16.24 |
| 2026-10-07 08:46 | favourite | cs2 | Copenhagen Wolves | Bread Eaters Esports | NO Bread Eaters Esports | 11 | 0.81 | 0.80 | 0.80 | won | $1.97 |

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

