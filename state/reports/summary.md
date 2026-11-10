# Esports paper trading (fake money)

Updated 2026-11-10 09:08 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 642 | 54 | 588 | 208 | -$171.19 | -2.6% | -0.2c (631) | $828.81 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1036 | 84 | 952 | 627 | -$455.03 | -7.6% | -1.6c (1021) | $544.97 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2152 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5864 | 0.2020 |
| model | 0.6516 | 0.2302 |
| blend | 0.5868 | 0.2023 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1368 | 0.5944 | 0.6586 |
| dota2 | 361 | 0.5624 | 0.6405 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 103 | 0.6402 | 0.6754 |
| lol | 96 | 0.5872 | 0.7110 |
| r6 | 83 | 0.5710 | 0.6597 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-10 08:53 | favourite | dota2 | Team Synapse | Zenith | YES Team Synapse | 6 | 0.87 | 0.87 | 0.87 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | Zenith | Team Synapse | NO Team Synapse | 111 | 0.14 | 0.23 | 0.13 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | Xipto Esports | potn9ki | YES Xipto Esports | 6 | 0.86 | 0.86 | 0.86 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | potn9ki | Xipto Esports | YES potn9ki | 76 | 0.14 | 0.28 | 0.14 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | PlayTime | Nemiga Gaming | YES PlayTime | 7 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | Nemiga Gaming | PlayTime | YES Nemiga Gaming | 32 | 0.26 | 0.31 | 0.25 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | LEGION | Yellow Submarine | YES LEGION | 9 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | Yellow Submarine | LEGION | NO LEGION | 33 | 0.48 | 0.61 | 0.47 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | Team Allied | Time to Sleep | YES Team Allied | 7 | 0.76 | 0.75 | 0.75 | open | - |
| 2026-11-10 07:53 | favourite | cs2 | Brute | ILLYRIANS | YES Brute | 7 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-11-10 07:53 | favourite | cs2 | Copenhagen Wolves | Bad Beavers | NO Bad Beavers | 6 | 0.81 | 0.81 | 0.80 | open | - |
| 2026-11-10 07:53 | model-only | cs2 | ILLYRIANS | Brute | YES ILLYRIANS | 49 | 0.32 | 0.42 | 0.31 | open | - |
| 2026-11-10 07:53 | model-only | cs2 | Sokerorg | NAVI Junior | NO NAVI Junior | 51 | 0.31 | 0.45 | 0.30 | open | - |
| 2026-11-10 07:53 | favourite | cs2 | NAVI Junior | Sokerorg | YES NAVI Junior | 7 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-11-10 05:23 | favourite | r6 | G2 Esports | Geekay Esports | YES G2 Esports | 6 | 0.90 | 0.86 | 0.86 | won | $0.56 |
| 2026-11-10 02:22 | favourite | r6 | M80 | Virtus.pro | YES M80 | 7 | 0.68 | 0.64 | 0.64 | lost | -$4.87 |
| 2026-11-10 02:22 | favourite | r6 | DarkZero Esports | Sharper Esport | YES DarkZero Esports | 6 | 0.82 | 0.79 | 0.79 | won | $1.01 |
| 2026-11-09 23:22 | favourite | r6 | Cloud9 | Weibo Gaming | YES Cloud9 | 1 | 0.62 | 0.61 | 0.61 | lost | -$0.64 |
| 2026-11-09 17:51 | favourite | cs2 | Huskies eSport | Pandaric eSports | YES Huskies eSport | 1 | 0.55 | 0.55 | 0.55 | won | $0.43 |
| 2026-11-09 17:51 | favourite | cs2 | MASONIC | EAC Extra | NO EAC Extra | 3 | 0.54 | 0.55 | 0.55 | lost | -$1.68 |
| 2026-11-09 16:51 | favourite | cs2 | Team ACES | ex-Zero Tenacity | YES Team ACES | 1 | 0.70 | 0.68 | 0.68 | lost | -$0.72 |
| 2026-11-09 15:51 | model-only | cs2 | TEAM GELO | MTX | NO MTX | 13 | 0.50 | 0.56 | 0.49 | lost | -$6.73 |
| 2026-11-09 15:51 | model-only | cs2 | MASQ | STATE | YES MASQ | 168 | 0.10 | 0.26 | 0.09 | lost | -$17.86 |
| 2026-11-09 15:51 | favourite | cs2 | Team LEISURE | Huskies eSport | NO Huskies eSport | 2 | 0.70 | 0.69 | 0.70 | won | $0.57 |
| 2026-11-09 15:51 | model-only | cs2 | Hermine Esports Club | ZOTIX | NO ZOTIX | 9 | 0.45 | 0.54 | 0.45 | lost | -$4.21 |

## Backtest on real Kalshi prices

9586 settled matches from 2026-05-28 to 2026-11-09, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2015 | $9,315.01 | -$992.01 | -10.6% | -18.8% to -2.6% | 32% | -0.6c | 99% |
| always the favourite (1% flat) | 4643 | $17,908.06 | -$833.06 | -4.7% | -6.9% to -2.4% | 67% | -1.8c | 84% |
| always the underdog (1% flat) | 3790 | $8,967.07 | -$986.07 | -11.0% | -16.9% to -5.1% | 31% | -1.2c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 9361 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5754 | 0.1970 | 68.9% |
| model | 0.6596 | 0.2339 | 59.6% |
| blend | 0.5751 | 0.1970 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1567 | 0.525 | 0.523 |
| (0.55, 0.6] | 1580 | 0.577 | 0.551 |
| (0.6, 0.65] | 1426 | 0.626 | 0.626 |
| (0.65, 0.7] | 1257 | 0.676 | 0.699 |
| (0.7, 0.75] | 1053 | 0.726 | 0.769 |
| (0.75, 0.8] | 889 | 0.776 | 0.805 |
| (0.8, 0.85] | 761 | 0.826 | 0.825 |
| (0.85, 0.9] | 562 | 0.877 | 0.902 |
| (0.9, 1.0] | 491 | 0.932 | 0.959 |

