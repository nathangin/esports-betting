# Esports paper trading (fake money)

Updated 2026-10-06 16:08 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 30 | 10 | 20 | 4 | $51.00 | +23.2% | -0.5c (26) | $1,051.00 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 53 | 16 | 37 | 27 | -$16.71 | -5.7% | -1.0c (48) | $983.29 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

42 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5163 | 0.1692 |
| model | 0.6464 | 0.2268 |
| blend | 0.5135 | 0.1678 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 17 | 0.6448 | 0.6534 |
| lol | 9 | 0.2057 | 0.6560 |
| dota2 | 6 | 0.4819 | 0.5610 |
| r6 | 6 | 0.8571 | 0.8141 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-06 15:53 | favourite | dota2 | MOUZ | LEGION | NO LEGION | 17 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-06 15:53 | model-only | dota2 | LEGION | MOUZ | YES LEGION | 42 | 0.48 | 0.62 | 0.48 | open | - |
| 2026-10-06 15:53 | favourite | cs2 | Team Falcons | Natus Vincere | YES Team Falcons | 16 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-06 15:53 | favourite | cs2 | MASONIC | MASQ | NO MASQ | 14 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-10-06 15:53 | model-only | cs2 | MASQ | MASONIC | NO MASONIC | 2 | 0.33 | 0.49 | 0.33 | open | - |
| 2026-10-06 15:53 | favourite | cs2 | Legacy | M80 | YES Legacy | 17 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-10-06 15:53 | model-only | cs2 | Legacy | M80 | YES Legacy | 37 | 0.55 | 0.63 | 0.55 | open | - |
| 2026-10-06 15:53 | favourite | cs2 | Lavked | WRAITH PCIFIC | YES Lavked | 16 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-06 15:53 | model-only | cs2 | WRAITH PCIFIC | Lavked | YES WRAITH PCIFIC | 47 | 0.43 | 0.58 | 0.43 | open | - |
| 2026-10-06 14:53 | favourite | lol | TLN Pirates | Bushido Wildcats | YES TLN Pirates | 11 | 0.84 | 0.84 | 0.84 | open | - |
| 2026-10-06 14:53 | model-only | lol | Berlin International Gaming | Galions | YES Berlin International Gaming | 94 | 0.21 | 0.45 | 0.20 | open | - |
| 2026-10-06 14:53 | favourite | lol | Galions | Berlin International Gaming | NO Berlin International Gaming | 12 | 0.80 | 0.80 | 0.80 | open | - |
| 2026-10-06 14:53 | favourite | r6 | Geekay Esports | Shifters | YES Geekay Esports | 1 | 0.66 | 0.63 | 0.63 | open | - |
| 2026-10-06 14:53 | favourite | lol | Movistar KOI Fénix | Frites Esports Club | NO Frites Esports Club | 11 | 0.89 | 0.89 | 0.89 | open | - |
| 2026-10-06 14:53 | model-only | r6 | Shifters | Geekay Esports | NO Geekay Esports | 24 | 0.39 | 0.44 | 0.37 | open | - |
| 2026-10-06 13:23 | favourite | cs2 | BetBoom Team | 9z | YES BetBoom Team | 16 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-06 13:23 | favourite | cs2 | FURIA | Aurora Gaming | NO Aurora Gaming | 17 | 0.55 | 0.55 | 0.54 | open | - |
| 2026-10-06 12:53 | model-only | cs2 | mellren | Gothic | NO Gothic | 42 | 0.44 | 0.61 | 0.44 | open | - |
| 2026-10-06 12:53 | model-only | cs2 | ex-RUSTEC | Butterfly | NO Butterfly | 41 | 0.45 | 0.54 | 0.44 | open | - |
| 2026-10-06 12:53 | favourite | cs2 | Butterfly | ex-RUSTEC | YES Butterfly | 17 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-06 12:53 | favourite | cs2 | Gothic | mellren | YES Gothic | 4 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-06 12:53 | favourite | dota2 | Yellow Submarine | Team Synapse | YES Yellow Submarine | 17 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-06 12:53 | model-only | dota2 | Team Synapse | Yellow Submarine | NO Yellow Submarine | 38 | 0.44 | 0.62 | 0.43 | open | - |
| 2026-10-06 10:53 | favourite | ow | MURASH GAMING | Lazuli | NO Lazuli | 4 | 0.79 | 0.77 | 0.77 | won | $0.79 |
| 2026-10-06 10:53 | model-only | ow | Lazuli | MURASH GAMING | YES Lazuli | 1 | 0.24 | 0.35 | 0.23 | lost | -$0.26 |

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

