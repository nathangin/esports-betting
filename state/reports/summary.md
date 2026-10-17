# Esports paper trading (fake money)

Updated 2026-10-17 07:39 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 211 | 21 | 190 | 48 | -$389.51 | -17.6% | -0.7c (204) | $610.49 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 311 | 27 | 284 | 196 | -$120.31 | -5.8% | -1.3c (306) | $879.69 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

735 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5656 | 0.1924 |
| model | 0.6550 | 0.2314 |
| blend | 0.5645 | 0.1920 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 463 | 0.5740 | 0.6558 |
| dota2 | 122 | 0.5500 | 0.6474 |
| lol | 56 | 0.5519 | 0.7119 |
| ow | 41 | 0.4441 | 0.5241 |
| r6 | 33 | 0.6423 | 0.7254 |
| valorant | 20 | 0.6286 | 0.6749 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-17 06:54 | favourite | r6 | CAG by VARREL | Dplus | YES CAG by VARREL | 12 | 0.69 | 0.67 | 0.67 | open | - |
| 2026-10-17 06:54 | model-only | r6 | Dplus | CAG by VARREL | NO CAG by VARREL | 14 | 0.34 | 0.44 | 0.33 | open | - |
| 2026-10-17 06:54 | model-only | ow | ZANSIDE GAMING | T1 | NO T1 | 104 | 0.11 | 0.21 | 0.09 | open | - |
| 2026-10-17 06:54 | favourite | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 16 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-17 06:54 | model-only | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 22 | 0.53 | 0.70 | 0.53 | open | - |
| 2026-10-17 06:24 | favourite | ow | Crazy Raccoon | Falcons | YES Crazy Raccoon | 4 | 0.84 | 0.82 | 0.82 | open | - |
| 2026-10-17 05:54 | favourite | valorant | 100 Thieves | Team Vitality | YES 100 Thieves | 12 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-17 05:54 | favourite | dota2 | Nemiga Gaming | LFO | NO LFO | 13 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-17 04:53 | favourite | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.71 | 0.71 | open | - |
| 2026-10-17 04:53 | model-only | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.79 | 0.71 | open | - |
| 2026-10-17 03:53 | favourite | dota2 | Xtreme Gaming | Yakult's Brothers | YES Xtreme Gaming | 10 | 0.81 | 0.79 | 0.79 | won | $1.79 |
| 2026-10-17 02:53 | favourite | dota2 | Xipto Esports | InterActive Philippines | NO InterActive Philippines | 11 | 0.74 | 0.72 | 0.72 | won | $2.71 |
| 2026-10-17 02:53 | model-only | dota2 | InterActive Philippines | Xipto Esports | YES InterActive Philippines | 40 | 0.29 | 0.39 | 0.28 | lost | -$12.18 |
| 2026-10-16 15:22 | favourite | dota2 | Stariy bog Team | Korb3n Team | YES Stariy bog Team | 2 | 0.62 | 0.61 | 0.61 | lost | -$1.28 |
| 2026-10-16 12:51 | model-only | cs2 | 9z | Aurora Gaming | YES 9z | 16 | 0.31 | 0.36 | 0.31 | lost | -$5.20 |
| 2026-10-16 11:51 | favourite | cs2 | Joga de terno | your end | YES Joga de terno | 14 | 0.58 | 0.57 | 0.57 | lost | -$8.36 |
| 2026-10-16 11:51 | favourite | cs2 | Black Phoenix | X-CITY | YES Black Phoenix | 10 | 0.86 | 0.83 | 0.83 | won | $1.31 |
| 2026-10-16 11:51 | favourite | cs2 | Young TigeRES | Young27 | YES Young TigeRES | 6 | 0.58 | 0.57 | 0.57 | won | $2.41 |
| 2026-10-16 10:51 | favourite | r6 | Elevate | Fury | NO Fury | 2 | 0.74 | 0.72 | 0.72 | won | $0.49 |
| 2026-10-16 10:51 | favourite | dota2 | Royal Bear | InterActive Philippines | YES Royal Bear | 10 | 0.81 | 0.80 | 0.80 | won | $1.79 |
| 2026-10-16 10:51 | favourite | dota2 | by Owl Team | ALOHADANCE Team | YES by Owl Team | 6 | 0.71 | 0.70 | 0.71 | lost | -$4.35 |
| 2026-10-16 10:51 | favourite | cs2 | Voca | HAVU | NO HAVU | 14 | 0.60 | 0.58 | 0.58 | lost | -$8.64 |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Saint Sinners | YES ex-RUSTEC | 12 | 0.70 | 0.69 | 0.69 | won | $3.42 |
| 2026-10-16 09:51 | model-only | cs2 | Saint Sinners | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.32 | 0.40 | 0.31 | lost | -$0.34 |
| 2026-10-16 09:51 | favourite | cs2 | Team Nemesis | Nuclear TigeRES | YES Team Nemesis | 14 | 0.58 | 0.57 | 0.57 | won | $5.64 |

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

