# Esports paper trading (fake money)

Updated 2026-10-22 11:23 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 299 | 30 | 269 | 76 | -$408.72 | -14.2% | -1.0c (294) | $591.28 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 474 | 47 | 427 | 294 | -$140.81 | -4.5% | -1.3c (468) | $859.19 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1013 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5718 | 0.1952 |
| model | 0.6569 | 0.2326 |
| blend | 0.5708 | 0.1948 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 670 | 0.5845 | 0.6635 |
| dota2 | 155 | 0.5391 | 0.6412 |
| lol | 61 | 0.5472 | 0.7010 |
| ow | 60 | 0.4906 | 0.5267 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 32 | 0.5749 | 0.6781 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-22 10:53 | favourite | lol | Galions | Solary | NO Solary | 14 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-22 10:53 | model-only | lol | Solary | Galions | NO Galions | 26 | 0.42 | 0.55 | 0.42 | open | - |
| 2026-10-22 10:53 | favourite | dota2 | HULIGANI | Team Lynx | YES HULIGANI | 14 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-10-22 09:52 | favourite | cs2 | Walczaki | mellren | YES Walczaki | 14 | 0.59 | 0.54 | 0.54 | open | - |
| 2026-10-22 09:52 | model-only | cs2 | Phantom Academy | Falcons Force | NO Falcons Force | 30 | 0.37 | 0.47 | 0.35 | open | - |
| 2026-10-22 09:52 | favourite | cs2 | Falcons Force | Phantom Academy | YES Falcons Force | 12 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-10-22 09:52 | model-only | cs2 | Just_Players | FORZE Reload | NO FORZE Reload | 18 | 0.36 | 0.41 | 0.34 | open | - |
| 2026-10-22 09:52 | favourite | cs2 | FORZE Reload | Just_Players | YES FORZE Reload | 12 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-22 09:52 | favourite | cs2 | Butterfly | Lavked | YES Butterfly | 14 | 0.59 | 0.56 | 0.56 | open | - |
| 2026-10-22 09:52 | favourite | cs2 | TheMongolz | BIG | NO BIG | 16 | 0.51 | 0.50 | 0.50 | open | - |
| 2026-10-22 09:52 | favourite | dota2 | Team Spirit | LEGION | YES Team Spirit | 9 | 0.90 | 0.90 | 0.90 | open | - |
| 2026-10-22 09:52 | model-only | valorant | Any Questions Gaming | Nova Esports | YES Any Questions Gaming | 37 | 0.30 | 0.44 | 0.29 | open | - |
| 2026-10-22 09:52 | favourite | valorant | Nova Esports | Any Questions Gaming | YES Nova Esports | 11 | 0.71 | 0.71 | 0.71 | open | - |
| 2026-10-22 09:52 | favourite | valorant | Blezz | Team George | YES Blezz | 15 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-22 09:52 | model-only | valorant | Natus Vincere | Eternal Fire | NO Eternal Fire | 26 | 0.42 | 0.48 | 0.41 | open | - |
| 2026-10-22 09:52 | favourite | valorant | Eternal Fire | Natus Vincere | YES Eternal Fire | 13 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-10-22 09:22 | favourite | cs2 | Elite Klan | Revenge | YES Elite Klan | 15 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-22 09:22 | model-only | cs2 | Revenge | Elite Klan | YES Revenge | 23 | 0.48 | 0.63 | 0.46 | open | - |
| 2026-10-22 08:52 | favourite | cs2 | Team Nemesis | WW Team | YES Team Nemesis | 9 | 0.88 | 0.79 | 0.79 | open | - |
| 2026-10-22 07:57 | model-only | valorant | KeepBest Gaming | Wolves Esports | YES KeepBest Gaming | 23 | 0.48 | 0.62 | 0.47 | won | $11.55 |
| 2026-10-22 07:57 | favourite | dota2 | Yangon Galacticos | Team Nemesis Academy | NO Team Nemesis Academy | 1 | 0.88 | 0.83 | 0.83 | won | $0.11 |
| 2026-10-22 07:57 | favourite | valorant | Wolves Esports | KeepBest Gaming | NO KeepBest Gaming | 5 | 0.56 | 0.53 | 0.53 | lost | -$2.89 |
| 2026-10-22 06:54 | favourite | cs2 | Spirit Academy | GenOne | YES Spirit Academy | 14 | 0.57 | 0.58 | 0.58 | won | $5.77 |
| 2026-10-22 06:54 | model-only | cs2 | Bushido Wildcats | ex-6666 | YES Bushido Wildcats | 31 | 0.36 | 0.46 | 0.34 | lost | -$11.66 |
| 2026-10-22 06:54 | favourite | cs2 | ex-6666 | Bushido Wildcats | YES ex-6666 | 12 | 0.67 | 0.66 | 0.66 | won | $3.77 |

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

