# Esports paper trading (fake money)

Updated 2026-10-17 23:56 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 221 | 17 | 204 | 51 | -$454.72 | -19.5% | -0.8c (217) | $545.28 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 329 | 23 | 306 | 211 | -$117.94 | -5.3% | -1.4c (326) | $882.06 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

769 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5683 | 0.1935 |
| model | 0.6560 | 0.2319 |
| blend | 0.5674 | 0.1931 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 471 | 0.5756 | 0.6570 |
| dota2 | 134 | 0.5501 | 0.6469 |
| lol | 58 | 0.5569 | 0.7146 |
| ow | 50 | 0.4680 | 0.5357 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 21 | 0.6521 | 0.6977 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-17 21:51 | favourite | ow | NTMR | Disguised | NO Disguised | 15 | 0.57 | 0.53 | 0.53 | open | - |
| 2026-10-17 20:21 | favourite | ow | Team Liquid | The Kafe | YES Team Liquid | 12 | 0.73 | 0.70 | 0.70 | won | $3.07 |
| 2026-10-17 18:51 | favourite | ow | Geekay Esports | Team Peps | YES Geekay Esports | 8 | 0.65 | 0.63 | 0.63 | won | $2.67 |
| 2026-10-17 17:51 | favourite | dota2 | CyberHero | Inner Circle | YES CyberHero | 11 | 0.76 | 0.75 | 0.75 | lost | -$8.51 |
| 2026-10-17 17:51 | favourite | cs2 | 6yuBoJlbl | WRAITH PCIFIC | YES 6yuBoJlbl | 15 | 0.58 | 0.55 | 0.54 | open | - |
| 2026-10-17 16:51 | favourite | lol | FURIA Esports | MVK Esports | YES FURIA Esports | 13 | 0.64 | 0.64 | 0.64 | lost | -$8.53 |
| 2026-10-17 15:50 | favourite | cs2 | MIBR | NIP | YES MIBR | 15 | 0.57 | 0.55 | 0.55 | lost | -$8.81 |
| 2026-10-17 15:50 | favourite | cs2 | BBL | ex-RUSTEC | NO ex-RUSTEC | 7 | 0.60 | 0.59 | 0.59 | won | $2.68 |
| 2026-10-17 15:50 | favourite | cs2 | Team Falcons | BetBoom Team | YES Team Falcons | 12 | 0.73 | 0.73 | 0.73 | lost | -$8.93 |
| 2026-10-17 15:50 | model-only | cs2 | BetBoom Team | Team Falcons | YES BetBoom Team | 24 | 0.27 | 0.37 | 0.27 | won | $17.18 |
| 2026-10-17 14:50 | favourite | dota2 | Yellow Submarine | Dawn Bulls | NO Dawn Bulls | 12 | 0.68 | 0.67 | 0.67 | won | $3.65 |
| 2026-10-17 14:50 | model-only | dota2 | Dawn Bulls | Yellow Submarine | NO Yellow Submarine | 31 | 0.34 | 0.44 | 0.33 | lost | -$11.03 |
| 2026-10-17 14:50 | favourite | dota2 | Zero Tenacity | Inner Circle | NO Inner Circle | 14 | 0.62 | 0.60 | 0.60 | won | $5.08 |
| 2026-10-17 14:50 | model-only | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 25 | 0.42 | 0.51 | 0.40 | lost | -$10.93 |
| 2026-10-17 11:50 | favourite | dota2 | Yellow Submarine | Spirit Academy | YES Yellow Submarine | 9 | 0.89 | 0.89 | 0.89 | won | $0.92 |
| 2026-10-17 11:50 | model-only | dota2 | Spirit Academy | Yellow Submarine | YES Spirit Academy | 2 | 0.12 | 0.26 | 0.12 | lost | -$0.26 |
| 2026-10-17 11:50 | model-only | ow | Solus Victorem | Weibo Gaming | YES Solus Victorem | 71 | 0.10 | 0.21 | 0.09 | lost | -$7.55 |
| 2026-10-17 10:54 | favourite | dota2 | Nix Team | by Owl Team | NO by Owl Team | 12 | 0.69 | 0.67 | 0.67 | won | $3.54 |
| 2026-10-17 10:54 | model-only | dota2 | by Owl Team | Nix Team | YES by Owl Team | 33 | 0.35 | 0.57 | 0.33 | lost | -$12.08 |
| 2026-10-17 09:54 | favourite | r6 | SCARZ | FearX | NO FearX | 11 | 0.59 | 0.58 | 0.58 | won | $4.32 |
| 2026-10-17 09:54 | model-only | r6 | FearX | SCARZ | YES FearX | 22 | 0.43 | 0.48 | 0.42 | lost | -$9.84 |
| 2026-10-17 08:54 | favourite | dota2 | Inner Circle | PuckChamp | YES Inner Circle | 10 | 0.83 | 0.82 | 0.82 | won | $1.60 |
| 2026-10-17 08:54 | model-only | dota2 | PuckChamp | Inner Circle | YES PuckChamp | 60 | 0.19 | 0.35 | 0.18 | lost | -$12.05 |
| 2026-10-17 08:54 | favourite | dota2 | Team Lynx | Dawn Bulls | NO Dawn Bulls | 16 | 0.53 | 0.52 | 0.52 | won | $7.24 |
| 2026-10-17 07:54 | favourite | lol | BNK FEARX | Team WE | NO Team WE | 12 | 0.68 | 0.68 | 0.68 | won | $3.65 |

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

