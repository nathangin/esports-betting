# Esports paper trading (fake money)

Updated 2026-11-03 02:00 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 500 | 35 | 465 | 159 | -$67.06 | -1.3% | -0.3c (493) | $932.94 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 810 | 51 | 759 | 495 | -$443.75 | -8.6% | -1.5c (803) | $556.25 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1683 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5820 | 0.2002 |
| model | 0.6516 | 0.2303 |
| blend | 0.5822 | 0.2005 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1104 | 0.5932 | 0.6597 |
| dota2 | 259 | 0.5505 | 0.6296 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-03 00:50 | favourite | cs2 | Heroic | TheMongolz | YES Heroic | 10 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-11-03 00:50 | model-only | cs2 | Heroic | TheMongolz | YES Heroic | 35 | 0.51 | 0.61 | 0.51 | open | - |
| 2026-11-02 17:53 | model-only | cs2 | Huskies eSport | Playing Ducks | NO Playing Ducks | 91 | 0.19 | 0.27 | 0.17 | lost | -$18.28 |
| 2026-11-02 17:53 | model-only | cs2 | Al Ahli | Fortress | YES Al Ahli | 2 | 0.70 | 0.77 | 0.69 | won | $0.57 |
| 2026-11-02 17:53 | model-only | cs2 | Pandaric eSports | BLUEJAYS.de | NO BLUEJAYS.de | 10 | 0.15 | 0.37 | 0.15 | lost | -$1.59 |
| 2026-11-02 16:53 | favourite | cs2 | STATE | ECSTATIC | NO ECSTATIC | 4 | 0.77 | 0.76 | 0.76 | won | $0.87 |
| 2026-11-02 16:53 | favourite | cs2 | ILLYRIANS | Sokerorg | YES ILLYRIANS | 9 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-11-02 16:53 | favourite | cs2 | ex-ENCE | SINQU | YES ex-ENCE | 6 | 0.89 | 0.88 | 0.88 | won | $0.61 |
| 2026-11-02 16:53 | favourite | cs2 | LPH Gaming | eSuba | NO eSuba | 8 | 0.65 | 0.64 | 0.64 | lost | -$5.33 |
| 2026-11-02 16:53 | model-only | cs2 | eSuba | LPH Gaming | NO LPH Gaming | 11 | 0.36 | 0.48 | 0.36 | won | $6.86 |
| 2026-11-02 16:53 | favourite | cs2 | KUUSAMO.gg | BOJONG | NO BOJONG | 8 | 0.66 | 0.64 | 0.64 | lost | -$5.41 |
| 2026-11-02 16:53 | model-only | cs2 | BOJONG | KUUSAMO.gg | YES BOJONG | 47 | 0.38 | 0.51 | 0.36 | won | $28.36 |
| 2026-11-02 15:53 | favourite | cs2 | PARTIZAN | Regnum4Games | YES PARTIZAN | 10 | 0.53 | 0.52 | 0.52 | lost | -$5.48 |
| 2026-11-02 15:53 | model-only | cs2 | XI Esport | ECSTATIC | NO ECSTATIC | 14 | 0.58 | 0.66 | 0.55 | lost | -$8.36 |
| 2026-11-02 15:53 | favourite | cs2 | MASONIC | MASQ | NO MASQ | 7 | 0.76 | 0.73 | 0.73 | open | - |
| 2026-11-02 15:53 | model-only | cs2 | Regnum4Games | PARTIZAN | NO PARTIZAN | 36 | 0.50 | 0.63 | 0.48 | won | $17.37 |
| 2026-11-02 15:53 | favourite | cs2 | XI Esport | ECSTATIC | NO ECSTATIC | 9 | 0.58 | 0.55 | 0.55 | lost | -$5.38 |
| 2026-11-02 15:53 | model-only | cs2 | EAC Extra | STATE | YES EAC Extra | 14 | 0.24 | 0.41 | 0.23 | won | $10.46 |
| 2026-11-02 15:53 | model-only | cs2 | Vitality Academy | Young TigeRES | YES Vitality Academy | 73 | 0.24 | 0.34 | 0.22 | lost | -$18.46 |
| 2026-11-02 15:53 | favourite | cs2 | STATE | EAC Extra | NO EAC Extra | 7 | 0.79 | 0.78 | 0.78 | lost | -$5.62 |
| 2026-11-02 15:53 | favourite | cs2 | Young TigeRES | Vitality Academy | YES Young TigeRES | 3 | 0.78 | 0.78 | 0.78 | won | $0.62 |
| 2026-11-02 14:23 | favourite | cs2 | HAVU | Nordic Valor | YES HAVU | 6 | 0.87 | 0.86 | 0.86 | won | $0.73 |
| 2026-11-02 13:53 | model-only | cs2 | Misa Esports | PsychoFace | YES Misa Esports | 38 | 0.47 | 0.69 | 0.46 | lost | -$18.53 |
| 2026-11-02 13:53 | favourite | cs2 | Saint Sinners | Lilmix | NO Lilmix | 7 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-11-02 13:53 | model-only | cs2 | Lilmix | Saint Sinners | YES Lilmix | 57 | 0.30 | 0.37 | 0.28 | open | - |

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

