# Esports paper trading (fake money)

Updated 2026-10-04 12:15 UTC. Model fitted 2026-10-04T12:10. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

No finished matches yet.

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

