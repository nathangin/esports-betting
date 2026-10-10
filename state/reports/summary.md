# Esports paper trading (fake money)

Updated 2026-10-10 09:33 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 99 | 17 | 82 | 19 | -$208.62 | -19.1% | -0.8c (89) | $791.38 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 177 | 23 | 154 | 100 | -$160.26 | -13.4% | -1.2c (173) | $839.74 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1090 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6583 | 0.2343 |
| model | 0.6749 | 0.2411 |
| blend | 0.6600 | 0.2351 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 625 | 0.6954 | 0.6792 |
| cs2 | 234 | 0.5968 | 0.6672 |
| ebasketballgame | 139 | 0.6793 | 0.6871 |
| lol | 29 | 0.3933 | 0.6710 |
| dota2 | 26 | 0.5941 | 0.6300 |
| r6 | 19 | 0.6783 | 0.7255 |
| valorant | 10 | 0.6330 | 0.6398 |
| ow | 8 | 0.3528 | 0.4414 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-10 09:22 | model-only | dota2 | Team Spirit | Team Yandex | NO Team Yandex | 39 | 0.38 | 0.47 | 0.38 | open | - |
| 2026-10-10 09:22 | model-only | cs2 | VP.Future 3 | EAC Extra | YES VP.Future 3 | 1 | 0.36 | 0.55 | 0.34 | open | - |
| 2026-10-10 08:52 | model-only | cs2 | PURE | Sangal | NO Sangal | 1 | 0.35 | 0.43 | 0.34 | open | - |
| 2026-10-10 08:52 | favourite | cs2 | Black Phoenix | Nexus | YES Black Phoenix | 5 | 0.53 | 0.54 | 0.54 | open | - |
| 2026-10-10 08:52 | model-only | cs2 | Black Phoenix | Nexus | YES Black Phoenix | 28 | 0.53 | 0.61 | 0.54 | open | - |
| 2026-10-10 08:52 | favourite | cs2 | FaZe | NAVI Junior | YES FaZe | 9 | 0.89 | 0.89 | 0.89 | open | - |
| 2026-10-10 08:52 | favourite | cs2 | fnatic | HOTU | YES fnatic | 15 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-10-10 08:52 | model-only | cs2 | HOTU | fnatic | YES HOTU | 31 | 0.48 | 0.57 | 0.48 | open | - |
| 2026-10-10 08:22 | favourite | cs2 | KZG | BGNS Orange | YES KZG | 1 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | MARKandLARRY | Orgless | YES MARKandLARRY | 14 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | Rooster | Ice Block | NO Ice Block | 3 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-10-10 07:52 | model-only | cs2 | Orgless | MARKandLARRY | YES Orgless | 32 | 0.48 | 0.58 | 0.46 | open | - |
| 2026-10-10 07:52 | favourite | ow | Solus Victorem | HUNENG | YES Solus Victorem | 10 | 0.78 | 0.71 | 0.71 | open | - |
| 2026-10-10 07:52 | model-only | cs2 | Dynamo Eclot Phoenix | Vitality Academy | NO Vitality Academy | 1 | 0.26 | 0.42 | 0.25 | open | - |
| 2026-10-10 07:52 | favourite | cs2 | Vitality Academy | Dynamo Eclot Phoenix | NO Dynamo Eclot Phoenix | 10 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-10-10 06:52 | model-only | dota2 | KukuysV3 | InterActive Philippines | YES KukuysV3 | 4 | 0.35 | 0.46 | 0.34 | open | - |
| 2026-10-10 06:52 | model-only | cs2 | Honvéd | mellren | YES Honvéd | 55 | 0.22 | 0.28 | 0.21 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | mellren | Honvéd | YES mellren | 10 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | TheChampionGG | 3DMAX Academy | NO 3DMAX Academy | 3 | 0.60 | 0.58 | 0.58 | open | - |
| 2026-10-10 06:52 | favourite | cs2 | XI Esport | THE UNIT | NO THE UNIT | 13 | 0.63 | 0.61 | 0.61 | open | - |
| 2026-10-10 06:52 | favourite | r6 | Man eSports LFO | 7VEN | YES Man eSports LFO | 12 | 0.65 | 0.61 | 0.61 | open | - |
| 2026-10-10 06:52 | favourite | dota2 | InterActive Philippines | KukuysV3 | YES InterActive Philippines | 12 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-10 06:52 | model-only | lol | West Point Esports PH | PART TIMERS | YES West Point Esports PH | 44 | 0.35 | 0.50 | 0.35 | open | - |
| 2026-10-10 06:52 | favourite | lol | PART TIMERS | West Point Esports PH | YES PART TIMERS | 12 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-10 06:22 | favourite | ow | Crazy Raccoon | T1 | YES Crazy Raccoon | 6 | 0.72 | 0.68 | 0.68 | open | - |

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

