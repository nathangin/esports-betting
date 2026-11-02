# Esports paper trading (fake money)

Updated 2026-11-02 05:21 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 486 | 33 | 453 | 154 | -$44.56 | -0.9% | -0.4c (480) | $955.44 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 785 | 48 | 737 | 486 | -$386.58 | -7.7% | -1.4c (778) | $613.42 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1641 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5811 | 0.1998 |
| model | 0.6517 | 0.2303 |
| blend | 0.5812 | 0.1999 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1073 | 0.5928 | 0.6598 |
| dota2 | 248 | 0.5466 | 0.6295 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-02 03:21 | favourite | cs2 | Aurora Gaming | Liquid | YES Aurora Gaming | 8 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-11-02 03:21 | favourite | cs2 | G2 | PARIVISION | YES G2 | 10 | 0.55 | 0.55 | 0.55 | open | - |
| 2026-11-02 00:51 | favourite | cs2 | Legacy | TheMongolz | YES Legacy | 11 | 0.51 | 0.51 | 0.51 | lost | -$5.81 |
| 2026-11-02 00:51 | favourite | cs2 | Heroic | B8 | NO B8 | 9 | 0.62 | 0.61 | 0.61 | won | $3.27 |
| 2026-11-01 18:50 | favourite | cs2 | DENDELE CS | Imperial | NO Imperial | 5 | 0.58 | 0.58 | 0.58 | won | $2.01 |
| 2026-11-01 17:50 | favourite | cs2 | Metizport | WBT Academy | YES Metizport | 9 | 0.67 | 0.66 | 0.66 | lost | -$6.17 |
| 2026-11-01 17:50 | model-only | cs2 | WBT Academy | Metizport | NO Metizport | 2 | 0.35 | 0.41 | 0.34 | won | $1.26 |
| 2026-11-01 16:50 | favourite | ow | Twisted Minds | 1234 | YES Twisted Minds | 5 | 0.89 | 0.86 | 0.86 | won | $0.51 |
| 2026-11-01 16:50 | model-only | ow | 1234 | Twisted Minds | YES 1234 | 17 | 0.16 | 0.24 | 0.14 | lost | -$2.88 |
| 2026-11-01 16:50 | model-only | valorant | KRÜ Blaze | Gentle Mates GC | YES KRÜ Blaze | 50 | 0.35 | 0.44 | 0.35 | won | $31.70 |
| 2026-11-01 16:50 | favourite | valorant | Gentle Mates GC | KRÜ Blaze | NO KRÜ Blaze | 9 | 0.66 | 0.65 | 0.65 | lost | -$6.09 |
| 2026-11-01 15:50 | favourite | cs2 | Wildcard | BARCA | NO BARCA | 9 | 0.62 | 0.61 | 0.61 | won | $3.27 |
| 2026-11-01 15:20 | favourite | cs2 | prodigy | Ducks | NO Ducks | 11 | 0.54 | 0.50 | 0.50 | won | $4.86 |
| 2026-11-01 13:54 | favourite | cs2 | Misa Esports | Donstu Esports | YES Misa Esports | 10 | 0.59 | 0.58 | 0.58 | lost | -$6.07 |
| 2026-11-01 13:54 | model-only | cs2 | Misa Esports | Donstu Esports | YES Misa Esports | 27 | 0.59 | 0.64 | 0.58 | lost | -$16.39 |
| 2026-11-01 13:54 | favourite | cs2 | Low Cortisol | naocopulas | NO naocopulas | 9 | 0.62 | 0.62 | 0.62 | won | $3.27 |
| 2026-11-01 13:54 | model-only | cs2 | naocopulas | Low Cortisol | NO Low Cortisol | 3 | 0.38 | 0.62 | 0.38 | lost | -$1.19 |
| 2026-11-01 12:54 | favourite | cs2 | FOKUS | Acend | NO Acend | 8 | 0.75 | 0.74 | 0.74 | won | $1.89 |
| 2026-11-01 12:54 | model-only | cs2 | Acend | FOKUS | YES Acend | 10 | 0.26 | 0.35 | 0.26 | lost | -$2.74 |
| 2026-11-01 12:54 | favourite | cs2 | 100 Thieves | BESTIA Academy | NO BESTIA Academy | 7 | 0.82 | 0.82 | 0.82 | won | $1.18 |
| 2026-11-01 11:54 | favourite | dota2 | Team Yandex | Team Spirit | YES Team Yandex | 9 | 0.66 | 0.66 | 0.66 | lost | -$6.09 |
| 2026-11-01 11:54 | model-only | dota2 | Team Spirit | Team Yandex | YES Team Spirit | 40 | 0.35 | 0.41 | 0.34 | won | $25.36 |
| 2026-11-01 11:54 | favourite | cs2 | Iberian Soul | WBT Academy | YES Iberian Soul | 8 | 0.77 | 0.77 | 0.77 | lost | -$6.26 |
| 2026-11-01 11:54 | model-only | cs2 | WBT Academy | Iberian Soul | NO Iberian Soul | 64 | 0.24 | 0.45 | 0.23 | won | $47.82 |
| 2026-11-01 11:54 | favourite | cs2 | 1WIN | HOTU | YES 1WIN | 11 | 0.54 | 0.54 | 0.54 | won | $4.86 |

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

