# Esports paper trading (fake money)

Updated 2026-10-19 22:57 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 254 | 19 | 235 | 60 | -$518.90 | -20.1% | -1.0c (250) | $481.10 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 391 | 26 | 365 | 253 | -$91.90 | -3.4% | -1.4c (387) | $908.10 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

874 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5677 | 0.1933 |
| model | 0.6538 | 0.2311 |
| blend | 0.5664 | 0.1929 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 555 | 0.5740 | 0.6579 |
| dota2 | 142 | 0.5495 | 0.6454 |
| lol | 60 | 0.5511 | 0.7049 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 22 | 0.6473 | 0.6972 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-19 19:52 | model-only | cs2 | ARK E-sports | RED Canids Academy | YES ARK E-sports | 16 | 0.18 | 0.30 | 0.16 | lost | -$3.05 |
| 2026-10-19 17:52 | model-only | cs2 | Hacha Esports | Rush | YES Hacha Esports | 2 | 0.38 | 0.50 | 0.35 | lost | -$0.80 |
| 2026-10-19 16:21 | favourite | cs2 | UNiTY esports | 9INE | NO 9INE | 2 | 0.51 | 0.50 | 0.50 | won | $0.94 |
| 2026-10-19 15:51 | favourite | cs2 | ex-6666 | Fire Flux Esports | NO Fire Flux Esports | 2 | 0.52 | 0.51 | 0.51 | won | $0.92 |
| 2026-10-19 14:51 | model-only | cs2 | Pandaric eSports | Regnum4Games | YES Pandaric eSports | 1 | 0.25 | 0.38 | 0.23 | lost | -$0.27 |
| 2026-10-19 14:51 | favourite | cs2 | MASONIC | Linx Legacy Esport | NO Linx Legacy Esport | 5 | 0.65 | 0.61 | 0.61 | lost | -$3.33 |
| 2026-10-19 13:51 | model-only | cs2 | Brute | Phantom | YES Brute | 22 | 0.40 | 0.49 | 0.40 | won | $12.83 |
| 2026-10-19 13:51 | favourite | cs2 | Phantom | Brute | YES Phantom | 3 | 0.60 | 0.60 | 0.60 | lost | -$1.86 |
| 2026-10-19 13:51 | model-only | cs2 | fnatic | Liquid | NO Liquid | 20 | 0.44 | 0.55 | 0.44 | won | $10.85 |
| 2026-10-19 12:51 | favourite | cs2 | Saint Sinners | Lilmix | NO Lilmix | 11 | 0.80 | 0.79 | 0.79 | won | $2.07 |
| 2026-10-19 12:51 | model-only | cs2 | Lilmix | Saint Sinners | YES Lilmix | 30 | 0.23 | 0.29 | 0.21 | lost | -$7.28 |
| 2026-10-19 12:51 | favourite | cs2 | mellren | G2 Ares | NO G2 Ares | 13 | 0.67 | 0.65 | 0.65 | lost | -$8.92 |
| 2026-10-19 12:51 | favourite | cs2 | ex-Zero Tenacity | Bushido Wildcats | YES ex-Zero Tenacity | 12 | 0.72 | 0.70 | 0.70 | won | $3.19 |
| 2026-10-19 12:51 | favourite | cs2 | BBL | Apogee Esports | YES BBL | 15 | 0.57 | 0.56 | 0.56 | won | $6.19 |
| 2026-10-19 12:36 | favourite | cs2 | aimclub | Insiders Esport | NO Insiders Esport | 2 | 0.88 | 0.83 | 0.83 | won | $0.22 |
| 2026-10-19 10:50 | model-only | cs2 | GenOne | Omega | YES GenOne | 17 | 0.54 | 0.59 | 0.53 | won | $7.52 |
| 2026-10-19 10:50 | favourite | cs2 | TheMongolz | Alliance | NO Alliance | 11 | 0.75 | 0.74 | 0.74 | won | $2.60 |
| 2026-10-19 10:50 | favourite | cs2 | GenOne | Omega | YES GenOne | 16 | 0.54 | 0.53 | 0.53 | won | $7.08 |
| 2026-10-19 10:50 | favourite | dota2 | HULIGANI | Nemiga Gaming | YES HULIGANI | 12 | 0.69 | 0.69 | 0.69 | won | $3.54 |
| 2026-10-19 10:50 | model-only | dota2 | Nemiga Gaming | HULIGANI | NO HULIGANI | 29 | 0.32 | 0.46 | 0.31 | lost | -$9.73 |
| 2026-10-19 09:50 | favourite | cs2 | Bushido Wildcats | Saint Sinners | YES Bushido Wildcats | 16 | 0.54 | 0.52 | 0.52 | lost | -$8.92 |
| 2026-10-19 09:50 | model-only | cs2 | Saint Sinners | Bushido Wildcats | NO Bushido Wildcats | 19 | 0.50 | 0.57 | 0.48 | won | $9.16 |
| 2026-10-19 09:50 | favourite | cs2 | ex-6666 | Privateer Gaming | YES ex-6666 | 15 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-19 09:50 | model-only | cs2 | ex-6666 | Privateer Gaming | YES ex-6666 | 17 | 0.58 | 0.63 | 0.56 | open | - |
| 2026-10-19 09:50 | favourite | cs2 | Bebop | Honvéd | YES Bebop | 14 | 0.60 | 0.58 | 0.58 | won | $5.36 |

## Backtest on real Kalshi prices

8346 settled matches from 2026-05-28 to 2026-10-19, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 23 | $422.99 | -$10.99 | -2.6% | -39.0% to +46.3% | 57% | -0.0c | 8% |
| model only | 1998 | $8,526.95 | -$990.95 | -11.6% | -20.1% to -3.0% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4018 | $16,341.50 | -$762.50 | -4.7% | -6.9% to -2.4% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3742 | $8,889.87 | -$982.87 | -11.1% | -16.6% to -5.4% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8121 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5723 | 0.1955 | 69.3% |
| model | 0.6605 | 0.2343 | 59.6% |
| blend | 0.5719 | 0.1954 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1335 | 0.525 | 0.524 |
| (0.55, 0.6] | 1359 | 0.577 | 0.550 |
| (0.6, 0.65] | 1254 | 0.626 | 0.635 |
| (0.65, 0.7] | 1092 | 0.676 | 0.702 |
| (0.7, 0.75] | 921 | 0.726 | 0.773 |
| (0.75, 0.8] | 786 | 0.776 | 0.812 |
| (0.8, 0.85] | 668 | 0.826 | 0.826 |
| (0.85, 0.9] | 503 | 0.877 | 0.903 |
| (0.9, 1.0] | 428 | 0.932 | 0.956 |

