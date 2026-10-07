# Esports paper trading (fake money)

Updated 2026-10-07 09:41 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 50 | 14 | 36 | 10 | $15.10 | +3.2% | -1.4c (45) | $1,015.10 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 83 | 24 | 59 | 40 | -$60.12 | -13.1% | -0.6c (71) | $939.88 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

71 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5462 | 0.1820 |
| model | 0.6421 | 0.2247 |
| blend | 0.5460 | 0.1814 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 34 | 0.6396 | 0.6703 |
| lol | 16 | 0.3318 | 0.6367 |
| dota2 | 9 | 0.5545 | 0.5259 |
| r6 | 8 | 0.7369 | 0.7490 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-07 08:46 | favourite | cs2 | OG | SINQU | YES OG | 1 | 0.89 | 0.89 | 0.89 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | TheChampionGG | WRAITH PCIFIC | YES TheChampionGG | 95 | 0.20 | 0.43 | 0.20 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | Falcons Force | G2 Ares | YES Falcons Force | 34 | 0.46 | 0.51 | 0.45 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | G2 Ares | Falcons Force | YES G2 Ares | 16 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | SINQU | PURE | NO PURE | 86 | 0.22 | 0.41 | 0.20 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | PURE | SINQU | YES PURE | 11 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | Falcons Force | OG | YES Falcons Force | 66 | 0.29 | 0.43 | 0.28 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | OG | Falcons Force | NO Falcons Force | 12 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | PURE | Orion Wanderers | NO Orion Wanderers | 10 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | SINQU | G2 Ares | NO G2 Ares | 79 | 0.24 | 0.39 | 0.23 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | G2 Ares | SINQU | YES G2 Ares | 11 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | Copenhagen Wolves | Bread Eaters Esports | NO Bread Eaters Esports | 11 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | WRAITH PCIFIC | TheChampionGG | YES WRAITH PCIFIC | 11 | 0.80 | 0.80 | 0.80 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | Esport Academy Copenhagen | Gothic | YES Esport Academy Copenhagen | 13 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | LPH Gaming | Gothic | YES LPH Gaming | 6 | 0.25 | 0.48 | 0.25 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | Gothic | LPH Gaming | YES Gothic | 12 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | ENJOY | ILLYRIANS | YES ENJOY | 17 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-10-07 08:46 | favourite | lol | FlyQuest | Shopify Rebellion | YES FlyQuest | 14 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | Falcons Force | Orion Wanderers | NO Orion Wanderers | 11 | 0.80 | 0.79 | 0.79 | open | - |
| 2026-10-07 08:46 | favourite | cs2 | PURE | G2 Ares | NO G2 Ares | 16 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-10-07 08:46 | model-only | cs2 | Gothic | Esport Academy Copenhagen | YES Gothic | 60 | 0.32 | 0.48 | 0.31 | open | - |
| 2026-10-07 07:50 | favourite | dota2 | Yellow Submarine | Blasterbl | YES Yellow Submarine | 16 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-07 07:50 | favourite | cs2 | HOTU | STATE | YES HOTU | 11 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-10-07 07:50 | model-only | dota2 | Yangon Galacticos | Direborn | YES Yangon Galacticos | 3 | 0.34 | 0.43 | 0.33 | open | - |
| 2026-10-07 07:50 | favourite | dota2 | Direborn | Yangon Galacticos | YES Direborn | 6 | 0.70 | 0.67 | 0.67 | open | - |

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

