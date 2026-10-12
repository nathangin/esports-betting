# Esports paper trading (fake money)

Updated 2026-10-12 12:47 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 18 | 0 | 18 | 9 | -$23.83 | -8.5% | -2.3c (18) | $976.17 |
| model-only | Elo win model alone (control: ignores the market) | 143 | 13 | 130 | 35 | -$192.08 | -11.8% | -0.4c (140) | $807.92 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 241 | 11 | 230 | 148 | -$165.43 | -9.7% | -1.9c (240) | $834.57 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

2269 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6663 | 0.2377 |
| model | 0.6693 | 0.2383 |
| blend | 0.6688 | 0.2389 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 1460 | 0.6907 | 0.6708 |
| ebasketballgame | 339 | 0.6810 | 0.6682 |
| cs2 | 308 | 0.5875 | 0.6635 |
| dota2 | 39 | 0.5521 | 0.6510 |
| lol | 39 | 0.5192 | 0.7034 |
| ow | 30 | 0.5281 | 0.5915 |
| r6 | 23 | 0.6353 | 0.7140 |
| mlbb | 18 | 0.6203 | 0.7106 |
| valorant | 13 | 0.6397 | 0.6656 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-12 11:15 | model-only | ebasketballgame | Denver Nuggets (Jake) | Dallas Mavericks (Barry) | YES Denver Nuggets (Jake) | 19 | 0.16 | 0.53 | 0.55 | open | - |
| 2026-10-12 10:45 | model-only | ebasketballgame | Denver Nuggets (Jake) | Dallas Mavericks (Tatum) | NO Dallas Mavericks (Tatum) | 105 | 0.15 | 0.35 | 0.12 | lost | -$16.69 |
| 2026-10-12 09:20 | model-only | cs2 | Sokerorg | MOUZ NXT | YES Sokerorg | 30 | 0.52 | 0.60 | 0.52 | open | - |
| 2026-10-12 08:50 | model-only | cs2 | Sangal | Inner Circle Esports | NO Inner Circle Esports | 47 | 0.34 | 0.51 | 0.33 | lost | -$16.72 |
| 2026-10-12 08:50 | model-only | cs2 | Apogee Esports | NIP | NO NIP | 2 | 0.22 | 0.38 | 0.22 | open | - |
| 2026-10-12 08:30 | model-only | ebasketballgame | Golden State Warriors (Shaq) | Brooklyn Nets (IceKimi) | YES Golden State Warriors (Shaq) | 24 | 0.66 | 0.73 | 0.80 | won | $7.78 |
| 2026-10-12 08:30 | blend | ebasketballgame | New York Knicks (Tatum) | Los Angeles Lakers (Barry) | YES New York Knicks (Tatum) | 25 | 0.61 | 0.80 | 0.78 | won | $9.33 |
| 2026-10-12 08:00 | blend | ebasketballgame | Indiana Pacers (Jake) | New Orleans Pelicans (Barry) | YES Indiana Pacers (Jake) | 22 | 0.18 | 0.57 | 0.56 | lost | -$4.19 |
| 2026-10-12 08:00 | blend | ebasketballgame | Denver Nuggets (Shaq) | Dallas Mavericks (Clyde) | YES Denver Nuggets (Shaq) | 36 | 0.50 | 0.75 | 0.72 | lost | -$18.63 |
| 2026-10-12 08:00 | model-only | ebasketballgame | Indiana Pacers (Jake) | New Orleans Pelicans (Barry) | YES Indiana Pacers (Jake) | 22 | 0.18 | 0.54 | 0.56 | lost | -$4.19 |
| 2026-10-12 07:50 | model-only | lol | KT Rolster | Team Vitality | YES KT Rolster | 36 | 0.36 | 0.42 | 0.36 | won | $22.45 |
| 2026-10-12 07:30 | blend | ebasketballgame | New Orleans Pelicans (Tatum) | Indiana Pacers (Jake) | YES New Orleans Pelicans (Tatum) | 24 | 0.84 | 0.92 | 0.89 | won | $3.61 |
| 2026-10-12 07:30 | favourite | ebasketballgame | Denver Nuggets (IceKimi) | Dallas Mavericks (Clyde) | YES Denver Nuggets (IceKimi) | 7 | 0.37 | 0.66 | 0.66 | lost | -$2.71 |
| 2026-10-12 07:30 | model-only | ebasketballgame | Denver Nuggets (IceKimi) | Dallas Mavericks (Clyde) | YES Denver Nuggets (IceKimi) | 29 | 0.37 | 0.42 | 0.66 | lost | -$11.21 |
| 2026-10-12 07:30 | blend | ebasketballgame | Denver Nuggets (IceKimi) | Dallas Mavericks (Clyde) | YES Denver Nuggets (IceKimi) | 29 | 0.37 | 0.68 | 0.66 | lost | -$11.21 |
| 2026-10-12 07:04 | blend | ebasketballgame | Dallas Mavericks (Shaq) | Denver Nuggets (IceKimi) | YES Dallas Mavericks (Shaq) | 31 | 0.63 | 0.81 | 0.79 | lost | -$20.04 |
| 2026-10-12 07:04 | blend | ebasketballgame | New Orleans Pelicans (Tatum) | Indiana Pacers (Barry) | YES New Orleans Pelicans (Tatum) | 33 | 0.60 | 0.79 | 0.77 | lost | -$20.36 |
| 2026-10-12 06:54 | model-only | cs2 | STATE | THE UNIT | YES STATE | 22 | 0.47 | 0.65 | 0.45 | open | - |
| 2026-10-12 06:54 | favourite | cs2 | Bread Eaters Esports | Passion Academy | YES Bread Eaters Esports | 2 | 0.59 | 0.57 | 0.57 | won | $0.78 |
| 2026-10-12 06:34 | blend | ebasketballgame | Golden State Warriors (Jake) | Brooklyn Nets (Barry) | YES Golden State Warriors (Jake) | 19 | 0.15 | 0.56 | 0.55 | lost | -$3.02 |
| 2026-10-12 06:34 | favourite | ebasketballgame | New York Knicks (Shaq) | Los Angeles Lakers (Clyde) | YES New York Knicks (Shaq) | 7 | 0.48 | 0.71 | 0.71 | won | $3.51 |
| 2026-10-12 06:34 | blend | ebasketballgame | New York Knicks (Shaq) | Los Angeles Lakers (Clyde) | YES New York Knicks (Shaq) | 31 | 0.48 | 0.74 | 0.71 | won | $15.57 |
| 2026-10-12 06:34 | model-only | ebasketballgame | Golden State Warriors (Jake) | Brooklyn Nets (Barry) | YES Golden State Warriors (Jake) | 19 | 0.15 | 0.46 | 0.55 | lost | -$3.02 |
| 2026-10-12 06:34 | favourite | ebasketballgame | Golden State Warriors (Jake) | Brooklyn Nets (Barry) | YES Golden State Warriors (Jake) | 1 | 0.15 | 0.55 | 0.55 | lost | -$0.16 |
| 2026-10-12 06:09 | favourite | ebasketballgame | Brooklyn Nets (Tatum) | Golden State Warriors (Jake) | YES Brooklyn Nets (Tatum) | 1 | 0.84 | 0.89 | 0.89 | won | $0.15 |

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

