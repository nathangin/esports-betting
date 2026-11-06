# Esports paper trading (fake money)

Updated 2026-11-06 10:06 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 569 | 52 | 517 | 184 | -$64.29 | -1.1% | -0.3c (562) | $935.71 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 917 | 80 | 837 | 548 | -$462.17 | -8.4% | -1.6c (909) | $537.83 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1872 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5842 | 0.2012 |
| model | 0.6515 | 0.2302 |
| blend | 0.5844 | 0.2014 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1244 | 0.5963 | 0.6599 |
| dota2 | 294 | 0.5518 | 0.6303 |
| ow | 111 | 0.5147 | 0.5254 |
| lol | 92 | 0.5722 | 0.7188 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 49 | 0.6060 | 0.6898 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-06 08:51 | favourite | valorant | An Angel Anbandonned | LPD | YES An Angel Anbandonned | 9 | 0.55 | 0.51 | 0.51 | open | - |
| 2026-11-06 08:51 | favourite | dota2 | potn9ki | Zenith | YES potn9ki | 7 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-11-06 08:51 | model-only | dota2 | Zenith | potn9ki | NO potn9ki | 54 | 0.33 | 0.40 | 0.31 | open | - |
| 2026-11-06 08:51 | favourite | dota2 | PlayTime | Team Synapse | YES PlayTime | 9 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-11-06 08:51 | model-only | dota2 | Team Synapse | PlayTime | NO PlayTime | 38 | 0.47 | 0.70 | 0.45 | open | - |
| 2026-11-06 08:51 | favourite | dota2 | Froglings | Xipto Esports | YES Froglings | 7 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-06 08:51 | model-only | dota2 | Xipto Esports | Froglings | YES Xipto Esports | 5 | 0.36 | 0.57 | 0.35 | open | - |
| 2026-11-06 08:51 | favourite | dota2 | angry birds | Nemiga Gaming | YES angry birds | 8 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-11-06 08:51 | model-only | dota2 | angry birds | Nemiga Gaming | YES angry birds | 29 | 0.61 | 0.70 | 0.59 | open | - |
| 2026-11-06 08:36 | favourite | cs2 | FURIA | BetBoom Team | NO BetBoom Team | 7 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-11-06 08:36 | model-only | cs2 | BetBoom Team | FURIA | NO FURIA | 51 | 0.35 | 0.43 | 0.34 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | BakS eSports | Fire Flux Esports | YES BakS eSports | 8 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | SAW Youngsters | Four Magic | NO Four Magic | 7 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-11-06 07:51 | model-only | cs2 | Bad Beavers | The Chosen Few | NO The Chosen Few | 21 | 0.42 | 0.55 | 0.42 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | The Chosen Few | Bad Beavers | NO Bad Beavers | 9 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-11-06 07:51 | model-only | cs2 | Fire Flux Esports | BakS eSports | NO BakS eSports | 43 | 0.41 | 0.47 | 0.41 | open | - |
| 2026-11-06 07:51 | model-only | cs2 | Four Magic | SAW Youngsters | YES Four Magic | 55 | 0.32 | 0.56 | 0.32 | open | - |
| 2026-11-06 07:51 | model-only | cs2 | NAVI Junior | FORZE Reload | NO FORZE Reload | 63 | 0.28 | 0.41 | 0.28 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | QUAZAR | Revise | YES QUAZAR | 6 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-11-06 07:51 | model-only | cs2 | The Last Resort | G2 Ares | NO G2 Ares | 42 | 0.41 | 0.47 | 0.41 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | G2 Ares | The Last Resort | NO The Last Resort | 8 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-11-06 07:51 | favourite | cs2 | FORZE Reload | NAVI Junior | YES FORZE Reload | 7 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-11-06 06:50 | favourite | valorant | Hoc Vien 96 | God Chosen | YES Hoc Vien 96 | 6 | 0.63 | 0.59 | 0.59 | open | - |
| 2026-11-06 06:20 | favourite | r6 | Weibo Gaming | Virtus.pro | YES Weibo Gaming | 10 | 0.52 | 0.51 | 0.51 | open | - |
| 2026-11-06 05:50 | favourite | dota2 | Royal Bear | Direborn | NO Direborn | 7 | 0.75 | 0.74 | 0.74 | open | - |

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

