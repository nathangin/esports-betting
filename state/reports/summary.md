# Esports paper trading (fake money)

Updated 2026-10-21 10:06 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 284 | 33 | 251 | 67 | -$482.76 | -17.8% | -1.1c (273) | $517.24 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 442 | 50 | 392 | 272 | -$109.13 | -3.8% | -1.3c (429) | $890.87 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

942 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5690 | 0.1938 |
| model | 0.6560 | 0.2322 |
| blend | 0.5678 | 0.1934 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 613 | 0.5786 | 0.6621 |
| dota2 | 149 | 0.5417 | 0.6429 |
| lol | 61 | 0.5472 | 0.7010 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 24 | 0.6212 | 0.6892 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-21 09:51 | favourite | cs2 | Bebop | Phantom Academy | YES Bebop | 15 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | FaZe | JiJieHao | NO JiJieHao | 11 | 0.74 | 0.73 | 0.73 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | BASEMENT BOYS | Eternal Fire | YES BASEMENT BOYS | 44 | 0.22 | 0.41 | 0.21 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | Eternal Fire | BASEMENT BOYS | NO BASEMENT BOYS | 11 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | Inner Circle Academy | HAVU | YES Inner Circle Academy | 14 | 0.61 | 0.60 | 0.60 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | Sinners | Heroic | YES Sinners | 20 | 0.30 | 0.35 | 0.29 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | JiJieHao | FaZe | NO FaZe | 35 | 0.28 | 0.49 | 0.27 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | Heroic | Sinners | YES Heroic | 12 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | NOCTIS | eternal premium | NO eternal premium | 24 | 0.40 | 0.50 | 0.38 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | eternal premium | NOCTIS | NO NOCTIS | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | BC.Game Esports | Nexus | YES BC.Game Esports | 10 | 0.80 | 0.80 | 0.80 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | Privateer Gaming | Falcons Force | YES Privateer Gaming | 51 | 0.19 | 0.39 | 0.18 | open | - |
| 2026-10-21 09:51 | favourite | cs2 | Falcons Force | Privateer Gaming | YES Falcons Force | 10 | 0.83 | 0.82 | 0.82 | open | - |
| 2026-10-21 09:51 | model-only | cs2 | Phantom Academy | Bebop | YES Phantom Academy | 14 | 0.48 | 0.57 | 0.47 | open | - |
| 2026-10-21 09:21 | favourite | cs2 | 9INE Academy | CTRL Esports | YES 9INE Academy | 14 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-10-21 09:21 | model-only | cs2 | CTRL Esports | 9INE Academy | YES CTRL Esports | 23 | 0.43 | 0.50 | 0.41 | open | - |
| 2026-10-21 08:51 | favourite | valorant | Dragon Ranger Gaming | Rare Atom | YES Dragon Ranger Gaming | 11 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | NEXVOID | Chinggis Warriors | YES NEXVOID | 1 | 0.49 | 0.58 | 0.49 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | magic | TheMongolz | YES magic | 22 | 0.45 | 0.54 | 0.45 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | TheMongolz | magic | YES TheMongolz | 15 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | Chinggis Warriors | NEXVOID | YES Chinggis Warriors | 16 | 0.52 | 0.51 | 0.51 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | Brute | Sangal | YES Brute | 25 | 0.39 | 0.51 | 0.38 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | Sangal | Brute | YES Sangal | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-21 07:51 | favourite | dota2 | Inner Circle | Power Rangers | YES Inner Circle | 14 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-21 06:50 | favourite | valorant | Octagonal Disposition Gaming | Unsettled Resentment | YES Octagonal Disposition Gaming | 16 | 0.53 | 0.52 | 0.52 | open | - |

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

