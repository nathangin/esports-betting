# Esports paper trading (fake money)

Updated 2026-10-04 21:05 UTC. Model fitted 2026-10-04T12:10. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 6 | 0 | 6 | 1 | $56.52 | +82.5% | +3.5c (6) | $1,056.52 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 10 | 1 | 9 | 7 | $13.12 | +15.1% | -2.4c (10) | $1,013.12 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

10 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5156 | 0.1678 |
| model | 0.5974 | 0.2027 |
| blend | 0.5150 | 0.1659 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 4 | 0.4450 | 0.5386 |
| lol | 3 | 0.1246 | 0.4360 |
| r6 | 3 | 1.0008 | 0.8372 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-04 20:02 | favourite | r6 | FURIA Esports | Lucky Five | YES FURIA Esports | 13 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-10-04 16:52 | model-only | r6 | LOS | Team Liquid | NO Team Liquid | 7 | 0.34 | 0.41 | 0.32 | lost | -$2.49 |
| 2026-10-04 16:52 | favourite | r6 | Team Liquid | LOS | YES Team Liquid | 14 | 0.68 | 0.68 | 0.68 | won | $4.26 |
| 2026-10-04 16:52 | model-only | r6 | LOUD | Fluxo W7M | NO Fluxo W7M | 8 | 0.38 | 0.44 | 0.37 | lost | -$3.18 |
| 2026-10-04 16:52 | favourite | r6 | Fluxo W7M | LOUD | YES Fluxo W7M | 15 | 0.63 | 0.63 | 0.63 | won | $5.30 |
| 2026-10-04 15:23 | model-only | lol | UCAM Esports Club | Movistar KOI Fénix | NO Movistar KOI Fénix | 13 | 0.24 | 0.39 | 0.24 | lost | -$3.29 |
| 2026-10-04 15:23 | favourite | lol | Movistar KOI Fénix | UCAM Esports Club | YES Movistar KOI Fénix | 12 | 0.77 | 0.76 | 0.76 | won | $2.61 |
| 2026-10-04 15:23 | favourite | r6 | INTZ | Imperial Esports | NO Imperial Esports | 18 | 0.53 | 0.52 | 0.52 | lost | -$9.86 |
| 2026-10-04 15:23 | model-only | cs2 | M80 | BetBoom Team | YES M80 | 59 | 0.32 | 0.43 | 0.32 | lost | -$19.78 |
| 2026-10-04 15:23 | favourite | cs2 | BetBoom Team | M80 | YES BetBoom Team | 14 | 0.68 | 0.68 | 0.68 | won | $4.26 |
| 2026-10-04 15:23 | model-only | cs2 | Natus Vincere | Vitality | YES Natus Vincere | 70 | 0.27 | 0.34 | 0.27 | lost | -$19.87 |
| 2026-10-04 15:23 | favourite | cs2 | Vitality | Natus Vincere | YES Vitality | 13 | 0.73 | 0.73 | 0.73 | won | $3.33 |
| 2026-10-04 15:23 | favourite | cs2 | ex-RUSTEC | ENJOY | NO ENJOY | 15 | 0.64 | 0.64 | 0.64 | won | $5.15 |
| 2026-10-04 15:23 | model-only | r6 | Black Dragons e-Sports | FaZe Clan | YES Black Dragons e-Sports | 125 | 0.15 | 0.30 | 0.15 | won | $105.13 |
| 2026-10-04 15:23 | favourite | r6 | FaZe Clan | Black Dragons e-Sports | YES FaZe Clan | 11 | 0.85 | 0.85 | 0.85 | lost | -$9.45 |
| 2026-10-04 15:23 | favourite | cs2 | Turma do Pagode | Bounty Hunters Esports | NO Bounty Hunters Esports | 17 | 0.54 | 0.54 | 0.53 | won | $7.52 |

## Backtest on real Kalshi prices

7469 settled matches from 2026-05-28 to 2026-10-04, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 1864 | $9,187.48 | -$979.48 | -10.7% | -18.8% to -2.9% | 34% | -0.8c | 98% |
| always the favourite (1% flat) | 3572 | $15,221.32 | -$737.32 | -4.8% | -7.4% to -2.4% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3602 | $8,682.70 | -$978.70 | -11.3% | -16.9% to -5.0% | 32% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7244 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5734 | 0.1961 | 69.1% |
| model | 0.6616 | 0.2348 | 59.3% |
| blend | 0.5731 | 0.1960 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1188 | 0.525 | 0.519 |
| (0.55, 0.6] | 1241 | 0.577 | 0.553 |
| (0.6, 0.65] | 1118 | 0.626 | 0.633 |
| (0.65, 0.7] | 982 | 0.676 | 0.700 |
| (0.7, 0.75] | 829 | 0.726 | 0.774 |
| (0.75, 0.8] | 702 | 0.776 | 0.808 |
| (0.8, 0.85] | 592 | 0.826 | 0.826 |
| (0.85, 0.9] | 441 | 0.877 | 0.905 |
| (0.9, 1.0] | 376 | 0.932 | 0.957 |

