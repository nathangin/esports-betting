# Esports paper trading (fake money)

Updated 2026-10-09 07:35 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 73 | 7 | 66 | 15 | -$93.97 | -10.7% | -0.8c (70) | $906.03 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 136 | 14 | 122 | 83 | -$98.89 | -10.4% | -0.7c (128) | $901.11 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

526 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6334 | 0.2227 |
| model | 0.6808 | 0.2440 |
| blend | 0.6333 | 0.2226 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 233 | 0.6905 | 0.6858 |
| cs2 | 177 | 0.5946 | 0.6738 |
| ebasketballgame | 46 | 0.6705 | 0.7183 |
| lol | 26 | 0.3970 | 0.6526 |
| dota2 | 21 | 0.6117 | 0.6346 |
| r6 | 13 | 0.6902 | 0.7295 |
| valorant | 6 | 0.5347 | 0.7195 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-09 07:24 | favourite | cs2 | Aurora Gaming | 1WIN | NO 1WIN | 12 | 0.71 | 0.70 | 0.71 | open | - |
| 2026-10-09 06:53 | favourite | r6 | Chiefs Esports Club | 7VEN | NO 7VEN | 10 | 0.85 | 0.84 | 0.84 | open | - |
| 2026-10-09 06:53 | favourite | cs2 | Teletubisie | STATE | YES Teletubisie | 14 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-10-09 06:53 | favourite | cs2 | Royal Foxes Esports | Elite Klan | NO Elite Klan | 13 | 0.64 | 0.63 | 0.63 | open | - |
| 2026-10-09 06:53 | model-only | cs2 | Elite Klan | Royal Foxes Esports | YES Elite Klan | 46 | 0.37 | 0.44 | 0.37 | open | - |
| 2026-10-09 06:53 | favourite | cs2 | Acend | Nexus | YES Acend | 14 | 0.61 | 0.57 | 0.57 | open | - |
| 2026-10-09 06:53 | favourite | cs2 | Fire Flux Esports | Lavked | NO Lavked | 11 | 0.75 | 0.57 | 0.57 | open | - |
| 2026-10-09 06:53 | favourite | cs2 | mellren | Bebop | NO Bebop | 13 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-10-09 06:53 | model-only | cs2 | mellren | Bebop | NO Bebop | 26 | 0.66 | 0.73 | 0.66 | open | - |
| 2026-10-09 05:53 | favourite | cs2 | Chinggis Warriors | 1337 | YES Chinggis Warriors | 10 | 0.88 | 0.86 | 0.86 | open | - |
| 2026-10-09 03:53 | favourite | r6 | ENTERPRISE Esports | Man eSports LFO | NO Man eSports LFO | 4 | 0.83 | 0.84 | 0.84 | won | $0.64 |
| 2026-10-09 02:53 | model-only | cs2 | The Audacity | The Huns Esports | YES The Audacity | 1 | 0.30 | 0.54 | 0.30 | lost | -$0.32 |
| 2026-10-09 02:53 | favourite | cs2 | The Huns Esports | The Audacity | NO The Audacity | 12 | 0.72 | 0.70 | 0.70 | won | $3.19 |
| 2026-10-09 02:48 | favourite | ebasketballgame | New Orleans Pelicans (Tim) | Indiana Pacers (Larry) | NO Indiana Pacers (Larry) | 10 | 0.73 | 0.70 | 0.71 | won | $2.56 |
| 2026-10-09 02:48 | model-only | ebasketballgame | Indiana Pacers (Larry) | New Orleans Pelicans (Tim) | YES Indiana Pacers (Larry) | 10 | 0.32 | 0.43 | 0.29 | lost | -$3.36 |
| 2026-10-09 02:18 | favourite | ebasketballgame | New Orleans Pelicans (Zion) | Indiana Pacers (Larry) | NO Indiana Pacers (Larry) | 13 | 0.68 | 0.65 | 0.65 | won | $3.96 |
| 2026-10-09 01:53 | favourite | ebasketballgame | Brooklyn Nets (Zion) | Golden State Warriors (Tim) | NO Golden State Warriors (Tim) | 16 | 0.54 | 0.51 | 0.51 | lost | -$8.92 |
| 2026-10-09 01:17 | favourite | esoccergame | FC Augsburg (Aron) | Dortmund (Declan) | YES FC Augsburg (Aron) | 20 | 0.44 | 0.50 | 0.50 | lost | -$9.15 |
| 2026-10-09 01:07 | favourite | esoccergame | FC Augsburg (Aron) | 1. FC Köln (Frost) | YES FC Augsburg (Aron) | 12 | 0.73 | 0.77 | 0.77 | lost | -$8.93 |
| 2026-10-09 00:52 | favourite | esoccergame | FSV Mainz 05 (Pedri) | Dortmund (Declan) | YES FSV Mainz 05 (Pedri) | 19 | 0.46 | 0.51 | 0.51 | lost | -$9.08 |
| 2026-10-09 00:52 | favourite | esoccergame | Leverkusen (Frenkie) | 1. FC Köln (Frost) | YES Leverkusen (Frenkie) | 11 | 0.81 | 0.82 | 0.82 | won | $1.97 |
| 2026-10-09 00:37 | favourite | esoccergame | São Paulo (Declan) | Estudiantes (Frost) | YES São Paulo (Declan) | 13 | 0.69 | 0.72 | 0.72 | won | $3.83 |
| 2026-10-08 14:38 | favourite | cs2 | EAC Extra | Linx Legacy Esport | YES EAC Extra | 5 | 0.73 | 0.61 | 0.61 | won | $1.28 |
| 2026-10-08 12:50 | model-only | cs2 | Azuolas | Misa Esports | NO Misa Esports | 4 | 0.22 | 0.31 | 0.20 | lost | -$0.93 |
| 2026-10-08 12:50 | model-only | cs2 | Nexus | CYBERSHOKE Esports | YES Nexus | 52 | 0.31 | 0.52 | 0.31 | open | - |

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

