# Esports paper trading (fake money)

Updated 2026-10-10 05:27 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 88 | 8 | 80 | 19 | -$192.23 | -17.9% | -0.7c (82) | $807.77 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 161 | 12 | 149 | 98 | -$158.79 | -13.6% | -1.3c (157) | $841.21 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1005 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6550 | 0.2328 |
| model | 0.6744 | 0.2408 |
| blend | 0.6565 | 0.2336 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 561 | 0.6957 | 0.6805 |
| cs2 | 231 | 0.5985 | 0.6682 |
| ebasketballgame | 125 | 0.6778 | 0.6818 |
| lol | 29 | 0.3933 | 0.6710 |
| dota2 | 24 | 0.5756 | 0.6162 |
| r6 | 18 | 0.6914 | 0.7324 |
| valorant | 10 | 0.6330 | 0.6398 |
| ow | 7 | 0.1414 | 0.3682 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-10 04:52 | favourite | ow | ZANSIDE GAMING | SEIJI ESPORTS | NO SEIJI ESPORTS | 2 | 0.86 | 0.84 | 0.84 | open | - |
| 2026-10-10 04:52 | favourite | dota2 | Cloud Dawning | Cresent | NO Cresent | 14 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-10-10 04:52 | model-only | dota2 | Cresent | Cloud Dawning | NO Cloud Dawning | 33 | 0.47 | 0.61 | 0.45 | open | - |
| 2026-10-10 04:52 | favourite | dota2 | Cloud Rising | Zenith | YES Cloud Rising | 1 | 0.71 | 0.64 | 0.64 | open | - |
| 2026-10-10 02:52 | favourite | cs2 | NEXVOID | 5star | NO 5star | 10 | 0.77 | 0.63 | 0.63 | open | - |
| 2026-10-10 02:47 | favourite | ebasketballgame | New Orleans Pelicans (Zach) | Indiana Pacers (James) | NO Indiana Pacers (James) | 9 | 0.88 | 0.84 | 0.84 | won | $1.01 |
| 2026-10-10 02:47 | favourite | ebasketballgame | Denver Nuggets (Lonzo) | Dallas Mavericks (Cade) | NO Dallas Mavericks (Cade) | 10 | 0.83 | 0.80 | 0.80 | won | $1.60 |
| 2026-10-10 02:22 | favourite | cs2 | Abyssal | Mindfreak | NO Mindfreak | 11 | 0.72 | 0.72 | 0.72 | open | - |
| 2026-10-10 02:22 | model-only | cs2 | Mindfreak | Abyssal | NO Abyssal | 1 | 0.28 | 0.40 | 0.28 | open | - |
| 2026-10-10 02:17 | favourite | ebasketballgame | Indiana Pacers (James) | New Orleans Pelicans (Davis) | NO New Orleans Pelicans (Davis) | 14 | 0.57 | 0.54 | 0.53 | won | $5.77 |
| 2026-10-10 02:17 | favourite | ebasketballgame | Dallas Mavericks (Cade) | Denver Nuggets (Bryce) | NO Denver Nuggets (Bryce) | 13 | 0.61 | 0.57 | 0.57 | lost | -$8.15 |
| 2026-10-10 01:52 | favourite | ebasketballgame | Los Angeles Lakers (Lonzo) | New York Knicks (Bryce) | NO New York Knicks (Bryce) | 10 | 0.84 | 0.80 | 0.80 | lost | -$8.50 |
| 2026-10-10 01:52 | favourite | ebasketballgame | Golden State Warriors (Zach) | Brooklyn Nets (Davis) | NO Brooklyn Nets (Davis) | 9 | 0.88 | 0.84 | 0.84 | won | $1.01 |
| 2026-10-10 01:17 | favourite | esoccergame | FC Augsburg (Aron) | Dortmund (Frost) | YES FC Augsburg (Aron) | 11 | 0.76 | 0.79 | 0.79 | lost | -$8.51 |
| 2026-10-10 01:07 | favourite | esoccergame | FC Augsburg (Aron) | 1. FC Köln (Kevin) | YES FC Augsburg (Aron) | 13 | 0.61 | 0.66 | 0.66 | lost | -$8.15 |
| 2026-10-10 00:51 | favourite | esoccergame | Leverkusen (Frenkie) | 1. FC Köln (Kevin) | YES Leverkusen (Frenkie) | 12 | 0.67 | 0.69 | 0.69 | won | $3.77 |
| 2026-10-10 00:41 | favourite | esoccergame | Botafogo (Frenkie) | Universitario (Aron) | YES Botafogo (Frenkie) | 15 | 0.56 | 0.61 | 0.61 | lost | -$8.66 |
| 2026-10-09 22:46 | blend | esoccergame | Montpellier (Ellen) | Nantes (Lucy) | YES Montpellier (Ellen) | 30 | 0.64 | 0.77 | 0.74 | lost | -$19.69 |
| 2026-10-09 12:24 | model-only | cs2 | ENCE Prospects | Passion Academy | YES ENCE Prospects | 43 | 0.40 | 0.54 | 0.39 | lost | -$17.93 |
| 2026-10-09 12:24 | model-only | cs2 | NAVI Junior | G2 Ares | YES NAVI Junior | 34 | 0.50 | 0.60 | 0.50 | won | $16.40 |
| 2026-10-09 11:54 | model-only | cs2 | Vitalem Aerem | Rare Atom | NO Rare Atom | 1 | 0.27 | 0.37 | 0.27 | won | $0.71 |
| 2026-10-09 11:24 | model-only | dota2 | 1win | PARIVISION | YES 1win | 11 | 0.14 | 0.28 | 0.14 | lost | -$1.64 |
| 2026-10-09 10:54 | model-only | valorant | T1 | Paper Rex | NO Paper Rex | 63 | 0.27 | 0.50 | 0.28 | won | $45.12 |
| 2026-10-09 10:54 | model-only | cs2 | Sinners | GamerLegion | YES Sinners | 42 | 0.41 | 0.58 | 0.42 | lost | -$17.94 |
| 2026-10-09 10:54 | model-only | cs2 | K27 | fnatic | YES K27 | 35 | 0.50 | 0.56 | 0.49 | lost | -$18.12 |

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

