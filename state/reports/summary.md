# Esports paper trading (fake money)

Updated 2026-10-29 20:01 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 434 | 33 | 401 | 135 | -$86.11 | -2.0% | -0.4c (429) | $913.89 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 692 | 50 | 642 | 422 | -$332.29 | -7.3% | -1.5c (687) | $667.71 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1465 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5800 | 0.1992 |
| model | 0.6538 | 0.2312 |
| blend | 0.5797 | 0.1992 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 960 | 0.5933 | 0.6604 |
| dota2 | 224 | 0.5451 | 0.6288 |
| lol | 83 | 0.5638 | 0.7223 |
| ow | 83 | 0.5090 | 0.5369 |
| valorant | 71 | 0.5927 | 0.6790 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-29 18:21 | favourite | cs2 | Diamant Esports | Esport BERG | YES Diamant Esports | 1 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-29 18:06 | favourite | cs2 | Monte | Spirit Academy Black | YES Monte | 8 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-10-29 18:06 | favourite | cs2 | prodigy | Ducks | NO Ducks | 10 | 0.62 | 0.60 | 0.60 | open | - |
| 2026-10-29 17:51 | favourite | cs2 | Inner Circle Prospect | Fraternity | NO Fraternity | 9 | 0.68 | 0.66 | 0.66 | lost | -$6.26 |
| 2026-10-29 17:21 | favourite | cs2 | Astralis | Eternal Fire | YES Astralis | 10 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-29 16:51 | favourite | dota2 | OG | GamerLegion | NO GamerLegion | 11 | 0.56 | 0.56 | 0.55 | open | - |
| 2026-10-29 16:51 | favourite | cs2 | OldBoys | Hermine Esports Club | YES OldBoys | 1 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-29 16:51 | favourite | cs2 | GamerLegion | HOTU | YES GamerLegion | 1 | 0.54 | 0.52 | 0.52 | lost | -$0.56 |
| 2026-10-29 16:51 | favourite | cs2 | B8 Academy | BANGARANGA | NO BANGARANGA | 1 | 0.60 | 0.60 | 0.60 | won | $0.38 |
| 2026-10-29 16:51 | favourite | cs2 | Team ACES | 9INE | NO 9INE | 11 | 0.54 | 0.50 | 0.50 | open | - |
| 2026-10-29 16:31 | favourite | cs2 | Iberian Soul | TYLOO | NO TYLOO | 1 | 0.57 | 0.54 | 0.54 | open | - |
| 2026-10-29 15:50 | favourite | cs2 | FURIA | BetBoom Team | NO BetBoom Team | 8 | 0.75 | 0.74 | 0.74 | won | $1.89 |
| 2026-10-29 15:20 | favourite | cs2 | TTG Esports | Winx | YES TTG Esports | 12 | 0.53 | 0.51 | 0.51 | won | $5.43 |
| 2026-10-29 15:20 | favourite | cs2 | Aurora Young Blood | SPARX | YES Aurora Young Blood | 10 | 0.60 | 0.60 | 0.60 | won | $3.83 |
| 2026-10-29 14:50 | model-only | cs2 | fnatic | MIBR | YES fnatic | 30 | 0.43 | 0.49 | 0.42 | won | $16.58 |
| 2026-10-29 14:50 | favourite | cs2 | MIBR | fnatic | NO fnatic | 11 | 0.58 | 0.57 | 0.57 | lost | -$6.57 |
| 2026-10-29 14:50 | favourite | cs2 | Spirit Academy Green | RoundsGG | NO RoundsGG | 1 | 0.80 | 0.78 | 0.78 | won | $0.18 |
| 2026-10-29 13:50 | favourite | dota2 | Team Yandex | PARIVISION | NO PARIVISION | 11 | 0.57 | 0.57 | 0.57 | won | $4.54 |
| 2026-10-29 13:50 | favourite | cs2 | Acend | Saint Sinners | YES Acend | 10 | 0.62 | 0.60 | 0.60 | won | $3.63 |
| 2026-10-29 13:50 | model-only | cs2 | Saint Sinners | Acend | NO Acend | 1 | 0.40 | 0.45 | 0.40 | lost | -$0.42 |
| 2026-10-29 13:50 | favourite | cs2 | DNK | Fortress | NO Fortress | 1 | 0.68 | 0.69 | 0.69 | won | $0.30 |
| 2026-10-29 13:50 | model-only | cs2 | Fortress | DNK | NO DNK | 60 | 0.30 | 0.38 | 0.31 | lost | -$18.89 |
| 2026-10-29 12:50 | favourite | cs2 | MOUZ | Aurora Gaming | YES MOUZ | 10 | 0.63 | 0.63 | 0.63 | won | $3.53 |
| 2026-10-29 12:50 | favourite | cs2 | Iberian Soul | ZOTIX | YES Iberian Soul | 7 | 0.86 | 0.85 | 0.85 | won | $0.92 |
| 2026-10-29 12:50 | model-only | cs2 | Aurora Gaming | MOUZ | YES Aurora Gaming | 50 | 0.37 | 0.47 | 0.37 | lost | -$19.32 |

## Backtest on real Kalshi prices

8779 settled matches from 2026-05-28 to 2026-10-26, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 2012 | $8,014.92 | -$990.92 | -12.4% | -20.6% to -4.1% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4205 | $16,392.93 | -$775.93 | -4.7% | -7.0% to -2.5% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3757 | $9,447.49 | -$982.49 | -10.4% | -15.7% to -4.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8554 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5736 | 0.1961 | 69.2% |
| model | 0.6609 | 0.2344 | 59.5% |
| blend | 0.5732 | 0.1960 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1402 | 0.525 | 0.529 |
| (0.55, 0.6] | 1444 | 0.577 | 0.551 |
| (0.6, 0.65] | 1325 | 0.626 | 0.629 |
| (0.65, 0.7] | 1152 | 0.676 | 0.702 |
| (0.7, 0.75] | 964 | 0.726 | 0.772 |
| (0.75, 0.8] | 823 | 0.776 | 0.810 |
| (0.8, 0.85] | 698 | 0.826 | 0.827 |
| (0.85, 0.9] | 521 | 0.877 | 0.902 |
| (0.9, 1.0] | 450 | 0.932 | 0.956 |

