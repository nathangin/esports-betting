# Esports paper trading (fake money)

Updated 2026-10-06 14:43 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 24 | 5 | 19 | 4 | $51.34 | +23.4% | -0.5c (24) | $1,051.34 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 44 | 9 | 35 | 26 | -$10.74 | -3.9% | -1.0c (44) | $989.26 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

39 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5137 | 0.1680 |
| model | 0.6380 | 0.2227 |
| blend | 0.5117 | 0.1669 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 15 | 0.6426 | 0.6234 |
| lol | 9 | 0.2057 | 0.6560 |
| r6 | 6 | 0.8571 | 0.8141 |
| dota2 | 5 | 0.5126 | 0.5709 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-06 13:23 | favourite | cs2 | BetBoom Team | 9z | YES BetBoom Team | 16 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-06 13:23 | favourite | cs2 | FURIA | Aurora Gaming | NO Aurora Gaming | 17 | 0.55 | 0.55 | 0.54 | open | - |
| 2026-10-06 12:53 | favourite | cs2 | Gothic | mellren | YES Gothic | 4 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-06 12:53 | favourite | cs2 | Butterfly | ex-RUSTEC | YES Butterfly | 17 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-06 12:53 | model-only | cs2 | mellren | Gothic | NO Gothic | 42 | 0.44 | 0.61 | 0.44 | open | - |
| 2026-10-06 12:53 | model-only | cs2 | ex-RUSTEC | Butterfly | NO Butterfly | 41 | 0.45 | 0.54 | 0.44 | open | - |
| 2026-10-06 12:53 | model-only | dota2 | Team Synapse | Yellow Submarine | NO Yellow Submarine | 38 | 0.44 | 0.62 | 0.43 | open | - |
| 2026-10-06 12:53 | favourite | dota2 | Yellow Submarine | Team Synapse | YES Yellow Submarine | 17 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-06 10:53 | favourite | ow | MURASH GAMING | Lazuli | NO Lazuli | 4 | 0.79 | 0.77 | 0.77 | won | $0.79 |
| 2026-10-06 10:53 | model-only | ow | Lazuli | MURASH GAMING | YES Lazuli | 1 | 0.24 | 0.35 | 0.23 | lost | -$0.26 |
| 2026-10-06 10:53 | favourite | cs2 | G2 | PARIVISION | YES G2 | 15 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-06 10:53 | favourite | cs2 | Spirit | 1WIN | NO 1WIN | 11 | 0.87 | 0.86 | 0.86 | lost | -$9.66 |
| 2026-10-06 10:53 | model-only | cs2 | 1WIN | Spirit | YES 1WIN | 131 | 0.14 | 0.37 | 0.14 | won | $111.55 |
| 2026-10-06 09:52 | favourite | cs2 | Noir Verse | maybe | NO maybe | 12 | 0.78 | 0.78 | 0.78 | lost | -$9.51 |
| 2026-10-06 09:52 | model-only | cs2 | MASONIC | ex-Zero Tenacity | YES MASONIC | 123 | 0.15 | 0.34 | 0.15 | lost | -$19.55 |
| 2026-10-06 09:52 | favourite | cs2 | ex-Zero Tenacity | MASONIC | YES ex-Zero Tenacity | 11 | 0.85 | 0.85 | 0.85 | won | $1.55 |
| 2026-10-06 09:52 | model-only | cs2 | maybe | Noir Verse | NO Noir Verse | 4 | 0.22 | 0.43 | 0.22 | won | $3.07 |
| 2026-10-06 09:52 | model-only | dota2 | Nemiga Gaming | Blasterbl | NO Blasterbl | 64 | 0.29 | 0.40 | 0.28 | lost | -$19.49 |
| 2026-10-06 09:52 | favourite | dota2 | Blasterbl | Nemiga Gaming | YES Blasterbl | 13 | 0.72 | 0.72 | 0.72 | won | $3.45 |
| 2026-10-06 09:52 | favourite | lol | Team Vitality | RED Canids | NO RED Canids | 11 | 0.87 | 0.86 | 0.86 | won | $1.34 |
| 2026-10-06 09:22 | favourite | cs2 | VP.Future 3 | 3DMAX Academy | YES VP.Future 3 | 14 | 0.68 | 0.68 | 0.68 | won | $4.26 |
| 2026-10-06 09:22 | model-only | cs2 | 3DMAX Academy | VP.Future 3 | YES 3DMAX Academy | 2 | 0.32 | 0.46 | 0.32 | lost | -$0.68 |
| 2026-10-06 09:22 | favourite | cs2 | Teletubisie | THE UNIT | NO THE UNIT | 1 | 0.82 | 0.82 | 0.82 | won | $0.16 |
| 2026-10-06 08:27 | favourite | dota2 | Yangon Galacticos | Cloud Dawning | YES Yangon Galacticos | 1 | 0.80 | 0.51 | 0.51 | won | $0.18 |
| 2026-10-06 07:52 | favourite | lol | JD Gaming | LGD Gaming | YES JD Gaming | 18 | 0.53 | 0.53 | 0.53 | lost | -$9.86 |

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

