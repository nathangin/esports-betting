# Esports paper trading (fake money)

Updated 2026-10-12 03:10 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 128 | 11 | 117 | 31 | -$157.05 | -10.7% | -0.8c (122) | $842.95 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 223 | 17 | 206 | 130 | -$216.11 | -13.9% | -1.8c (218) | $783.89 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

2069 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6665 | 0.2377 |
| model | 0.6686 | 0.2380 |
| blend | 0.6689 | 0.2389 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 1313 | 0.6908 | 0.6696 |
| cs2 | 301 | 0.5899 | 0.6637 |
| ebasketballgame | 301 | 0.6846 | 0.6672 |
| lol | 38 | 0.5060 | 0.6989 |
| dota2 | 34 | 0.5809 | 0.6527 |
| ow | 28 | 0.5446 | 0.6029 |
| r6 | 23 | 0.6353 | 0.7140 |
| mlbb | 18 | 0.6203 | 0.7106 |
| valorant | 13 | 0.6397 | 0.6656 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-12 02:44 | favourite | ebasketballgame | Denver Nuggets (Larry) | Dallas Mavericks (Miles) | YES Denver Nuggets (Larry) | 12 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-12 02:44 | model-only | ebasketballgame | Dallas Mavericks (Miles) | Denver Nuggets (Larry) | YES Dallas Mavericks (Miles) | 25 | 0.38 | 0.48 | 0.41 | open | - |
| 2026-10-12 02:44 | favourite | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (Donovan) | YES Indiana Pacers (Lenny) | 12 | 0.60 | 0.62 | 0.62 | open | - |
| 2026-10-12 02:44 | model-only | ebasketballgame | New Orleans Pelicans (Donovan) | Indiana Pacers (Lenny) | NO Indiana Pacers (Lenny) | 39 | 0.41 | 0.61 | 0.38 | open | - |
| 2026-10-12 02:19 | favourite | ebasketballgame | Denver Nuggets (Walt) | Dallas Mavericks (Miles) | NO Dallas Mavericks (Miles) | 10 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-10-12 02:19 | favourite | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (James) | YES Indiana Pacers (Lenny) | 14 | 0.52 | 0.55 | 0.54 | open | - |
| 2026-10-12 02:19 | model-only | ebasketballgame | New Orleans Pelicans (James) | Indiana Pacers (Lenny) | NO Indiana Pacers (Lenny) | 33 | 0.49 | 0.59 | 0.46 | open | - |
| 2026-10-12 02:14 | favourite | esoccergame | Argentina (Millie) | England (July) | YES Argentina (Millie) | 12 | 0.62 | 0.66 | 0.66 | won | $4.36 |
| 2026-10-12 01:49 | favourite | ebasketballgame | Golden State Warriors (Donovan) | Brooklyn Nets (James) | YES Golden State Warriors (Donovan) | 15 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-10-12 01:49 | favourite | ebasketballgame | Los Angeles Lakers (Larry) | New York Knicks (Walt) | YES Los Angeles Lakers (Larry) | 14 | 0.56 | 0.57 | 0.57 | open | - |
| 2026-10-12 01:23 | favourite | esoccergame | 1. FC Köln (PinkElephant) | FSV Mainz 05 (Eder) | YES 1. FC Köln (PinkElephant) | 13 | 0.57 | 0.61 | 0.61 | lost | -$7.64 |
| 2026-10-12 01:18 | favourite | esoccergame | Dortmund (Niskanen15) | FC Augsburg (Rooney) | YES Dortmund (Niskanen15) | 15 | 0.51 | 0.56 | 0.56 | lost | -$7.92 |
| 2026-10-12 01:08 | favourite | esoccergame | Leverkusen (Hurricane) | FSV Mainz 05 (Eder) | YES Leverkusen (Hurricane) | 16 | 0.47 | 0.52 | 0.52 | lost | -$7.80 |
| 2026-10-12 01:03 | favourite | esoccergame | 1. FC Köln (PinkElephant) | FC Augsburg (Rooney) | YES 1. FC Köln (PinkElephant) | 13 | 0.59 | 0.63 | 0.63 | won | $5.10 |
| 2026-10-12 00:53 | favourite | esoccergame | 1. FC Köln (PinkElephant) | Leverkusen (Hurricane) | YES 1. FC Köln (PinkElephant) | 16 | 0.48 | 0.53 | 0.53 | lost | -$7.96 |
| 2026-10-12 00:38 | favourite | esoccergame | Estudiantes (PinkElephant) | São Paulo (Niskanen15) | YES Estudiantes (PinkElephant) | 13 | 0.59 | 0.63 | 0.63 | lost | -$7.90 |
| 2026-10-11 15:53 | model-only | cs2 | antidaun | Saint Sinners | YES antidaun | 8 | 0.19 | 0.43 | 0.18 | lost | -$1.61 |
| 2026-10-11 14:52 | model-only | r6 | Fluxo W7M | Team Liquid | YES Fluxo W7M | 45 | 0.36 | 0.44 | 0.35 | lost | -$16.93 |
| 2026-10-11 13:52 | model-only | cs2 | MOUZ | Vitality | YES MOUZ | 42 | 0.35 | 0.44 | 0.34 | lost | -$15.37 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy | 9INE | YES Spirit Academy | 34 | 0.41 | 0.65 | 0.41 | won | $19.48 |
| 2026-10-11 12:52 | model-only | cs2 | mellren | Bebop | YES mellren | 23 | 0.62 | 0.71 | 0.61 | won | $8.36 |
| 2026-10-11 12:52 | model-only | cs2 | MASONIC | Aurora Young Blood | NO Aurora Young Blood | 33 | 0.43 | 0.55 | 0.42 | lost | -$14.76 |
| 2026-10-11 12:52 | model-only | cs2 | aimclub | ARGOS | YES aimclub | 30 | 0.47 | 0.54 | 0.47 | won | $15.37 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy Black | Metizport | NO Metizport | 9 | 0.20 | 0.36 | 0.18 | lost | -$1.91 |
| 2026-10-11 11:52 | model-only | cs2 | The KnockoutX | Alter Ego | YES The KnockoutX | 22 | 0.24 | 0.40 | 0.23 | lost | -$5.57 |

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

