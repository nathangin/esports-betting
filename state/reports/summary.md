# Esports paper trading (fake money)

Updated 2026-11-04 12:09 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 523 | 41 | 482 | 167 | -$118.27 | -2.2% | -0.3c (514) | $881.73 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 856 | 67 | 789 | 516 | -$447.59 | -8.5% | -1.5c (845) | $552.41 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1758 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5820 | 0.2002 |
| model | 0.6516 | 0.2302 |
| blend | 0.5821 | 0.2004 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1162 | 0.5942 | 0.6602 |
| dota2 | 273 | 0.5453 | 0.6263 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 90 | 0.5780 | 0.7232 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 46 | 0.6128 | 0.6882 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-04 11:54 | favourite | dota2 | GamerLegion | OG | YES GamerLegion | 10 | 0.51 | 0.50 | 0.50 | open | - |
| 2026-11-04 11:54 | favourite | dota2 | Zero Tenacity | angry birds | NO angry birds | 8 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-11-04 11:54 | model-only | dota2 | angry birds | Zero Tenacity | YES angry birds | 7 | 0.39 | 0.51 | 0.38 | open | - |
| 2026-11-04 11:54 | favourite | cs2 | MEIA NOITE | Damajuana | NO Damajuana | 6 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-11-04 11:54 | model-only | cs2 | Damajuana | MEIA NOITE | NO MEIA NOITE | 79 | 0.21 | 0.35 | 0.21 | open | - |
| 2026-11-04 10:54 | favourite | cs2 | ex-Zero Tenacity | PsychoFace | NO PsychoFace | 6 | 0.87 | 0.84 | 0.84 | open | - |
| 2026-11-04 10:54 | model-only | cs2 | PsychoFace | ex-Zero Tenacity | YES PsychoFace | 5 | 0.17 | 0.24 | 0.16 | open | - |
| 2026-11-04 10:54 | favourite | cs2 | megoshort | Honvéd | NO Honvéd | 9 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-11-04 10:24 | favourite | cs2 | Inner Circle Prospect | BRUTE SQ | YES Inner Circle Prospect | 9 | 0.55 | 0.52 | 0.52 | open | - |
| 2026-11-04 09:54 | favourite | dota2 | Natus Vincere | Yellow Submarine | YES Natus Vincere | 7 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-11-04 08:54 | favourite | dota2 | Inner Circle | PuckChamp | YES Inner Circle | 6 | 0.84 | 0.81 | 0.81 | open | - |
| 2026-11-04 08:24 | favourite | cs2 | FURIA | TheMongolz | YES FURIA | 7 | 0.74 | 0.73 | 0.73 | open | - |
| 2026-11-04 08:24 | model-only | cs2 | TheMongolz | FURIA | NO FURIA | 61 | 0.27 | 0.36 | 0.27 | open | - |
| 2026-11-04 08:24 | favourite | cs2 | Team Falcons | Natus Vincere | NO Natus Vincere | 9 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-04 07:53 | favourite | cs2 | ILLYRIANS | Bebop | YES ILLYRIANS | 8 | 0.66 | 0.65 | 0.65 | won | $2.59 |
| 2026-11-04 07:53 | favourite | cs2 | Leo Team | Spirit Academy | YES Leo Team | 8 | 0.60 | 0.59 | 0.59 | lost | -$4.94 |
| 2026-11-04 07:53 | model-only | cs2 | Spirit Academy | Leo Team | NO Leo Team | 7 | 0.42 | 0.55 | 0.41 | won | $3.94 |
| 2026-11-04 07:53 | favourite | cs2 | BakS eSports | Gothic | YES BakS eSports | 8 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-11-04 07:53 | favourite | cs2 | EYEBALLERS | Esport Academy Copenhagen | YES EYEBALLERS | 8 | 0.60 | 0.61 | 0.61 | open | - |
| 2026-11-04 07:53 | model-only | cs2 | Esport Academy Copenhagen | EYEBALLERS | YES Esport Academy Copenhagen | 37 | 0.39 | 0.45 | 0.39 | open | - |
| 2026-11-04 05:53 | favourite | cs2 | BetBoom Team | Liquid | YES BetBoom Team | 8 | 0.66 | 0.66 | 0.66 | won | $2.59 |
| 2026-11-04 03:23 | favourite | cs2 | Natus Vincere | B8 | NO B8 | 6 | 0.80 | 0.80 | 0.80 | won | $1.13 |
| 2026-11-04 03:23 | favourite | cs2 | BetBoom Team | Aurora Gaming | YES BetBoom Team | 7 | 0.73 | 0.72 | 0.72 | won | $1.79 |
| 2026-11-04 00:53 | favourite | cs2 | Team Falcons | Heroic | NO Heroic | 7 | 0.68 | 0.68 | 0.68 | won | $2.13 |
| 2026-11-04 00:53 | model-only | cs2 | Heroic | Team Falcons | NO Team Falcons | 51 | 0.33 | 0.52 | 0.32 | lost | -$17.62 |

## Backtest on real Kalshi prices

9155 settled matches from 2026-05-28 to 2026-11-02, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2020 | $9,242.02 | -$992.02 | -10.7% | -18.4% to -3.0% | 33% | -0.7c | 99% |
| always the favourite (1% flat) | 4414 | $17,347.39 | -$838.39 | -4.8% | -7.1% to -2.7% | 67% | -1.7c | 84% |
| always the underdog (1% flat) | 3784 | $8,995.47 | -$985.47 | -11.0% | -16.5% to -4.9% | 31% | -1.3c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8930 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5749 | 0.1968 | 68.9% |
| model | 0.6599 | 0.2340 | 59.6% |
| blend | 0.5747 | 0.1968 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1475 | 0.525 | 0.525 |
| (0.55, 0.6] | 1510 | 0.577 | 0.547 |
| (0.6, 0.65] | 1371 | 0.626 | 0.628 |
| (0.65, 0.7] | 1202 | 0.676 | 0.700 |
| (0.7, 0.75] | 1004 | 0.726 | 0.770 |
| (0.75, 0.8] | 855 | 0.776 | 0.807 |
| (0.8, 0.85] | 729 | 0.826 | 0.823 |
| (0.85, 0.9] | 536 | 0.877 | 0.903 |
| (0.9, 1.0] | 473 | 0.932 | 0.958 |

