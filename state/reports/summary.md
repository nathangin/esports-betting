# Esports paper trading (fake money)

Updated 2026-11-03 12:51 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 514 | 45 | 469 | 160 | -$91.99 | -1.8% | -0.3c (504) | $908.01 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 834 | 69 | 765 | 499 | -$444.61 | -8.6% | -1.5c (821) | $555.39 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1692 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5818 | 0.2001 |
| model | 0.6514 | 0.2302 |
| blend | 0.5819 | 0.2004 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1111 | 0.5934 | 0.6598 |
| dota2 | 261 | 0.5481 | 0.6278 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-03 12:51 | favourite | cs2 | Saint Sinners | Drama eSports | NO Drama eSports | 9 | 0.55 | 0.53 | 0.53 | open | - |
| 2026-11-03 12:51 | model-only | cs2 | Drama eSports | Saint Sinners | YES Drama eSports | 35 | 0.50 | 0.64 | 0.47 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | Rebels Gaming | maybe | NO maybe | 6 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | mellren | Lilmix | NO Lilmix | 8 | 0.61 | 0.58 | 0.58 | open | - |
| 2026-11-03 12:51 | model-only | cs2 | mellren | Lilmix | NO Lilmix | 26 | 0.61 | 0.75 | 0.58 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | BakS eSports | KUUSAMO.gg | YES BakS eSports | 6 | 0.90 | 0.90 | 0.90 | open | - |
| 2026-11-03 12:51 | model-only | cs2 | KUUSAMO.gg | BakS eSports | NO BakS eSports | 155 | 0.11 | 0.26 | 0.10 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | WRAITH PCIFIC | Falcons Force | YES WRAITH PCIFIC | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | Acend | Four Magic | NO Four Magic | 1 | 0.85 | 0.85 | 0.85 | open | - |
| 2026-11-03 11:51 | favourite | dota2 | CyberHero | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-11-03 11:51 | favourite | cs2 | Rush | MIBR fe | NO MIBR fe | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-03 11:51 | favourite | dota2 | Xipto Esports | PuckChamp | YES Xipto Esports | 6 | 0.88 | 0.87 | 0.87 | open | - |
| 2026-11-03 11:51 | model-only | dota2 | PuckChamp | Xipto Esports | YES PuckChamp | 98 | 0.14 | 0.20 | 0.13 | open | - |
| 2026-11-03 10:51 | favourite | cs2 | Spirit Academy | PsychoFace | YES Spirit Academy | 9 | 0.55 | 0.54 | 0.53 | open | - |
| 2026-11-03 10:51 | model-only | cs2 | Spirit Academy | PsychoFace | YES Spirit Academy | 32 | 0.55 | 0.77 | 0.53 | open | - |
| 2026-11-03 10:51 | favourite | cs2 | GenOne | Lilmix | NO Lilmix | 2 | 0.79 | 0.76 | 0.76 | open | - |
| 2026-11-03 10:20 | favourite | cs2 | XI Esport | 9INE Academy | NO 9INE Academy | 7 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-11-03 10:20 | model-only | cs2 | 9INE Academy | XI Esport | YES 9INE Academy | 14 | 0.28 | 0.36 | 0.28 | open | - |
| 2026-11-03 10:20 | favourite | cs2 | Falcons Force | maybe | YES Falcons Force | 8 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-11-03 10:20 | model-only | cs2 | maybe | Falcons Force | YES maybe | 1 | 0.34 | 0.43 | 0.34 | open | - |
| 2026-11-03 08:50 | model-only | dota2 | LEGION | OG | YES LEGION | 20 | 0.28 | 0.49 | 0.27 | open | - |
| 2026-11-03 08:50 | favourite | dota2 | OG | LEGION | YES OG | 7 | 0.73 | 0.73 | 0.73 | open | - |
| 2026-11-03 08:20 | favourite | cs2 | FURIA | Natus Vincere | YES FURIA | 9 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-03 08:20 | model-only | cs2 | FURIA | Natus Vincere | YES FURIA | 33 | 0.54 | 0.63 | 0.54 | open | - |
| 2026-11-03 07:50 | favourite | cs2 | Spirit Academy | Saint Sinners | NO Saint Sinners | 6 | 0.80 | 0.79 | 0.79 | open | - |

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

