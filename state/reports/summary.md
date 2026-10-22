# Esports paper trading (fake money)

Updated 2026-10-22 20:29 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 305 | 23 | 282 | 82 | -$417.90 | -14.0% | -1.0c (301) | $582.10 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 480 | 35 | 445 | 306 | -$132.92 | -4.1% | -1.3c (476) | $867.08 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1069 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5728 | 0.1956 |
| model | 0.6563 | 0.2323 |
| blend | 0.5717 | 0.1953 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 709 | 0.5870 | 0.6623 |
| dota2 | 162 | 0.5400 | 0.6450 |
| lol | 62 | 0.5472 | 0.7027 |
| ow | 60 | 0.4906 | 0.5267 |
| valorant | 41 | 0.5456 | 0.6573 |
| r6 | 35 | 0.6531 | 0.7263 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-22 14:53 | favourite | cs2 | Sinners | Eternal Fire | NO Eternal Fire | 3 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-22 13:53 | model-only | dota2 | CyberHero | Yellow Submarine | YES CyberHero | 8 | 0.21 | 0.28 | 0.20 | won | $6.22 |
| 2026-10-22 12:53 | model-only | cs2 | mellren | 33 | YES mellren | 1 | 0.37 | 0.56 | 0.36 | won | $0.61 |
| 2026-10-22 12:38 | model-only | cs2 | Quintessence | Ryvex | YES Quintessence | 10 | 0.62 | 0.67 | 0.61 | won | $3.63 |
| 2026-10-22 11:53 | model-only | cs2 | Nexus | JiJieHao | YES Nexus | 30 | 0.37 | 0.53 | 0.36 | lost | -$11.59 |
| 2026-10-22 11:53 | favourite | cs2 | FaZe | BC.Game Esports | NO BC.Game Esports | 14 | 0.57 | 0.56 | 0.56 | lost | -$8.23 |
| 2026-10-22 11:53 | model-only | cs2 | KUUSAMO.gg | LPH Gaming | YES KUUSAMO.gg | 40 | 0.28 | 0.44 | 0.28 | lost | -$11.77 |
| 2026-10-22 11:53 | favourite | cs2 | Tropa do KinGui | Martians | NO Martians | 9 | 0.90 | 0.89 | 0.89 | won | $0.84 |
| 2026-10-22 11:53 | favourite | cs2 | LPH Gaming | KUUSAMO.gg | NO KUUSAMO.gg | 11 | 0.73 | 0.72 | 0.72 | won | $2.81 |
| 2026-10-22 11:53 | favourite | cs2 | JiJieHao | Nexus | YES JiJieHao | 13 | 0.65 | 0.64 | 0.64 | won | $4.34 |
| 2026-10-22 11:53 | favourite | cs2 | Spirit Academy Green | maybe | YES Spirit Academy Green | 9 | 0.58 | 0.55 | 0.54 | lost | -$5.38 |
| 2026-10-22 11:53 | model-only | cs2 | TheChampionGG | ENCE Prospects | YES TheChampionGG | 1 | 0.52 | 0.60 | 0.51 | lost | -$0.54 |
| 2026-10-22 10:53 | favourite | lol | Galions | Solary | NO Solary | 14 | 0.58 | 0.58 | 0.58 | won | $5.64 |
| 2026-10-22 10:53 | model-only | lol | Solary | Galions | NO Galions | 26 | 0.42 | 0.55 | 0.42 | lost | -$11.37 |
| 2026-10-22 10:53 | favourite | dota2 | HULIGANI | Team Lynx | YES HULIGANI | 14 | 0.56 | 0.55 | 0.55 | won | $5.91 |
| 2026-10-22 09:52 | favourite | cs2 | TheMongolz | BIG | NO BIG | 16 | 0.51 | 0.50 | 0.50 | won | $7.56 |
| 2026-10-22 09:52 | model-only | cs2 | Phantom Academy | Falcons Force | NO Falcons Force | 30 | 0.37 | 0.47 | 0.35 | won | $18.41 |
| 2026-10-22 09:52 | favourite | cs2 | Falcons Force | Phantom Academy | YES Falcons Force | 12 | 0.66 | 0.65 | 0.65 | lost | -$8.11 |
| 2026-10-22 09:52 | model-only | cs2 | Just_Players | FORZE Reload | NO FORZE Reload | 18 | 0.36 | 0.41 | 0.34 | lost | -$6.78 |
| 2026-10-22 09:52 | favourite | cs2 | FORZE Reload | Just_Players | YES FORZE Reload | 12 | 0.67 | 0.66 | 0.66 | won | $3.77 |
| 2026-10-22 09:52 | favourite | cs2 | Butterfly | Lavked | YES Butterfly | 14 | 0.59 | 0.56 | 0.56 | lost | -$8.50 |
| 2026-10-22 09:52 | favourite | cs2 | Walczaki | mellren | YES Walczaki | 14 | 0.59 | 0.54 | 0.54 | open | - |
| 2026-10-22 09:52 | favourite | dota2 | Team Spirit | LEGION | YES Team Spirit | 9 | 0.90 | 0.90 | 0.90 | won | $0.84 |
| 2026-10-22 09:52 | model-only | valorant | Any Questions Gaming | Nova Esports | YES Any Questions Gaming | 37 | 0.30 | 0.44 | 0.29 | lost | -$11.65 |
| 2026-10-22 09:52 | favourite | valorant | Nova Esports | Any Questions Gaming | YES Nova Esports | 11 | 0.71 | 0.71 | 0.71 | won | $3.03 |

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

