# Esports paper trading (fake money)

Updated 2026-10-13 09:56 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 138 | 16 | 122 | 32 | -$197.22 | -12.8% | -0.8c (134) | $802.78 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 191 | 22 | 169 | 116 | -$96.34 | -7.7% | -0.9c (188) | $903.66 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

489 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5700 | 0.1939 |
| model | 0.6663 | 0.2364 |
| blend | 0.5693 | 0.1937 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 326 | 0.5832 | 0.6627 |
| dota2 | 48 | 0.5259 | 0.6565 |
| lol | 45 | 0.5018 | 0.7255 |
| ow | 31 | 0.5130 | 0.5872 |
| r6 | 25 | 0.6521 | 0.7187 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-13 09:51 | favourite | cs2 | Bushido Wildcats | ILLYRIANS | YES Bushido Wildcats | 14 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-13 09:21 | favourite | cs2 | Vitality Academy | RoundsGG | YES Vitality Academy | 16 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-13 09:21 | model-only | cs2 | Vitality Academy | RoundsGG | YES Vitality Academy | 28 | 0.54 | 0.66 | 0.53 | open | - |
| 2026-10-13 08:51 | favourite | cs2 | 100 Thieves | JiJieHao | YES 100 Thieves | 13 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-13 08:51 | model-only | cs2 | JiJieHao | 100 Thieves | NO 100 Thieves | 1 | 0.34 | 0.45 | 0.34 | open | - |
| 2026-10-13 08:51 | favourite | cs2 | Liquid | BBL | NO BBL | 12 | 0.71 | 0.70 | 0.71 | open | - |
| 2026-10-13 08:51 | model-only | cs2 | BBL | Liquid | YES BBL | 51 | 0.30 | 0.46 | 0.29 | open | - |
| 2026-10-13 07:51 | favourite | dota2 | HULIGANI | Nemiga Gaming | YES HULIGANI | 15 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-13 07:51 | model-only | dota2 | Kalmychata | Yellow Submarine | YES Kalmychata | 58 | 0.26 | 0.43 | 0.26 | open | - |
| 2026-10-13 07:51 | favourite | dota2 | Yellow Submarine | Kalmychata | NO Kalmychata | 11 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-10-13 07:51 | model-only | lol | LGD Gaming | OKSavingsBank BRION | NO OKSavingsBank BRION | 28 | 0.54 | 0.65 | 0.54 | open | - |
| 2026-10-13 07:51 | favourite | lol | LGD Gaming | OKSavingsBank BRION | NO OKSavingsBank BRION | 16 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-10-13 06:51 | model-only | cs2 | WRAITH PCIFIC | STATE | NO STATE | 38 | 0.38 | 0.44 | 0.36 | open | - |
| 2026-10-13 06:51 | favourite | dota2 | Cloud Rising | Cloud Dawning | NO Cloud Dawning | 10 | 0.83 | 0.80 | 0.80 | open | - |
| 2026-10-13 06:51 | favourite | cs2 | Copenhagen Wolves | VP.Future 3 | YES Copenhagen Wolves | 3 | 0.77 | 0.77 | 0.77 | open | - |
| 2026-10-13 06:51 | favourite | cs2 | BakS eSports | Spirit Academy | YES BakS eSports | 15 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-10-13 06:51 | model-only | cs2 | Spirit Academy | BakS eSports | YES Spirit Academy | 34 | 0.45 | 0.60 | 0.45 | open | - |
| 2026-10-13 06:51 | favourite | cs2 | STATE | WRAITH PCIFIC | YES STATE | 13 | 0.65 | 0.64 | 0.64 | open | - |
| 2026-10-13 05:50 | favourite | dota2 | Team Lynx | Zero Tenacity | YES Team Lynx | 14 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-10-13 04:50 | favourite | lol | Team WE | FlyQuest | NO FlyQuest | 10 | 0.81 | 0.81 | 0.80 | open | - |
| 2026-10-13 02:50 | favourite | dota2 | Team Resilience | Imperial Power | NO Imperial Power | 9 | 0.90 | 0.88 | 0.88 | won | $0.84 |
| 2026-10-12 21:54 | favourite | lol | Disguised | Maryville University | NO Maryville University | 3 | 0.59 | 0.59 | 0.59 | won | $1.17 |
| 2026-10-12 19:14 | favourite | cs2 | Galorys | Bounty Hunters Esports | NO Bounty Hunters Esports | 7 | 0.67 | 0.67 | 0.67 | won | $2.20 |
| 2026-10-12 19:14 | favourite | lol | G2 HEL | AZ Rising Eterna | NO AZ Rising Eterna | 15 | 0.57 | 0.55 | 0.55 | won | $6.19 |
| 2026-10-12 09:20 | model-only | cs2 | Sokerorg | MOUZ NXT | YES Sokerorg | 30 | 0.52 | 0.60 | 0.52 | open | - |

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

