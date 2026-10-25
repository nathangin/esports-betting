# Esports paper trading (fake money)

Updated 2026-10-25 06:52 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 352 | 29 | 323 | 99 | -$212.53 | -6.4% | -0.8c (345) | $787.47 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 543 | 38 | 505 | 342 | -$198.11 | -5.4% | -1.4c (536) | $801.89 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1210 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5780 | 0.1979 |
| model | 0.6592 | 0.2336 |
| blend | 0.5773 | 0.1976 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 784 | 0.5907 | 0.6649 |
| dota2 | 181 | 0.5581 | 0.6470 |
| lol | 74 | 0.5528 | 0.7199 |
| ow | 73 | 0.5228 | 0.5545 |
| valorant | 55 | 0.5533 | 0.6569 |
| r6 | 43 | 0.6007 | 0.6818 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-25 06:52 | favourite | dota2 | Team Liquid | OG | YES Team Liquid | 13 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-10-25 06:52 | model-only | dota2 | OG | Team Liquid | NO Team Liquid | 36 | 0.42 | 0.50 | 0.41 | open | - |
| 2026-10-25 06:52 | favourite | cs2 | Spirit | TYLOO | YES Spirit | 8 | 0.90 | 0.90 | 0.90 | open | - |
| 2026-10-25 06:52 | model-only | cs2 | TYLOO | Spirit | NO Spirit | 134 | 0.11 | 0.23 | 0.10 | open | - |
| 2026-10-25 06:52 | favourite | cs2 | FUT Esports | Liquid | YES FUT Esports | 10 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-25 06:52 | model-only | cs2 | Liquid | FUT Esports | NO FUT Esports | 53 | 0.28 | 0.44 | 0.28 | open | - |
| 2026-10-24 19:51 | model-only | valorant | SK Nebula | Shopify Rebellion GC | YES SK Nebula | 3 | 0.34 | 0.42 | 0.33 | lost | -$1.07 |
| 2026-10-24 17:51 | model-only | cs2 | Los Ninos | BORRACHEIROS | NO BORRACHEIROS | 1 | 0.33 | 0.41 | 0.31 | lost | -$0.35 |
| 2026-10-24 16:50 | model-only | dota2 | TheBot$ | CyberHero | NO CyberHero | 1 | 0.19 | 0.31 | 0.18 | open | - |
| 2026-10-24 16:50 | model-only | cs2 | Galorys | paiN | NO paiN | 11 | 0.42 | 0.64 | 0.42 | lost | -$4.81 |
| 2026-10-24 14:50 | model-only | cs2 | DENDELE CS | FURIA | YES DENDELE CS | 1 | 0.18 | 0.36 | 0.17 | lost | -$0.20 |
| 2026-10-24 14:20 | model-only | cs2 | ZOTIX | prodigy | NO prodigy | 35 | 0.42 | 0.50 | 0.40 | lost | -$15.30 |
| 2026-10-24 14:20 | model-only | cs2 | SPARX | X-CITY | YES SPARX | 22 | 0.48 | 0.54 | 0.46 | lost | -$10.95 |
| 2026-10-24 12:35 | favourite | cs2 | Phantom Academy | TitanFlow | NO TitanFlow | 1 | 0.68 | 0.68 | 0.68 | lost | -$0.70 |
| 2026-10-24 11:50 | favourite | cs2 | Legacy | Nemiga | YES Legacy | 7 | 0.67 | 0.66 | 0.66 | lost | -$4.80 |
| 2026-10-24 11:50 | favourite | cs2 | Tropa do KinGui | MEIA NOITE | NO MEIA NOITE | 12 | 0.63 | 0.62 | 0.62 | won | $4.24 |
| 2026-10-24 11:50 | favourite | cs2 | Vitality | 9z | NO 9z | 9 | 0.84 | 0.83 | 0.83 | won | $1.35 |
| 2026-10-24 10:54 | favourite | dota2 | Team Synapse | Zero Tenacity | YES Team Synapse | 15 | 0.53 | 0.51 | 0.51 | won | $6.78 |
| 2026-10-24 10:54 | favourite | cs2 | G2 Ares | The Last Resort | YES G2 Ares | 10 | 0.77 | 0.75 | 0.75 | lost | -$7.83 |
| 2026-10-24 10:54 | model-only | cs2 | The Last Resort | G2 Ares | NO G2 Ares | 28 | 0.27 | 0.45 | 0.25 | won | $20.05 |
| 2026-10-24 09:54 | favourite | cs2 | Team Nemesis | mellren | YES Team Nemesis | 10 | 0.76 | 0.76 | 0.76 | won | $2.27 |
| 2026-10-24 09:54 | model-only | cs2 | Azuolas | HAVU | YES Azuolas | 2 | 0.23 | 0.38 | 0.21 | lost | -$0.49 |
| 2026-10-24 09:54 | favourite | cs2 | HAVU | Azuolas | NO Azuolas | 10 | 0.79 | 0.79 | 0.79 | won | $1.98 |
| 2026-10-24 09:54 | model-only | cs2 | mellren | Team Nemesis | YES mellren | 6 | 0.25 | 0.38 | 0.24 | lost | -$1.58 |
| 2026-10-24 09:54 | favourite | cs2 | Spirit Academy | Lavked | YES Spirit Academy | 12 | 0.65 | 0.65 | 0.65 | won | $4.00 |

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

