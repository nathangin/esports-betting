# Esports paper trading (fake money)

Updated 2026-10-28 00:11 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 403 | 32 | 371 | 123 | -$120.14 | -3.1% | -0.5c (398) | $879.86 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 628 | 40 | 588 | 389 | -$307.16 | -7.3% | -1.5c (623) | $692.84 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1372 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5796 | 0.1990 |
| model | 0.6565 | 0.2325 |
| blend | 0.5792 | 0.1990 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 893 | 0.5931 | 0.6637 |
| dota2 | 205 | 0.5521 | 0.6362 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 82 | 0.5655 | 0.7200 |
| valorant | 65 | 0.5659 | 0.6724 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-27 15:50 | model-only | lol | Mental Rush | Rising Bees | NO Rising Bees | 5 | 0.32 | 0.47 | 0.31 | lost | -$1.68 |
| 2026-10-27 15:50 | favourite | cs2 | Vitality | Natus Vincere | NO Natus Vincere | 5 | 0.69 | 0.69 | 0.69 | won | $1.47 |
| 2026-10-27 15:50 | favourite | cs2 | HOTU | Luminosity | NO Luminosity | 1 | 0.59 | 0.60 | 0.60 | won | $0.39 |
| 2026-10-27 15:50 | model-only | cs2 | HOTU | Luminosity | NO Luminosity | 1 | 0.59 | 0.65 | 0.60 | won | $0.39 |
| 2026-10-27 15:50 | favourite | cs2 | Banger Gang | aimers | YES Banger Gang | 11 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-10-27 15:50 | model-only | cs2 | Banger Gang | aimers | YES Banger Gang | 30 | 0.57 | 0.67 | 0.56 | open | - |
| 2026-10-27 15:24 | favourite | cs2 | Winx | eSuba | YES Winx | 12 | 0.54 | 0.53 | 0.53 | won | $5.31 |
| 2026-10-27 15:24 | model-only | cs2 | eSuba | Winx | NO Winx | 28 | 0.48 | 0.55 | 0.47 | lost | -$13.93 |
| 2026-10-27 14:54 | favourite | dota2 | BetBoom Team | Astra Invicta | NO Astra Invicta | 10 | 0.66 | 0.66 | 0.66 | lost | -$6.76 |
| 2026-10-27 14:54 | favourite | cs2 | fnatic | Astralis | NO Astralis | 11 | 0.59 | 0.58 | 0.58 | won | $4.32 |
| 2026-10-27 14:54 | model-only | cs2 | Astralis | fnatic | YES Astralis | 40 | 0.42 | 0.53 | 0.41 | lost | -$17.49 |
| 2026-10-27 13:54 | favourite | cs2 | BakS eSports | Saint Sinners | YES BakS eSports | 10 | 0.65 | 0.64 | 0.64 | won | $3.34 |
| 2026-10-27 13:54 | model-only | cs2 | Saint Sinners | BakS eSports | NO BakS eSports | 1 | 0.37 | 0.42 | 0.36 | lost | -$0.39 |
| 2026-10-27 13:54 | favourite | cs2 | Wingman | Revise | YES Wingman | 12 | 0.56 | 0.54 | 0.54 | lost | -$6.93 |
| 2026-10-27 13:54 | favourite | dota2 | Zero Tenacity | Pibbles Corp | NO Pibbles Corp | 2 | 0.84 | 0.80 | 0.80 | won | $0.30 |
| 2026-10-27 13:24 | favourite | dota2 | BetBoom Team | LEGION | NO LEGION | 10 | 0.68 | 0.68 | 0.68 | lost | -$6.96 |
| 2026-10-27 13:24 | model-only | dota2 | LEGION | BetBoom Team | NO BetBoom Team | 39 | 0.32 | 0.51 | 0.32 | won | $25.92 |
| 2026-10-27 12:54 | favourite | cs2 | Spirit | MOUZ | NO MOUZ | 12 | 0.55 | 0.55 | 0.54 | lost | -$6.81 |
| 2026-10-27 12:54 | favourite | cs2 | Legacy | TheMongolz | YES Legacy | 12 | 0.57 | 0.56 | 0.56 | lost | -$7.05 |
| 2026-10-27 12:54 | model-only | cs2 | TheMongolz | Legacy | NO Legacy | 34 | 0.44 | 0.49 | 0.44 | won | $18.45 |
| 2026-10-27 12:24 | favourite | cs2 | Inner Circle Esports | Team Nemesis | YES Inner Circle Esports | 9 | 0.78 | 0.77 | 0.77 | won | $1.87 |
| 2026-10-27 11:54 | favourite | dota2 | Astra Invicta | LEGION | YES Astra Invicta | 10 | 0.68 | 0.67 | 0.67 | lost | -$6.96 |
| 2026-10-27 10:54 | favourite | cs2 | ex-RUSTEC | Spirit Academy | YES ex-RUSTEC | 13 | 0.53 | 0.52 | 0.52 | lost | -$7.12 |
| 2026-10-27 10:54 | model-only | cs2 | Spirit Academy | ex-RUSTEC | NO ex-RUSTEC | 4 | 0.49 | 0.57 | 0.48 | won | $1.97 |
| 2026-10-27 10:54 | favourite | cs2 | Nuclear TigeRES | FOKUS | YES Nuclear TigeRES | 14 | 0.51 | 0.51 | 0.51 | lost | -$7.39 |

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

