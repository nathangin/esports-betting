# Esports paper trading (fake money)

Updated 2026-10-29 11:05 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 1 | 0 | 0 | $0.00 | - | +4.0c (1) | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 427 | 40 | 387 | 130 | -$69.10 | -1.7% | -0.4c (419) | $930.90 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 668 | 52 | 616 | 406 | -$321.33 | -7.3% | -1.5c (658) | $678.67 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1428 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5821 | 0.2000 |
| model | 0.6562 | 0.2323 |
| blend | 0.5819 | 0.2001 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 930 | 0.5966 | 0.6634 |
| dota2 | 219 | 0.5493 | 0.6323 |
| lol | 83 | 0.5638 | 0.7223 |
| ow | 83 | 0.5090 | 0.5369 |
| valorant | 69 | 0.5804 | 0.6781 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-29 10:50 | model-only | dota2 | LEGION | Team Spirit | NO Team Spirit | 175 | 0.10 | 0.31 | 0.09 | open | - |
| 2026-10-29 10:50 | favourite | cs2 | ex-INOX Division | Spirit Academy | YES ex-INOX Division | 12 | 0.53 | 0.51 | 0.51 | open | - |
| 2026-10-29 10:50 | favourite | cs2 | MORROW | Honvéd | NO Honvéd | 12 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-10-29 10:50 | favourite | cs2 | FaZe | GamerLegion | YES FaZe | 11 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-29 10:20 | favourite | cs2 | gothboiclique | Revenge | YES gothboiclique | 1 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-29 10:20 | model-only | cs2 | Revenge | gothboiclique | NO gothboiclique | 50 | 0.35 | 0.53 | 0.34 | open | - |
| 2026-10-29 10:20 | favourite | cs2 | MOUZ NXT | eSuba | NO eSuba | 9 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-10-29 10:20 | model-only | cs2 | eSuba | MOUZ NXT | YES eSuba | 52 | 0.34 | 0.58 | 0.34 | open | - |
| 2026-10-29 09:50 | favourite | valorant | TEC Esports | World Sports Invictus Gaming | YES TEC Esports | 9 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-10-29 09:50 | model-only | valorant | World Sports Invictus Gaming | TEC Esports | NO TEC Esports | 52 | 0.34 | 0.44 | 0.33 | open | - |
| 2026-10-29 09:50 | favourite | cs2 | Vitality | Natus Vincere | YES Vitality | 9 | 0.71 | 0.71 | 0.71 | open | - |
| 2026-10-29 09:50 | favourite | cs2 | BIG | Eternal Fire | YES BIG | 10 | 0.63 | 0.63 | 0.63 | open | - |
| 2026-10-29 07:50 | model-only | dota2 | Astra Invicta | Team Liquid | YES Astra Invicta | 34 | 0.36 | 0.41 | 0.31 | open | - |
| 2026-10-29 07:50 | model-only | cs2 | HOTU | B8 | NO B8 | 42 | 0.42 | 0.53 | 0.45 | open | - |
| 2026-10-29 07:50 | favourite | cs2 | B8 | HOTU | YES B8 | 11 | 0.59 | 0.55 | 0.55 | open | - |
| 2026-10-29 07:50 | blend | dota2 | Team Liquid | Astra Invicta | NO Astra Invicta | 30 | 0.65 | 0.71 | 0.69 | open | - |
| 2026-10-29 07:50 | favourite | dota2 | Team Liquid | Astra Invicta | NO Astra Invicta | 10 | 0.65 | 0.69 | 0.69 | open | - |
| 2026-10-29 07:50 | model-only | valorant | Unsettled Resentment | KeepBest Gaming | NO KeepBest Gaming | 50 | 0.35 | 0.55 | 0.40 | open | - |
| 2026-10-29 07:50 | favourite | valorant | KeepBest Gaming | Unsettled Resentment | YES KeepBest Gaming | 3 | 0.68 | 0.60 | 0.60 | open | - |
| 2026-10-29 06:50 | favourite | cs2 | FUT Esports | Nemiga | YES FUT Esports | 9 | 0.69 | 0.69 | 0.69 | lost | -$6.35 |
| 2026-10-28 19:53 | model-only | valorant | KRÜ Blaze | Team Liquid Brazil | YES KRÜ Blaze | 8 | 0.16 | 0.35 | 0.15 | won | $6.64 |
| 2026-10-28 16:53 | model-only | dota2 | LEGION | GamerLegion | NO GamerLegion | 13 | 0.32 | 0.55 | 0.31 | lost | -$4.36 |
| 2026-10-28 16:23 | favourite | cs2 | Privateer Gaming | wnT | YES Privateer Gaming | 11 | 0.61 | 0.59 | 0.59 | won | $4.10 |
| 2026-10-28 16:23 | model-only | cs2 | wnT | Privateer Gaming | NO Privateer Gaming | 32 | 0.43 | 0.56 | 0.41 | lost | -$14.31 |
| 2026-10-28 15:53 | favourite | cs2 | BLUEJAYS.de | Team LEISURE | YES BLUEJAYS.de | 9 | 0.77 | 0.75 | 0.75 | lost | -$7.05 |

## Backtest on real Kalshi prices

8779 settled matches from 2026-05-28 to 2026-10-26, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 2012 | $8,014.92 | -$990.92 | -12.4% | -20.6% to -4.1% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4205 | $16,392.93 | -$775.93 | -4.7% | -7.0% to -2.5% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3757 | $9,447.49 | -$982.49 | -10.4% | -15.7% to -4.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8554 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5736 | 0.1961 | 69.2% |
| model | 0.6609 | 0.2344 | 59.5% |
| blend | 0.5732 | 0.1960 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1402 | 0.525 | 0.529 |
| (0.55, 0.6] | 1444 | 0.577 | 0.551 |
| (0.6, 0.65] | 1325 | 0.626 | 0.629 |
| (0.65, 0.7] | 1152 | 0.676 | 0.702 |
| (0.7, 0.75] | 964 | 0.726 | 0.772 |
| (0.75, 0.8] | 823 | 0.776 | 0.810 |
| (0.8, 0.85] | 698 | 0.826 | 0.827 |
| (0.85, 0.9] | 521 | 0.877 | 0.902 |
| (0.9, 1.0] | 450 | 0.932 | 0.956 |

