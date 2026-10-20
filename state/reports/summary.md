# Esports paper trading (fake money)

Updated 2026-10-20 11:09 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 268 | 31 | 237 | 62 | -$503.15 | -19.4% | -1.1c (261) | $496.85 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 413 | 42 | 371 | 257 | -$102.67 | -3.8% | -1.4c (406) | $897.33 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

883 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5659 | 0.1926 |
| model | 0.6534 | 0.2309 |
| blend | 0.5645 | 0.1921 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 563 | 0.5716 | 0.6568 |
| dota2 | 143 | 0.5475 | 0.6467 |
| lol | 60 | 0.5511 | 0.7049 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 22 | 0.6473 | 0.6972 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-20 10:54 | favourite | dota2 | Team Lynx | Power Rangers | YES Team Lynx | 13 | 0.64 | 0.63 | 0.63 | open | - |
| 2026-10-20 10:54 | model-only | dota2 | Team Lynx | Power Rangers | YES Team Lynx | 14 | 0.64 | 0.76 | 0.63 | open | - |
| 2026-10-20 10:54 | favourite | cs2 | Liquid | magic | YES Liquid | 15 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-20 10:54 | model-only | cs2 | magic | Liquid | YES magic | 15 | 0.43 | 0.48 | 0.43 | open | - |
| 2026-10-20 10:54 | favourite | cs2 | Sangal | Aurora Young Blood | NO Aurora Young Blood | 10 | 0.86 | 0.84 | 0.84 | open | - |
| 2026-10-20 10:54 | model-only | cs2 | Aurora Young Blood | Sangal | YES Aurora Young Blood | 53 | 0.17 | 0.40 | 0.16 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | ILLYRIANS | BakS eSports | NO BakS eSports | 23 | 0.40 | 0.47 | 0.38 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | BC.Game Esports | BBL | YES BC.Game Esports | 13 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | BASEMENT BOYS | FaZe | NO FaZe | 24 | 0.37 | 0.44 | 0.34 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | FaZe | BASEMENT BOYS | YES FaZe | 13 | 0.68 | 0.66 | 0.66 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | ex-Zero Tenacity | FORZE Reload | YES ex-Zero Tenacity | 22 | 0.41 | 0.50 | 0.40 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | FORZE Reload | ex-Zero Tenacity | YES FORZE Reload | 14 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | BBL | BC.Game Esports | YES BBL | 25 | 0.36 | 0.53 | 0.36 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | BakS eSports | ILLYRIANS | YES BakS eSports | 14 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | Eternal Fire | Infinite | YES Eternal Fire | 11 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | MORROW | maybe | YES MORROW | 16 | 0.55 | 0.53 | 0.53 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | Nexus | Envy | YES Nexus | 18 | 0.50 | 0.63 | 0.48 | open | - |
| 2026-10-20 09:54 | favourite | cs2 | Envy | Nexus | YES Envy | 16 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-20 09:54 | model-only | cs2 | Infinite | Eternal Fire | YES Infinite | 35 | 0.26 | 0.36 | 0.26 | open | - |
| 2026-10-20 07:53 | favourite | cs2 | NEXVOID | Vitalem Aerem | YES NEXVOID | 11 | 0.79 | 0.76 | 0.76 | open | - |
| 2026-10-20 07:53 | model-only | cs2 | PRIVATE | Alliance | NO Alliance | 22 | 0.42 | 0.53 | 0.42 | won | $12.38 |
| 2026-10-20 07:53 | favourite | cs2 | Alliance | PRIVATE | YES Alliance | 14 | 0.59 | 0.58 | 0.58 | lost | -$8.50 |
| 2026-10-20 07:53 | favourite | cs2 | Metizport | ex-RUSTEC | NO ex-RUSTEC | 6 | 0.55 | 0.53 | 0.53 | open | - |
| 2026-10-20 07:53 | model-only | dota2 | Power Rangers | HULIGANI | YES Power Rangers | 26 | 0.35 | 0.55 | 0.34 | open | - |
| 2026-10-20 07:53 | favourite | dota2 | HULIGANI | Power Rangers | YES HULIGANI | 13 | 0.66 | 0.66 | 0.66 | open | - |

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

