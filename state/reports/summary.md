# Esports paper trading (fake money)

Updated 2026-10-26 08:51 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 372 | 33 | 339 | 108 | -$232.57 | -6.6% | -0.8c (368) | $767.43 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 581 | 46 | 535 | 360 | -$202.03 | -5.2% | -1.4c (577) | $797.97 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1269 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5758 | 0.1972 |
| model | 0.6571 | 0.2328 |
| blend | 0.5749 | 0.1969 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 818 | 0.5881 | 0.6639 |
| dota2 | 188 | 0.5532 | 0.6409 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 77 | 0.5593 | 0.7265 |
| valorant | 59 | 0.5641 | 0.6698 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-26 07:50 | favourite | cs2 | UNiTY esports | gothboiclique | NO gothboiclique | 8 | 0.90 | 0.88 | 0.88 | open | - |
| 2026-10-26 07:50 | model-only | cs2 | gothboiclique | UNiTY esports | YES gothboiclique | 103 | 0.14 | 0.24 | 0.12 | open | - |
| 2026-10-26 07:50 | favourite | cs2 | Nexus | Revise | YES Nexus | 9 | 0.79 | 0.77 | 0.77 | open | - |
| 2026-10-26 07:50 | model-only | cs2 | Revise | Nexus | NO Nexus | 31 | 0.25 | 0.30 | 0.23 | open | - |
| 2026-10-26 07:50 | favourite | cs2 | Falcons Force | KUUSAMO.gg | YES Falcons Force | 11 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-26 07:50 | favourite | cs2 | Team Nemesis | INOX Division | NO INOX Division | 10 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-10-26 07:50 | model-only | cs2 | INOX Division | Team Nemesis | NO Team Nemesis | 56 | 0.26 | 0.37 | 0.25 | open | - |
| 2026-10-26 06:50 | favourite | dota2 | OG | GamerLegion | NO GamerLegion | 13 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-26 06:50 | favourite | cs2 | MOUZ | TheMongolz | NO TheMongolz | 10 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-10-26 06:50 | model-only | cs2 | TheMongolz | MOUZ | YES TheMongolz | 59 | 0.25 | 0.39 | 0.24 | open | - |
| 2026-10-26 06:50 | favourite | cs2 | Aurora Gaming | Nemiga | YES Aurora Gaming | 11 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-10-26 04:50 | model-only | dota2 | Team Kinetix | Direborn | NO Direborn | 4 | 0.22 | 0.37 | 0.22 | open | - |
| 2026-10-26 04:50 | favourite | dota2 | Direborn | Team Kinetix | NO Team Kinetix | 10 | 0.78 | 0.78 | 0.78 | open | - |
| 2026-10-26 01:50 | favourite | dota2 | Direborn | Cloud Dawning | YES Direborn | 5 | 0.77 | 0.76 | 0.76 | won | $1.08 |
| 2026-10-26 01:50 | model-only | dota2 | Cloud Dawning | Direborn | NO Direborn | 55 | 0.27 | 0.35 | 0.24 | lost | -$15.61 |
| 2026-10-26 01:50 | favourite | cs2 | Off Chops | Ground Zero | NO Ground Zero | 9 | 0.80 | 0.79 | 0.79 | won | $1.69 |
| 2026-10-26 01:50 | favourite | cs2 | NEXVOID | Alter Ego | NO Alter Ego | 6 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-26 01:50 | model-only | cs2 | Alter Ego | NEXVOID | YES Alter Ego | 30 | 0.45 | 0.51 | 0.43 | open | - |
| 2026-10-25 19:23 | favourite | cs2 | Marsborne | LAG Gaming | NO LAG Gaming | 1 | 0.64 | 0.63 | 0.63 | lost | -$0.66 |
| 2026-10-25 15:53 | favourite | cs2 | FURIA | Natus Vincere | YES FURIA | 9 | 0.54 | 0.54 | 0.54 | lost | -$5.02 |
| 2026-10-25 15:23 | favourite | cs2 | DINERO | DimoniX Esports | NO DimoniX Esports | 2 | 0.60 | 0.61 | 0.61 | lost | -$1.24 |
| 2026-10-25 14:53 | favourite | r6 | FaZe Clan | FURIA Esports | NO FURIA Esports | 11 | 0.69 | 0.69 | 0.69 | lost | -$7.76 |
| 2026-10-25 14:53 | model-only | r6 | FURIA Esports | FaZe Clan | YES FURIA Esports | 13 | 0.32 | 0.37 | 0.31 | won | $8.64 |
| 2026-10-25 13:52 | favourite | cs2 | Brute | Infinite | YES Brute | 13 | 0.58 | 0.56 | 0.56 | won | $5.23 |
| 2026-10-25 13:52 | favourite | cs2 | Team ACES | Inner Circle Academy | YES Team ACES | 9 | 0.86 | 0.82 | 0.82 | won | $1.18 |

## Backtest on real Kalshi prices

8346 settled matches from 2026-05-28 to 2026-10-19, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 23 | $422.99 | -$10.99 | -2.6% | -39.0% to +46.3% | 57% | -0.0c | 8% |
| model only | 1998 | $8,526.95 | -$990.95 | -11.6% | -20.1% to -3.0% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4018 | $16,341.50 | -$762.50 | -4.7% | -6.9% to -2.4% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3742 | $8,889.87 | -$982.87 | -11.1% | -16.6% to -5.4% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8121 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5723 | 0.1955 | 69.3% |
| model | 0.6605 | 0.2343 | 59.6% |
| blend | 0.5719 | 0.1954 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1335 | 0.525 | 0.524 |
| (0.55, 0.6] | 1359 | 0.577 | 0.550 |
| (0.6, 0.65] | 1254 | 0.626 | 0.635 |
| (0.65, 0.7] | 1092 | 0.676 | 0.702 |
| (0.7, 0.75] | 921 | 0.726 | 0.773 |
| (0.75, 0.8] | 786 | 0.776 | 0.812 |
| (0.8, 0.85] | 668 | 0.826 | 0.826 |
| (0.85, 0.9] | 503 | 0.877 | 0.903 |
| (0.9, 1.0] | 428 | 0.932 | 0.956 |

