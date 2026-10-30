# Esports paper trading (fake money)

Updated 2026-10-30 09:43 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 438 | 36 | 402 | 135 | -$104.28 | -2.4% | -0.4c (432) | $895.72 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 700 | 50 | 650 | 427 | -$342.77 | -7.5% | -1.5c (694) | $657.23 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1490 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5804 | 0.1993 |
| model | 0.6545 | 0.2316 |
| blend | 0.5800 | 0.1994 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 977 | 0.5932 | 0.6604 |
| dota2 | 229 | 0.5466 | 0.6332 |
| lol | 85 | 0.5694 | 0.7245 |
| ow | 84 | 0.5064 | 0.5346 |
| valorant | 71 | 0.5927 | 0.6790 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-30 08:53 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 11 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-10-30 08:53 | model-only | dota2 | Team Spirit | PARIVISION | NO PARIVISION | 37 | 0.46 | 0.52 | 0.45 | open | - |
| 2026-10-30 07:53 | favourite | valorant | Nova Esports | A Team | NO A Team | 7 | 0.82 | 0.81 | 0.80 | open | - |
| 2026-10-30 07:53 | favourite | cs2 | UNiTY esports | Gatorian | NO Gatorian | 1 | 0.80 | 0.81 | 0.81 | open | - |
| 2026-10-30 07:53 | model-only | cs2 | Gatorian | UNiTY esports | NO UNiTY esports | 89 | 0.19 | 0.32 | 0.19 | open | - |
| 2026-10-30 07:53 | favourite | cs2 | BASEMENT BOYS | Teletubisie | NO Teletubisie | 11 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-30 07:53 | model-only | cs2 | Teletubisie | BASEMENT BOYS | NO BASEMENT BOYS | 40 | 0.42 | 0.65 | 0.42 | open | - |
| 2026-10-30 07:53 | favourite | cs2 | Donstu Esports | KUUSAMO.gg | NO KUUSAMO.gg | 1 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-30 07:53 | favourite | cs2 | BakS eSports | GenOne | YES BakS eSports | 10 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-30 01:52 | favourite | cs2 | FlyQuest | NEXVOID | YES FlyQuest | 8 | 0.75 | 0.74 | 0.74 | won | $1.89 |
| 2026-10-30 01:52 | model-only | cs2 | NEXVOID | FlyQuest | NO FlyQuest | 64 | 0.27 | 0.40 | 0.26 | lost | -$18.17 |
| 2026-10-30 01:52 | favourite | cs2 | Alter Ego | Abyssal | NO Abyssal | 7 | 0.89 | 0.89 | 0.89 | won | $0.72 |
| 2026-10-29 18:21 | favourite | cs2 | Diamant Esports | Esport BERG | YES Diamant Esports | 1 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-29 18:06 | favourite | cs2 | Monte | Spirit Academy Black | YES Monte | 8 | 0.81 | 0.80 | 0.80 | won | $1.43 |
| 2026-10-29 18:06 | favourite | cs2 | prodigy | Ducks | NO Ducks | 10 | 0.62 | 0.60 | 0.60 | won | $3.63 |
| 2026-10-29 17:51 | favourite | cs2 | Inner Circle Prospect | Fraternity | NO Fraternity | 9 | 0.68 | 0.66 | 0.66 | lost | -$6.26 |
| 2026-10-29 17:21 | favourite | cs2 | Astralis | Eternal Fire | YES Astralis | 10 | 0.59 | 0.58 | 0.58 | lost | -$6.07 |
| 2026-10-29 16:51 | favourite | dota2 | OG | GamerLegion | NO GamerLegion | 11 | 0.56 | 0.56 | 0.55 | lost | -$6.35 |
| 2026-10-29 16:51 | favourite | cs2 | OldBoys | Hermine Esports Club | YES OldBoys | 1 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-29 16:51 | favourite | cs2 | GamerLegion | HOTU | YES GamerLegion | 1 | 0.54 | 0.52 | 0.52 | lost | -$0.56 |
| 2026-10-29 16:51 | favourite | cs2 | B8 Academy | BANGARANGA | NO BANGARANGA | 1 | 0.60 | 0.60 | 0.60 | won | $0.38 |
| 2026-10-29 16:51 | favourite | cs2 | Team ACES | 9INE | NO 9INE | 11 | 0.54 | 0.50 | 0.50 | lost | -$6.14 |
| 2026-10-29 16:31 | favourite | cs2 | Iberian Soul | TYLOO | NO TYLOO | 1 | 0.57 | 0.54 | 0.54 | won | $0.41 |
| 2026-10-29 15:50 | favourite | cs2 | FURIA | BetBoom Team | NO BetBoom Team | 8 | 0.75 | 0.74 | 0.74 | won | $1.89 |
| 2026-10-29 15:20 | favourite | cs2 | TTG Esports | Winx | YES TTG Esports | 12 | 0.53 | 0.51 | 0.51 | won | $5.43 |

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

