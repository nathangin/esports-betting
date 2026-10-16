# Esports paper trading (fake money)

Updated 2026-10-16 21:28 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 206 | 17 | 189 | 48 | -$377.33 | -17.2% | -0.7c (202) | $622.67 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 303 | 21 | 282 | 194 | -$124.81 | -6.1% | -1.2c (300) | $875.19 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

727 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5656 | 0.1926 |
| model | 0.6561 | 0.2319 |
| blend | 0.5644 | 0.1923 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 460 | 0.5755 | 0.6566 |
| dota2 | 119 | 0.5575 | 0.6511 |
| lol | 55 | 0.5191 | 0.7132 |
| ow | 41 | 0.4441 | 0.5241 |
| r6 | 32 | 0.6506 | 0.7267 |
| valorant | 20 | 0.6286 | 0.6749 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-16 15:22 | favourite | dota2 | Stariy bog Team | Korb3n Team | YES Stariy bog Team | 2 | 0.62 | 0.61 | 0.61 | lost | -$1.28 |
| 2026-10-16 12:51 | model-only | cs2 | 9z | Aurora Gaming | YES 9z | 16 | 0.31 | 0.36 | 0.31 | lost | -$5.20 |
| 2026-10-16 11:51 | favourite | cs2 | Young TigeRES | Young27 | YES Young TigeRES | 6 | 0.58 | 0.57 | 0.57 | won | $2.41 |
| 2026-10-16 11:51 | favourite | cs2 | Joga de terno | your end | YES Joga de terno | 14 | 0.58 | 0.57 | 0.57 | lost | -$8.36 |
| 2026-10-16 11:51 | favourite | cs2 | Black Phoenix | X-CITY | YES Black Phoenix | 10 | 0.86 | 0.83 | 0.83 | won | $1.31 |
| 2026-10-16 10:51 | favourite | dota2 | Royal Bear | InterActive Philippines | YES Royal Bear | 10 | 0.81 | 0.80 | 0.80 | won | $1.79 |
| 2026-10-16 10:51 | favourite | dota2 | by Owl Team | ALOHADANCE Team | YES by Owl Team | 6 | 0.71 | 0.70 | 0.71 | lost | -$4.35 |
| 2026-10-16 10:51 | favourite | cs2 | Voca | HAVU | NO HAVU | 14 | 0.60 | 0.58 | 0.58 | lost | -$8.64 |
| 2026-10-16 10:51 | favourite | r6 | Elevate | Fury | NO Fury | 2 | 0.74 | 0.72 | 0.72 | won | $0.49 |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Saint Sinners | YES ex-RUSTEC | 12 | 0.70 | 0.69 | 0.69 | won | $3.42 |
| 2026-10-16 09:51 | model-only | cs2 | Saint Sinners | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.32 | 0.40 | 0.31 | lost | -$0.34 |
| 2026-10-16 09:51 | favourite | cs2 | Team Nemesis | Nuclear TigeRES | YES Team Nemesis | 14 | 0.58 | 0.57 | 0.57 | won | $5.64 |
| 2026-10-16 09:51 | favourite | cs2 | ILLYRIANS | MORROW | YES ILLYRIANS | 10 | 0.80 | 0.77 | 0.77 | lost | -$8.12 |
| 2026-10-16 09:51 | model-only | cs2 | MORROW | ILLYRIANS | YES MORROW | 46 | 0.26 | 0.40 | 0.23 | won | $33.42 |
| 2026-10-16 09:51 | favourite | cs2 | Heroic | fnatic | YES Heroic | 13 | 0.66 | 0.66 | 0.66 | won | $4.21 |
| 2026-10-16 09:51 | model-only | cs2 | fnatic | Heroic | YES fnatic | 35 | 0.34 | 0.42 | 0.34 | lost | -$12.45 |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Bushido Wildcats | NO Bushido Wildcats | 14 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-10-16 09:21 | model-only | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.67 | 0.56 | open | - |
| 2026-10-16 09:21 | favourite | cs2 | Sokerorg | Bread Eaters Esports | NO Bread Eaters Esports | 11 | 0.78 | 0.77 | 0.77 | won | $2.28 |
| 2026-10-16 09:21 | favourite | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.56 | 0.56 | open | - |
| 2026-10-16 08:51 | model-only | dota2 | potn9ki | White Sails | YES potn9ki | 1 | 0.42 | 0.50 | 0.42 | open | - |
| 2026-10-16 08:51 | model-only | dota2 | PuckChamp | Dawn Bulls | NO Dawn Bulls | 130 | 0.10 | 0.23 | 0.09 | lost | -$13.82 |
| 2026-10-16 08:51 | favourite | dota2 | CyberHero | Mena Warriors | YES CyberHero | 10 | 0.86 | 0.85 | 0.85 | won | $1.31 |
| 2026-10-16 08:51 | favourite | cs2 | HAVU | RoundsGG | YES HAVU | 10 | 0.83 | 0.82 | 0.82 | won | $1.60 |
| 2026-10-16 08:51 | model-only | cs2 | RoundsGG | HAVU | NO HAVU | 69 | 0.19 | 0.40 | 0.18 | lost | -$13.86 |

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

