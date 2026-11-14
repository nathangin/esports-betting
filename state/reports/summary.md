# Esports paper trading (fake money)

Updated 2026-11-14 04:34 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 707 | 53 | 654 | 225 | -$325.91 | -4.5% | -0.3c (699) | $674.09 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1119 | 86 | 1033 | 678 | -$496.26 | -7.9% | -1.5c (1108) | $503.74 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2414 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5851 | 0.2014 |
| model | 0.6540 | 0.2313 |
| blend | 0.5851 | 0.2015 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1513 | 0.5937 | 0.6600 |
| dota2 | 426 | 0.5701 | 0.6459 |
| ow | 132 | 0.5132 | 0.5386 |
| valorant | 132 | 0.6254 | 0.6859 |
| lol | 100 | 0.5725 | 0.7120 |
| r6 | 91 | 0.5702 | 0.6572 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-14 00:09 | favourite | r6 | Virtus.pro | DarkZero Esports | NO DarkZero Esports | 2 | 0.51 | 0.51 | 0.51 | lost | -$1.06 |
| 2026-11-13 20:53 | favourite | cs2 | BARCA | BORRACHEIROS | YES BARCA | 1 | 0.87 | 0.86 | 0.86 | won | $0.12 |
| 2026-11-13 14:53 | favourite | cs2 | Galorys | RED Canids Academy | YES Galorys | 1 | 0.84 | 0.84 | 0.84 | won | $0.15 |
| 2026-11-13 14:53 | favourite | cs2 | Team NS | WorldEdit Club | YES Team NS | 9 | 0.52 | 0.51 | 0.51 | lost | -$4.84 |
| 2026-11-13 14:53 | favourite | cs2 | Team PCH3LK1N | Team cutierover | NO Team cutierover | 1 | 0.62 | 0.60 | 0.60 | lost | -$0.64 |
| 2026-11-13 12:52 | model-only | cs2 | Drama eSports | 6yuBoJlbl | YES Drama eSports | 25 | 0.39 | 0.52 | 0.38 | lost | -$10.17 |
| 2026-11-13 12:52 | model-only | cs2 | Balkan Outlaws | Saint Sinners | YES Balkan Outlaws | 26 | 0.51 | 0.61 | 0.51 | lost | -$13.72 |
| 2026-11-13 11:52 | model-only | dota2 | 4ikibamboni | Spirit Academy | YES 4ikibamboni | 1 | 0.39 | 0.48 | 0.39 | lost | -$0.41 |
| 2026-11-13 10:52 | model-only | cs2 | GenOne | Team ACES | NO Team ACES | 26 | 0.34 | 0.39 | 0.34 | lost | -$9.25 |
| 2026-11-13 10:52 | model-only | cs2 | Butterfly | PRIVATE | YES Butterfly | 1 | 0.36 | 0.57 | 0.35 | lost | -$0.38 |
| 2026-11-13 10:52 | model-only | cs2 | ex-Zero Tenacity | BakS eSports | YES ex-Zero Tenacity | 26 | 0.51 | 0.60 | 0.51 | won | $12.28 |
| 2026-11-13 10:22 | model-only | cs2 | ex-ENCE | Noir Verse | YES ex-ENCE | 31 | 0.41 | 0.47 | 0.40 | won | $17.76 |
| 2026-11-13 08:52 | favourite | dota2 | GamerLegion | CyberHero | YES GamerLegion | 6 | 0.75 | 0.76 | 0.76 | won | $1.42 |
| 2026-11-13 08:52 | model-only | cs2 | Team Bratishkin | Team Jerry | YES Team Bratishkin | 25 | 0.51 | 0.60 | 0.50 | lost | -$13.19 |
| 2026-11-13 08:52 | favourite | cs2 | Team Bratishkin | Team Jerry | YES Team Bratishkin | 9 | 0.51 | 0.50 | 0.50 | lost | -$4.75 |
| 2026-11-13 08:52 | model-only | dota2 | PlayTime | HULIGANI | YES PlayTime | 23 | 0.57 | 0.63 | 0.57 | lost | -$13.51 |
| 2026-11-13 08:52 | favourite | dota2 | PlayTime | HULIGANI | YES PlayTime | 3 | 0.57 | 0.57 | 0.57 | lost | -$1.77 |
| 2026-11-13 08:22 | model-only | r6 | G2 Esports | FaZe Clan | NO FaZe Clan | 31 | 0.36 | 0.42 | 0.36 | lost | -$11.66 |
| 2026-11-13 07:52 | model-only | cs2 | Brute | 33 | YES Brute | 26 | 0.50 | 0.64 | 0.49 | won | $12.54 |
| 2026-11-13 07:52 | model-only | cs2 | gothboiclique | NAVI Junior | YES gothboiclique | 31 | 0.42 | 0.52 | 0.38 | won | $17.45 |
| 2026-11-13 07:21 | model-only | valorant | XJG | Havoc & Yonder | NO Havoc & Yonder | 29 | 0.31 | 0.50 | 0.29 | lost | -$9.43 |
| 2026-11-13 06:51 | model-only | cs2 | MOUZ | Vitality | YES MOUZ | 30 | 0.44 | 0.54 | 0.43 | won | $16.28 |
| 2026-11-13 05:21 | favourite | r6 | Falcons Esport | Geekay Esports | YES Falcons Esport | 4 | 0.73 | 0.72 | 0.72 | won | $1.02 |
| 2026-11-13 05:21 | model-only | r6 | Geekay Esports | Falcons Esport | NO Falcons Esport | 44 | 0.29 | 0.41 | 0.28 | lost | -$13.40 |
| 2026-11-13 04:51 | favourite | valorant | Young Gaming | LGD Gaming | YES Young Gaming | 1 | 0.53 | 0.53 | 0.53 | won | $0.45 |

## Backtest on real Kalshi prices

9586 settled matches from 2026-05-28 to 2026-11-09, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2015 | $9,315.01 | -$992.01 | -10.6% | -18.8% to -2.6% | 32% | -0.6c | 99% |
| always the favourite (1% flat) | 4643 | $17,908.06 | -$833.06 | -4.7% | -6.9% to -2.4% | 67% | -1.8c | 84% |
| always the underdog (1% flat) | 3790 | $8,967.07 | -$986.07 | -11.0% | -16.9% to -5.1% | 31% | -1.2c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 9361 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5754 | 0.1970 | 68.9% |
| model | 0.6596 | 0.2339 | 59.6% |
| blend | 0.5751 | 0.1970 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1567 | 0.525 | 0.523 |
| (0.55, 0.6] | 1580 | 0.577 | 0.551 |
| (0.6, 0.65] | 1426 | 0.626 | 0.626 |
| (0.65, 0.7] | 1257 | 0.676 | 0.699 |
| (0.7, 0.75] | 1053 | 0.726 | 0.769 |
| (0.75, 0.8] | 889 | 0.776 | 0.805 |
| (0.8, 0.85] | 761 | 0.826 | 0.825 |
| (0.85, 0.9] | 562 | 0.877 | 0.902 |
| (0.9, 1.0] | 491 | 0.932 | 0.959 |

