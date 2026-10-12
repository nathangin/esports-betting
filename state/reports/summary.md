# Esports paper trading (fake money)

Updated 2026-10-12 19:20 UTC. Model fitted 2026-10-05T18:34. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | -2.3c (18) | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 131 | 9 | 122 | 32 | -$197.22 | -12.8% | -0.4c (140) | $802.78 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 176 | 11 | 165 | 112 | -$106.74 | -8.7% | -2.0c (241) | $893.26 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

474 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5755 | 0.1962 |
| model | 0.6643 | 0.2356 |
| blend | 0.5754 | 0.1961 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 320 | 0.5863 | 0.6633 |
| dota2 | 43 | 0.5590 | 0.6519 |
| lol | 42 | 0.5098 | 0.7096 |
| ow | 31 | 0.5130 | 0.5872 |
| r6 | 24 | 0.6373 | 0.7153 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-12 19:14 | favourite | cs2 | Galorys | Bounty Hunters Esports | NO Bounty Hunters Esports | 7 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-10-12 19:14 | favourite | lol | G2 HEL | AZ Rising Eterna | NO AZ Rising Eterna | 15 | 0.57 | 0.55 | 0.55 | open | - |
| 2026-10-12 09:20 | model-only | cs2 | Sokerorg | MOUZ NXT | YES Sokerorg | 30 | 0.52 | 0.60 | 0.52 | open | - |
| 2026-10-12 08:50 | model-only | cs2 | Sangal | Inner Circle Esports | NO Inner Circle Esports | 47 | 0.34 | 0.51 | 0.33 | lost | -$16.72 |
| 2026-10-12 08:50 | model-only | cs2 | Apogee Esports | NIP | NO NIP | 2 | 0.22 | 0.38 | 0.22 | lost | -$0.47 |
| 2026-10-12 07:50 | model-only | lol | KT Rolster | Team Vitality | YES KT Rolster | 36 | 0.36 | 0.42 | 0.36 | won | $22.45 |
| 2026-10-12 06:54 | model-only | cs2 | STATE | THE UNIT | YES STATE | 22 | 0.47 | 0.65 | 0.45 | open | - |
| 2026-10-12 06:54 | favourite | cs2 | Bread Eaters Esports | Passion Academy | YES Bread Eaters Esports | 2 | 0.59 | 0.57 | 0.57 | won | $0.78 |
| 2026-10-12 05:54 | favourite | dota2 | Yellow Submarine | Nemiga Gaming | NO Nemiga Gaming | 9 | 0.86 | 0.85 | 0.85 | won | $1.18 |
| 2026-10-12 05:54 | model-only | dota2 | Nemiga Gaming | Yellow Submarine | NO Yellow Submarine | 99 | 0.16 | 0.24 | 0.15 | lost | -$16.78 |
| 2026-10-12 04:54 | favourite | lol | BNK FEARX | JD Gaming | YES BNK FEARX | 11 | 0.68 | 0.68 | 0.68 | won | $3.35 |
| 2026-10-12 04:54 | model-only | lol | JD Gaming | BNK FEARX | NO BNK FEARX | 48 | 0.33 | 0.50 | 0.32 | lost | -$16.59 |
| 2026-10-11 15:53 | model-only | cs2 | antidaun | Saint Sinners | YES antidaun | 8 | 0.19 | 0.43 | 0.18 | lost | -$1.61 |
| 2026-10-11 14:52 | model-only | r6 | Fluxo W7M | Team Liquid | YES Fluxo W7M | 45 | 0.36 | 0.44 | 0.35 | lost | -$16.93 |
| 2026-10-11 13:52 | model-only | cs2 | MOUZ | Vitality | YES MOUZ | 42 | 0.35 | 0.44 | 0.34 | lost | -$15.37 |
| 2026-10-11 12:52 | model-only | cs2 | MASONIC | Aurora Young Blood | NO Aurora Young Blood | 33 | 0.43 | 0.55 | 0.42 | lost | -$14.76 |
| 2026-10-11 12:52 | model-only | cs2 | aimclub | ARGOS | YES aimclub | 30 | 0.47 | 0.54 | 0.47 | won | $15.37 |
| 2026-10-11 12:52 | model-only | cs2 | mellren | Bebop | YES mellren | 23 | 0.62 | 0.71 | 0.61 | won | $8.36 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy Black | Metizport | NO Metizport | 9 | 0.20 | 0.36 | 0.18 | lost | -$1.91 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy | 9INE | YES Spirit Academy | 34 | 0.41 | 0.65 | 0.41 | won | $19.48 |
| 2026-10-11 11:52 | model-only | cs2 | The KnockoutX | Alter Ego | YES The KnockoutX | 22 | 0.24 | 0.40 | 0.23 | lost | -$5.57 |
| 2026-10-11 10:22 | favourite | cs2 | Spirit | Aurora Gaming | NO Aurora Gaming | 1 | 0.68 | 0.68 | 0.68 | lost | -$0.70 |
| 2026-10-11 09:52 | model-only | cs2 | Fire Flux Esports | Gothic | NO Gothic | 27 | 0.53 | 0.60 | 0.52 | won | $12.21 |
| 2026-10-11 09:21 | model-only | cs2 | TheChampionGG | VP.Future 3 | YES TheChampionGG | 37 | 0.39 | 0.45 | 0.39 | lost | -$15.05 |
| 2026-10-11 09:21 | favourite | cs2 | Teletubisie | THE UNIT | YES Teletubisie | 9 | 0.88 | 0.87 | 0.87 | lost | -$7.99 |

## Backtest on real Kalshi prices

7529 settled matches from 2026-05-28 to 2026-10-05, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 1878 | $9,311.87 | -$978.87 | -10.5% | -19.1% to -2.2% | 34% | -0.6c | 98% |
| always the favourite (1% flat) | 3613 | $15,734.92 | -$707.92 | -4.5% | -6.9% to -2.0% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3616 | $8,324.33 | -$978.33 | -11.8% | -17.4% to -5.9% | 32% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7304 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5732 | 0.1960 | 69.2% |
| model | 0.6611 | 0.2345 | 59.4% |
| blend | 0.5729 | 0.1959 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1200 | 0.525 | 0.521 |
| (0.55, 0.6] | 1249 | 0.577 | 0.553 |
| (0.6, 0.65] | 1130 | 0.626 | 0.634 |
| (0.65, 0.7] | 988 | 0.676 | 0.701 |
| (0.7, 0.75] | 838 | 0.726 | 0.773 |
| (0.75, 0.8] | 706 | 0.776 | 0.809 |
| (0.8, 0.85] | 594 | 0.826 | 0.825 |
| (0.85, 0.9] | 443 | 0.877 | 0.905 |
| (0.9, 1.0] | 381 | 0.932 | 0.958 |

