# Esports paper trading (fake money)

Updated 2026-11-08 09:22 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 609 | 54 | 555 | 198 | -$116.21 | -1.9% | -0.2c (598) | $883.79 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 979 | 83 | 896 | 590 | -$455.84 | -7.9% | -1.6c (966) | $544.16 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2025 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5848 | 0.2013 |
| model | 0.6516 | 0.2302 |
| blend | 0.5850 | 0.2016 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1306 | 0.5947 | 0.6598 |
| dota2 | 323 | 0.5580 | 0.6363 |
| ow | 118 | 0.5258 | 0.5321 |
| valorant | 96 | 0.6402 | 0.6786 |
| lol | 94 | 0.5645 | 0.7179 |
| r6 | 71 | 0.5919 | 0.6686 |
| cod | 17 | 0.5127 | 0.5460 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-08 08:52 | model-only | dota2 | Zenith | Xipto Esports | YES Zenith | 166 | 0.10 | 0.31 | 0.10 | open | - |
| 2026-11-08 08:52 | favourite | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 8 | 0.60 | 0.57 | 0.57 | open | - |
| 2026-11-08 08:52 | model-only | dota2 | Zero Tenacity | Inner Circle | NO Inner Circle | 37 | 0.46 | 0.53 | 0.43 | open | - |
| 2026-11-08 08:52 | favourite | dota2 | Team Synapse | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.68 | 0.66 | 0.66 | open | - |
| 2026-11-08 08:52 | model-only | dota2 | Team Synapse | Nemiga Gaming | NO Nemiga Gaming | 17 | 0.68 | 0.82 | 0.66 | open | - |
| 2026-11-08 08:52 | favourite | dota2 | PlayTime | Power Rangers | YES PlayTime | 7 | 0.70 | 0.70 | 0.70 | open | - |
| 2026-11-08 08:52 | favourite | dota2 | CyberHero | angry birds | NO angry birds | 9 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-11-08 08:52 | model-only | dota2 | angry birds | CyberHero | YES angry birds | 35 | 0.48 | 0.58 | 0.45 | open | - |
| 2026-11-08 07:51 | favourite | cs2 | ILLYRIANS | Bebop | NO Bebop | 8 | 0.64 | 0.63 | 0.63 | open | - |
| 2026-11-08 07:51 | favourite | cs2 | Esport Academy Copenhagen | BRUTE SQ | NO BRUTE SQ | 7 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-11-08 07:51 | favourite | cs2 | Inner Circle Academy | G2 Ares | NO G2 Ares | 8 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-11-08 07:51 | model-only | cs2 | Spirit Academy | BASEMENT BOYS | NO BASEMENT BOYS | 38 | 0.44 | 0.60 | 0.43 | open | - |
| 2026-11-08 07:51 | favourite | cs2 | BASEMENT BOYS | Spirit Academy | YES BASEMENT BOYS | 9 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-11-08 07:36 | favourite | r6 | Weibo Gaming | EDward Gaming | YES Weibo Gaming | 7 | 0.72 | 0.68 | 0.68 | won | $1.86 |
| 2026-11-08 06:21 | favourite | cs2 | MOUZ | TheMongolz | NO TheMongolz | 6 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-11-08 06:21 | model-only | cs2 | TheMongolz | MOUZ | NO MOUZ | 76 | 0.22 | 0.36 | 0.21 | open | - |
| 2026-11-08 04:51 | favourite | valorant | Oasis Gaming | Maxxing | NO Maxxing | 7 | 0.75 | 0.69 | 0.70 | open | - |
| 2026-11-08 02:51 | favourite | cs2 | Natus Vincere | BetBoom Team | YES Natus Vincere | 8 | 0.60 | 0.60 | 0.60 | won | $3.06 |
| 2026-11-08 02:51 | model-only | cs2 | BetBoom Team | Natus Vincere | YES BetBoom Team | 42 | 0.40 | 0.54 | 0.40 | lost | -$17.51 |
| 2026-11-08 02:21 | favourite | r6 | Virtus.pro | ENTERPRISE Esports | NO ENTERPRISE Esports | 6 | 0.81 | 0.76 | 0.76 | won | $1.07 |
| 2026-11-08 02:21 | favourite | r6 | Falcons Esport | Fluxo W7M | YES Falcons Esport | 7 | 0.67 | 0.65 | 0.65 | won | $2.20 |
| 2026-11-08 01:21 | model-only | r6 | Weibo Gaming | Geekay Esports | YES Weibo Gaming | 17 | 0.43 | 0.56 | 0.42 | lost | -$7.61 |
| 2026-11-08 01:21 | favourite | r6 | FaZe Clan | G2 Esports | YES FaZe Clan | 9 | 0.52 | 0.50 | 0.50 | won | $4.16 |
| 2026-11-08 01:21 | model-only | r6 | FaZe Clan | G2 Esports | YES FaZe Clan | 32 | 0.52 | 0.61 | 0.50 | won | $14.80 |
| 2026-11-08 01:21 | favourite | r6 | Geekay Esports | Weibo Gaming | YES Geekay Esports | 8 | 0.59 | 0.58 | 0.58 | won | $3.14 |

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

