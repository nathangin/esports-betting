# Esports paper trading (fake money)

Updated 2026-10-25 12:53 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 363 | 34 | 329 | 101 | -$261.78 | -7.7% | -0.9c (357) | $738.22 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 563 | 49 | 514 | 348 | -$192.86 | -5.1% | -1.3c (555) | $807.14 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1224 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5775 | 0.1977 |
| model | 0.6582 | 0.2332 |
| blend | 0.5767 | 0.1975 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 792 | 0.5902 | 0.6647 |
| dota2 | 181 | 0.5581 | 0.6470 |
| ow | 78 | 0.5178 | 0.5419 |
| lol | 74 | 0.5528 | 0.7199 |
| valorant | 56 | 0.5588 | 0.6651 |
| r6 | 43 | 0.6007 | 0.6818 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-25 12:52 | favourite | dota2 | Team Spirit | Astra Invicta | YES Team Spirit | 9 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-10-25 12:52 | favourite | cs2 | INOX Division | Acend | YES INOX Division | 1 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-25 12:52 | model-only | cs2 | Acend | INOX Division | YES Acend | 4 | 0.36 | 0.41 | 0.34 | open | - |
| 2026-10-25 12:52 | favourite | cs2 | Aurora Gaming | G2 | NO G2 | 13 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-25 12:52 | favourite | cs2 | MOUZ | 9z | NO 9z | 10 | 0.77 | 0.77 | 0.77 | open | - |
| 2026-10-25 12:52 | model-only | cs2 | 9z | MOUZ | YES 9z | 58 | 0.24 | 0.32 | 0.23 | open | - |
| 2026-10-25 11:52 | favourite | cs2 | STATE | G2 Ares | NO G2 Ares | 13 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-25 11:52 | model-only | cs2 | STATE | G2 Ares | NO G2 Ares | 25 | 0.58 | 0.67 | 0.56 | open | - |
| 2026-10-25 10:52 | favourite | dota2 | Inner Circle | Nemiga Gaming | YES Inner Circle | 11 | 0.70 | 0.68 | 0.68 | open | - |
| 2026-10-25 10:52 | favourite | cs2 | Spirit Academy | Sokerorg | YES Spirit Academy | 10 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-10-25 10:52 | favourite | cs2 | Metizport | BakS eSports | NO BakS eSports | 12 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-10-25 10:52 | model-only | cs2 | BakS eSports | Metizport | NO Metizport | 38 | 0.38 | 0.45 | 0.38 | open | - |
| 2026-10-25 10:22 | favourite | cs2 | Bread Eaters Esports | Gatorian | YES Bread Eaters Esports | 14 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-25 10:22 | favourite | cs2 | ILLYRIANS | eSuba | YES ILLYRIANS | 14 | 0.52 | 0.51 | 0.51 | open | - |
| 2026-10-25 10:22 | model-only | cs2 | Gatorian | Bread Eaters Esports | YES Gatorian | 29 | 0.49 | 0.58 | 0.47 | open | - |
| 2026-10-25 10:22 | favourite | valorant | Fire Flux Esports | BBL Esports | NO BBL Esports | 12 | 0.61 | 0.61 | 0.61 | open | - |
| 2026-10-25 10:22 | model-only | valorant | BBL Esports | Fire Flux Esports | YES BBL Esports | 24 | 0.40 | 0.45 | 0.39 | open | - |
| 2026-10-25 09:52 | favourite | cs2 | BetBoom Team | Nemiga | YES BetBoom Team | 13 | 0.59 | 0.58 | 0.58 | won | $5.10 |
| 2026-10-25 09:52 | model-only | cs2 | Nemiga | BetBoom Team | NO BetBoom Team | 35 | 0.42 | 0.65 | 0.42 | lost | -$15.30 |
| 2026-10-25 09:52 | favourite | cs2 | Vitality | TheMongolz | NO TheMongolz | 10 | 0.74 | 0.73 | 0.73 | won | $2.46 |
| 2026-10-25 09:52 | favourite | cs2 | ex-Zero Tenacity | Spirit Academy | YES ex-Zero Tenacity | 13 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-10-25 07:52 | favourite | dota2 | Team Lynx | salamit | YES Team Lynx | 12 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-25 07:52 | favourite | cs2 | mellren | Lavked | NO Lavked | 12 | 0.64 | 0.63 | 0.63 | lost | -$7.88 |
| 2026-10-25 07:52 | favourite | cs2 | MOUZ NXT | Vexar | YES MOUZ NXT | 13 | 0.56 | 0.52 | 0.52 | won | $5.49 |
| 2026-10-25 07:52 | model-only | cs2 | UNiTY esports | Acend | NO Acend | 25 | 0.59 | 0.66 | 0.59 | won | $9.82 |

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

