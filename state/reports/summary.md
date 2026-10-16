# Esports paper trading (fake money)

Updated 2026-10-16 04:05 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 189 | 18 | 171 | 47 | -$258.04 | -12.7% | -0.6c (185) | $741.96 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 271 | 21 | 250 | 171 | -$128.55 | -6.9% | -1.1c (268) | $871.45 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

664 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5715 | 0.1950 |
| model | 0.6611 | 0.2342 |
| blend | 0.5707 | 0.1948 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 422 | 0.5731 | 0.6589 |
| dota2 | 102 | 0.5842 | 0.6587 |
| lol | 54 | 0.5255 | 0.7203 |
| ow | 38 | 0.4673 | 0.5439 |
| r6 | 30 | 0.6785 | 0.7286 |
| valorant | 18 | 0.6413 | 0.6852 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-16 02:50 | model-only | dota2 | Ivory | Xipto Esports | NO Xipto Esports | 139 | 0.10 | 0.19 | 0.08 | open | - |
| 2026-10-16 02:50 | favourite | dota2 | Execration | Team Kinetix | NO Team Kinetix | 4 | 0.84 | 0.81 | 0.81 | open | - |
| 2026-10-16 02:50 | model-only | dota2 | Team Kinetix | Execration | NO Execration | 3 | 0.20 | 0.37 | 0.18 | open | - |
| 2026-10-15 17:23 | favourite | cs2 | ZOTIX | eternal premium | YES ZOTIX | 1 | 0.52 | 0.51 | 0.51 | lost | -$0.54 |
| 2026-10-15 15:53 | favourite | cs2 | Sokerorg | Gothic | YES Sokerorg | 13 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-15 15:53 | favourite | cs2 | 99firepower 1utility | Fraternity | YES 99firepower 1utility | 12 | 0.67 | 0.64 | 0.64 | lost | -$8.23 |
| 2026-10-15 14:52 | favourite | cs2 | FURIA | Legacy | YES FURIA | 14 | 0.60 | 0.59 | 0.59 | won | $5.36 |
| 2026-10-15 14:52 | model-only | cs2 | BOJONG | WBT Academy | NO WBT Academy | 14 | 0.16 | 0.33 | 0.13 | lost | -$2.38 |
| 2026-10-15 14:52 | favourite | cs2 | WBT Academy | BOJONG | YES WBT Academy | 9 | 0.89 | 0.87 | 0.87 | won | $0.92 |
| 2026-10-15 14:52 | favourite | dota2 | Stray Team | Korb3n Team | YES Stray Team | 12 | 0.71 | 0.70 | 0.70 | lost | -$8.70 |
| 2026-10-15 14:52 | favourite | cs2 | UPGRADE | Lavked | YES UPGRADE | 13 | 0.63 | 0.62 | 0.62 | won | $4.59 |
| 2026-10-15 14:52 | favourite | dota2 | Inner Circle | Mena Warriors | YES Inner Circle | 2 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-15 12:52 | model-only | cs2 | The Last Resort | Spirit Academy | YES The Last Resort | 1 | 0.25 | 0.31 | 0.24 | lost | -$0.27 |
| 2026-10-15 12:52 | model-only | cs2 | BOJONG | Esport Academy Copenhagen | YES BOJONG | 77 | 0.19 | 0.41 | 0.17 | lost | -$15.46 |
| 2026-10-15 12:52 | favourite | cs2 | Esport Academy Copenhagen | BOJONG | NO BOJONG | 10 | 0.85 | 0.83 | 0.83 | won | $1.41 |
| 2026-10-15 12:52 | model-only | cs2 | Fire Flux Esports | Butterfly | NO Butterfly | 1 | 0.38 | 0.54 | 0.37 | won | $0.60 |
| 2026-10-15 12:52 | favourite | cs2 | Butterfly | Fire Flux Esports | YES Butterfly | 13 | 0.64 | 0.63 | 0.63 | lost | -$8.53 |
| 2026-10-15 12:52 | model-only | dota2 | White Sails | Team Synapse | NO Team Synapse | 77 | 0.19 | 0.38 | 0.17 | lost | -$15.46 |
| 2026-10-15 12:52 | favourite | cs2 | Spirit Academy | The Last Resort | NO The Last Resort | 11 | 0.78 | 0.76 | 0.76 | won | $2.28 |
| 2026-10-15 12:52 | favourite | cs2 | 6666 | ENJOY | YES 6666 | 13 | 0.65 | 0.64 | 0.64 | won | $4.34 |
| 2026-10-15 12:52 | favourite | dota2 | Team Synapse | White Sails | YES Team Synapse | 10 | 0.85 | 0.83 | 0.83 | won | $1.41 |
| 2026-10-15 12:22 | favourite | cs2 | PARIVISION | BetBoom Team | YES PARIVISION | 16 | 0.52 | 0.52 | 0.52 | lost | -$8.60 |
| 2026-10-15 12:22 | model-only | cs2 | BetBoom Team | PARIVISION | YES BetBoom Team | 32 | 0.48 | 0.55 | 0.48 | won | $16.08 |
| 2026-10-15 10:22 | model-only | cs2 | Ryvex | maybe | YES Ryvex | 30 | 0.47 | 0.54 | 0.46 | lost | -$14.63 |
| 2026-10-15 10:22 | model-only | cs2 | 9z | Team Falcons | NO Team Falcons | 56 | 0.25 | 0.34 | 0.24 | lost | -$14.74 |

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

