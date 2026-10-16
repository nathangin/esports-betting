# Esports paper trading (fake money)

Updated 2026-10-16 11:51 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 205 | 21 | 184 | 47 | -$378.94 | -17.6% | -0.7c (201) | $621.06 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 302 | 36 | 266 | 183 | -$121.73 | -6.2% | -1.2c (296) | $878.27 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

684 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5685 | 0.1938 |
| model | 0.6601 | 0.2337 |
| blend | 0.5674 | 0.1935 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 431 | 0.5752 | 0.6616 |
| dota2 | 109 | 0.5670 | 0.6467 |
| lol | 54 | 0.5255 | 0.7203 |
| ow | 40 | 0.4539 | 0.5356 |
| r6 | 31 | 0.6612 | 0.7248 |
| valorant | 19 | 0.6386 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-16 11:51 | favourite | cs2 | Young TigeRES | Young27 | YES Young TigeRES | 6 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-16 11:51 | favourite | cs2 | Joga de terno | your end | YES Joga de terno | 14 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-16 11:51 | favourite | cs2 | Black Phoenix | X-CITY | YES Black Phoenix | 10 | 0.86 | 0.83 | 0.83 | open | - |
| 2026-10-16 10:51 | favourite | r6 | Elevate | Fury | NO Fury | 2 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-10-16 10:51 | favourite | dota2 | Royal Bear | InterActive Philippines | YES Royal Bear | 10 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-10-16 10:51 | favourite | dota2 | by Owl Team | ALOHADANCE Team | YES by Owl Team | 6 | 0.71 | 0.70 | 0.71 | open | - |
| 2026-10-16 10:51 | favourite | cs2 | Voca | HAVU | NO HAVU | 14 | 0.60 | 0.58 | 0.58 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Saint Sinners | YES ex-RUSTEC | 12 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | Saint Sinners | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.32 | 0.40 | 0.31 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | Team Nemesis | Nuclear TigeRES | YES Team Nemesis | 14 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | ILLYRIANS | MORROW | YES ILLYRIANS | 10 | 0.80 | 0.77 | 0.77 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | MORROW | ILLYRIANS | YES MORROW | 46 | 0.26 | 0.40 | 0.23 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | Heroic | fnatic | YES Heroic | 13 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-10-16 09:51 | model-only | cs2 | fnatic | Heroic | YES fnatic | 35 | 0.34 | 0.42 | 0.34 | open | - |
| 2026-10-16 09:51 | favourite | cs2 | ex-RUSTEC | Bushido Wildcats | NO Bushido Wildcats | 14 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-10-16 09:21 | favourite | cs2 | Sokerorg | Bread Eaters Esports | NO Bread Eaters Esports | 11 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-16 09:21 | model-only | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.67 | 0.56 | open | - |
| 2026-10-16 09:21 | favourite | cs2 | STATE | TheChampionGG | NO TheChampionGG | 2 | 0.59 | 0.56 | 0.56 | open | - |
| 2026-10-16 08:51 | favourite | dota2 | White Sails | potn9ki | NO potn9ki | 14 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-16 08:51 | model-only | dota2 | potn9ki | White Sails | YES potn9ki | 1 | 0.42 | 0.50 | 0.42 | open | - |
| 2026-10-16 08:51 | model-only | dota2 | PuckChamp | Dawn Bulls | NO Dawn Bulls | 130 | 0.10 | 0.23 | 0.09 | open | - |
| 2026-10-16 08:51 | favourite | dota2 | CyberHero | Mena Warriors | YES CyberHero | 10 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-16 08:51 | favourite | cs2 | HAVU | RoundsGG | YES HAVU | 10 | 0.83 | 0.82 | 0.82 | won | $1.60 |
| 2026-10-16 08:51 | model-only | cs2 | RoundsGG | HAVU | NO HAVU | 69 | 0.19 | 0.40 | 0.18 | lost | -$13.86 |
| 2026-10-16 08:21 | model-only | ow | Cheeseburger | T1 | NO T1 | 9 | 0.20 | 0.25 | 0.20 | lost | -$1.91 |

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

