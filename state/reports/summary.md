# Esports paper trading (fake money)

Updated 2026-10-28 18:43 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 419 | 38 | 381 | 126 | -$173.25 | -4.3% | -0.6c (414) | $826.75 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 656 | 46 | 610 | 405 | -$291.14 | -6.7% | -1.4c (651) | $708.86 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1400 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5777 | 0.1981 |
| model | 0.6546 | 0.2316 |
| blend | 0.5771 | 0.1980 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 911 | 0.5923 | 0.6622 |
| dota2 | 213 | 0.5443 | 0.6296 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 82 | 0.5655 | 0.7200 |
| valorant | 67 | 0.5622 | 0.6739 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-28 16:53 | model-only | dota2 | LEGION | GamerLegion | NO GamerLegion | 13 | 0.32 | 0.55 | 0.31 | open | - |
| 2026-10-28 16:23 | favourite | cs2 | Privateer Gaming | wnT | YES Privateer Gaming | 11 | 0.61 | 0.59 | 0.59 | won | $4.10 |
| 2026-10-28 16:23 | model-only | cs2 | wnT | Privateer Gaming | NO Privateer Gaming | 32 | 0.43 | 0.56 | 0.41 | lost | -$14.31 |
| 2026-10-28 15:53 | favourite | cs2 | Spirit | Natus Vincere | YES Spirit | 10 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-10-28 15:53 | favourite | cs2 | BLUEJAYS.de | Team LEISURE | YES BLUEJAYS.de | 9 | 0.77 | 0.75 | 0.75 | open | - |
| 2026-10-28 15:53 | model-only | cs2 | Team LEISURE | BLUEJAYS.de | YES Team LEISURE | 11 | 0.25 | 0.48 | 0.25 | open | - |
| 2026-10-28 15:23 | favourite | cs2 | Aurora Young Blood | DimoniX Esports | YES Aurora Young Blood | 4 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-10-28 15:23 | model-only | cs2 | DimoniX Esports | Aurora Young Blood | NO Aurora Young Blood | 1 | 0.37 | 0.45 | 0.36 | open | - |
| 2026-10-28 15:23 | favourite | cs2 | Team Nemesis Academy | SPARX | NO SPARX | 6 | 0.66 | 0.63 | 0.63 | open | - |
| 2026-10-28 14:53 | favourite | cs2 | BIG | fnatic | YES BIG | 12 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-28 14:53 | model-only | cs2 | fnatic | BIG | NO BIG | 36 | 0.44 | 0.60 | 0.44 | open | - |
| 2026-10-28 13:53 | favourite | dota2 | Team Synapse | SOLID | YES Team Synapse | 10 | 0.68 | 0.66 | 0.66 | won | $3.04 |
| 2026-10-28 13:53 | favourite | dota2 | angry birds | Roshan Hunters | NO Roshan Hunters | 9 | 0.75 | 0.73 | 0.73 | open | - |
| 2026-10-28 13:53 | model-only | dota2 | Roshan Hunters | angry birds | NO angry birds | 56 | 0.28 | 0.45 | 0.27 | open | - |
| 2026-10-28 13:53 | model-only | dota2 | OG | Team Spirit | YES OG | 91 | 0.17 | 0.27 | 0.17 | open | - |
| 2026-10-28 13:53 | favourite | cs2 | 6yuBoJlbl | Sokerorg | YES 6yuBoJlbl | 12 | 0.56 | 0.53 | 0.53 | lost | -$6.93 |
| 2026-10-28 12:52 | favourite | cs2 | FURIA | Liquid | YES FURIA | 9 | 0.75 | 0.74 | 0.74 | won | $2.13 |
| 2026-10-28 12:52 | model-only | cs2 | Liquid | FURIA | NO FURIA | 60 | 0.26 | 0.38 | 0.26 | lost | -$16.41 |
| 2026-10-28 12:52 | model-only | cs2 | HOTU | GamerLegion | NO GamerLegion | 33 | 0.48 | 0.65 | 0.47 | won | $16.58 |
| 2026-10-28 12:52 | favourite | cs2 | GamerLegion | HOTU | YES GamerLegion | 12 | 0.53 | 0.53 | 0.53 | lost | -$6.57 |
| 2026-10-28 12:22 | favourite | cs2 | Eternal Fire | Team Nemesis | YES Eternal Fire | 8 | 0.79 | 0.79 | 0.79 | won | $1.58 |
| 2026-10-28 10:52 | favourite | dota2 | angry birds | Level Up Academy | YES angry birds | 7 | 0.88 | 0.87 | 0.87 | won | $0.78 |
| 2026-10-28 10:52 | favourite | cs2 | Inner Circle Academy | Saint Sinners | YES Inner Circle Academy | 11 | 0.60 | 0.57 | 0.57 | lost | -$6.79 |
| 2026-10-28 10:52 | favourite | cs2 | SINQU | Fortress | NO Fortress | 12 | 0.54 | 0.52 | 0.52 | won | $5.31 |
| 2026-10-28 10:22 | favourite | cs2 | UNiTY esports | Copenhagen Wolves | NO Copenhagen Wolves | 9 | 0.73 | 0.72 | 0.72 | won | $2.30 |

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

