# Esports paper trading (fake money)

Updated 2026-10-06 08:07 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 15 | 3 | 12 | 2 | -$22.38 | -14.1% | -0.3c (15) | $977.62 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 29 | 8 | 21 | 16 | $13.10 | +7.4% | -1.9c (28) | $1,013.10 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

24 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5081 | 0.1665 |
| model | 0.6432 | 0.2250 |
| blend | 0.5031 | 0.1644 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 9 | 0.5609 | 0.6217 |
| lol | 6 | 0.1220 | 0.5869 |
| r6 | 6 | 0.8571 | 0.8141 |
| dota2 | 2 | 0.4931 | 0.5672 |
| ow | 1 | 0.2844 | 0.3003 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-06 07:52 | favourite | lol | JD Gaming | LGD Gaming | YES JD Gaming | 18 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-06 06:52 | favourite | dota2 | HULIGANI | CyberHero | NO CyberHero | 18 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-06 06:52 | favourite | cs2 | EAC Extra | TheChampionGG | NO TheChampionGG | 13 | 0.71 | 0.69 | 0.69 | open | - |
| 2026-10-06 06:52 | model-only | cs2 | TheChampionGG | EAC Extra | YES TheChampionGG | 1 | 0.32 | 0.51 | 0.31 | open | - |
| 2026-10-06 06:52 | favourite | cs2 | Just_Players | MORROW | YES Just_Players | 3 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-10-06 06:52 | model-only | cs2 | MORROW | Just_Players | NO Just_Players | 3 | 0.29 | 0.45 | 0.28 | open | - |
| 2026-10-06 05:52 | favourite | lol | OKSavingsBank BRION | Natus Vincere | YES OKSavingsBank BRION | 12 | 0.80 | 0.80 | 0.80 | open | - |
| 2026-10-06 04:51 | favourite | dota2 | Xipto Esports | Direborn | NO Direborn | 3 | 0.88 | 0.86 | 0.86 | open | - |
| 2026-10-06 01:51 | favourite | dota2 | InterActive Philippines | Yangon Galacticos | NO Yangon Galacticos | 2 | 0.55 | 0.54 | 0.54 | won | $0.86 |
| 2026-10-05 18:18 | favourite | cs2 | XI Esport | struggletony | YES XI Esport | 5 | 0.80 | 0.55 | 0.55 | open | - |
| 2026-10-05 18:18 | model-only | cs2 | Linx Legacy Esport | EAC Extra | NO EAC Extra | 4 | 0.50 | 0.62 | 0.49 | open | - |
| 2026-10-05 18:18 | favourite | cs2 | EAC Extra | Linx Legacy Esport | YES EAC Extra | 18 | 0.53 | 0.51 | 0.51 | open | - |
| 2026-10-05 18:18 | favourite | lol | KaBuM! Ilha das Lendas | 9z Globant | NO 9z Globant | 11 | 0.89 | 0.88 | 0.88 | won | $1.13 |
| 2026-10-05 18:18 | model-only | r6 | Virtus.pro | G2 Esports | NO G2 Esports | 6 | 0.37 | 0.47 | 0.34 | lost | -$2.32 |
| 2026-10-05 18:18 | favourite | r6 | G2 Esports | Virtus.pro | YES G2 Esports | 1 | 0.68 | 0.66 | 0.66 | won | $0.30 |
| 2026-10-05 08:50 | favourite | dota2 | Yellow Submarine | CyberHero | YES Yellow Submarine | 14 | 0.69 | 0.69 | 0.69 | won | $4.13 |
| 2026-10-05 08:50 | favourite | cs2 | Natus Vincere | 9z | NO 9z | 13 | 0.71 | 0.70 | 0.71 | won | $3.58 |
| 2026-10-05 08:50 | model-only | cs2 | 9z | Natus Vincere | YES 9z | 67 | 0.30 | 0.47 | 0.29 | lost | -$21.09 |
| 2026-10-05 08:50 | favourite | cs2 | Legacy | 1WIN | YES Legacy | 17 | 0.55 | 0.55 | 0.55 | lost | -$9.65 |
| 2026-10-05 08:50 | favourite | lol | JD Gaming | Shopify Rebellion | NO Shopify Rebellion | 11 | 0.87 | 0.88 | 0.88 | won | $1.34 |
| 2026-10-05 08:50 | model-only | lol | Shopify Rebellion | JD Gaming | NO JD Gaming | 165 | 0.12 | 0.36 | 0.12 | lost | -$21.02 |
| 2026-10-05 08:50 | model-only | dota2 | CyberHero | Yellow Submarine | YES CyberHero | 65 | 0.31 | 0.43 | 0.31 | lost | -$21.13 |
| 2026-10-05 08:50 | model-only | cs2 | MORROW | Noir Verse | YES MORROW | 11 | 0.29 | 0.38 | 0.27 | won | $7.65 |
| 2026-10-05 08:50 | favourite | cs2 | Esport Academy Copenhagen | Lavked | YES Esport Academy Copenhagen | 14 | 0.66 | 0.66 | 0.66 | won | $4.54 |
| 2026-10-05 08:50 | model-only | cs2 | Lavked | Esport Academy Copenhagen | YES Lavked | 59 | 0.34 | 0.47 | 0.34 | lost | -$20.99 |

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

