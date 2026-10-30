# Esports paper trading (fake money)

Updated 2026-10-30 13:48 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 446 | 41 | 405 | 136 | -$117.79 | -2.7% | -0.4c (441) | $882.21 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 712 | 56 | 656 | 432 | -$339.63 | -7.4% | -1.5c (706) | $660.37 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1500 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5789 | 0.1987 |
| model | 0.6527 | 0.2308 |
| blend | 0.5785 | 0.1987 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 982 | 0.5926 | 0.6596 |
| dota2 | 231 | 0.5436 | 0.6303 |
| ow | 86 | 0.5026 | 0.5286 |
| lol | 85 | 0.5694 | 0.7245 |
| valorant | 72 | 0.5874 | 0.6728 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-30 11:53 | favourite | dota2 | Team Liquid | OG | NO OG | 1 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-10-30 11:53 | model-only | dota2 | OG | Team Liquid | NO Team Liquid | 49 | 0.35 | 0.54 | 0.35 | open | - |
| 2026-10-30 11:53 | favourite | cs2 | naocopulas | QUINTESSENCIA | YES naocopulas | 8 | 0.74 | 0.74 | 0.74 | open | - |
| 2026-10-30 11:53 | favourite | cs2 | ShindeN | Isurus | NO Isurus | 1 | 0.82 | 0.82 | 0.82 | open | - |
| 2026-10-30 11:53 | model-only | cs2 | Isurus | ShindeN | YES Isurus | 89 | 0.19 | 0.38 | 0.18 | open | - |
| 2026-10-30 11:53 | favourite | cs2 | MIBR | Eternal Fire | YES MIBR | 10 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-10-30 11:53 | model-only | cs2 | Eternal Fire | MIBR | YES Eternal Fire | 43 | 0.40 | 0.56 | 0.40 | open | - |
| 2026-10-30 10:53 | favourite | dota2 | Team Synapse | potn9ki | YES Team Synapse | 7 | 0.84 | 0.82 | 0.82 | open | - |
| 2026-10-30 10:53 | model-only | dota2 | potn9ki | Team Synapse | NO Team Synapse | 33 | 0.20 | 0.33 | 0.18 | open | - |
| 2026-10-30 10:53 | favourite | cs2 | Vitality | Nemiga | YES Vitality | 7 | 0.82 | 0.82 | 0.82 | open | - |
| 2026-10-30 10:53 | favourite | cs2 | FOKUS | Sokerorg | YES FOKUS | 7 | 0.84 | 0.83 | 0.83 | open | - |
| 2026-10-30 10:53 | model-only | cs2 | Sokerorg | FOKUS | YES Sokerorg | 102 | 0.17 | 0.29 | 0.17 | open | - |
| 2026-10-30 10:53 | favourite | cs2 | Nuclear TigeRES | PRIVATE | NO PRIVATE | 11 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-10-30 10:53 | model-only | cs2 | Nuclear TigeRES | PRIVATE | NO PRIVATE | 31 | 0.53 | 0.58 | 0.53 | open | - |
| 2026-10-30 10:53 | favourite | cs2 | Dark Moon | Lilmix | NO Lilmix | 7 | 0.76 | 0.72 | 0.72 | won | $1.59 |
| 2026-10-30 10:23 | favourite | cs2 | Copenhagen Wolves | gothboiclique | YES Copenhagen Wolves | 10 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-10-30 10:23 | model-only | cs2 | Invicta | Falcons Force | NO Falcons Force | 51 | 0.34 | 0.47 | 0.34 | lost | -$18.15 |
| 2026-10-30 10:23 | favourite | cs2 | Falcons Force | Invicta | YES Falcons Force | 9 | 0.67 | 0.66 | 0.66 | won | $2.83 |
| 2026-10-30 09:53 | favourite | valorant | FunPlus Phoenix | Any Questions Gaming | NO Any Questions Gaming | 10 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-10-30 09:53 | model-only | valorant | Any Questions Gaming | FunPlus Phoenix | YES Any Questions Gaming | 42 | 0.42 | 0.53 | 0.41 | open | - |
| 2026-10-30 08:53 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 11 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-10-30 08:53 | model-only | dota2 | Team Spirit | PARIVISION | NO PARIVISION | 37 | 0.46 | 0.52 | 0.45 | open | - |
| 2026-10-30 07:53 | favourite | cs2 | BASEMENT BOYS | Teletubisie | NO Teletubisie | 11 | 0.58 | 0.58 | 0.58 | lost | -$6.57 |
| 2026-10-30 07:53 | favourite | valorant | Nova Esports | A Team | NO A Team | 7 | 0.82 | 0.81 | 0.80 | won | $1.18 |
| 2026-10-30 07:53 | favourite | cs2 | UNiTY esports | Gatorian | NO Gatorian | 1 | 0.80 | 0.81 | 0.81 | won | $0.18 |

## Backtest on real Kalshi prices

8779 settled matches from 2026-05-28 to 2026-10-26, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 2012 | $8,014.92 | -$990.92 | -12.4% | -20.6% to -4.1% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4205 | $16,392.93 | -$775.93 | -4.7% | -7.0% to -2.5% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3757 | $9,447.49 | -$982.49 | -10.4% | -15.7% to -4.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8554 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5736 | 0.1961 | 69.2% |
| model | 0.6609 | 0.2344 | 59.5% |
| blend | 0.5732 | 0.1960 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1402 | 0.525 | 0.529 |
| (0.55, 0.6] | 1444 | 0.577 | 0.551 |
| (0.6, 0.65] | 1325 | 0.626 | 0.629 |
| (0.65, 0.7] | 1152 | 0.676 | 0.702 |
| (0.7, 0.75] | 964 | 0.726 | 0.772 |
| (0.75, 0.8] | 823 | 0.776 | 0.810 |
| (0.8, 0.85] | 698 | 0.826 | 0.827 |
| (0.85, 0.9] | 521 | 0.877 | 0.902 |
| (0.9, 1.0] | 450 | 0.932 | 0.956 |

