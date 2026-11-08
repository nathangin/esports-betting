# Esports paper trading (fake money)

Updated 2026-11-08 13:53 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 616 | 55 | 561 | 200 | -$160.79 | -2.6% | -0.3c (609) | $839.21 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 990 | 86 | 904 | 596 | -$450.30 | -7.8% | -1.6c (980) | $549.70 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2038 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5845 | 0.2012 |
| model | 0.6512 | 0.2300 |
| blend | 0.5848 | 0.2015 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1312 | 0.5946 | 0.6592 |
| dota2 | 326 | 0.5567 | 0.6366 |
| ow | 119 | 0.5275 | 0.5338 |
| valorant | 97 | 0.6410 | 0.6788 |
| lol | 94 | 0.5645 | 0.7179 |
| r6 | 73 | 0.5876 | 0.6652 |
| cod | 17 | 0.5127 | 0.5460 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-08 13:53 | favourite | cs2 | SAW Youngsters | MASONIC | NO MASONIC | 3 | 0.54 | 0.54 | 0.53 | open | - |
| 2026-11-08 12:52 | favourite | cs2 | Balkan Outlaws | The Last Resort | YES Balkan Outlaws | 5 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-11-08 12:52 | model-only | cs2 | The Last Resort | Balkan Outlaws | NO Balkan Outlaws | 3 | 0.30 | 0.40 | 0.30 | open | - |
| 2026-11-08 12:52 | favourite | cs2 | PRIVATE | G2 Ares | YES PRIVATE | 6 | 0.84 | 0.83 | 0.83 | open | - |
| 2026-11-08 12:52 | model-only | cs2 | G2 Ares | PRIVATE | NO PRIVATE | 1 | 0.18 | 0.33 | 0.17 | open | - |
| 2026-11-08 12:52 | favourite | cs2 | 9INE | 6yuBoJlbl | YES 9INE | 8 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-08 12:52 | model-only | cs2 | 6yuBoJlbl | 9INE | NO 9INE | 10 | 0.36 | 0.53 | 0.35 | open | - |
| 2026-11-08 11:52 | model-only | dota2 | Xipto Esports | Nemiga Gaming | NO Nemiga Gaming | 26 | 0.66 | 0.71 | 0.65 | open | - |
| 2026-11-08 11:52 | model-only | cs2 | Zetta Games | MEIA NOITE | NO MEIA NOITE | 6 | 0.18 | 0.42 | 0.18 | open | - |
| 2026-11-08 11:52 | favourite | cs2 | MEIA NOITE | Zetta Games | YES MEIA NOITE | 6 | 0.83 | 0.82 | 0.82 | open | - |
| 2026-11-08 11:52 | favourite | dota2 | Xipto Esports | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-08 11:52 | favourite | dota2 | Froglings | potn9ki | YES Froglings | 5 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-11-08 11:52 | model-only | dota2 | Team Synapse | Power Rangers | YES Team Synapse | 27 | 0.63 | 0.82 | 0.63 | open | - |
| 2026-11-08 11:52 | favourite | dota2 | Team Synapse | Power Rangers | YES Team Synapse | 8 | 0.63 | 0.63 | 0.63 | open | - |
| 2026-11-08 10:52 | favourite | cs2 | Gothic | The Last Resort | YES Gothic | 9 | 0.54 | 0.51 | 0.51 | open | - |
| 2026-11-08 10:52 | favourite | cs2 | Prestige | KUUSAMO.gg | NO KUUSAMO.gg | 8 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-11-08 10:52 | model-only | cs2 | Prestige | KUUSAMO.gg | NO KUUSAMO.gg | 19 | 0.65 | 0.70 | 0.65 | open | - |
| 2026-11-08 10:52 | favourite | cs2 | Drama eSports | Noir Verse | YES Drama eSports | 9 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-11-08 08:52 | favourite | dota2 | Team Synapse | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.68 | 0.66 | 0.66 | won | $2.13 |
| 2026-11-08 08:52 | model-only | dota2 | angry birds | CyberHero | YES angry birds | 35 | 0.48 | 0.58 | 0.45 | lost | -$17.42 |
| 2026-11-08 08:52 | favourite | dota2 | CyberHero | angry birds | NO angry birds | 9 | 0.58 | 0.55 | 0.55 | won | $3.62 |
| 2026-11-08 08:52 | model-only | dota2 | Team Synapse | Nemiga Gaming | NO Nemiga Gaming | 17 | 0.68 | 0.82 | 0.66 | won | $5.18 |
| 2026-11-08 08:52 | favourite | dota2 | PlayTime | Power Rangers | YES PlayTime | 7 | 0.70 | 0.70 | 0.70 | open | - |
| 2026-11-08 08:52 | model-only | dota2 | Zero Tenacity | Inner Circle | NO Inner Circle | 37 | 0.46 | 0.53 | 0.43 | lost | -$17.67 |
| 2026-11-08 08:52 | favourite | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 8 | 0.60 | 0.57 | 0.57 | won | $3.06 |

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

