# Esports paper trading (fake money)

Updated 2026-11-03 09:50 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 507 | 40 | 467 | 160 | -$55.07 | -1.1% | -0.3c (500) | $944.93 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 821 | 59 | 762 | 497 | -$445.10 | -8.6% | -1.5c (814) | $554.90 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1686 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5818 | 0.2002 |
| model | 0.6514 | 0.2302 |
| blend | 0.5820 | 0.2004 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1106 | 0.5934 | 0.6596 |
| dota2 | 260 | 0.5487 | 0.6283 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-03 08:50 | favourite | dota2 | OG | LEGION | YES OG | 7 | 0.73 | 0.73 | 0.73 | open | - |
| 2026-11-03 08:50 | model-only | dota2 | LEGION | OG | YES LEGION | 20 | 0.28 | 0.49 | 0.27 | open | - |
| 2026-11-03 08:20 | favourite | cs2 | FURIA | Natus Vincere | YES FURIA | 9 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-03 08:20 | model-only | cs2 | FURIA | Natus Vincere | YES FURIA | 33 | 0.54 | 0.63 | 0.54 | open | - |
| 2026-11-03 07:50 | favourite | cs2 | Spirit Academy | Saint Sinners | NO Saint Sinners | 6 | 0.80 | 0.79 | 0.79 | open | - |
| 2026-11-03 07:50 | favourite | cs2 | Leo Team | Noir Verse | YES Leo Team | 7 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-11-03 07:50 | favourite | cs2 | MOUZ NXT | megoshort | NO megoshort | 8 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-11-03 07:50 | model-only | cs2 | megoshort | MOUZ NXT | YES megoshort | 45 | 0.41 | 0.55 | 0.41 | open | - |
| 2026-11-03 07:50 | favourite | cs2 | QUAZAR | Just_Players | YES QUAZAR | 9 | 0.54 | 0.51 | 0.51 | open | - |
| 2026-11-03 05:50 | favourite | dota2 | Direborn | Yangon Galacticos | YES Direborn | 7 | 0.69 | 0.67 | 0.67 | won | $2.06 |
| 2026-11-03 05:50 | favourite | cs2 | Team Falcons | FaZe | YES Team Falcons | 7 | 0.73 | 0.73 | 0.73 | open | - |
| 2026-11-03 05:50 | model-only | cs2 | FaZe | Team Falcons | YES FaZe | 65 | 0.27 | 0.44 | 0.27 | open | - |
| 2026-11-03 03:20 | favourite | cs2 | MOUZ | BetBoom Team | NO BetBoom Team | 7 | 0.71 | 0.70 | 0.71 | won | $1.92 |
| 2026-11-03 03:20 | model-only | cs2 | TYLOO | 9z | NO 9z | 49 | 0.36 | 0.48 | 0.35 | won | $30.56 |
| 2026-11-03 03:20 | model-only | cs2 | BetBoom Team | MOUZ | YES BetBoom Team | 59 | 0.30 | 0.39 | 0.29 | lost | -$18.57 |
| 2026-11-03 03:20 | favourite | cs2 | 9z | TYLOO | YES 9z | 8 | 0.65 | 0.65 | 0.65 | lost | -$5.33 |
| 2026-11-03 03:20 | model-only | cs2 | B8 | Legacy | NO Legacy | 45 | 0.39 | 0.53 | 0.39 | open | - |
| 2026-11-03 03:20 | favourite | cs2 | Legacy | B8 | NO B8 | 8 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-11-03 00:50 | favourite | cs2 | Heroic | TheMongolz | YES Heroic | 10 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-11-03 00:50 | model-only | cs2 | Heroic | TheMongolz | YES Heroic | 35 | 0.51 | 0.61 | 0.51 | open | - |
| 2026-11-02 17:53 | model-only | cs2 | Huskies eSport | Playing Ducks | NO Playing Ducks | 91 | 0.19 | 0.27 | 0.17 | lost | -$18.28 |
| 2026-11-02 17:53 | model-only | cs2 | Al Ahli | Fortress | YES Al Ahli | 2 | 0.70 | 0.77 | 0.69 | won | $0.57 |
| 2026-11-02 17:53 | model-only | cs2 | Pandaric eSports | BLUEJAYS.de | NO BLUEJAYS.de | 10 | 0.15 | 0.37 | 0.15 | lost | -$1.59 |
| 2026-11-02 16:53 | favourite | cs2 | LPH Gaming | eSuba | NO eSuba | 8 | 0.65 | 0.64 | 0.64 | lost | -$5.33 |
| 2026-11-02 16:53 | model-only | cs2 | BOJONG | KUUSAMO.gg | YES BOJONG | 47 | 0.38 | 0.51 | 0.36 | won | $28.36 |

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

