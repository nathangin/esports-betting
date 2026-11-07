# Esports paper trading (fake money)

Updated 2026-11-07 21:05 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 599 | 50 | 549 | 195 | -$124.97 | -2.0% | -0.2c (592) | $875.03 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 961 | 73 | 888 | 584 | -$464.98 | -8.1% | -1.6c (952) | $535.02 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1990 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5848 | 0.2014 |
| model | 0.6514 | 0.2301 |
| blend | 0.5851 | 0.2017 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1296 | 0.5955 | 0.6598 |
| dota2 | 316 | 0.5540 | 0.6338 |
| ow | 118 | 0.5258 | 0.5321 |
| valorant | 94 | 0.6392 | 0.6783 |
| lol | 93 | 0.5681 | 0.7213 |
| r6 | 59 | 0.5903 | 0.6778 |
| cod | 14 | 0.5073 | 0.5108 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-07 17:50 | model-only | cs2 | Rcave | Spirit HU | NO Spirit HU | 2 | 0.46 | 0.53 | 0.44 | won | $1.04 |
| 2026-11-07 16:50 | model-only | cod | Riyadh Falcons | Toronto KOI | YES Riyadh Falcons | 15 | 0.45 | 0.54 | 0.45 | open | - |
| 2026-11-07 16:50 | model-only | cod | OpTic Texas | Cloud9 New York | NO Cloud9 New York | 22 | 0.80 | 0.86 | 0.79 | won | $4.15 |
| 2026-11-07 14:54 | model-only | dota2 | InterActive Philippines | PuckChamp | NO PuckChamp | 24 | 0.69 | 0.78 | 0.68 | lost | -$16.92 |
| 2026-11-07 14:54 | model-only | dota2 | angry birds | Xipto Esports | YES angry birds | 40 | 0.41 | 0.51 | 0.39 | open | - |
| 2026-11-07 14:54 | model-only | dota2 | Amaru Gaming | Yakult's Brothers | NO Yakult's Brothers | 14 | 0.26 | 0.46 | 0.24 | open | - |
| 2026-11-07 13:54 | favourite | cs2 | SAW Youngsters | Sokerorg | YES SAW Youngsters | 1 | 0.52 | 0.50 | 0.50 | lost | -$0.54 |
| 2026-11-07 13:54 | favourite | cs2 | ex-Zero Tenacity | Leo Team | YES ex-Zero Tenacity | 1 | 0.66 | 0.65 | 0.65 | won | $0.32 |
| 2026-11-07 13:54 | model-only | cs2 | Leo Team | ex-Zero Tenacity | YES Leo Team | 28 | 0.35 | 0.40 | 0.35 | lost | -$10.25 |
| 2026-11-07 12:54 | favourite | cs2 | OG | G2 Ares | NO G2 Ares | 7 | 0.76 | 0.75 | 0.75 | won | $1.59 |
| 2026-11-07 12:54 | favourite | cs2 | 9INE | 6yuBoJlbl | YES 9INE | 7 | 0.72 | 0.71 | 0.71 | won | $1.86 |
| 2026-11-07 12:54 | favourite | cs2 | aimclub | LPH Gaming | NO LPH Gaming | 8 | 0.62 | 0.60 | 0.60 | won | $2.90 |
| 2026-11-07 12:54 | model-only | cs2 | G2 Ares | OG | YES G2 Ares | 66 | 0.25 | 0.43 | 0.25 | lost | -$17.37 |
| 2026-11-07 12:54 | favourite | cs2 | Balkan Outlaws | The Last Resort | YES Balkan Outlaws | 9 | 0.55 | 0.54 | 0.54 | won | $3.89 |
| 2026-11-07 12:54 | favourite | cs2 | Alliance | maybe | YES Alliance | 6 | 0.89 | 0.88 | 0.88 | won | $0.61 |
| 2026-11-07 12:54 | model-only | cs2 | Ryvex | Acend | NO Acend | 4 | 0.10 | 0.33 | 0.10 | lost | -$0.43 |
| 2026-11-07 12:54 | favourite | cs2 | Acend | Ryvex | NO Ryvex | 6 | 0.90 | 0.90 | 0.90 | won | $0.56 |
| 2026-11-07 11:54 | favourite | dota2 | Nemiga Gaming | PuckChamp | YES Nemiga Gaming | 6 | 0.84 | 0.83 | 0.83 | lost | -$5.10 |
| 2026-11-07 11:54 | model-only | dota2 | Ka4kanarskie cyxariki | CyberHero | NO CyberHero | 11 | 0.39 | 0.45 | 0.38 | won | $6.52 |
| 2026-11-07 11:54 | favourite | dota2 | CyberHero | Ka4kanarskie cyxariki | YES CyberHero | 8 | 0.63 | 0.62 | 0.62 | lost | -$5.18 |
| 2026-11-07 11:54 | model-only | dota2 | PuckChamp | Nemiga Gaming | YES PuckChamp | 70 | 0.18 | 0.34 | 0.17 | won | $56.67 |
| 2026-11-07 11:54 | model-only | dota2 | Xipto Esports | PlayTime | NO PlayTime | 43 | 0.39 | 0.58 | 0.38 | lost | -$17.49 |
| 2026-11-07 11:54 | model-only | dota2 | potn9ki | Team Synapse | YES potn9ki | 10 | 0.24 | 0.34 | 0.22 | lost | -$2.53 |
| 2026-11-07 11:54 | favourite | dota2 | Team Synapse | potn9ki | NO potn9ki | 6 | 0.80 | 0.78 | 0.78 | won | $1.13 |
| 2026-11-07 11:54 | favourite | dota2 | Power Rangers | Zenith | YES Power Rangers | 6 | 0.84 | 0.84 | 0.84 | won | $0.90 |

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

