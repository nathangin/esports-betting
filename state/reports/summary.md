# Esports paper trading (fake money)

Updated 2026-10-20 16:24 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 271 | 25 | 246 | 66 | -$444.66 | -16.6% | -1.1c (266) | $555.34 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 420 | 35 | 385 | 268 | -$89.35 | -3.2% | -1.4c (416) | $910.65 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

903 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5678 | 0.1932 |
| model | 0.6551 | 0.2317 |
| blend | 0.5665 | 0.1927 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 580 | 0.5750 | 0.6597 |
| dota2 | 146 | 0.5456 | 0.6457 |
| lol | 60 | 0.5511 | 0.7049 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 22 | 0.6473 | 0.6972 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-20 15:54 | model-only | cs2 | Lavked | ex-6666 | NO ex-6666 | 2 | 0.38 | 0.48 | 0.37 | open | - |
| 2026-10-20 14:54 | favourite | cs2 | B8 Academy | maybe | YES B8 Academy | 4 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-20 13:54 | model-only | dota2 | Team Synapse | Yellow Submarine | YES Team Synapse | 25 | 0.26 | 0.40 | 0.24 | open | - |
| 2026-10-20 13:54 | model-only | cs2 | ex-Zero Tenacity | FOKUS | YES ex-Zero Tenacity | 32 | 0.33 | 0.52 | 0.34 | open | - |
| 2026-10-20 12:54 | favourite | cs2 | Revise | Wingman | YES Revise | 10 | 0.65 | 0.64 | 0.64 | open | - |
| 2026-10-20 12:54 | favourite | cs2 | Team Nemesis | Apogee Esports | NO Apogee Esports | 12 | 0.69 | 0.68 | 0.68 | open | - |
| 2026-10-20 12:54 | favourite | cs2 | Iberian Soul | JiJieHao | YES Iberian Soul | 16 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-10-20 12:54 | favourite | cs2 | Heroic | HyperSpirit | YES Heroic | 10 | 0.89 | 0.89 | 0.89 | won | $1.03 |
| 2026-10-20 12:54 | favourite | cs2 | BakS eSports | mellren | YES BakS eSports | 15 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-10-20 12:54 | favourite | cs2 | Luminosity | ASTRAL | NO ASTRAL | 15 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-20 10:54 | model-only | cs2 | magic | Liquid | YES magic | 15 | 0.43 | 0.48 | 0.43 | won | $8.29 |
| 2026-10-20 10:54 | model-only | cs2 | Aurora Young Blood | Sangal | YES Aurora Young Blood | 53 | 0.17 | 0.40 | 0.16 | lost | -$9.54 |
| 2026-10-20 10:54 | favourite | cs2 | Sangal | Aurora Young Blood | NO Aurora Young Blood | 10 | 0.86 | 0.84 | 0.84 | won | $1.31 |
| 2026-10-20 10:54 | favourite | dota2 | Team Lynx | Power Rangers | YES Team Lynx | 13 | 0.64 | 0.63 | 0.63 | won | $4.47 |
| 2026-10-20 10:54 | favourite | cs2 | Liquid | magic | YES Liquid | 15 | 0.56 | 0.56 | 0.56 | lost | -$8.66 |
| 2026-10-20 10:54 | model-only | dota2 | Team Lynx | Power Rangers | YES Team Lynx | 14 | 0.64 | 0.76 | 0.63 | won | $4.81 |
| 2026-10-20 09:54 | model-only | cs2 | ILLYRIANS | BakS eSports | NO BakS eSports | 23 | 0.40 | 0.47 | 0.38 | lost | -$9.59 |
| 2026-10-20 09:54 | model-only | cs2 | BBL | BC.Game Esports | YES BBL | 25 | 0.36 | 0.53 | 0.36 | lost | -$9.41 |
| 2026-10-20 09:54 | favourite | cs2 | BC.Game Esports | BBL | YES BC.Game Esports | 13 | 0.64 | 0.64 | 0.64 | won | $4.47 |
| 2026-10-20 09:54 | model-only | cs2 | BASEMENT BOYS | FaZe | NO FaZe | 24 | 0.37 | 0.44 | 0.34 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | FaZe | BASEMENT BOYS | YES FaZe | 13 | 0.68 | 0.66 | 0.66 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | ex-Zero Tenacity | FORZE Reload | YES ex-Zero Tenacity | 22 | 0.41 | 0.50 | 0.40 | won | $12.60 |
| 2026-10-20 09:54 | favourite | cs2 | FORZE Reload | ex-Zero Tenacity | YES FORZE Reload | 14 | 0.60 | 0.60 | 0.60 | lost | -$8.64 |
| 2026-10-20 09:54 | favourite | cs2 | MORROW | maybe | YES MORROW | 16 | 0.55 | 0.53 | 0.53 | won | $6.92 |
| 2026-10-20 09:54 | favourite | cs2 | BakS eSports | ILLYRIANS | YES BakS eSports | 14 | 0.63 | 0.62 | 0.62 | won | $4.95 |

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

