# Esports paper trading (fake money)

Updated 2026-11-07 12:35 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 590 | 55 | 535 | 189 | -$122.55 | -2.1% | -0.3c (579) | $877.45 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 953 | 84 | 869 | 572 | -$455.46 | -8.1% | -1.6c (939) | $544.54 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1950 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5847 | 0.2013 |
| model | 0.6512 | 0.2300 |
| blend | 0.5850 | 0.2015 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1276 | 0.5958 | 0.6600 |
| dota2 | 303 | 0.5477 | 0.6261 |
| ow | 115 | 0.5235 | 0.5364 |
| lol | 93 | 0.5681 | 0.7213 |
| valorant | 93 | 0.6419 | 0.6793 |
| r6 | 59 | 0.5903 | 0.6778 |
| cod | 11 | 0.5753 | 0.5483 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-07 11:54 | favourite | dota2 | Power Rangers | Zenith | YES Power Rangers | 6 | 0.84 | 0.84 | 0.84 | open | - |
| 2026-11-07 11:54 | favourite | dota2 | Team Synapse | potn9ki | NO potn9ki | 6 | 0.80 | 0.78 | 0.78 | open | - |
| 2026-11-07 11:54 | model-only | dota2 | potn9ki | Team Synapse | YES potn9ki | 10 | 0.24 | 0.34 | 0.22 | open | - |
| 2026-11-07 11:54 | favourite | dota2 | PlayTime | Xipto Esports | YES PlayTime | 5 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-07 11:54 | model-only | dota2 | Xipto Esports | PlayTime | NO PlayTime | 43 | 0.39 | 0.58 | 0.38 | open | - |
| 2026-11-07 11:54 | favourite | dota2 | Nemiga Gaming | PuckChamp | YES Nemiga Gaming | 6 | 0.84 | 0.83 | 0.83 | open | - |
| 2026-11-07 11:54 | model-only | dota2 | PuckChamp | Nemiga Gaming | YES PuckChamp | 70 | 0.18 | 0.34 | 0.17 | open | - |
| 2026-11-07 11:54 | favourite | dota2 | CyberHero | Ka4kanarskie cyxariki | YES CyberHero | 8 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-07 11:54 | model-only | dota2 | Ka4kanarskie cyxariki | CyberHero | NO CyberHero | 11 | 0.39 | 0.45 | 0.38 | open | - |
| 2026-11-07 10:54 | favourite | dota2 | Mena Warriors | oveA | YES Mena Warriors | 8 | 0.62 | 0.57 | 0.57 | open | - |
| 2026-11-07 10:54 | favourite | cs2 | Johnny Speeds | Drama eSports | YES Johnny Speeds | 6 | 0.71 | 0.70 | 0.70 | lost | -$4.35 |
| 2026-11-07 10:24 | model-only | cs2 | XI Esport | Teletubisie | NO Teletubisie | 69 | 0.25 | 0.43 | 0.24 | open | - |
| 2026-11-07 10:24 | model-only | cs2 | maybe | Lunacy Team | NO Lunacy Team | 1 | 0.33 | 0.53 | 0.32 | open | - |
| 2026-11-07 10:24 | favourite | cs2 | Lunacy Team | maybe | NO maybe | 3 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-11-07 10:24 | favourite | cs2 | Teletubisie | XI Esport | YES Teletubisie | 6 | 0.77 | 0.76 | 0.76 | open | - |
| 2026-11-07 08:54 | favourite | dota2 | Froglings | Zenith | NO Zenith | 1 | 0.88 | 0.87 | 0.87 | won | $0.11 |
| 2026-11-07 08:54 | favourite | dota2 | Yellow Submarine | HULIGANI | NO HULIGANI | 8 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-11-07 08:54 | favourite | dota2 | Inner Circle | Spirit Academy | YES Inner Circle | 7 | 0.75 | 0.73 | 0.73 | open | - |
| 2026-11-07 08:54 | model-only | dota2 | Spirit Academy | Inner Circle | NO Inner Circle | 13 | 0.30 | 0.44 | 0.27 | open | - |
| 2026-11-07 08:54 | favourite | dota2 | Power Rangers | Xipto Esports | YES Power Rangers | 9 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-11-07 08:54 | favourite | dota2 | Nemiga Gaming | potn9ki | YES Nemiga Gaming | 7 | 0.74 | 0.73 | 0.73 | won | $1.72 |
| 2026-11-07 08:39 | favourite | cs2 | MOUZ | BetBoom Team | NO BetBoom Team | 7 | 0.72 | 0.71 | 0.72 | won | $1.86 |
| 2026-11-07 08:39 | model-only | cs2 | BetBoom Team | MOUZ | YES BetBoom Team | 57 | 0.29 | 0.41 | 0.28 | lost | -$17.36 |
| 2026-11-07 07:54 | model-only | cs2 | maybe | Butterfly | NO Butterfly | 72 | 0.23 | 0.47 | 0.22 | lost | -$17.46 |
| 2026-11-07 07:54 | model-only | cs2 | 9INE Academy | gothboiclique | YES 9INE Academy | 12 | 0.27 | 0.42 | 0.27 | lost | -$3.41 |

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

