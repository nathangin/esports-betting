# Esports paper trading (fake money)

Updated 2026-10-23 17:02 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 324 | 28 | 296 | 88 | -$362.84 | -11.7% | -0.9c (318) | $637.16 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 509 | 42 | 467 | 320 | -$161.04 | -4.7% | -1.4c (505) | $838.96 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1108 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5712 | 0.1950 |
| model | 0.6555 | 0.2320 |
| blend | 0.5700 | 0.1947 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 730 | 0.5853 | 0.6629 |
| dota2 | 169 | 0.5489 | 0.6456 |
| ow | 63 | 0.4710 | 0.5157 |
| lol | 62 | 0.5472 | 0.7027 |
| valorant | 46 | 0.5477 | 0.6593 |
| r6 | 38 | 0.6330 | 0.7095 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-23 16:52 | model-only | valorant | Gentle Mates GC | Team Liquid Brazil | YES Gentle Mates GC | 1 | 0.36 | 0.48 | 0.36 | open | - |
| 2026-10-23 16:52 | model-only | cs2 | OldBoys | Hermine Esports Club | NO Hermine Esports Club | 16 | 0.55 | 0.67 | 0.53 | open | - |
| 2026-10-23 14:52 | favourite | cs2 | BORRACHEIROS | QUINTESSENCIA | YES BORRACHEIROS | 4 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-10-23 14:52 | model-only | cs2 | QUINTESSENCIA | BORRACHEIROS | NO BORRACHEIROS | 3 | 0.32 | 0.55 | 0.31 | open | - |
| 2026-10-23 13:51 | favourite | dota2 | Team Lynx | Inner Circle | YES Team Lynx | 11 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-23 12:51 | favourite | dota2 | BetBoom Team | Astra Invicta | YES BetBoom Team | 15 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-23 12:51 | favourite | cs2 | INOX Division | Team ACES | NO Team ACES | 5 | 0.60 | 0.56 | 0.56 | open | - |
| 2026-10-23 11:51 | favourite | cs2 | ALKA | Los Ninos | YES ALKA | 11 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-23 11:51 | model-only | cs2 | JiJieHao | Eternal Fire | NO Eternal Fire | 20 | 0.43 | 0.48 | 0.43 | open | - |
| 2026-10-23 11:51 | favourite | cs2 | Eternal Fire | JiJieHao | NO JiJieHao | 15 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-23 11:51 | model-only | cs2 | Los Ninos | ALKA | YES Los Ninos | 29 | 0.24 | 0.42 | 0.23 | open | - |
| 2026-10-23 11:51 | favourite | cs2 | Sokerorg | maybe | YES Sokerorg | 13 | 0.66 | 0.64 | 0.64 | won | $4.21 |
| 2026-10-23 11:51 | favourite | cs2 | K27 | Virtus.pro | YES K27 | 15 | 0.55 | 0.55 | 0.55 | lost | -$8.51 |
| 2026-10-23 11:51 | favourite | cs2 | WBT Academy | LPH Gaming | NO LPH Gaming | 13 | 0.65 | 0.63 | 0.63 | won | $4.34 |
| 2026-10-23 10:51 | favourite | dota2 | Dawn Bulls | Team Synapse | YES Dawn Bulls | 14 | 0.61 | 0.59 | 0.59 | lost | -$8.78 |
| 2026-10-23 10:51 | model-only | dota2 | Team Synapse | Dawn Bulls | YES Team Synapse | 26 | 0.42 | 0.51 | 0.41 | won | $14.63 |
| 2026-10-23 09:51 | model-only | dota2 | GamerLegion | Team Liquid | YES GamerLegion | 50 | 0.22 | 0.37 | 0.23 | won | $38.39 |
| 2026-10-23 09:51 | model-only | cs2 | ILLYRIANS | Nuclear TigeRES | NO Nuclear TigeRES | 64 | 0.17 | 0.36 | 0.15 | lost | -$11.52 |
| 2026-10-23 09:51 | favourite | cs2 | Nuclear TigeRES | ILLYRIANS | NO ILLYRIANS | 9 | 0.87 | 0.85 | 0.85 | won | $1.09 |
| 2026-10-23 09:51 | favourite | cs2 | Spirit Academy | Inner Circle Academy | NO Inner Circle Academy | 15 | 0.56 | 0.56 | 0.55 | lost | -$8.66 |
| 2026-10-23 09:51 | favourite | cs2 | XI Esport | eSuba | YES XI Esport | 14 | 0.57 | 0.55 | 0.55 | open | - |
| 2026-10-23 09:51 | model-only | cs2 | Spirit Academy | Inner Circle Academy | NO Inner Circle Academy | 20 | 0.56 | 0.63 | 0.55 | lost | -$11.55 |
| 2026-10-23 09:51 | favourite | dota2 | Team Liquid | GamerLegion | YES Team Liquid | 11 | 0.77 | 0.78 | 0.78 | lost | -$8.61 |
| 2026-10-23 09:51 | favourite | valorant | Dragon Ranger Gaming | FunPlus Phoenix | YES Dragon Ranger Gaming | 15 | 0.56 | 0.55 | 0.55 | won | $6.34 |
| 2026-10-23 09:51 | model-only | valorant | FunPlus Phoenix | Dragon Ranger Gaming | YES FunPlus Phoenix | 24 | 0.45 | 0.65 | 0.45 | lost | -$11.22 |

## Backtest on real Kalshi prices

8346 settled matches from 2026-05-28 to 2026-10-19, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 23 | $422.99 | -$10.99 | -2.6% | -39.0% to +46.3% | 57% | -0.0c | 8% |
| model only | 1998 | $8,526.95 | -$990.95 | -11.6% | -20.1% to -3.0% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4018 | $16,341.50 | -$762.50 | -4.7% | -6.9% to -2.4% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3742 | $8,889.87 | -$982.87 | -11.1% | -16.6% to -5.4% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8121 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5723 | 0.1955 | 69.3% |
| model | 0.6605 | 0.2343 | 59.6% |
| blend | 0.5719 | 0.1954 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1335 | 0.525 | 0.524 |
| (0.55, 0.6] | 1359 | 0.577 | 0.550 |
| (0.6, 0.65] | 1254 | 0.626 | 0.635 |
| (0.65, 0.7] | 1092 | 0.676 | 0.702 |
| (0.7, 0.75] | 921 | 0.726 | 0.773 |
| (0.75, 0.8] | 786 | 0.776 | 0.812 |
| (0.8, 0.85] | 668 | 0.826 | 0.826 |
| (0.85, 0.9] | 503 | 0.877 | 0.903 |
| (0.9, 1.0] | 428 | 0.932 | 0.956 |

