# Esports paper trading (fake money)

Updated 2026-10-13 03:36 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 131 | 9 | 122 | 32 | -$197.22 | -12.8% | -0.7c (128) | $802.78 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 178 | 10 | 168 | 115 | -$97.18 | -7.8% | -0.9c (176) | $902.82 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

487 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5718 | 0.1947 |
| model | 0.6663 | 0.2364 |
| blend | 0.5712 | 0.1944 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 326 | 0.5832 | 0.6627 |
| dota2 | 46 | 0.5434 | 0.6562 |
| lol | 45 | 0.5018 | 0.7255 |
| ow | 31 | 0.5130 | 0.5872 |
| r6 | 25 | 0.6521 | 0.7187 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-13 02:50 | favourite | dota2 | Team Resilience | Imperial Power | NO Imperial Power | 9 | 0.90 | 0.88 | 0.88 | open | - |
| 2026-10-12 21:54 | favourite | lol | Disguised | Maryville University | NO Maryville University | 3 | 0.59 | 0.59 | 0.59 | won | $1.17 |
| 2026-10-12 19:14 | favourite | cs2 | Galorys | Bounty Hunters Esports | NO Bounty Hunters Esports | 7 | 0.67 | 0.67 | 0.67 | won | $2.20 |
| 2026-10-12 19:14 | favourite | lol | G2 HEL | AZ Rising Eterna | NO AZ Rising Eterna | 15 | 0.57 | 0.55 | 0.55 | won | $6.19 |
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
| 2026-10-11 12:52 | model-only | cs2 | mellren | Bebop | YES mellren | 23 | 0.62 | 0.71 | 0.61 | won | $8.36 |
| 2026-10-11 12:52 | model-only | cs2 | aimclub | ARGOS | YES aimclub | 30 | 0.47 | 0.54 | 0.47 | won | $15.37 |
| 2026-10-11 12:52 | model-only | cs2 | MASONIC | Aurora Young Blood | NO Aurora Young Blood | 33 | 0.43 | 0.55 | 0.42 | lost | -$14.76 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy | 9INE | YES Spirit Academy | 34 | 0.41 | 0.65 | 0.41 | won | $19.48 |
| 2026-10-11 12:52 | model-only | cs2 | Spirit Academy Black | Metizport | NO Metizport | 9 | 0.20 | 0.36 | 0.18 | lost | -$1.91 |
| 2026-10-11 11:52 | model-only | cs2 | The KnockoutX | Alter Ego | YES The KnockoutX | 22 | 0.24 | 0.40 | 0.23 | lost | -$5.57 |
| 2026-10-11 10:22 | favourite | cs2 | Spirit | Aurora Gaming | NO Aurora Gaming | 1 | 0.68 | 0.68 | 0.68 | lost | -$0.70 |
| 2026-10-11 09:52 | model-only | cs2 | Fire Flux Esports | Gothic | NO Gothic | 27 | 0.53 | 0.60 | 0.52 | won | $12.21 |

## Backtest on real Kalshi prices

7979 settled matches from 2026-05-28 to 2026-10-12, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $439.42 | -$30.42 | -6.9% | -43.8% to +40.9% | 54% | -0.0c | 10% |
| model only | 1968 | $8,857.80 | -$985.80 | -11.1% | -19.2% to -3.2% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 3824 | $15,776.22 | -$733.22 | -4.6% | -7.0% to -2.2% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3731 | $8,550.73 | -$978.73 | -11.4% | -17.1% to -5.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7754 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5731 | 0.1959 | 69.2% |
| model | 0.6615 | 0.2347 | 59.5% |
| blend | 0.5727 | 0.1958 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1281 | 0.525 | 0.522 |
| (0.55, 0.6] | 1311 | 0.577 | 0.548 |
| (0.6, 0.65] | 1192 | 0.626 | 0.638 |
| (0.65, 0.7] | 1041 | 0.676 | 0.701 |
| (0.7, 0.75] | 880 | 0.726 | 0.773 |
| (0.75, 0.8] | 755 | 0.776 | 0.812 |
| (0.8, 0.85] | 636 | 0.826 | 0.824 |
| (0.85, 0.9] | 478 | 0.877 | 0.902 |
| (0.9, 1.0] | 405 | 0.932 | 0.956 |

