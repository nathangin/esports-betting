# Esports paper trading (fake money)

Updated 2026-10-23 09:36 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 313 | 31 | 282 | 82 | -$417.90 | -14.0% | -0.9c (309) | $582.10 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 493 | 46 | 447 | 308 | -$129.18 | -3.9% | -1.4c (488) | $870.82 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1082 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5706 | 0.1947 |
| model | 0.6562 | 0.2322 |
| blend | 0.5693 | 0.1943 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 717 | 0.5857 | 0.6626 |
| dota2 | 163 | 0.5394 | 0.6442 |
| lol | 62 | 0.5472 | 0.7027 |
| ow | 61 | 0.4831 | 0.5245 |
| valorant | 42 | 0.5382 | 0.6638 |
| r6 | 37 | 0.6371 | 0.7146 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-23 08:51 | favourite | cs2 | Team Nemesis | Team ACES | YES Team Nemesis | 7 | 0.85 | 0.81 | 0.81 | open | - |
| 2026-10-23 08:20 | favourite | ow | Falcons | ZANSIDE GAMING | YES Falcons | 9 | 0.89 | 0.86 | 0.86 | open | - |
| 2026-10-23 08:20 | model-only | ow | ZANSIDE GAMING | Falcons | YES ZANSIDE GAMING | 8 | 0.16 | 0.35 | 0.14 | open | - |
| 2026-10-23 07:50 | favourite | valorant | TEC Esports | Unsettled Resentment | YES TEC Esports | 3 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-23 07:50 | model-only | valorant | Unsettled Resentment | TEC Esports | YES Unsettled Resentment | 26 | 0.43 | 0.50 | 0.43 | open | - |
| 2026-10-23 07:50 | favourite | dota2 | Novus Gaming | Team Nemesis Academy | NO Team Nemesis Academy | 11 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-23 07:50 | model-only | dota2 | Team Nemesis Academy | Novus Gaming | YES Team Nemesis Academy | 3 | 0.27 | 0.40 | 0.26 | open | - |
| 2026-10-23 07:50 | favourite | dota2 | salamit | Nemiga Gaming | YES salamit | 15 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-23 06:50 | favourite | cs2 | Copenhagen Wolves | The Chosen Few | YES Copenhagen Wolves | 11 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-10-23 06:50 | model-only | cs2 | NOCTIS | eternal premium | NO eternal premium | 35 | 0.31 | 0.51 | 0.30 | open | - |
| 2026-10-23 06:50 | favourite | cs2 | eternal premium | NOCTIS | YES eternal premium | 11 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-10-23 06:50 | favourite | cs2 | ex-Zero Tenacity | ex-RUSTEC | NO ex-RUSTEC | 8 | 0.60 | 0.58 | 0.58 | open | - |
| 2026-10-23 06:50 | model-only | cs2 | The Chosen Few | Copenhagen Wolves | YES The Chosen Few | 35 | 0.31 | 0.47 | 0.30 | open | - |
| 2026-10-23 06:50 | model-only | dota2 | OG | 1win | NO 1win | 28 | 0.39 | 0.56 | 0.38 | open | - |
| 2026-10-23 06:50 | favourite | dota2 | 1win | OG | YES 1win | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-23 06:50 | model-only | valorant | CGN Esports | Natus Vincere | NO Natus Vincere | 20 | 0.56 | 0.80 | 0.56 | open | - |
| 2026-10-23 06:50 | favourite | valorant | CGN Esports | Natus Vincere | NO Natus Vincere | 15 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-23 04:50 | favourite | dota2 | Yangon Galacticos | Cloud Dawning | YES Yangon Galacticos | 11 | 0.71 | 0.67 | 0.67 | open | - |
| 2026-10-23 03:50 | favourite | cs2 | Rare Atom | NEXVOID | NO NEXVOID | 5 | 0.57 | 0.56 | 0.55 | open | - |
| 2026-10-23 03:50 | model-only | cs2 | NEXVOID | Rare Atom | NO Rare Atom | 2 | 0.45 | 0.59 | 0.45 | open | - |
| 2026-10-23 01:50 | favourite | cs2 | Lynn Vision | Chinggis Warriors | YES Lynn Vision | 11 | 0.77 | 0.76 | 0.76 | won | $2.39 |
| 2026-10-22 14:53 | favourite | cs2 | Sinners | Eternal Fire | NO Eternal Fire | 3 | 0.53 | 0.53 | 0.53 | won | $1.35 |
| 2026-10-22 13:53 | model-only | dota2 | CyberHero | Yellow Submarine | YES CyberHero | 8 | 0.21 | 0.28 | 0.20 | won | $6.22 |
| 2026-10-22 12:53 | model-only | cs2 | mellren | 33 | YES mellren | 1 | 0.37 | 0.56 | 0.36 | won | $0.61 |
| 2026-10-22 12:38 | model-only | cs2 | Quintessence | Ryvex | YES Quintessence | 10 | 0.62 | 0.67 | 0.61 | won | $3.63 |

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

