# Esports paper trading (fake money)

Updated 2026-11-01 13:10 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 481 | 40 | 441 | 148 | -$185.56 | -3.8% | -0.4c (474) | $814.44 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 773 | 55 | 718 | 475 | -$369.00 | -7.5% | -1.5c (764) | $631.00 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1610 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5795 | 0.1990 |
| model | 0.6512 | 0.2301 |
| blend | 0.5794 | 0.1991 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1049 | 0.5918 | 0.6594 |
| dota2 | 245 | 0.5413 | 0.6276 |
| ow | 103 | 0.5118 | 0.5284 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 80 | 0.6047 | 0.6734 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-01 12:54 | favourite | cs2 | 100 Thieves | BESTIA Academy | NO BESTIA Academy | 7 | 0.82 | 0.82 | 0.82 | open | - |
| 2026-11-01 12:54 | favourite | cs2 | FOKUS | Acend | NO Acend | 8 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-11-01 12:54 | model-only | cs2 | Acend | FOKUS | YES Acend | 10 | 0.26 | 0.35 | 0.26 | open | - |
| 2026-11-01 11:54 | favourite | dota2 | Team Yandex | Team Spirit | YES Team Yandex | 9 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-11-01 11:54 | model-only | dota2 | Team Spirit | Team Yandex | YES Team Spirit | 40 | 0.35 | 0.41 | 0.34 | open | - |
| 2026-11-01 11:54 | favourite | cs2 | Iberian Soul | WBT Academy | YES Iberian Soul | 8 | 0.77 | 0.77 | 0.77 | open | - |
| 2026-11-01 11:54 | model-only | cs2 | WBT Academy | Iberian Soul | NO Iberian Soul | 64 | 0.24 | 0.45 | 0.23 | open | - |
| 2026-11-01 11:54 | favourite | cs2 | 1WIN | HOTU | YES 1WIN | 11 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-01 10:54 | favourite | dota2 | Xipto Esports | potn9ki | YES Xipto Esports | 7 | 0.79 | 0.78 | 0.78 | open | - |
| 2026-11-01 10:54 | model-only | dota2 | potn9ki | Xipto Esports | YES potn9ki | 71 | 0.23 | 0.35 | 0.22 | open | - |
| 2026-11-01 10:54 | favourite | cs2 | ILLYRIANS | Fortress | NO Fortress | 6 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-11-01 10:54 | model-only | cs2 | Fortress | ILLYRIANS | NO ILLYRIANS | 13 | 0.12 | 0.25 | 0.12 | open | - |
| 2026-11-01 09:54 | favourite | ow | Weibo Gaming | JD Gaming | YES Weibo Gaming | 6 | 0.81 | 0.80 | 0.80 | won | $1.07 |
| 2026-11-01 09:54 | favourite | cs2 | Apogee Esports | Phantom | YES Apogee Esports | 11 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-11-01 09:54 | model-only | cs2 | Phantom | Apogee Esports | YES Phantom | 36 | 0.47 | 0.54 | 0.47 | open | - |
| 2026-11-01 08:54 | favourite | cs2 | JiJieHao | Metizport | NO Metizport | 10 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-11-01 08:54 | model-only | cs2 | Metizport | JiJieHao | NO JiJieHao | 41 | 0.41 | 0.52 | 0.40 | open | - |
| 2026-11-01 08:54 | favourite | ow | T1 | Cheeseburger | NO Cheeseburger | 1 | 0.82 | 0.79 | 0.79 | won | $0.16 |
| 2026-11-01 07:54 | favourite | cs2 | 5star | The Huns Esports | YES 5star | 9 | 0.64 | 0.63 | 0.63 | lost | -$5.91 |
| 2026-11-01 07:54 | model-only | cs2 | gothboiclique | UNiTY esports | YES gothboiclique | 68 | 0.23 | 0.30 | 0.21 | lost | -$16.49 |
| 2026-11-01 07:54 | favourite | cs2 | UNiTY esports | gothboiclique | NO gothboiclique | 7 | 0.79 | 0.79 | 0.79 | won | $1.38 |
| 2026-11-01 07:54 | model-only | cs2 | eternal premium | maybe | NO maybe | 2 | 0.43 | 0.57 | 0.42 | lost | -$0.90 |
| 2026-11-01 07:54 | model-only | cs2 | Saint Sinners | PsychoFace | YES Saint Sinners | 34 | 0.50 | 0.61 | 0.49 | lost | -$17.60 |
| 2026-11-01 07:54 | favourite | cs2 | PsychoFace | Saint Sinners | NO Saint Sinners | 11 | 0.52 | 0.51 | 0.51 | won | $5.08 |
| 2026-11-01 07:54 | favourite | cs2 | maybe | eternal premium | NO eternal premium | 10 | 0.59 | 0.58 | 0.58 | won | $3.93 |

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

