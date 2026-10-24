# Esports paper trading (fake money)

Updated 2026-10-24 11:34 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 342 | 35 | 307 | 93 | -$340.37 | -10.6% | -0.9c (337) | $659.63 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 536 | 52 | 484 | 330 | -$175.07 | -4.9% | -1.3c (530) | $824.93 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1149 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5724 | 0.1956 |
| model | 0.6568 | 0.2326 |
| blend | 0.5712 | 0.1953 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 751 | 0.5867 | 0.6633 |
| dota2 | 175 | 0.5525 | 0.6482 |
| lol | 68 | 0.5539 | 0.7164 |
| ow | 66 | 0.4712 | 0.5150 |
| valorant | 49 | 0.5508 | 0.6655 |
| r6 | 40 | 0.6166 | 0.6957 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-24 10:54 | favourite | dota2 | Team Synapse | Zero Tenacity | YES Team Synapse | 15 | 0.53 | 0.51 | 0.51 | open | - |
| 2026-10-24 10:54 | favourite | cs2 | G2 Ares | The Last Resort | YES G2 Ares | 10 | 0.77 | 0.75 | 0.75 | open | - |
| 2026-10-24 10:54 | model-only | cs2 | The Last Resort | G2 Ares | NO G2 Ares | 28 | 0.27 | 0.45 | 0.25 | open | - |
| 2026-10-24 09:54 | favourite | cs2 | Team Nemesis | mellren | YES Team Nemesis | 10 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-10-24 09:54 | favourite | cs2 | HAVU | Azuolas | NO Azuolas | 10 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-24 09:54 | favourite | cs2 | Spirit Academy | Lavked | YES Spirit Academy | 12 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-24 09:54 | model-only | cs2 | mellren | Team Nemesis | YES mellren | 6 | 0.25 | 0.38 | 0.24 | open | - |
| 2026-10-24 09:54 | model-only | cs2 | Azuolas | HAVU | YES Azuolas | 2 | 0.23 | 0.38 | 0.21 | open | - |
| 2026-10-24 09:54 | favourite | cs2 | Donstu Esports | Quintessence | NO Quintessence | 14 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-10-24 09:54 | favourite | dota2 | Team Yandex | OG | NO OG | 5 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-10-24 09:54 | favourite | valorant | Dragon Ranger Gaming | TEC Esports | YES Dragon Ranger Gaming | 13 | 0.61 | 0.60 | 0.60 | open | - |
| 2026-10-24 09:54 | favourite | cs2 | XI Esport | Wingman | YES XI Esport | 13 | 0.61 | 0.58 | 0.58 | open | - |
| 2026-10-24 09:24 | favourite | cs2 | megoshort | RoundsGG | NO RoundsGG | 10 | 0.81 | 0.79 | 0.79 | open | - |
| 2026-10-24 09:24 | model-only | cs2 | Revenge | Passion Academy | YES Revenge | 29 | 0.41 | 0.66 | 0.42 | open | - |
| 2026-10-24 09:24 | favourite | cs2 | Passion Academy | Revenge | YES Passion Academy | 13 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-24 09:24 | model-only | cs2 | RoundsGG | megoshort | NO megoshort | 49 | 0.24 | 0.40 | 0.21 | open | - |
| 2026-10-24 09:24 | model-only | valorant | Fire Flux Esports | FUT Esports | YES Fire Flux Esports | 25 | 0.48 | 0.57 | 0.47 | open | - |
| 2026-10-24 09:24 | favourite | valorant | FUT Esports | Fire Flux Esports | NO Fire Flux Esports | 15 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-24 08:54 | favourite | cs2 | MOUZ | Liquid | YES MOUZ | 9 | 0.85 | 0.85 | 0.85 | open | - |
| 2026-10-24 08:54 | model-only | cs2 | Liquid | MOUZ | YES Liquid | 80 | 0.15 | 0.32 | 0.15 | open | - |
| 2026-10-24 08:54 | favourite | cs2 | Spirit | BetBoom Team | YES Spirit | 10 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-24 08:54 | model-only | cs2 | BetBoom Team | Spirit | YES BetBoom Team | 58 | 0.21 | 0.34 | 0.21 | open | - |
| 2026-10-24 07:54 | model-only | r6 | SCARZ | CAG by VARREL | NO CAG by VARREL | 20 | 0.33 | 0.44 | 0.32 | open | - |
| 2026-10-24 07:54 | model-only | dota2 | Team Lynx | Nemiga Gaming | YES Team Lynx | 3 | 0.59 | 0.80 | 0.59 | lost | -$1.83 |
| 2026-10-24 07:54 | favourite | ow | SEIJI ESPORTS | Poker Face | NO Poker Face | 1 | 0.63 | 0.59 | 0.59 | open | - |

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

