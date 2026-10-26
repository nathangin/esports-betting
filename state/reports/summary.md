# Esports paper trading (fake money)

Updated 2026-10-26 16:26 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 382 | 37 | 345 | 110 | -$228.47 | -6.4% | -0.8c (376) | $771.53 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 599 | 52 | 547 | 367 | -$225.43 | -5.7% | -1.4c (591) | $774.57 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1283 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5769 | 0.1976 |
| model | 0.6574 | 0.2329 |
| blend | 0.5762 | 0.1975 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 829 | 0.5899 | 0.6645 |
| dota2 | 191 | 0.5528 | 0.6397 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 77 | 0.5593 | 0.7265 |
| valorant | 59 | 0.5641 | 0.6698 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-26 15:51 | favourite | cs2 | Natus Vincere | BetBoom Team | NO BetBoom Team | 6 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-26 15:51 | favourite | cs2 | ECSTATIC | MASQ | YES ECSTATIC | 10 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-10-26 15:51 | model-only | cs2 | MASQ | ECSTATIC | NO ECSTATIC | 6 | 0.30 | 0.51 | 0.28 | open | - |
| 2026-10-26 15:51 | favourite | cs2 | G2 | DENDELE CS | NO DENDELE CS | 10 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-26 15:51 | model-only | cs2 | DENDELE CS | G2 | YES DENDELE CS | 56 | 0.26 | 0.43 | 0.26 | open | - |
| 2026-10-26 15:51 | favourite | cs2 | BIG Academy | Sissi State Punks | YES BIG Academy | 8 | 0.89 | 0.87 | 0.87 | open | - |
| 2026-10-26 15:21 | favourite | cs2 | TTG Esports | DINERO | NO DINERO | 1 | 0.78 | 0.73 | 0.73 | open | - |
| 2026-10-26 15:21 | model-only | cs2 | DINERO | TTG Esports | YES DINERO | 1 | 0.25 | 0.43 | 0.27 | open | - |
| 2026-10-26 15:21 | favourite | cs2 | Aurora Young Blood | Four Magic | YES Aurora Young Blood | 10 | 0.71 | 0.67 | 0.67 | open | - |
| 2026-10-26 13:51 | favourite | cs2 | Nuclear TigeRES | UNiTY esports | YES Nuclear TigeRES | 1 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-26 13:51 | model-only | cs2 | UNiTY esports | Nuclear TigeRES | YES UNiTY esports | 42 | 0.35 | 0.55 | 0.35 | open | - |
| 2026-10-26 13:51 | favourite | cs2 | ILLYRIANS | HAVU | NO HAVU | 14 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-26 12:51 | favourite | cs2 | Legacy | Liquid | YES Legacy | 11 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-10-26 12:51 | model-only | cs2 | FURIA | Spirit | NO Spirit | 27 | 0.37 | 0.42 | 0.36 | open | - |
| 2026-10-26 12:51 | favourite | cs2 | Spirit | FURIA | NO FURIA | 12 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-10-26 12:51 | model-only | cs2 | Liquid | Legacy | NO Legacy | 47 | 0.30 | 0.43 | 0.30 | open | - |
| 2026-10-26 12:51 | model-only | dota2 | Team Spirit | PARIVISION | NO PARIVISION | 38 | 0.37 | 0.48 | 0.36 | open | - |
| 2026-10-26 12:51 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 12 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-10-26 10:50 | favourite | cs2 | Walczaki | Wingman | YES Walczaki | 12 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-26 10:50 | model-only | cs2 | Wingman | Walczaki | YES Wingman | 36 | 0.40 | 0.55 | 0.39 | open | - |
| 2026-10-26 10:50 | favourite | cs2 | ex-6666 | Sokerorg | YES ex-6666 | 11 | 0.66 | 0.62 | 0.62 | lost | -$7.44 |
| 2026-10-26 10:50 | favourite | cs2 | Metizport | Brute | YES Metizport | 13 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-26 10:20 | favourite | cs2 | Copenhagen Wolves | WonderKids | NO WonderKids | 6 | 0.85 | 0.84 | 0.84 | won | $0.84 |
| 2026-10-26 09:50 | favourite | dota2 | Team Yandex | Team Liquid | YES Team Yandex | 9 | 0.84 | 0.84 | 0.84 | open | - |
| 2026-10-26 09:50 | model-only | dota2 | Team Liquid | Team Yandex | YES Team Liquid | 56 | 0.16 | 0.21 | 0.16 | open | - |

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

