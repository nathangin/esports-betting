# Esports paper trading (fake money)

Updated 2026-10-18 08:07 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 222 | 18 | 204 | 51 | -$454.72 | -19.5% | -0.8c (218) | $545.28 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 336 | 27 | 309 | 214 | -$109.87 | -4.9% | -1.4c (333) | $890.13 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

772 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5676 | 0.1931 |
| model | 0.6556 | 0.2317 |
| blend | 0.5666 | 0.1928 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 472 | 0.5751 | 0.6569 |
| dota2 | 134 | 0.5501 | 0.6469 |
| lol | 58 | 0.5569 | 0.7146 |
| ow | 52 | 0.4649 | 0.5352 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 21 | 0.6521 | 0.6977 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-18 06:52 | favourite | cs2 | Black Phoenix | Saint Sinners | NO Saint Sinners | 10 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-18 06:52 | favourite | cs2 | Passion Academy | Elite Klan | YES Passion Academy | 15 | 0.55 | 0.54 | 0.53 | open | - |
| 2026-10-18 06:52 | favourite | cs2 | ex-RUSTEC | Butterfly | NO Butterfly | 13 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-18 06:52 | favourite | cs2 | EAC Extra | VP.Future 3 | YES EAC Extra | 15 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-18 04:52 | favourite | valorant | LOUD | Team Vitality | NO Team Vitality | 6 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-18 04:52 | model-only | valorant | Team Vitality | LOUD | NO LOUD | 24 | 0.42 | 0.50 | 0.42 | open | - |
| 2026-10-18 04:52 | favourite | ow | Cheeseburger | SEIJI ESPORTS | YES Cheeseburger | 4 | 0.89 | 0.88 | 0.88 | won | $0.41 |
| 2026-10-18 01:51 | favourite | cs2 | NEXVOID | Off Chops | YES NEXVOID | 6 | 0.74 | 0.70 | 0.70 | won | $1.47 |
| 2026-10-17 21:51 | favourite | ow | NTMR | Disguised | NO Disguised | 15 | 0.57 | 0.53 | 0.53 | won | $6.19 |
| 2026-10-17 20:21 | favourite | ow | Team Liquid | The Kafe | YES Team Liquid | 12 | 0.73 | 0.70 | 0.70 | won | $3.07 |
| 2026-10-17 18:51 | favourite | ow | Geekay Esports | Team Peps | YES Geekay Esports | 8 | 0.65 | 0.63 | 0.63 | won | $2.67 |
| 2026-10-17 17:51 | favourite | dota2 | CyberHero | Inner Circle | YES CyberHero | 11 | 0.76 | 0.75 | 0.75 | lost | -$8.51 |
| 2026-10-17 17:51 | favourite | cs2 | 6yuBoJlbl | WRAITH PCIFIC | YES 6yuBoJlbl | 15 | 0.58 | 0.55 | 0.54 | open | - |
| 2026-10-17 16:51 | favourite | lol | FURIA Esports | MVK Esports | YES FURIA Esports | 13 | 0.64 | 0.64 | 0.64 | lost | -$8.53 |
| 2026-10-17 15:50 | favourite | cs2 | BBL | ex-RUSTEC | NO ex-RUSTEC | 7 | 0.60 | 0.59 | 0.59 | won | $2.68 |
| 2026-10-17 15:50 | model-only | cs2 | BetBoom Team | Team Falcons | YES BetBoom Team | 24 | 0.27 | 0.37 | 0.27 | won | $17.18 |
| 2026-10-17 15:50 | favourite | cs2 | Team Falcons | BetBoom Team | YES Team Falcons | 12 | 0.73 | 0.73 | 0.73 | lost | -$8.93 |
| 2026-10-17 15:50 | favourite | cs2 | MIBR | NIP | YES MIBR | 15 | 0.57 | 0.55 | 0.55 | lost | -$8.81 |
| 2026-10-17 14:50 | favourite | dota2 | Yellow Submarine | Dawn Bulls | NO Dawn Bulls | 12 | 0.68 | 0.67 | 0.67 | won | $3.65 |
| 2026-10-17 14:50 | model-only | dota2 | Dawn Bulls | Yellow Submarine | NO Yellow Submarine | 31 | 0.34 | 0.44 | 0.33 | lost | -$11.03 |
| 2026-10-17 14:50 | favourite | dota2 | Zero Tenacity | Inner Circle | NO Inner Circle | 14 | 0.62 | 0.60 | 0.60 | won | $5.08 |
| 2026-10-17 14:50 | model-only | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 25 | 0.42 | 0.51 | 0.40 | lost | -$10.93 |
| 2026-10-17 11:50 | model-only | dota2 | Spirit Academy | Yellow Submarine | YES Spirit Academy | 2 | 0.12 | 0.26 | 0.12 | lost | -$0.26 |
| 2026-10-17 11:50 | model-only | ow | Solus Victorem | Weibo Gaming | YES Solus Victorem | 71 | 0.10 | 0.21 | 0.09 | lost | -$7.55 |
| 2026-10-17 11:50 | favourite | dota2 | Yellow Submarine | Spirit Academy | YES Yellow Submarine | 9 | 0.89 | 0.89 | 0.89 | won | $0.92 |

## Backtest on real Kalshi prices

7979 settled matches from 2026-05-28 to 2026-10-12, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $439.42 | -$30.42 | -6.9% | -43.8% to +40.9% | 54% | -0.0c | 10% |
| model only | 1968 | $8,857.80 | -$985.80 | -11.1% | -19.2% to -3.2% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 3824 | $15,776.22 | -$733.22 | -4.6% | -7.0% to -2.2% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3731 | $8,550.73 | -$978.73 | -11.4% | -17.1% to -5.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7754 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5731 | 0.1959 | 69.2% |
| model | 0.6615 | 0.2347 | 59.5% |
| blend | 0.5727 | 0.1958 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1281 | 0.525 | 0.522 |
| (0.55, 0.6] | 1311 | 0.577 | 0.548 |
| (0.6, 0.65] | 1192 | 0.626 | 0.638 |
| (0.65, 0.7] | 1041 | 0.676 | 0.701 |
| (0.7, 0.75] | 880 | 0.726 | 0.773 |
| (0.75, 0.8] | 755 | 0.776 | 0.812 |
| (0.8, 0.85] | 636 | 0.826 | 0.824 |
| (0.85, 0.9] | 478 | 0.877 | 0.902 |
| (0.9, 1.0] | 405 | 0.932 | 0.956 |

