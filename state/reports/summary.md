# Esports paper trading (fake money)

Updated 2026-10-22 08:32 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 293 | 28 | 265 | 74 | -$414.17 | -14.6% | -1.0c (288) | $585.83 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 461 | 43 | 418 | 288 | -$138.37 | -4.5% | -1.3c (455) | $861.63 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1004 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5724 | 0.1954 |
| model | 0.6586 | 0.2334 |
| blend | 0.5713 | 0.1950 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 664 | 0.5843 | 0.6649 |
| dota2 | 154 | 0.5420 | 0.6440 |
| lol | 61 | 0.5472 | 0.7010 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 30 | 0.5846 | 0.6907 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-22 07:57 | favourite | valorant | Wolves Esports | KeepBest Gaming | NO KeepBest Gaming | 5 | 0.56 | 0.53 | 0.53 | open | - |
| 2026-10-22 07:57 | model-only | valorant | KeepBest Gaming | Wolves Esports | YES KeepBest Gaming | 23 | 0.48 | 0.62 | 0.47 | open | - |
| 2026-10-22 07:57 | favourite | dota2 | Yangon Galacticos | Team Nemesis Academy | NO Team Nemesis Academy | 1 | 0.88 | 0.83 | 0.83 | open | - |
| 2026-10-22 06:54 | favourite | cs2 | Spirit Academy | GenOne | YES Spirit Academy | 14 | 0.57 | 0.58 | 0.58 | open | - |
| 2026-10-22 06:54 | favourite | cs2 | BakS eSports | Azuolas | NO Azuolas | 11 | 0.75 | 0.71 | 0.71 | open | - |
| 2026-10-22 06:54 | favourite | cs2 | ex-6666 | Bushido Wildcats | YES ex-6666 | 12 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-22 06:54 | favourite | cs2 | Passion Academy | WonderKids | YES Passion Academy | 11 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-10-22 06:54 | model-only | cs2 | Spirit Academy | GenOne | YES Spirit Academy | 19 | 0.57 | 0.63 | 0.58 | open | - |
| 2026-10-22 06:54 | model-only | cs2 | Bushido Wildcats | ex-6666 | YES Bushido Wildcats | 31 | 0.36 | 0.46 | 0.34 | open | - |
| 2026-10-22 06:54 | favourite | cs2 | eSuba | TTG Esports | YES eSuba | 14 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-10-22 06:54 | favourite | valorant | Joblife | Habos Babos | NO Habos Babos | 9 | 0.90 | 0.89 | 0.89 | open | - |
| 2026-10-22 06:54 | model-only | valorant | CGN Esports | Eintracht Frankfurt | YES CGN Esports | 27 | 0.41 | 0.61 | 0.41 | open | - |
| 2026-10-22 06:54 | favourite | valorant | Eintracht Frankfurt | CGN Esports | YES Eintracht Frankfurt | 1 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-22 04:53 | favourite | dota2 | Team Kinetix | Novus Gaming | YES Team Kinetix | 11 | 0.71 | 0.69 | 0.69 | open | - |
| 2026-10-22 04:53 | model-only | dota2 | Novus Gaming | Team Kinetix | NO Team Kinetix | 33 | 0.33 | 0.51 | 0.31 | open | - |
| 2026-10-22 03:53 | favourite | cs2 | Rare Atom | Vitalem Aerem | NO Vitalem Aerem | 12 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-22 03:53 | model-only | cs2 | Vitalem Aerem | Rare Atom | NO Rare Atom | 7 | 0.31 | 0.43 | 0.31 | open | - |
| 2026-10-21 14:52 | model-only | cs2 | Martians | Joga de terno | YES Martians | 27 | 0.37 | 0.48 | 0.36 | won | $16.56 |
| 2026-10-21 13:52 | favourite | cs2 | CYBERSHOKE Esports | BlinkDagger | NO BlinkDagger | 3 | 0.83 | 0.80 | 0.80 | won | $0.48 |
| 2026-10-21 12:51 | favourite | cs2 | Fluxo W7M | Galorys | YES Fluxo W7M | 3 | 0.64 | 0.62 | 0.62 | won | $1.03 |
| 2026-10-21 11:51 | favourite | cs2 | GenOne | Dark Moon | YES GenOne | 6 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-21 11:51 | favourite | cs2 | mellren | Four Magic | YES mellren | 10 | 0.84 | 0.83 | 0.83 | lost | -$8.50 |
| 2026-10-21 10:51 | favourite | cs2 | fnatic | PRIVATE | YES fnatic | 12 | 0.68 | 0.68 | 0.68 | lost | -$8.35 |
| 2026-10-21 10:51 | favourite | cs2 | Apogee Esports | aimclub | NO aimclub | 10 | 0.84 | 0.83 | 0.83 | won | $1.50 |
| 2026-10-21 10:51 | model-only | cs2 | PRIVATE | fnatic | YES PRIVATE | 32 | 0.32 | 0.45 | 0.32 | won | $21.27 |

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

