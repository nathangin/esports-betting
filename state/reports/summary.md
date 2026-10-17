# Esports paper trading (fake money)

Updated 2026-10-17 14:05 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 218 | 19 | 199 | 50 | -$437.60 | -19.1% | -0.8c (214) | $562.40 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 318 | 24 | 294 | 203 | -$112.01 | -5.2% | -1.3c (315) | $887.99 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

748 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5653 | 0.1923 |
| model | 0.6548 | 0.2313 |
| blend | 0.5642 | 0.1920 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 463 | 0.5740 | 0.6558 |
| dota2 | 126 | 0.5483 | 0.6464 |
| lol | 57 | 0.5490 | 0.7107 |
| ow | 46 | 0.4389 | 0.5251 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 21 | 0.6521 | 0.6977 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-17 11:50 | model-only | ow | Solus Victorem | Weibo Gaming | YES Solus Victorem | 71 | 0.10 | 0.21 | 0.09 | lost | -$7.55 |
| 2026-10-17 11:50 | favourite | dota2 | Yellow Submarine | Spirit Academy | YES Yellow Submarine | 9 | 0.89 | 0.89 | 0.89 | open | - |
| 2026-10-17 11:50 | model-only | dota2 | Spirit Academy | Yellow Submarine | YES Spirit Academy | 2 | 0.12 | 0.26 | 0.12 | open | - |
| 2026-10-17 10:54 | favourite | dota2 | Nix Team | by Owl Team | NO by Owl Team | 12 | 0.69 | 0.67 | 0.67 | open | - |
| 2026-10-17 10:54 | model-only | dota2 | by Owl Team | Nix Team | YES by Owl Team | 33 | 0.35 | 0.57 | 0.33 | open | - |
| 2026-10-17 09:54 | favourite | r6 | SCARZ | FearX | NO FearX | 11 | 0.59 | 0.58 | 0.58 | won | $4.32 |
| 2026-10-17 09:54 | model-only | r6 | FearX | SCARZ | YES FearX | 22 | 0.43 | 0.48 | 0.42 | lost | -$9.84 |
| 2026-10-17 08:54 | model-only | dota2 | PuckChamp | Inner Circle | YES PuckChamp | 60 | 0.19 | 0.35 | 0.18 | lost | -$12.05 |
| 2026-10-17 08:54 | favourite | dota2 | Team Lynx | Dawn Bulls | NO Dawn Bulls | 16 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-17 08:54 | favourite | dota2 | Inner Circle | PuckChamp | YES Inner Circle | 10 | 0.83 | 0.82 | 0.82 | won | $1.60 |
| 2026-10-17 07:54 | favourite | lol | BNK FEARX | Team WE | NO Team WE | 12 | 0.68 | 0.68 | 0.68 | won | $3.65 |
| 2026-10-17 07:54 | model-only | lol | Team WE | BNK FEARX | NO BNK FEARX | 36 | 0.32 | 0.47 | 0.32 | lost | -$12.07 |
| 2026-10-17 07:54 | favourite | dota2 | Gorgc Team | ALOHADANCE Team | YES Gorgc Team | 13 | 0.64 | 0.63 | 0.63 | won | $4.47 |
| 2026-10-17 07:54 | model-only | dota2 | ALOHADANCE Team | Gorgc Team | YES ALOHADANCE Team | 30 | 0.38 | 0.46 | 0.37 | lost | -$11.90 |
| 2026-10-17 06:54 | model-only | ow | ZANSIDE GAMING | T1 | NO T1 | 104 | 0.11 | 0.21 | 0.09 | lost | -$12.16 |
| 2026-10-17 06:54 | model-only | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 22 | 0.53 | 0.70 | 0.53 | won | $9.95 |
| 2026-10-17 06:54 | favourite | dota2 | Team Resilience | Team Tidebound | NO Team Tidebound | 16 | 0.53 | 0.53 | 0.53 | won | $7.24 |
| 2026-10-17 06:54 | favourite | r6 | CAG by VARREL | Dplus | YES CAG by VARREL | 12 | 0.69 | 0.67 | 0.67 | lost | -$8.46 |
| 2026-10-17 06:54 | model-only | r6 | Dplus | CAG by VARREL | NO CAG by VARREL | 14 | 0.34 | 0.44 | 0.33 | won | $9.02 |
| 2026-10-17 06:24 | favourite | ow | Crazy Raccoon | Falcons | YES Crazy Raccoon | 4 | 0.84 | 0.82 | 0.82 | won | $0.60 |
| 2026-10-17 05:54 | favourite | valorant | 100 Thieves | Team Vitality | YES 100 Thieves | 12 | 0.68 | 0.68 | 0.68 | lost | -$8.35 |
| 2026-10-17 05:54 | favourite | dota2 | Nemiga Gaming | LFO | NO LFO | 13 | 0.62 | 0.61 | 0.61 | won | $4.72 |
| 2026-10-17 04:53 | favourite | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.71 | 0.71 | lost | -$1.49 |
| 2026-10-17 04:53 | model-only | ow | O2 Blast | Poker Face | YES O2 Blast | 2 | 0.73 | 0.79 | 0.71 | lost | -$1.49 |
| 2026-10-17 03:53 | favourite | dota2 | Xtreme Gaming | Yakult's Brothers | YES Xtreme Gaming | 10 | 0.81 | 0.79 | 0.79 | won | $1.79 |

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

