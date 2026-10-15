# Esports paper trading (fake money)

Updated 2026-10-15 16:09 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 187 | 21 | 166 | 45 | -$256.61 | -12.9% | -0.6c (183) | $743.39 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 269 | 30 | 239 | 165 | -$112.85 | -6.4% | -1.1c (264) | $887.15 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

625 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5658 | 0.1923 |
| model | 0.6591 | 0.2331 |
| blend | 0.5646 | 0.1919 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 399 | 0.5714 | 0.6604 |
| dota2 | 91 | 0.5741 | 0.6477 |
| lol | 52 | 0.5052 | 0.7198 |
| ow | 38 | 0.4673 | 0.5439 |
| r6 | 28 | 0.6762 | 0.7223 |
| valorant | 17 | 0.6143 | 0.6568 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-15 15:53 | favourite | cs2 | Sokerorg | Gothic | YES Sokerorg | 13 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-15 15:53 | favourite | cs2 | 99firepower 1utility | Fraternity | YES 99firepower 1utility | 12 | 0.67 | 0.64 | 0.64 | open | - |
| 2026-10-15 14:52 | favourite | dota2 | Inner Circle | Mena Warriors | YES Inner Circle | 2 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-15 14:52 | favourite | dota2 | Stray Team | Korb3n Team | YES Stray Team | 12 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-10-15 14:52 | favourite | cs2 | UPGRADE | Lavked | YES UPGRADE | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-15 14:52 | favourite | cs2 | FURIA | Legacy | YES FURIA | 14 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-10-15 14:52 | favourite | cs2 | WBT Academy | BOJONG | YES WBT Academy | 9 | 0.89 | 0.87 | 0.87 | open | - |
| 2026-10-15 14:52 | model-only | cs2 | BOJONG | WBT Academy | NO WBT Academy | 14 | 0.16 | 0.33 | 0.13 | open | - |
| 2026-10-15 12:52 | model-only | cs2 | The Last Resort | Spirit Academy | YES The Last Resort | 1 | 0.25 | 0.31 | 0.24 | open | - |
| 2026-10-15 12:52 | model-only | cs2 | BOJONG | Esport Academy Copenhagen | YES BOJONG | 77 | 0.19 | 0.41 | 0.17 | lost | -$15.46 |
| 2026-10-15 12:52 | favourite | cs2 | Esport Academy Copenhagen | BOJONG | NO BOJONG | 10 | 0.85 | 0.83 | 0.83 | won | $1.41 |
| 2026-10-15 12:52 | model-only | cs2 | Fire Flux Esports | Butterfly | NO Butterfly | 1 | 0.38 | 0.54 | 0.37 | open | - |
| 2026-10-15 12:52 | favourite | cs2 | Butterfly | Fire Flux Esports | YES Butterfly | 13 | 0.64 | 0.63 | 0.63 | open | - |
| 2026-10-15 12:52 | favourite | cs2 | Spirit Academy | The Last Resort | NO The Last Resort | 11 | 0.78 | 0.76 | 0.76 | open | - |
| 2026-10-15 12:52 | favourite | cs2 | 6666 | ENJOY | YES 6666 | 13 | 0.65 | 0.64 | 0.64 | open | - |
| 2026-10-15 12:52 | model-only | dota2 | White Sails | Team Synapse | NO Team Synapse | 77 | 0.19 | 0.38 | 0.17 | open | - |
| 2026-10-15 12:52 | favourite | dota2 | Team Synapse | White Sails | YES Team Synapse | 10 | 0.85 | 0.83 | 0.83 | open | - |
| 2026-10-15 12:22 | favourite | cs2 | PARIVISION | BetBoom Team | YES PARIVISION | 16 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-10-15 12:22 | model-only | cs2 | BetBoom Team | PARIVISION | YES BetBoom Team | 32 | 0.48 | 0.55 | 0.48 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | maybe | Ryvex | YES maybe | 1 | 0.54 | 0.54 | 0.54 | won | $0.44 |
| 2026-10-15 10:22 | model-only | cs2 | 9z | Team Falcons | NO Team Falcons | 56 | 0.25 | 0.34 | 0.24 | lost | -$14.74 |
| 2026-10-15 10:22 | favourite | cs2 | Team Falcons | 9z | NO 9z | 11 | 0.76 | 0.76 | 0.76 | won | $2.49 |
| 2026-10-15 10:22 | favourite | cs2 | ex-Zero Tenacity | Just_Players | YES ex-Zero Tenacity | 13 | 0.67 | 0.67 | 0.67 | won | $4.08 |
| 2026-10-15 10:22 | model-only | cs2 | Ryvex | maybe | YES Ryvex | 30 | 0.47 | 0.54 | 0.46 | lost | -$14.63 |
| 2026-10-15 10:22 | model-only | cs2 | Just_Players | ex-Zero Tenacity | YES Just_Players | 12 | 0.34 | 0.40 | 0.33 | lost | -$4.27 |

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

