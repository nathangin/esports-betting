# Esports paper trading (fake money)

Updated 2026-10-11 04:56 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 109 | 8 | 101 | 25 | -$222.90 | -17.6% | -0.6c (103) | $777.10 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 191 | 11 | 180 | 120 | -$128.77 | -9.4% | -1.4c (189) | $871.23 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1562 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6601 | 0.2351 |
| model | 0.6773 | 0.2420 |
| blend | 0.6615 | 0.2358 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 944 | 0.6916 | 0.6825 |
| cs2 | 277 | 0.5844 | 0.6676 |
| ebasketballgame | 217 | 0.6837 | 0.6779 |
| lol | 35 | 0.4622 | 0.7005 |
| dota2 | 33 | 0.5625 | 0.6477 |
| r6 | 22 | 0.6444 | 0.7203 |
| ow | 17 | 0.4559 | 0.4954 |
| valorant | 12 | 0.6525 | 0.6684 |
| mlbb | 5 | 0.6931 | 0.6964 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-11 04:51 | favourite | ow | O2 Blast | ZANSIDE GAMING | YES O2 Blast | 15 | 0.56 | 0.52 | 0.52 | open | - |
| 2026-10-11 02:50 | favourite | cs2 | Chinggis Warriors | NEXVOID | YES Chinggis Warriors | 14 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-10-11 02:50 | model-only | cs2 | NEXVOID | Chinggis Warriors | YES NEXVOID | 31 | 0.47 | 0.54 | 0.45 | open | - |
| 2026-10-11 01:50 | favourite | ebasketballgame | Golden State Warriors (Zach) | Brooklyn Nets (Davis) | NO Brooklyn Nets (Davis) | 10 | 0.78 | 0.74 | 0.74 | won | $2.07 |
| 2026-10-11 01:35 | favourite | esoccergame | Leverkusen (Hurricane) | Dortmund (Niskanen15) | YES Leverkusen (Hurricane) | 14 | 0.56 | 0.60 | 0.60 | lost | -$8.09 |
| 2026-10-11 01:20 | favourite | esoccergame | FSV Mainz 05 (Eder) | 1. FC Köln (Frenkie) | YES FSV Mainz 05 (Eder) | 13 | 0.63 | 0.67 | 0.67 | won | $4.59 |
| 2026-10-11 01:05 | favourite | esoccergame | Leverkusen (Hurricane) | FSV Mainz 05 (Eder) | YES Leverkusen (Hurricane) | 16 | 0.51 | 0.56 | 0.56 | won | $7.56 |
| 2026-10-11 01:05 | favourite | esoccergame | FC Augsburg (Danny) | 1. FC Köln (Frenkie) | YES FC Augsburg (Danny) | 15 | 0.55 | 0.58 | 0.58 | lost | -$8.51 |
| 2026-10-11 00:55 | favourite | esoccergame | FSV Mainz 05 (Eder) | Dortmund (Niskanen15) | YES FSV Mainz 05 (Eder) | 14 | 0.56 | 0.61 | 0.61 | won | $5.91 |
| 2026-10-11 00:50 | favourite | esoccergame | Leverkusen (Hurricane) | 1. FC Köln (Frenkie) | YES Leverkusen (Hurricane) | 12 | 0.66 | 0.69 | 0.69 | won | $3.89 |
| 2026-10-11 00:40 | favourite | esoccergame | Botafogo (Hurricane) | Universitario (Danny) | YES Botafogo (Hurricane) | 13 | 0.61 | 0.65 | 0.65 | won | $4.85 |
| 2026-10-11 00:35 | favourite | esoccergame | São Paulo (Niskanen15) | Estudiantes (Frenkie) | YES São Paulo (Niskanen15) | 13 | 0.63 | 0.67 | 0.67 | won | $4.59 |
| 2026-10-10 22:24 | model-only | cs2 | Abyssal | Ground Zero | YES Abyssal | 1 | 0.37 | 0.43 | 0.36 | lost | -$0.39 |
| 2026-10-10 19:09 | model-only | cs2 | Wildcard | NRG | NO NRG | 4 | 0.41 | 0.58 | 0.38 | won | $2.29 |
| 2026-10-10 15:53 | favourite | cs2 | Spirit | MOUZ | NO MOUZ | 1 | 0.59 | 0.58 | 0.58 | lost | -$0.61 |
| 2026-10-10 12:38 | model-only | cs2 | Aurora Gaming | Vitality | YES Aurora Gaming | 21 | 0.24 | 0.39 | 0.23 | lost | -$5.31 |
| 2026-10-10 11:53 | favourite | cs2 | Iberian Soul | Nemiga | NO Nemiga | 3 | 0.81 | 0.81 | 0.81 | won | $0.53 |
| 2026-10-10 11:53 | model-only | cs2 | Just Swing | Kaleido | YES Just Swing | 31 | 0.46 | 0.60 | 0.43 | won | $16.20 |
| 2026-10-10 11:53 | model-only | cs2 | PRIVATE | GamerLegion | YES PRIVATE | 19 | 0.32 | 0.51 | 0.32 | won | $12.63 |
| 2026-10-10 10:52 | model-only | valorant | NRG | LOUD | YES NRG | 12 | 0.51 | 0.60 | 0.52 | lost | -$6.33 |
| 2026-10-10 10:52 | model-only | cs2 | LPH Gaming | UNiTY esports | YES LPH Gaming | 43 | 0.24 | 0.33 | 0.23 | lost | -$10.87 |
| 2026-10-10 09:52 | model-only | ow | JD Gaming | Weibo Gaming | YES JD Gaming | 37 | 0.21 | 0.31 | 0.20 | lost | -$8.20 |
| 2026-10-10 09:52 | model-only | cs2 | Saint Sinners | WBT Academy | YES Saint Sinners | 36 | 0.42 | 0.51 | 0.42 | won | $20.26 |
| 2026-10-10 09:47 | favourite | esoccergame | RB Leipzig (Kylian) | Mönchengladbach (Bradley) | YES RB Leipzig (Kylian) | 1 | 0.57 | 0.61 | 0.61 | lost | -$0.59 |
| 2026-10-10 09:22 | model-only | dota2 | Team Spirit | Team Yandex | NO Team Yandex | 39 | 0.38 | 0.47 | 0.38 | lost | -$15.47 |

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

