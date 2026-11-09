# Esports paper trading (fake money)

Updated 2026-11-09 02:14 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 618 | 50 | 568 | 202 | -$169.55 | -2.7% | -0.3c (610) | $830.45 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 994 | 77 | 917 | 606 | -$444.45 | -7.6% | -1.6c (983) | $555.55 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2087 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5849 | 0.2014 |
| model | 0.6512 | 0.2300 |
| blend | 0.5852 | 0.2016 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1333 | 0.5936 | 0.6579 |
| dota2 | 343 | 0.5589 | 0.6387 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 102 | 0.6397 | 0.6752 |
| lol | 95 | 0.5646 | 0.7154 |
| r6 | 73 | 0.5876 | 0.6652 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-09 01:24 | favourite | r6 | FaZe Clan | Falcons Esport | YES FaZe Clan | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-09 01:24 | favourite | r6 | 100 Thieves | ENTERPRISE Esports | NO ENTERPRISE Esports | 7 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-11-09 01:24 | model-only | r6 | ENTERPRISE Esports | 100 Thieves | YES ENTERPRISE Esports | 52 | 0.30 | 0.52 | 0.30 | open | - |
| 2026-11-09 00:24 | favourite | r6 | M80 | Sharper Esport | YES M80 | 9 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-11-09 00:24 | model-only | r6 | Sharper Esport | M80 | NO M80 | 12 | 0.47 | 0.55 | 0.44 | open | - |
| 2026-11-08 14:53 | favourite | cs2 | RED Canids Academy | BESTIA Academy | YES RED Canids Academy | 3 | 0.66 | 0.67 | 0.67 | won | $0.97 |
| 2026-11-08 13:53 | favourite | cs2 | SAW Youngsters | MASONIC | NO MASONIC | 3 | 0.54 | 0.54 | 0.53 | lost | -$1.68 |
| 2026-11-08 12:52 | favourite | cs2 | PRIVATE | G2 Ares | YES PRIVATE | 6 | 0.84 | 0.83 | 0.83 | won | $0.90 |
| 2026-11-08 12:52 | model-only | cs2 | 6yuBoJlbl | 9INE | NO 9INE | 10 | 0.36 | 0.53 | 0.35 | lost | -$3.77 |
| 2026-11-08 12:52 | favourite | cs2 | 9INE | 6yuBoJlbl | YES 9INE | 8 | 0.66 | 0.65 | 0.65 | won | $2.59 |
| 2026-11-08 12:52 | model-only | cs2 | G2 Ares | PRIVATE | NO PRIVATE | 1 | 0.18 | 0.33 | 0.17 | lost | -$0.20 |
| 2026-11-08 12:52 | model-only | cs2 | The Last Resort | Balkan Outlaws | NO Balkan Outlaws | 3 | 0.30 | 0.40 | 0.30 | lost | -$0.95 |
| 2026-11-08 12:52 | favourite | cs2 | Balkan Outlaws | The Last Resort | YES Balkan Outlaws | 5 | 0.71 | 0.70 | 0.70 | won | $1.37 |
| 2026-11-08 11:52 | favourite | dota2 | Team Synapse | Power Rangers | YES Team Synapse | 8 | 0.63 | 0.63 | 0.63 | lost | -$5.18 |
| 2026-11-08 11:52 | model-only | dota2 | Team Synapse | Power Rangers | YES Team Synapse | 27 | 0.63 | 0.82 | 0.63 | lost | -$17.46 |
| 2026-11-08 11:52 | favourite | dota2 | Froglings | potn9ki | YES Froglings | 5 | 0.89 | 0.88 | 0.88 | won | $0.51 |
| 2026-11-08 11:52 | favourite | dota2 | Xipto Esports | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.66 | 0.65 | 0.65 | won | $2.27 |
| 2026-11-08 11:52 | model-only | dota2 | Xipto Esports | Nemiga Gaming | NO Nemiga Gaming | 26 | 0.66 | 0.71 | 0.65 | won | $8.43 |
| 2026-11-08 11:52 | favourite | cs2 | MEIA NOITE | Zetta Games | YES MEIA NOITE | 6 | 0.83 | 0.82 | 0.82 | won | $0.96 |
| 2026-11-08 11:52 | model-only | cs2 | Zetta Games | MEIA NOITE | NO MEIA NOITE | 6 | 0.18 | 0.42 | 0.18 | lost | -$1.15 |
| 2026-11-08 10:52 | favourite | cs2 | Prestige | KUUSAMO.gg | NO KUUSAMO.gg | 8 | 0.65 | 0.65 | 0.65 | won | $2.67 |
| 2026-11-08 10:52 | favourite | cs2 | Drama eSports | Noir Verse | YES Drama eSports | 9 | 0.55 | 0.54 | 0.54 | won | $3.89 |
| 2026-11-08 10:52 | model-only | cs2 | Prestige | KUUSAMO.gg | NO KUUSAMO.gg | 19 | 0.65 | 0.70 | 0.65 | won | $6.34 |
| 2026-11-08 10:52 | favourite | cs2 | Gothic | The Last Resort | YES Gothic | 9 | 0.54 | 0.51 | 0.51 | open | - |
| 2026-11-08 08:52 | model-only | dota2 | Zenith | Xipto Esports | YES Zenith | 166 | 0.10 | 0.31 | 0.10 | lost | -$17.65 |

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

