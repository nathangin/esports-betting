# Esports paper trading (fake money)

Updated 2026-10-17 11:09 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 216 | 23 | 193 | 50 | -$372.03 | -16.7% | -0.8c (211) | $627.97 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 317 | 28 | 289 | 199 | -$117.70 | -5.6% | -1.3c (313) | $882.30 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

741 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5665 | 0.1928 |
| model | 0.6554 | 0.2316 |
| blend | 0.5654 | 0.1924 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 463 | 0.5740 | 0.6558 |
| dota2 | 124 | 0.5501 | 0.6471 |
| lol | 56 | 0.5519 | 0.7119 |
| ow | 44 | 0.4544 | 0.5381 |
| r6 | 34 | 0.6563 | 0.7282 |
| valorant | 20 | 0.6286 | 0.6749 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-17 10:54 | favourite | dota2 | Nix Team | by Owl Team | NO by Owl Team | 12 | 0.69 | 0.67 | 0.67 | open | - |
| 2026-10-17 10:54 | model-only | dota2 | by Owl Team | Nix Team | YES by Owl Team | 33 | 0.35 | 0.57 | 0.33 | open | - |
| 2026-10-17 09:54 | favourite | r6 | SCARZ | FearX | NO FearX | 11 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-17 09:54 | model-only | r6 | FearX | SCARZ | YES FearX | 22 | 0.43 | 0.48 | 0.42 | open | - |
| 2026-10-17 08:54 | favourite | dota2 | Inner Circle | PuckChamp | YES Inner Circle | 10 | 0.83 | 0.82 | 0.82 | open | - |
| 2026-10-17 08:54 | model-only | dota2 | PuckChamp | Inner Circle | YES PuckChamp | 60 | 0.19 | 0.35 | 0.18 | open | - |
| 2026-10-17 08:54 | favourite | dota2 | Team Lynx | Dawn Bulls | NO Dawn Bulls | 16 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-17 07:54 | favourite | lol | BNK FEARX | Team WE | NO Team WE | 12 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-17 07:54 | model-only | lol | Team WE | BNK FEARX | NO BNK FEARX | 36 | 0.32 | 0.47 | 0.32 | open | - |
| 2026-10-17 07:54 | favourite | dota2 | Gorgc Team | ALOHADANCE Team | YES Gorgc Team | 13 | 0.64 | 0.63 | 0.63 | open | - |
| 2026-10-17 07:54 | model-only | dota2 | ALOHADANCE Team | Gorgc Team | YES ALOHADANCE Team | 30 | 0.38 | 0.46 | 0.37 | open | - |
| 2026-10-17 06:54 | model-only | ow | ZANSIDE GAMING | T1 | NO T1 | 104 | 0.11 | 0.21 | 0.09 | open | - |
| 2026-10-17 06:54 | model-only | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 22 | 0.53 | 0.70 | 0.53 | won | $9.95 |
| 2026-10-17 06:54 | favourite | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 16 | 0.53 | 0.53 | 0.53 | won | $7.24 |
| 2026-10-17 06:54 | model-only | r6 | Dplus | CAG by VARREL | NO CAG by VARREL | 14 | 0.34 | 0.44 | 0.33 | won | $9.02 |
| 2026-10-17 06:54 | favourite | r6 | CAG by VARREL | Dplus | YES CAG by VARREL | 12 | 0.69 | 0.67 | 0.67 | lost | -$8.46 |
| 2026-10-17 06:24 | favourite | ow | Crazy Raccoon | Falcons | YES Crazy Raccoon | 4 | 0.84 | 0.82 | 0.82 | won | $0.60 |
| 2026-10-17 05:54 | favourite | valorant | 100 Thieves | Team Vitality | YES 100 Thieves | 12 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-17 05:54 | favourite | dota2 | Nemiga Gaming | LFO | NO LFO | 13 | 0.62 | 0.61 | 0.61 | won | $4.72 |
| 2026-10-17 04:53 | model-only | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.79 | 0.71 | lost | -$1.49 |
| 2026-10-17 04:53 | favourite | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.71 | 0.71 | lost | -$1.49 |
| 2026-10-17 03:53 | favourite | dota2 | Xtreme Gaming | Yakult's Brothers | YES Xtreme Gaming | 10 | 0.81 | 0.79 | 0.79 | won | $1.79 |
| 2026-10-17 02:53 | favourite | dota2 | Xipto Esports | InterActive Philippines | NO InterActive Philippines | 11 | 0.74 | 0.72 | 0.72 | won | $2.71 |
| 2026-10-17 02:53 | model-only | dota2 | InterActive Philippines | Xipto Esports | YES InterActive Philippines | 40 | 0.29 | 0.39 | 0.28 | lost | -$12.18 |
| 2026-10-16 15:22 | favourite | dota2 | Stariy bog Team | Korb3n Team | YES Stariy bog Team | 2 | 0.62 | 0.61 | 0.61 | lost | -$1.28 |

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

