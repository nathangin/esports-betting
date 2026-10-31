# Esports paper trading (fake money)

Updated 2026-10-31 16:37 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 466 | 37 | 429 | 145 | -$180.45 | -3.9% | -0.4c (460) | $819.55 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 751 | 56 | 695 | 457 | -$378.37 | -7.9% | -1.5c (742) | $621.63 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1572 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5791 | 0.1989 |
| model | 0.6516 | 0.2303 |
| blend | 0.5789 | 0.1990 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1029 | 0.5915 | 0.6591 |
| dota2 | 240 | 0.5443 | 0.6282 |
| ow | 95 | 0.5020 | 0.5282 |
| lol | 87 | 0.5779 | 0.7235 |
| valorant | 77 | 0.5981 | 0.6739 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-31 16:22 | favourite | cs2 | Iberian Soul | OG | NO OG | 10 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-31 15:52 | favourite | ow | Team Risk | 1234 | YES Team Risk | 9 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-10-31 15:52 | model-only | ow | 1234 | Team Risk | YES 1234 | 41 | 0.39 | 0.48 | 0.36 | open | - |
| 2026-10-31 15:52 | favourite | lol | LYON | LOS | YES LYON | 8 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-10-31 15:22 | favourite | cs2 | Turma do Pagode | Low Cortisol | NO Low Cortisol | 9 | 0.63 | 0.60 | 0.60 | open | - |
| 2026-10-31 15:22 | favourite | cs2 | Monte | prodigy | YES Monte | 7 | 0.79 | 0.76 | 0.76 | open | - |
| 2026-10-31 15:07 | favourite | cs2 | ShindeN | Isurus | NO Isurus | 7 | 0.84 | 0.84 | 0.84 | open | - |
| 2026-10-31 15:07 | model-only | cs2 | Isurus | ShindeN | YES Isurus | 93 | 0.17 | 0.38 | 0.16 | open | - |
| 2026-10-31 14:52 | favourite | cs2 | PRIVATE | Omega | NO Omega | 8 | 0.77 | 0.76 | 0.76 | open | - |
| 2026-10-31 14:52 | model-only | cs2 | Omega | PRIVATE | NO PRIVATE | 66 | 0.24 | 0.35 | 0.24 | open | - |
| 2026-10-31 13:52 | favourite | dota2 | potn9ki | Hokori | YES potn9ki | 7 | 0.88 | 0.84 | 0.84 | open | - |
| 2026-10-31 13:52 | favourite | cs2 | Sokerorg | Fortress | NO Fortress | 3 | 0.82 | 0.82 | 0.82 | open | - |
| 2026-10-31 13:52 | model-only | cs2 | Fortress | Sokerorg | NO Sokerorg | 85 | 0.19 | 0.29 | 0.18 | open | - |
| 2026-10-31 13:52 | favourite | cs2 | Acend | Butterfly | NO Butterfly | 8 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-31 13:22 | favourite | cs2 | JiJieHao | BASEMENT BOYS | NO BASEMENT BOYS | 7 | 0.77 | 0.77 | 0.77 | won | $1.52 |
| 2026-10-31 13:22 | model-only | cs2 | BASEMENT BOYS | JiJieHao | YES BASEMENT BOYS | 67 | 0.24 | 0.42 | 0.23 | lost | -$16.94 |
| 2026-10-31 11:51 | model-only | cs2 | Procyon Gaming | Galorys | NO Galorys | 5 | 0.26 | 0.46 | 0.25 | won | $3.63 |
| 2026-10-31 11:51 | model-only | cs2 | Bounty Hunters Esports | BARCA | NO BARCA | 1 | 0.44 | 0.63 | 0.44 | lost | -$0.46 |
| 2026-10-31 11:51 | favourite | cs2 | BARCA | Bounty Hunters Esports | NO Bounty Hunters Esports | 10 | 0.56 | 0.56 | 0.56 | won | $4.22 |
| 2026-10-31 11:51 | model-only | cs2 | WRAITH PCIFIC | Nuclear TigeRES | NO Nuclear TigeRES | 8 | 0.18 | 0.41 | 0.18 | won | $6.47 |
| 2026-10-31 11:51 | favourite | cs2 | paiN | naocopulas | NO naocopulas | 7 | 0.80 | 0.79 | 0.79 | lost | -$5.68 |
| 2026-10-31 11:51 | model-only | dota2 | GamerLegion | Team Yandex | NO Team Yandex | 124 | 0.13 | 0.23 | 0.13 | lost | -$17.11 |
| 2026-10-31 11:51 | favourite | cs2 | Galorys | Procyon Gaming | YES Galorys | 8 | 0.75 | 0.75 | 0.75 | lost | -$6.11 |
| 2026-10-31 11:51 | model-only | cs2 | 5star | 1WIN | NO 1WIN | 134 | 0.12 | 0.36 | 0.11 | lost | -$17.08 |
| 2026-10-31 11:51 | favourite | cs2 | 1WIN | 5star | YES 1WIN | 6 | 0.89 | 0.89 | 0.89 | won | $0.61 |

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

