# Esports paper trading (fake money)

Updated 2026-10-30 18:44 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 450 | 36 | 414 | 139 | -$133.64 | -3.0% | -0.5c (445) | $866.36 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 723 | 50 | 673 | 443 | -$359.32 | -7.7% | -1.4c (717) | $640.68 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1522 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5775 | 0.1981 |
| model | 0.6522 | 0.2305 |
| blend | 0.5770 | 0.1981 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 999 | 0.5907 | 0.6593 |
| dota2 | 234 | 0.5427 | 0.6300 |
| ow | 87 | 0.4980 | 0.5250 |
| lol | 85 | 0.5694 | 0.7245 |
| valorant | 73 | 0.5916 | 0.6722 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-30 16:54 | favourite | cs2 | Phantom | Lavked | NO Lavked | 1 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-10-30 15:54 | favourite | cs2 | Gremio Esports | DFX Peek | YES Gremio Esports | 7 | 0.71 | 0.71 | 0.71 | open | - |
| 2026-10-30 15:54 | model-only | cs2 | DFX Peek | Gremio Esports | YES DFX Peek | 1 | 0.30 | 0.50 | 0.29 | open | - |
| 2026-10-30 15:24 | favourite | cs2 | Aurora Young Blood | Ducks | YES Aurora Young Blood | 9 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-30 15:24 | model-only | cs2 | Ducks | Aurora Young Blood | NO Aurora Young Blood | 4 | 0.39 | 0.50 | 0.38 | open | - |
| 2026-10-30 15:24 | favourite | cs2 | Low Cortisol | ALKA | YES Low Cortisol | 8 | 0.71 | 0.70 | 0.70 | won | $2.20 |
| 2026-10-30 15:09 | favourite | cs2 | BC.Game Esports | OG | YES BC.Game Esports | 8 | 0.70 | 0.70 | 0.70 | won | $2.28 |
| 2026-10-30 15:09 | model-only | cs2 | OG | BC.Game Esports | NO BC.Game Esports | 19 | 0.31 | 0.42 | 0.30 | lost | -$6.18 |
| 2026-10-30 15:09 | favourite | cs2 | Metizport | SNITKO Esports | NO SNITKO Esports | 7 | 0.89 | 0.89 | 0.89 | won | $0.72 |
| 2026-10-30 13:53 | favourite | dota2 | old blood | Roshan Hunters | YES old blood | 12 | 0.52 | 0.50 | 0.50 | open | - |
| 2026-10-30 13:53 | favourite | cs2 | Omega | WRAITH PCIFIC | YES Omega | 9 | 0.65 | 0.65 | 0.65 | won | $3.00 |
| 2026-10-30 13:53 | favourite | cs2 | Apogee Esports | ILLYRIANS | YES Apogee Esports | 9 | 0.69 | 0.69 | 0.69 | won | $2.65 |
| 2026-10-30 13:53 | favourite | cs2 | Leo Team | Honvéd | NO Honvéd | 6 | 0.76 | 0.76 | 0.76 | won | $1.36 |
| 2026-10-30 13:53 | model-only | cs2 | Honvéd | Leo Team | NO Leo Team | 63 | 0.25 | 0.35 | 0.24 | lost | -$16.58 |
| 2026-10-30 13:53 | favourite | cs2 | MOUZ | FURIA | YES MOUZ | 10 | 0.59 | 0.59 | 0.59 | lost | -$6.07 |
| 2026-10-30 11:53 | favourite | cs2 | ShindeN | Isurus | NO Isurus | 1 | 0.82 | 0.82 | 0.82 | won | $0.16 |
| 2026-10-30 11:53 | model-only | cs2 | Eternal Fire | MIBR | YES Eternal Fire | 43 | 0.40 | 0.56 | 0.40 | won | $25.07 |
| 2026-10-30 11:53 | favourite | cs2 | MIBR | Eternal Fire | YES MIBR | 10 | 0.60 | 0.60 | 0.60 | lost | -$6.17 |
| 2026-10-30 11:53 | model-only | cs2 | Isurus | ShindeN | YES Isurus | 89 | 0.19 | 0.38 | 0.18 | lost | -$17.87 |
| 2026-10-30 11:53 | favourite | cs2 | naocopulas | QUINTESSENCIA | YES naocopulas | 8 | 0.74 | 0.74 | 0.74 | won | $1.97 |
| 2026-10-30 11:53 | model-only | dota2 | OG | Team Liquid | NO Team Liquid | 49 | 0.35 | 0.54 | 0.35 | lost | -$17.94 |
| 2026-10-30 11:53 | favourite | dota2 | Team Liquid | OG | NO OG | 1 | 0.65 | 0.65 | 0.65 | won | $0.33 |
| 2026-10-30 10:53 | favourite | dota2 | Team Synapse | potn9ki | YES Team Synapse | 7 | 0.84 | 0.82 | 0.82 | won | $1.05 |
| 2026-10-30 10:53 | model-only | dota2 | potn9ki | Team Synapse | NO Team Synapse | 33 | 0.20 | 0.33 | 0.18 | lost | -$6.97 |
| 2026-10-30 10:53 | favourite | cs2 | Vitality | Nemiga | YES Vitality | 7 | 0.82 | 0.82 | 0.82 | lost | -$5.82 |

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

