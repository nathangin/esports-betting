# Esports paper trading (fake money)

Updated 2026-10-07 07:50 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 43 | 11 | 32 | 8 | $27.58 | +6.8% | -0.7c (39) | $1,027.58 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 69 | 16 | 53 | 35 | -$61.61 | -14.6% | -1.4c (64) | $938.39 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

67 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5511 | 0.1838 |
| model | 0.6388 | 0.2230 |
| blend | 0.5515 | 0.1833 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 31 | 0.6527 | 0.6700 |
| lol | 15 | 0.3311 | 0.6278 |
| dota2 | 9 | 0.5545 | 0.5259 |
| r6 | 8 | 0.7369 | 0.7490 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-07 07:50 | favourite | valorant | NRG | T1 | NO T1 | 12 | 0.73 | 0.73 | 0.73 | open | - |
| 2026-10-07 07:50 | model-only | valorant | T1 | NRG | NO NRG | 72 | 0.27 | 0.38 | 0.27 | open | - |
| 2026-10-07 07:50 | favourite | lol | Shopify Rebellion | GAM Esports | YES Shopify Rebellion | 14 | 0.63 | 0.63 | 0.63 | open | - |
| 2026-10-07 07:50 | model-only | lol | GAM Esports | Shopify Rebellion | YES GAM Esports | 53 | 0.37 | 0.60 | 0.37 | open | - |
| 2026-10-07 07:50 | favourite | dota2 | Yellow Submarine | Blasterbl | YES Yellow Submarine | 16 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-07 07:50 | model-only | dota2 | Yellow Submarine | Blasterbl | YES Yellow Submarine | 35 | 0.56 | 0.63 | 0.56 | open | - |
| 2026-10-07 07:50 | favourite | dota2 | Direborn | Yangon Galacticos | YES Direborn | 6 | 0.70 | 0.67 | 0.67 | open | - |
| 2026-10-07 07:50 | model-only | dota2 | Yangon Galacticos | Direborn | YES Yangon Galacticos | 3 | 0.34 | 0.43 | 0.33 | open | - |
| 2026-10-07 07:50 | favourite | cs2 | HOTU | STATE | YES HOTU | 11 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-10-07 06:50 | model-only | cs2 | XI Esport | Passion Academy | YES XI Esport | 30 | 0.66 | 0.73 | 0.65 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | Leo Team | Walczaki | YES Leo Team | 16 | 0.54 | 0.50 | 0.50 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | los kogutos | MORROW | YES los kogutos | 13 | 0.69 | 0.60 | 0.60 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | MORROW | maybe | YES MORROW | 13 | 0.69 | 0.51 | 0.51 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | G2 Ares | Orion Wanderers | NO Orion Wanderers | 1 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | XI Esport | Passion Academy | YES XI Esport | 13 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-10-07 06:50 | model-only | cs2 | PURE | OG | NO OG | 29 | 0.34 | 0.41 | 0.33 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | OG | PURE | YES OG | 13 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-10-07 06:50 | favourite | cs2 | Falcons Force | SINQU | YES Falcons Force | 12 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-10-07 05:50 | favourite | lol | FlyQuest | GAM Esports | YES FlyQuest | 12 | 0.71 | 0.71 | 0.71 | open | - |
| 2026-10-07 05:50 | model-only | lol | GAM Esports | FlyQuest | YES GAM Esports | 67 | 0.29 | 0.54 | 0.29 | open | - |
| 2026-10-07 04:50 | favourite | dota2 | Xipto Esports | InterActive Philippines | YES Xipto Esports | 1 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-07 04:50 | model-only | dota2 | InterActive Philippines | Xipto Esports | YES InterActive Philippines | 81 | 0.24 | 0.39 | 0.23 | open | - |
| 2026-10-07 01:54 | favourite | dota2 | Direborn | IaChIo123 | YES Direborn | 1 | 0.73 | 0.59 | 0.59 | won | $0.25 |
| 2026-10-06 18:53 | model-only | lol | Fuego | Cupid Esports | NO Cupid Esports | 126 | 0.16 | 0.30 | 0.16 | lost | -$21.35 |
| 2026-10-06 17:53 | model-only | r6 | Twisted Minds | Virtus.pro | YES Twisted Minds | 51 | 0.27 | 0.41 | 0.26 | lost | -$14.48 |

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

