# Esports paper trading (fake money)

Updated 2026-10-16 10:36 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 205 | 23 | 182 | 47 | -$376.36 | -17.5% | -0.7c (198) | $623.64 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 295 | 34 | 261 | 180 | -$121.51 | -6.3% | -1.1c (287) | $878.49 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

678 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5685 | 0.1938 |
| model | 0.6595 | 0.2334 |
| blend | 0.5674 | 0.1935 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 428 | 0.5726 | 0.6591 |
| dota2 | 108 | 0.5698 | 0.6491 |
| lol | 54 | 0.5255 | 0.7203 |
| ow | 39 | 0.4599 | 0.5419 |
| r6 | 30 | 0.6785 | 0.7286 |
| valorant | 19 | 0.6386 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Saint Sinners | YES ex-RUSTEC | 12 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | Saint Sinners | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.32 | 0.40 | 0.31 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | Team Nemesis | Nuclear TigeRES | YES Team Nemesis | 14 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | ILLYRIANS | MORROW | YES ILLYRIANS | 10 | 0.80 | 0.77 | 0.77 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | MORROW | ILLYRIANS | YES MORROW | 46 | 0.26 | 0.40 | 0.23 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | Heroic | fnatic | YES Heroic | 13 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | fnatic | Heroic | YES fnatic | 35 | 0.34 | 0.42 | 0.34 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Bushido Wildcats | NO Bushido Wildcats | 14 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-10-16 09:21 | favourite | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.56 | 0.56 | open | - |
| 2026-10-16 09:21 | model-only | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.67 | 0.56 | open | - |
| 2026-10-16 09:21 | favourite | cs2 | Sokerorg | Bread Eaters Esports | NO Bread Eaters Esports | 11 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-16 08:51 | favourite | dota2 | CyberHero | Mena Warriors | YES CyberHero | 10 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-16 08:51 | model-only | cs2 | RoundsGG | HAVU | NO HAVU | 69 | 0.19 | 0.40 | 0.18 | lost | -$13.86 |
| 2026-10-16 08:51 | favourite | cs2 | HAVU | RoundsGG | YES HAVU | 10 | 0.83 | 0.82 | 0.82 | won | $1.60 |
| 2026-10-16 08:51 | model-only | dota2 | potn9ki | White Sails | YES potn9ki | 1 | 0.42 | 0.50 | 0.42 | open | - |
| 2026-10-16 08:51 | model-only | dota2 | PuckChamp | Dawn Bulls | NO Dawn Bulls | 130 | 0.10 | 0.23 | 0.09 | open | - |
| 2026-10-16 08:51 | favourite | dota2 | White Sails | potn9ki | NO potn9ki | 14 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-16 08:21 | favourite | ow | T1 | Cheeseburger | NO Cheeseburger | 1 | 0.80 | 0.80 | 0.80 | open | - |
| 2026-10-16 08:21 | model-only | ow | Cheeseburger | T1 | NO T1 | 9 | 0.20 | 0.25 | 0.20 | open | - |
| 2026-10-16 07:50 | favourite | valorant | 100 Thieves | G2 Esports | YES 100 Thieves | 13 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-16 07:50 | favourite | r6 | Weibo Gaming | Sharper Esport | NO Sharper Esport | 9 | 0.88 | 0.87 | 0.87 | open | - |
| 2026-10-16 06:50 | model-only | cs2 | Voca | Phantom | NO Phantom | 30 | 0.45 | 0.60 | 0.44 | lost | -$14.02 |
| 2026-10-16 06:50 | favourite | cs2 | Eternal Fire | Apogee Esports | YES Eternal Fire | 12 | 0.69 | 0.68 | 0.68 | open | - |
| 2026-10-16 06:50 | model-only | cs2 | Black Phoenix | ILLYRIANS | NO ILLYRIANS | 1 | 0.65 | 0.71 | 0.63 | open | - |
| 2026-10-16 06:50 | favourite | cs2 | Black Phoenix | ILLYRIANS | NO ILLYRIANS | 1 | 0.65 | 0.63 | 0.63 | open | - |

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

