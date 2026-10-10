# Esports paper trading (fake money)

Updated 2026-10-10 00:41 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 86 | 6 | 80 | 19 | -$192.23 | -17.9% | -0.7c (81) | $807.77 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 147 | 8 | 139 | 93 | -$129.98 | -11.9% | -0.8c (145) | $870.02 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

913 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6515 | 0.2313 |
| model | 0.6747 | 0.2411 |
| blend | 0.6527 | 0.2320 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 502 | 0.6942 | 0.6796 |
| cs2 | 219 | 0.5989 | 0.6727 |
| ebasketballgame | 106 | 0.6798 | 0.6945 |
| lol | 28 | 0.4019 | 0.6402 |
| dota2 | 24 | 0.5756 | 0.6162 |
| r6 | 17 | 0.6312 | 0.7195 |
| valorant | 10 | 0.6330 | 0.6398 |
| ow | 7 | 0.1414 | 0.3682 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-10 00:41 | favourite | esoccergame | Botafogo (Frenkie) | Universitario (Aron) | YES Botafogo (Frenkie) | 15 | 0.56 | 0.61 | 0.61 | open | - |
| 2026-10-09 22:46 | blend | esoccergame | Montpellier (Ellen) | Nantes (Lucy) | YES Montpellier (Ellen) | 30 | 0.64 | 0.77 | 0.74 | lost | -$19.69 |
| 2026-10-09 12:24 | model-only | cs2 | ENCE Prospects | Passion Academy | YES ENCE Prospects | 43 | 0.40 | 0.54 | 0.39 | lost | -$17.93 |
| 2026-10-09 12:24 | model-only | cs2 | NAVI Junior | G2 Ares | YES NAVI Junior | 34 | 0.50 | 0.60 | 0.50 | won | $16.40 |
| 2026-10-09 11:54 | model-only | cs2 | Vitalem Aerem | Rare Atom | NO Rare Atom | 1 | 0.27 | 0.37 | 0.27 | won | $0.71 |
| 2026-10-09 11:24 | model-only | dota2 | 1win | PARIVISION | YES 1win | 11 | 0.14 | 0.28 | 0.14 | lost | -$1.64 |
| 2026-10-09 10:54 | model-only | valorant | T1 | Paper Rex | NO Paper Rex | 63 | 0.27 | 0.50 | 0.28 | won | $45.12 |
| 2026-10-09 10:54 | model-only | cs2 | Sinners | GamerLegion | YES Sinners | 42 | 0.41 | 0.58 | 0.42 | lost | -$17.94 |
| 2026-10-09 10:54 | model-only | cs2 | K27 | fnatic | YES K27 | 35 | 0.50 | 0.56 | 0.49 | lost | -$18.12 |
| 2026-10-09 09:54 | model-only | cs2 | Honvéd | 6666 | YES Honvéd | 55 | 0.31 | 0.41 | 0.31 | lost | -$17.88 |
| 2026-10-09 09:54 | model-only | cs2 | PARIVISION | Vitality | NO Vitality | 106 | 0.16 | 0.27 | 0.15 | lost | -$17.96 |
| 2026-10-09 09:49 | favourite | esoccergame | Frankfurt (Fede) | Freiburg (Shaq) | YES Frankfurt (Fede) | 1 | 0.45 | 0.50 | 0.50 | won | $0.53 |
| 2026-10-09 09:49 | favourite | esoccergame | Portugal (Rose) | United States (Mia) | YES Portugal (Rose) | 10 | 0.47 | 0.53 | 0.53 | lost | -$4.88 |
| 2026-10-09 09:34 | favourite | esoccergame | Freiburg (Shaq) | Stuttgart (Niskanen15) | YES Freiburg (Shaq) | 13 | 0.63 | 0.68 | 0.68 | won | $4.59 |
| 2026-10-09 09:24 | favourite | cs2 | Vitality Academy | CTRL Esports | NO CTRL Esports | 13 | 0.63 | 0.62 | 0.62 | lost | -$8.41 |
| 2026-10-09 09:24 | favourite | cs2 | WRAITH PCIFIC | XI Esport | NO XI Esport | 11 | 0.75 | 0.75 | 0.75 | won | $2.60 |
| 2026-10-09 09:09 | favourite | esoccergame | Freiburg (Shaq) | Mönchengladbach (Eder) | YES Freiburg (Shaq) | 16 | 0.54 | 0.58 | 0.58 | lost | -$8.92 |
| 2026-10-09 08:54 | favourite | cs2 | Sangal | Esport Academy Copenhagen | YES Sangal | 12 | 0.69 | 0.69 | 0.69 | won | $3.54 |
| 2026-10-09 08:54 | model-only | cs2 | Esport Academy Copenhagen | Sangal | YES Esport Academy Copenhagen | 55 | 0.31 | 0.40 | 0.31 | lost | -$17.88 |
| 2026-10-09 08:54 | favourite | cs2 | Infinite | WBT Academy | YES Infinite | 14 | 0.59 | 0.60 | 0.60 | lost | -$8.50 |
| 2026-10-09 08:54 | model-only | cs2 | WBT Academy | Infinite | YES WBT Academy | 1 | 0.40 | 0.57 | 0.40 | won | $0.58 |
| 2026-10-09 07:54 | favourite | dota2 | Team Spirit | Aurora | NO Aurora | 12 | 0.69 | 0.69 | 0.69 | won | $3.54 |
| 2026-10-09 07:54 | model-only | dota2 | Aurora | Team Spirit | YES Aurora | 48 | 0.32 | 0.38 | 0.32 | lost | -$16.10 |
| 2026-10-09 07:54 | favourite | cs2 | HOTU | Acend | NO Acend | 11 | 0.75 | 0.74 | 0.74 | won | $2.60 |
| 2026-10-09 07:54 | model-only | cs2 | Acend | HOTU | NO HOTU | 66 | 0.26 | 0.36 | 0.26 | lost | -$18.05 |

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

