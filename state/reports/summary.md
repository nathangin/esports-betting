# Esports paper trading (fake money)

Updated 2026-11-13 10:22 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 701 | 60 | 641 | 221 | -$304.22 | -4.3% | -0.3c (692) | $695.78 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1114 | 89 | 1025 | 675 | -$484.89 | -7.7% | -1.5c (1103) | $515.11 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2346 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5842 | 0.2010 |
| model | 0.6526 | 0.2307 |
| blend | 0.5842 | 0.2012 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1470 | 0.5928 | 0.6587 |
| dota2 | 414 | 0.5679 | 0.6454 |
| ow | 129 | 0.5092 | 0.5375 |
| valorant | 124 | 0.6329 | 0.6779 |
| lol | 100 | 0.5725 | 0.7120 |
| r6 | 89 | 0.5700 | 0.6583 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-13 10:22 | model-only | cs2 | ex-ENCE | Noir Verse | YES ex-ENCE | 31 | 0.41 | 0.47 | 0.40 | open | - |
| 2026-11-13 08:52 | favourite | dota2 | PlayTime | HULIGANI | YES PlayTime | 3 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-13 08:52 | model-only | dota2 | PlayTime | HULIGANI | YES PlayTime | 23 | 0.57 | 0.63 | 0.57 | open | - |
| 2026-11-13 08:52 | favourite | dota2 | GamerLegion | CyberHero | YES GamerLegion | 6 | 0.75 | 0.76 | 0.76 | open | - |
| 2026-11-13 08:52 | favourite | cs2 | Team Bratishkin | Team Jerry | YES Team Bratishkin | 9 | 0.51 | 0.50 | 0.50 | open | - |
| 2026-11-13 08:52 | model-only | cs2 | Team Bratishkin | Team Jerry | YES Team Bratishkin | 25 | 0.51 | 0.60 | 0.50 | open | - |
| 2026-11-13 08:22 | model-only | r6 | G2 Esports | FaZe Clan | NO FaZe Clan | 31 | 0.36 | 0.42 | 0.36 | open | - |
| 2026-11-13 07:52 | model-only | cs2 | Brute | 33 | YES Brute | 26 | 0.50 | 0.64 | 0.49 | open | - |
| 2026-11-13 07:52 | model-only | cs2 | gothboiclique | NAVI Junior | YES gothboiclique | 31 | 0.42 | 0.52 | 0.38 | open | - |
| 2026-11-13 07:21 | model-only | valorant | XJG | Havoc & Yonder | NO Havoc & Yonder | 29 | 0.31 | 0.50 | 0.29 | open | - |
| 2026-11-13 06:51 | model-only | cs2 | MOUZ | Vitality | YES MOUZ | 30 | 0.44 | 0.54 | 0.43 | won | $16.28 |
| 2026-11-13 05:21 | favourite | r6 | Falcons Esport | Geekay Esports | YES Falcons Esport | 4 | 0.73 | 0.72 | 0.72 | won | $1.02 |
| 2026-11-13 05:21 | model-only | r6 | Geekay Esports | Falcons Esport | NO Falcons Esport | 44 | 0.29 | 0.41 | 0.28 | lost | -$13.40 |
| 2026-11-13 04:51 | favourite | valorant | Young Gaming | LGD Gaming | YES Young Gaming | 1 | 0.53 | 0.53 | 0.53 | won | $0.45 |
| 2026-11-13 04:51 | favourite | valorant | TEC Esports | Ambitious Legend Gaming | YES TEC Esports | 6 | 0.75 | 0.76 | 0.76 | won | $1.42 |
| 2026-11-13 02:21 | favourite | r6 | Team Liquid | DarkZero Esports | NO DarkZero Esports | 7 | 0.66 | 0.65 | 0.65 | lost | -$4.73 |
| 2026-11-13 02:21 | model-only | r6 | DarkZero Esports | Team Liquid | YES DarkZero Esports | 35 | 0.36 | 0.49 | 0.35 | won | $21.83 |
| 2026-11-12 23:21 | favourite | r6 | Virtus.pro | M80 | NO M80 | 8 | 0.57 | 0.56 | 0.56 | won | $3.30 |
| 2026-11-12 18:20 | favourite | cs2 | eSuba | NoTime | NO NoTime | 1 | 0.53 | 0.52 | 0.52 | lost | -$0.55 |
| 2026-11-12 17:50 | favourite | cs2 | tao toma | Procyon Gaming | YES tao toma | 1 | 0.64 | 0.64 | 0.64 | won | $0.34 |
| 2026-11-12 17:35 | favourite | cs2 | Team Bratishkin | Team Recrent | YES Team Bratishkin | 8 | 0.58 | 0.57 | 0.57 | won | $3.22 |
| 2026-11-12 16:50 | model-only | cs2 | Spirit Academy | ex-RUSTEC | YES Spirit Academy | 7 | 0.55 | 0.60 | 0.55 | lost | -$3.98 |
| 2026-11-12 16:50 | model-only | cs2 | maybe | Team ACES | NO Team ACES | 1 | 0.26 | 0.41 | 0.25 | open | - |
| 2026-11-12 16:50 | model-only | cs2 | Spirit HU | ENRAGE | NO ENRAGE | 44 | 0.30 | 0.42 | 0.29 | lost | -$13.85 |
| 2026-11-12 15:50 | favourite | cs2 | Fire Flux Esports | Banger Gang | NO Banger Gang | 1 | 0.64 | 0.62 | 0.62 | open | - |

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

