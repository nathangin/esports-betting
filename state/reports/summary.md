# Esports paper trading (fake money)

Updated 2026-10-12 05:10 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 7 | 4 | 3 | 2 | $10.52 | +20.4% | -7.6c (5) | $1,010.52 |
| model-only | Elo win model alone (control: ignores the market) | 130 | 10 | 120 | 32 | -$161.38 | -10.7% | -0.9c (125) | $838.62 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 230 | 16 | 214 | 136 | -$192.24 | -11.9% | -1.8c (226) | $807.76 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

2110 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6668 | 0.2379 |
| model | 0.6685 | 0.2379 |
| blend | 0.6693 | 0.2391 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 1345 | 0.6909 | 0.6694 |
| ebasketballgame | 309 | 0.6836 | 0.6669 |
| cs2 | 302 | 0.5901 | 0.6639 |
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
| 2026-10-12 04:54 | favourite | lol | BNK FEARX | JD Gaming | YES BNK FEARX | 11 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-12 04:54 | model-only | lol | JD Gaming | BNK FEARX | NO BNK FEARX | 48 | 0.33 | 0.50 | 0.32 | open | - |
| 2026-10-12 04:44 | favourite | ebasketballgame | Denver Nuggets (Tatum) | Dallas Mavericks (Jake) | YES Denver Nuggets (Tatum) | 9 | 0.85 | 0.90 | 0.90 | open | - |
| 2026-10-12 04:44 | blend | ebasketballgame | Denver Nuggets (Tatum) | Dallas Mavericks (Jake) | YES Denver Nuggets (Tatum) | 22 | 0.85 | 0.92 | 0.90 | open | - |
| 2026-10-12 04:44 | favourite | ebasketballgame | New Orleans Pelicans (IceKimi) | Indiana Pacers (Clyde) | YES New Orleans Pelicans (IceKimi) | 19 | 0.39 | 0.67 | 0.67 | open | - |
| 2026-10-12 04:44 | model-only | ebasketballgame | New Orleans Pelicans (IceKimi) | Indiana Pacers (Clyde) | YES New Orleans Pelicans (IceKimi) | 29 | 0.39 | 0.47 | 0.67 | open | - |
| 2026-10-12 04:44 | blend | ebasketballgame | New Orleans Pelicans (IceKimi) | Indiana Pacers (Clyde) | YES New Orleans Pelicans (IceKimi) | 29 | 0.39 | 0.69 | 0.67 | open | - |
| 2026-10-12 03:44 | blend | ebasketballgame | Denver Nuggets (Walt) | Dallas Mavericks (Miles) | YES Denver Nuggets (Walt) | 24 | 0.79 | 0.89 | 0.86 | open | - |
| 2026-10-12 03:44 | favourite | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (James) | YES Indiana Pacers (Lenny) | 16 | 0.48 | 0.71 | 0.71 | open | - |
| 2026-10-12 03:44 | blend | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (James) | YES Indiana Pacers (Lenny) | 39 | 0.48 | 0.74 | 0.71 | open | - |
| 2026-10-12 03:44 | favourite | ebasketballgame | Denver Nuggets (Walt) | Dallas Mavericks (Miles) | YES Denver Nuggets (Walt) | 9 | 0.79 | 0.86 | 0.86 | open | - |
| 2026-10-12 03:14 | favourite | ebasketballgame | Dallas Mavericks (Walt) | Denver Nuggets (Larry) | YES Dallas Mavericks (Walt) | 15 | 0.50 | 0.72 | 0.72 | won | $7.23 |
| 2026-10-12 03:14 | blend | ebasketballgame | Dallas Mavericks (Walt) | Denver Nuggets (Larry) | YES Dallas Mavericks (Walt) | 31 | 0.50 | 0.74 | 0.72 | won | $14.95 |
| 2026-10-12 03:14 | favourite | ebasketballgame | Indiana Pacers (James) | New Orleans Pelicans (Donovan) | YES Indiana Pacers (James) | 15 | 0.49 | 0.72 | 0.72 | won | $7.38 |
| 2026-10-12 03:14 | blend | ebasketballgame | Indiana Pacers (James) | New Orleans Pelicans (Donovan) | YES Indiana Pacers (James) | 31 | 0.49 | 0.75 | 0.72 | won | $15.26 |
| 2026-10-12 02:44 | favourite | ebasketballgame | Denver Nuggets (Larry) | Dallas Mavericks (Miles) | YES Denver Nuggets (Larry) | 12 | 0.59 | 0.59 | 0.59 | won | $4.71 |
| 2026-10-12 02:44 | model-only | ebasketballgame | Dallas Mavericks (Miles) | Denver Nuggets (Larry) | YES Dallas Mavericks (Miles) | 25 | 0.38 | 0.48 | 0.41 | lost | -$9.92 |
| 2026-10-12 02:44 | favourite | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (Donovan) | YES Indiana Pacers (Lenny) | 12 | 0.60 | 0.62 | 0.62 | lost | -$7.41 |
| 2026-10-12 02:44 | model-only | ebasketballgame | New Orleans Pelicans (Donovan) | Indiana Pacers (Lenny) | NO Indiana Pacers (Lenny) | 39 | 0.41 | 0.61 | 0.38 | won | $22.34 |
| 2026-10-12 02:19 | model-only | ebasketballgame | New Orleans Pelicans (James) | Indiana Pacers (Lenny) | NO Indiana Pacers (Lenny) | 33 | 0.49 | 0.59 | 0.46 | lost | -$16.75 |
| 2026-10-12 02:19 | favourite | ebasketballgame | Denver Nuggets (Walt) | Dallas Mavericks (Miles) | NO Dallas Mavericks (Miles) | 10 | 0.72 | 0.70 | 0.70 | lost | -$7.35 |
| 2026-10-12 02:19 | favourite | ebasketballgame | Indiana Pacers (Lenny) | New Orleans Pelicans (James) | YES Indiana Pacers (Lenny) | 14 | 0.52 | 0.55 | 0.54 | won | $6.47 |
| 2026-10-12 02:14 | favourite | esoccergame | Argentina (Millie) | England (July) | YES Argentina (Millie) | 12 | 0.62 | 0.66 | 0.66 | won | $4.36 |
| 2026-10-12 01:49 | favourite | ebasketballgame | Los Angeles Lakers (Larry) | New York Knicks (Walt) | YES Los Angeles Lakers (Larry) | 14 | 0.56 | 0.57 | 0.57 | won | $5.91 |
| 2026-10-12 01:49 | favourite | ebasketballgame | Golden State Warriors (Donovan) | Brooklyn Nets (James) | YES Golden State Warriors (Donovan) | 15 | 0.52 | 0.52 | 0.52 | won | $6.93 |

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

