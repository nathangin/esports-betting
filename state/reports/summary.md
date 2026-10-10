# Esports paper trading (fake money)

Updated 2026-10-10 08:08 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 94 | 13 | 81 | 19 | -$192.53 | -17.9% | -0.8c (87) | $807.47 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 173 | 22 | 151 | 99 | -$157.61 | -13.3% | -1.3c (168) | $842.39 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1062 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6569 | 0.2337 |
| model | 0.6747 | 0.2410 |
| blend | 0.6585 | 0.2345 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 606 | 0.6955 | 0.6794 |
| cs2 | 233 | 0.5950 | 0.6667 |
| ebasketballgame | 133 | 0.6787 | 0.6880 |
| lol | 29 | 0.3933 | 0.6710 |
| dota2 | 24 | 0.5756 | 0.6162 |
| r6 | 19 | 0.6783 | 0.7255 |
| valorant | 10 | 0.6330 | 0.6398 |
| ow | 8 | 0.3528 | 0.4414 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-10 07:52 | favourite | ow | Solus Victorem | HUNENG | YES Solus Victorem | 10 | 0.78 | 0.71 | 0.71 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | Vitality Academy | Dynamo Eclot Phoenix | NO Dynamo Eclot Phoenix | 10 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-10-10 07:52 | model-only | cs2 | Dynamo Eclot Phoenix | Vitality Academy | NO Vitality Academy | 1 | 0.26 | 0.42 | 0.25 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | MARKandLARRY | Orgless | YES MARKandLARRY | 14 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-10 07:52 | model-only | cs2 | Orgless | MARKandLARRY | YES Orgless | 32 | 0.48 | 0.58 | 0.46 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | Rooster | Ice Block | NO Ice Block | 3 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-10-10 06:52 | model-only | dota2 | KukuysV3 | InterActive Philippines | YES KukuysV3 | 4 | 0.35 | 0.46 | 0.34 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | mellren | Honvéd | YES mellren | 10 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | TheChampionGG | 3DMAX Academy | NO 3DMAX Academy | 3 | 0.60 | 0.58 | 0.58 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | XI Esport | THE UNIT | NO THE UNIT | 13 | 0.63 | 0.61 | 0.61 | open | - |
| 2026-10-10 06:52 | model-only | cs2 | Honvéd | mellren | YES Honvéd | 55 | 0.22 | 0.28 | 0.21 | open | - |
| 2026-10-10 06:52 | favourite | dota2 | InterActive Philippines | KukuysV3 | YES InterActive Philippines | 12 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-10 06:52 | favourite | lol | PART TIMERS | West Point Esports PH | YES PART TIMERS | 12 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-10 06:52 | favourite | r6 | Man eSports LFO | 7VEN | YES Man eSports LFO | 12 | 0.65 | 0.61 | 0.61 | open | - |
| 2026-10-10 06:52 | model-only | lol | West Point Esports PH | PART TIMERS | YES West Point Esports PH | 44 | 0.35 | 0.50 | 0.35 | open | - |
| 2026-10-10 06:22 | favourite | ow | Crazy Raccoon | T1 | YES Crazy Raccoon | 6 | 0.72 | 0.68 | 0.68 | open | - |
| 2026-10-10 05:52 | favourite | cs2 | Chinggis Warriors | The Huns Esports | YES Chinggis Warriors | 10 | 0.76 | 0.74 | 0.74 | open | - |
| 2026-10-10 05:52 | model-only | cs2 | The Huns Esports | Chinggis Warriors | YES The Huns Esports | 53 | 0.26 | 0.45 | 0.26 | open | - |
| 2026-10-10 04:52 | favourite | dota2 | Cloud Dawning | Cresent | NO Cresent | 14 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-10-10 04:52 | favourite | dota2 | Cloud Rising | Zenith | YES Cloud Rising | 1 | 0.71 | 0.64 | 0.64 | open | - |
| 2026-10-10 04:52 | model-only | dota2 | Cresent | Cloud Dawning | NO Cloud Dawning | 33 | 0.47 | 0.61 | 0.45 | open | - |
| 2026-10-10 04:52 | favourite | ow | ZANSIDE GAMING | SEIJI ESPORTS | NO SEIJI ESPORTS | 2 | 0.86 | 0.84 | 0.84 | lost | -$1.74 |
| 2026-10-10 02:52 | favourite | cs2 | NEXVOID | 5star | NO 5star | 10 | 0.77 | 0.63 | 0.63 | open | - |
| 2026-10-10 02:47 | favourite | ebasketballgame | New Orleans Pelicans (Zach) | Indiana Pacers (James) | NO Indiana Pacers (James) | 9 | 0.88 | 0.84 | 0.84 | won | $1.01 |
| 2026-10-10 02:47 | favourite | ebasketballgame | Denver Nuggets (Lonzo) | Dallas Mavericks (Cade) | NO Dallas Mavericks (Cade) | 10 | 0.83 | 0.80 | 0.80 | won | $1.60 |

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

