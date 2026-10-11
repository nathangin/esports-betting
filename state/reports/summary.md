# Esports paper trading (fake money)

Updated 2026-10-11 11:52 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 0 | -$19.69 | -100.0% | -13.5c (1) | $980.31 |
| model-only | Elo win model alone (control: ignores the market) | 117 | 14 | 103 | 25 | -$244.39 | -19.0% | -0.5c (113) | $755.61 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 210 | 19 | 191 | 126 | -$150.71 | -10.4% | -2.0c (209) | $849.29 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

1717 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6613 | 0.2357 |
| model | 0.6759 | 0.2414 |
| blend | 0.6627 | 0.2364 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| esoccergame | 1059 | 0.6908 | 0.6797 |
| cs2 | 281 | 0.5840 | 0.6673 |
| ebasketballgame | 243 | 0.6871 | 0.6815 |
| lol | 35 | 0.4622 | 0.7005 |
| dota2 | 33 | 0.5625 | 0.6477 |
| ow | 22 | 0.4138 | 0.4935 |
| r6 | 22 | 0.6444 | 0.7203 |
| valorant | 12 | 0.6525 | 0.6684 |
| mlbb | 10 | 0.6989 | 0.6956 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-11 11:52 | model-only | cs2 | The KnockoutX | Alter Ego | YES The KnockoutX | 22 | 0.24 | 0.40 | 0.23 | open | - |
| 2026-10-11 10:22 | favourite | cs2 | Spirit | Aurora Gaming | NO Aurora Gaming | 1 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-11 09:52 | model-only | cs2 | Fire Flux Esports | Gothic | NO Gothic | 27 | 0.53 | 0.60 | 0.52 | open | - |
| 2026-10-11 09:47 | favourite | esoccergame | RB Leipzig (Kylian) | Mönchengladbach (Bradley) | YES RB Leipzig (Kylian) | 2 | 0.63 | 0.66 | 0.66 | won | $0.70 |
| 2026-10-11 09:21 | favourite | esoccergame | Mönchengladbach (Bradley) | Stuttgart (Frost) | YES Mönchengladbach (Bradley) | 8 | 0.52 | 0.56 | 0.56 | lost | -$4.30 |
| 2026-10-11 09:21 | model-only | cs2 | TheChampionGG | VP.Future 3 | YES TheChampionGG | 37 | 0.39 | 0.45 | 0.39 | open | - |
| 2026-10-11 09:21 | favourite | cs2 | Teletubisie | THE UNIT | YES Teletubisie | 9 | 0.88 | 0.87 | 0.87 | open | - |
| 2026-10-11 09:21 | model-only | cs2 | THE UNIT | Teletubisie | NO Teletubisie | 102 | 0.14 | 0.25 | 0.13 | open | - |
| 2026-10-11 09:21 | favourite | esoccergame | RB Leipzig (Kylian) | Freiburg (Kevin) | YES RB Leipzig (Kylian) | 15 | 0.55 | 0.59 | 0.59 | lost | -$8.51 |
| 2026-10-11 09:06 | favourite | esoccergame | Freiburg (Kevin) | Mönchengladbach (Bradley) | YES Freiburg (Kevin) | 15 | 0.53 | 0.56 | 0.56 | lost | -$8.22 |
| 2026-10-11 08:51 | favourite | mlbb | ONIC | RRQ Hoshi | YES ONIC | 10 | 0.84 | 0.65 | 0.65 | open | - |
| 2026-10-11 07:51 | favourite | mlbb | Invictus Gaming | AC Esports | YES Invictus Gaming | 10 | 0.84 | 0.63 | 0.63 | lost | -$8.50 |
| 2026-10-11 07:51 | model-only | dota2 | Team Spirit | PARIVISION | NO PARIVISION | 47 | 0.31 | 0.44 | 0.31 | open | - |
| 2026-10-11 07:51 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 12 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-11 07:51 | favourite | lol | Saigon Warriors | MVK Academy | NO MVK Academy | 10 | 0.80 | 0.79 | 0.79 | open | - |
| 2026-10-11 07:51 | favourite | cs2 | Rooster | Orgless | NO Orgless | 11 | 0.77 | 0.62 | 0.62 | open | - |
| 2026-10-11 07:51 | favourite | ow | HUNENG | SHENGSHI Esports | YES HUNENG | 10 | 0.82 | 0.70 | 0.70 | won | $1.69 |
| 2026-10-11 07:51 | favourite | valorant | G2 Esports | T1 | YES G2 Esports | 13 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-11 07:51 | model-only | valorant | T1 | G2 Esports | NO G2 Esports | 38 | 0.39 | 0.47 | 0.39 | open | - |
| 2026-10-11 06:51 | model-only | cs2 | Elite Klan | Vitality Academy | YES Elite Klan | 73 | 0.20 | 0.35 | 0.19 | open | - |
| 2026-10-11 06:51 | favourite | lol | West Point Esports PH | Nothin'Here | NO Nothin'Here | 14 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-11 06:51 | favourite | cs2 | STATE | WRAITH PCIFIC | YES STATE | 12 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-10-11 06:51 | favourite | cs2 | ILLYRIANS | MORROW | YES ILLYRIANS | 12 | 0.63 | 0.60 | 0.60 | won | $4.24 |
| 2026-10-11 06:51 | favourite | cs2 | Just_Players | Misa Esports | YES Just_Players | 12 | 0.70 | 0.69 | 0.69 | won | $3.42 |
| 2026-10-11 06:51 | model-only | cs2 | Misa Esports | Just_Players | YES Misa Esports | 19 | 0.32 | 0.51 | 0.31 | lost | -$6.37 |

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

