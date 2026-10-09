# Esports paper trading (fake money)

Updated 2026-10-09 02:34 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 69 | 5 | 64 | 15 | -$90.29 | -10.3% | -0.8c (68) | $909.71 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 125 | 9 | 116 | 79 | -$91.17 | -10.0% | -0.6c (122) | $908.83 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

## Forecast scoring on the matches the trader looked at

403 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.6199 | 0.2165 |
| model | 0.6738 | 0.2407 |
| blend | 0.6199 | 0.2165 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 170 | 0.5977 | 0.6688 |
| esoccergame | 136 | 0.6883 | 0.6775 |
| ebasketballgame | 28 | 0.6641 | 0.7283 |
| lol | 26 | 0.3970 | 0.6526 |
| dota2 | 21 | 0.6117 | 0.6346 |
| r6 | 12 | 0.7332 | 0.7358 |
| valorant | 6 | 0.5347 | 0.7195 |
| ow | 4 | 0.2097 | 0.4720 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-09 02:18 | favourite | ebasketballgame | New Orleans Pelicans (Zion) | Indiana Pacers (Larry) | NO Indiana Pacers (Larry) | 13 | 0.68 | 0.65 | 0.65 | open | - |
| 2026-10-09 01:53 | favourite | ebasketballgame | Brooklyn Nets (Zion) | Golden State Warriors (Tim) | NO Golden State Warriors (Tim) | 16 | 0.54 | 0.51 | 0.51 | open | - |
| 2026-10-09 01:17 | favourite | esoccergame | FC Augsburg (Aron) | Dortmund (Declan) | YES FC Augsburg (Aron) | 20 | 0.44 | 0.50 | 0.50 | open | - |
| 2026-10-09 01:07 | favourite | esoccergame | FC Augsburg (Aron) | 1. FC Köln (Frost) | YES FC Augsburg (Aron) | 12 | 0.73 | 0.77 | 0.77 | lost | -$8.93 |
| 2026-10-09 00:52 | favourite | esoccergame | FSV Mainz 05 (Pedri) | Dortmund (Declan) | YES FSV Mainz 05 (Pedri) | 19 | 0.46 | 0.51 | 0.51 | lost | -$9.08 |
| 2026-10-09 00:52 | favourite | esoccergame | Leverkusen (Frenkie) | 1. FC Köln (Frost) | YES Leverkusen (Frenkie) | 11 | 0.81 | 0.82 | 0.82 | won | $1.97 |
| 2026-10-09 00:37 | favourite | esoccergame | São Paulo (Declan) | Estudiantes (Frost) | YES São Paulo (Declan) | 13 | 0.69 | 0.72 | 0.72 | won | $3.83 |
| 2026-10-08 14:38 | favourite | cs2 | EAC Extra | Linx Legacy Esport | YES EAC Extra | 5 | 0.73 | 0.61 | 0.61 | won | $1.28 |
| 2026-10-08 12:50 | model-only | cs2 | Nexus | CYBERSHOKE Esports | YES Nexus | 52 | 0.31 | 0.52 | 0.31 | open | - |
| 2026-10-08 12:50 | model-only | cs2 | Azuolas | Misa Esports | NO Misa Esports | 4 | 0.22 | 0.31 | 0.20 | lost | -$0.93 |
| 2026-10-08 11:50 | favourite | cs2 | mellren | Esport BERG | NO Esport BERG | 12 | 0.75 | 0.74 | 0.74 | won | $2.84 |
| 2026-10-08 11:50 | model-only | cs2 | bLight blue | Boring Players | NO Boring Players | 1 | 0.42 | 0.49 | 0.41 | lost | -$0.44 |
| 2026-10-08 11:50 | favourite | cs2 | Boring Players | bLight blue | NO bLight blue | 15 | 0.60 | 0.58 | 0.58 | won | $5.74 |
| 2026-10-08 11:50 | model-only | cs2 | Chinggis Warriors | Lynn Vision | YES Chinggis Warriors | 64 | 0.29 | 0.50 | 0.27 | lost | -$19.49 |
| 2026-10-08 11:50 | favourite | cs2 | HyperSpirit | los kogutos | YES HyperSpirit | 1 | 0.65 | 0.59 | 0.59 | won | $0.33 |
| 2026-10-08 11:50 | favourite | cs2 | Rare Atom | Just Swing | NO Just Swing | 10 | 0.85 | 0.83 | 0.83 | lost | -$8.59 |
| 2026-10-08 11:50 | favourite | cs2 | Alter Ego | Kaleido | YES Alter Ego | 13 | 0.67 | 0.65 | 0.65 | lost | -$8.92 |
| 2026-10-08 11:50 | favourite | cs2 | Lynn Vision | Chinggis Warriors | YES Lynn Vision | 12 | 0.74 | 0.73 | 0.73 | won | $2.95 |
| 2026-10-08 11:50 | favourite | cs2 | Not A Squad Esports | Legion | YES Not A Squad Esports | 2 | 0.79 | 0.78 | 0.78 | won | $0.39 |
| 2026-10-08 11:50 | model-only | cs2 | ENCE | Sokerorg | YES ENCE | 3 | 0.41 | 0.48 | 0.39 | won | $1.71 |
| 2026-10-08 11:50 | favourite | cs2 | Sokerorg | ENCE | NO ENCE | 14 | 0.63 | 0.61 | 0.61 | lost | -$9.05 |
| 2026-10-08 11:50 | model-only | cs2 | TEAM XDM | The Huns Esports | YES TEAM XDM | 31 | 0.39 | 0.52 | 0.38 | open | - |
| 2026-10-08 11:50 | favourite | cs2 | The Huns Esports | TEAM XDM | YES The Huns Esports | 3 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-08 11:50 | model-only | cs2 | THE UNIT | The KnockoutX | NO The KnockoutX | 39 | 0.38 | 0.48 | 0.36 | lost | -$15.47 |
| 2026-10-08 11:50 | favourite | cs2 | The Last Resort | Privateer Gaming | NO Privateer Gaming | 11 | 0.81 | 0.76 | 0.76 | lost | -$9.03 |

## Backtest on real Kalshi prices

7529 settled matches from 2026-05-28 to 2026-10-05, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 1878 | $9,311.87 | -$978.87 | -10.5% | -19.1% to -2.2% | 34% | -0.6c | 98% |
| always the favourite (1% flat) | 3613 | $15,734.92 | -$707.92 | -4.5% | -6.9% to -2.0% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3616 | $8,324.33 | -$978.33 | -11.8% | -17.4% to -5.9% | 32% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7304 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5732 | 0.1960 | 69.2% |
| model | 0.6611 | 0.2345 | 59.4% |
| blend | 0.5729 | 0.1959 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1200 | 0.525 | 0.521 |
| (0.55, 0.6] | 1249 | 0.577 | 0.553 |
| (0.6, 0.65] | 1130 | 0.626 | 0.634 |
| (0.65, 0.7] | 988 | 0.676 | 0.701 |
| (0.7, 0.75] | 838 | 0.726 | 0.773 |
| (0.75, 0.8] | 706 | 0.776 | 0.809 |
| (0.8, 0.85] | 594 | 0.826 | 0.825 |
| (0.85, 0.9] | 443 | 0.877 | 0.905 |
| (0.9, 1.0] | 381 | 0.932 | 0.958 |

