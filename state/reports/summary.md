# Esports paper trading (fake money)

Updated 2026-11-02 15:38 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 490 | 35 | 455 | 154 | -$65.46 | -1.3% | -0.3c (484) | $934.54 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 799 | 52 | 747 | 490 | -$412.12 | -8.1% | -1.5c (792) | $587.88 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1656 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5822 | 0.2003 |
| model | 0.6516 | 0.2303 |
| blend | 0.5823 | 0.2005 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1083 | 0.5934 | 0.6599 |
| dota2 | 253 | 0.5509 | 0.6288 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-02 14:23 | favourite | cs2 | HAVU | Nordic Valor | YES HAVU | 6 | 0.87 | 0.86 | 0.86 | open | - |
| 2026-11-02 13:53 | favourite | cs2 | Saint Sinners | Lilmix | NO Lilmix | 7 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-11-02 13:53 | model-only | cs2 | Lilmix | Saint Sinners | YES Lilmix | 57 | 0.30 | 0.37 | 0.28 | open | - |
| 2026-11-02 13:53 | favourite | cs2 | Spirit Academy | Noir Verse | NO Noir Verse | 7 | 0.83 | 0.80 | 0.80 | open | - |
| 2026-11-02 13:53 | favourite | cs2 | PsychoFace | Misa Esports | NO Misa Esports | 10 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-02 13:53 | model-only | cs2 | Misa Esports | PsychoFace | YES Misa Esports | 38 | 0.47 | 0.69 | 0.46 | open | - |
| 2026-11-02 11:52 | favourite | dota2 | OG | Yellow Submarine | YES OG | 8 | 0.73 | 0.73 | 0.73 | lost | -$5.96 |
| 2026-11-02 10:52 | favourite | cs2 | Falcons Force | megoshort | YES Falcons Force | 8 | 0.66 | 0.65 | 0.65 | lost | -$5.41 |
| 2026-11-02 10:52 | favourite | cs2 | Leo Team | Saint Sinners | NO Saint Sinners | 9 | 0.62 | 0.63 | 0.63 | won | $3.27 |
| 2026-11-02 10:52 | favourite | dota2 | HellNight- | potn9ki | YES HellNight- | 10 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-11-02 08:52 | favourite | dota2 | LEGION | HULIGANI | YES LEGION | 9 | 0.60 | 0.60 | 0.60 | lost | -$5.56 |
| 2026-11-02 08:22 | favourite | cs2 | MOUZ | TYLOO | NO TYLOO | 1 | 0.89 | 0.90 | 0.90 | won | $0.10 |
| 2026-11-02 08:22 | model-only | cs2 | TYLOO | MOUZ | NO MOUZ | 19 | 0.10 | 0.23 | 0.10 | lost | -$2.02 |
| 2026-11-02 08:22 | favourite | cs2 | Team Falcons | Natus Vincere | YES Team Falcons | 10 | 0.56 | 0.56 | 0.56 | lost | -$5.78 |
| 2026-11-02 07:52 | favourite | cs2 | maybe | Honvéd | NO Honvéd | 9 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-11-02 05:51 | favourite | cs2 | FURIA | FaZe | NO FaZe | 8 | 0.72 | 0.71 | 0.72 | won | $2.12 |
| 2026-11-02 05:51 | model-only | cs2 | FaZe | FURIA | YES FaZe | 62 | 0.29 | 0.37 | 0.28 | lost | -$18.88 |
| 2026-11-02 05:51 | favourite | cs2 | BetBoom Team | 9z | YES BetBoom Team | 9 | 0.65 | 0.65 | 0.65 | won | $3.00 |
| 2026-11-02 03:21 | favourite | cs2 | Aurora Gaming | Liquid | YES Aurora Gaming | 8 | 0.69 | 0.69 | 0.69 | lost | -$5.64 |
| 2026-11-02 03:21 | favourite | cs2 | G2 | PARIVISION | YES G2 | 10 | 0.55 | 0.55 | 0.55 | lost | -$5.68 |
| 2026-11-02 00:51 | favourite | cs2 | Legacy | TheMongolz | YES Legacy | 11 | 0.51 | 0.51 | 0.51 | lost | -$5.81 |
| 2026-11-02 00:51 | favourite | cs2 | Heroic | B8 | NO B8 | 9 | 0.62 | 0.61 | 0.61 | won | $3.27 |
| 2026-11-01 18:50 | favourite | cs2 | DENDELE CS | Imperial | NO Imperial | 5 | 0.58 | 0.58 | 0.58 | won | $2.01 |
| 2026-11-01 17:50 | favourite | cs2 | Metizport | WBT Academy | YES Metizport | 9 | 0.67 | 0.66 | 0.66 | lost | -$6.17 |
| 2026-11-01 17:50 | model-only | cs2 | WBT Academy | Metizport | NO Metizport | 2 | 0.35 | 0.41 | 0.34 | won | $1.26 |

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

