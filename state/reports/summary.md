# Esports paper trading (fake money)

Updated 2026-10-31 12:57 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 461 | 41 | 420 | 142 | -$143.97 | -3.2% | -0.4c (456) | $856.03 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 740 | 56 | 684 | 449 | -$379.58 | -8.0% | -1.4c (734) | $620.42 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1556 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5767 | 0.1979 |
| model | 0.6510 | 0.2300 |
| blend | 0.5763 | 0.1979 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1017 | 0.5891 | 0.6586 |
| dota2 | 238 | 0.5427 | 0.6284 |
| ow | 94 | 0.4924 | 0.5220 |
| lol | 87 | 0.5779 | 0.7235 |
| valorant | 76 | 0.6002 | 0.6750 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-31 11:51 | favourite | dota2 | Team Yandex | GamerLegion | NO GamerLegion | 7 | 0.87 | 0.87 | 0.87 | open | - |
| 2026-10-31 11:51 | model-only | dota2 | GamerLegion | Team Yandex | NO Team Yandex | 124 | 0.13 | 0.23 | 0.13 | open | - |
| 2026-10-31 11:51 | favourite | cs2 | 1WIN | 5star | YES 1WIN | 6 | 0.89 | 0.89 | 0.89 | open | - |
| 2026-10-31 11:51 | model-only | cs2 | 5star | 1WIN | NO 1WIN | 134 | 0.12 | 0.36 | 0.11 | open | - |
| 2026-10-31 11:51 | favourite | cs2 | Galorys | Procyon Gaming | YES Galorys | 8 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-10-31 11:51 | model-only | cs2 | Procyon Gaming | Galorys | NO Galorys | 5 | 0.26 | 0.46 | 0.25 | open | - |
| 2026-10-31 11:51 | favourite | cs2 | paiN | naocopulas | NO naocopulas | 7 | 0.80 | 0.79 | 0.79 | open | - |
| 2026-10-31 11:51 | model-only | cs2 | WRAITH PCIFIC | Nuclear TigeRES | NO Nuclear TigeRES | 8 | 0.18 | 0.41 | 0.18 | open | - |
| 2026-10-31 11:51 | favourite | cs2 | BARCA | Bounty Hunters Esports | NO Bounty Hunters Esports | 10 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-31 11:51 | model-only | cs2 | Bounty Hunters Esports | BARCA | NO BARCA | 1 | 0.44 | 0.63 | 0.44 | open | - |
| 2026-10-31 10:51 | favourite | cs2 | Saint Sinners | Misa Esports | YES Saint Sinners | 10 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-10-31 10:51 | model-only | cs2 | Misa Esports | Saint Sinners | YES Misa Esports | 39 | 0.41 | 0.58 | 0.41 | open | - |
| 2026-10-31 09:51 | favourite | valorant | Nova Esports | Any Questions Gaming | NO Any Questions Gaming | 9 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-31 09:51 | model-only | valorant | Any Questions Gaming | Nova Esports | YES Any Questions Gaming | 45 | 0.36 | 0.45 | 0.35 | open | - |
| 2026-10-31 09:51 | favourite | cs2 | FURIA | Nemiga | YES FURIA | 8 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-31 08:51 | favourite | cs2 | Optibet | Fraternity | NO Fraternity | 9 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-10-31 08:51 | model-only | cs2 | Fraternity | Optibet | NO Optibet | 1 | 0.38 | 0.57 | 0.36 | open | - |
| 2026-10-31 07:51 | model-only | cs2 | The Huns Esports | HOTU | YES The Huns Esports | 160 | 0.10 | 0.23 | 0.09 | lost | -$17.01 |
| 2026-10-31 07:51 | favourite | cs2 | Gatorian | gothboiclique | YES Gatorian | 11 | 0.54 | 0.52 | 0.52 | lost | -$6.14 |
| 2026-10-31 07:51 | favourite | cs2 | PsychoFace | Donstu Esports | NO Donstu Esports | 8 | 0.62 | 0.60 | 0.60 | lost | -$5.10 |
| 2026-10-31 07:51 | model-only | cs2 | Donstu Esports | PsychoFace | YES Donstu Esports | 37 | 0.44 | 0.59 | 0.40 | won | $20.08 |
| 2026-10-31 07:51 | favourite | cs2 | Apogee Esports | 9INE | NO 9INE | 10 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-31 07:51 | favourite | valorant | Unsettled Resentment | World Sports Invictus Gaming | YES Unsettled Resentment | 10 | 0.57 | 0.55 | 0.55 | won | $4.12 |
| 2026-10-31 06:51 | favourite | cs2 | Vitality | MOUZ | YES Vitality | 10 | 0.56 | 0.56 | 0.56 | lost | -$5.78 |
| 2026-10-31 06:20 | model-only | ow | ZETA DIVISION | T1 | YES ZETA DIVISION | 6 | 0.73 | 0.80 | 0.71 | won | $1.53 |

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

