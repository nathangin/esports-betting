# Esports paper trading (fake money)

Updated 2026-10-21 08:06 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 277 | 27 | 250 | 67 | -$472.09 | -17.5% | -1.1c (270) | $527.91 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 432 | 41 | 391 | 271 | -$109.60 | -3.8% | -1.3c (424) | $890.40 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

940 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5695 | 0.1941 |
| model | 0.6562 | 0.2322 |
| blend | 0.5683 | 0.1937 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 612 | 0.5790 | 0.6621 |
| dota2 | 149 | 0.5417 | 0.6429 |
| lol | 61 | 0.5472 | 0.7010 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 23 | 0.6357 | 0.6961 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-21 07:51 | favourite | dota2 | Inner Circle | Power Rangers | YES Inner Circle | 14 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | Sangal | Brute | YES Sangal | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | Brute | Sangal | YES Brute | 25 | 0.39 | 0.51 | 0.38 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | Chinggis Warriors | NEXVOID | YES Chinggis Warriors | 16 | 0.52 | 0.51 | 0.51 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | NEXVOID | Chinggis Warriors | YES NEXVOID | 1 | 0.49 | 0.58 | 0.49 | open | - |
| 2026-10-21 07:51 | favourite | cs2 | TheMongolz | magic | YES TheMongolz | 15 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-10-21 07:51 | model-only | cs2 | magic | TheMongolz | YES magic | 22 | 0.45 | 0.54 | 0.45 | open | - |
| 2026-10-21 06:50 | model-only | cs2 | Sokerorg | BakS eSports | NO BakS eSports | 43 | 0.23 | 0.34 | 0.21 | open | - |
| 2026-10-21 06:50 | favourite | cs2 | Brute | ex-6666 | YES Brute | 12 | 0.68 | 0.66 | 0.66 | open | - |
| 2026-10-21 06:50 | favourite | cs2 | KAMUI | eSuba | NO eSuba | 15 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-10-21 06:50 | favourite | cs2 | BakS eSports | Sokerorg | YES BakS eSports | 10 | 0.81 | 0.79 | 0.79 | open | - |
| 2026-10-21 06:50 | favourite | valorant | Octagonal Disposition Gaming | Unsettled Resentment | YES Octagonal Disposition Gaming | 16 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-21 05:50 | favourite | cs2 | Lynn Vision | Rare Atom | YES Lynn Vision | 11 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-21 04:50 | favourite | valorant | Any Questions Gaming | World Sports Invictus Gaming | YES Any Questions Gaming | 2 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-10-21 04:50 | model-only | valorant | World Sports Invictus Gaming | Any Questions Gaming | NO Any Questions Gaming | 39 | 0.26 | 0.41 | 0.25 | open | - |
| 2026-10-21 03:50 | favourite | cs2 | Vitalem Aerem | Wept Xyloid Melancholy | NO Wept Xyloid Melancholy | 10 | 0.80 | 0.80 | 0.80 | won | $1.88 |
| 2026-10-21 02:50 | favourite | valorant | Wolves Esports | A Team | NO A Team | 1 | 0.68 | 0.68 | 0.68 | won | $0.30 |
| 2026-10-21 02:50 | model-only | valorant | A Team | Wolves Esports | NO Wolves Esports | 32 | 0.32 | 0.49 | 0.32 | lost | -$10.73 |
| 2026-10-20 15:54 | model-only | cs2 | Lavked | ex-6666 | NO ex-6666 | 2 | 0.38 | 0.48 | 0.37 | won | $1.20 |
| 2026-10-20 14:54 | favourite | cs2 | B8 Academy | maybe | YES B8 Academy | 4 | 0.58 | 0.58 | 0.58 | won | $1.61 |
| 2026-10-20 13:54 | model-only | cs2 | ex-Zero Tenacity | FOKUS | YES ex-Zero Tenacity | 32 | 0.33 | 0.52 | 0.34 | lost | -$11.06 |
| 2026-10-20 13:54 | model-only | dota2 | Team Synapse | Yellow Submarine | YES Team Synapse | 25 | 0.26 | 0.40 | 0.24 | lost | -$6.84 |
| 2026-10-20 12:54 | favourite | cs2 | Revise | Wingman | YES Revise | 10 | 0.65 | 0.64 | 0.64 | lost | -$6.66 |
| 2026-10-20 12:54 | favourite | cs2 | Team Nemesis | Apogee Esports | NO Apogee Esports | 12 | 0.69 | 0.68 | 0.68 | lost | -$8.46 |
| 2026-10-20 12:54 | favourite | cs2 | Iberian Soul | JiJieHao | YES Iberian Soul | 16 | 0.54 | 0.54 | 0.54 | lost | -$8.92 |

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

