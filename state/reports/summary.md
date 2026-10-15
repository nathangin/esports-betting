# Esports paper trading (fake money)

Updated 2026-10-15 11:43 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 181 | 23 | 158 | 43 | -$204.13 | -10.7% | -0.6c (175) | $795.87 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 256 | 24 | 232 | 160 | -$104.42 | -6.1% | -1.1c (251) | $895.58 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

615 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5665 | 0.1925 |
| model | 0.6606 | 0.2339 |
| blend | 0.5654 | 0.1921 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 393 | 0.5725 | 0.6615 |
| dota2 | 88 | 0.5774 | 0.6514 |
| lol | 51 | 0.4986 | 0.7236 |
| ow | 38 | 0.4673 | 0.5439 |
| r6 | 28 | 0.6762 | 0.7223 |
| valorant | 17 | 0.6143 | 0.6568 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-15 10:22 | model-only | dota2 | PuckChamp | Zero Tenacity | YES PuckChamp | 127 | 0.11 | 0.34 | 0.11 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | Johnny Speeds | Bushido Wildcats | YES Johnny Speeds | 1 | 0.59 | 0.56 | 0.55 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | WBT Academy | ENCE | NO ENCE | 1 | 0.61 | 0.60 | 0.60 | open | - |
| 2026-10-15 10:22 | model-only | cs2 | ENCE | WBT Academy | YES ENCE | 17 | 0.40 | 0.48 | 0.40 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | maybe | Ryvex | YES maybe | 1 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-10-15 10:22 | model-only | cs2 | Ryvex | maybe | YES Ryvex | 30 | 0.47 | 0.54 | 0.46 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | ex-Zero Tenacity | Just_Players | YES ex-Zero Tenacity | 13 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-10-15 10:22 | model-only | cs2 | Just_Players | ex-Zero Tenacity | YES Just_Players | 12 | 0.34 | 0.40 | 0.33 | open | - |
| 2026-10-15 10:22 | favourite | cs2 | Team Falcons | 9z | NO 9z | 11 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-10-15 10:22 | model-only | cs2 | 9z | Team Falcons | NO Team Falcons | 56 | 0.25 | 0.34 | 0.24 | open | - |
| 2026-10-15 07:54 | favourite | lol | OKSavingsBank BRION | Team WE | YES OKSavingsBank BRION | 15 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-10-15 07:54 | model-only | lol | Team WE | OKSavingsBank BRION | NO OKSavingsBank BRION | 32 | 0.44 | 0.59 | 0.43 | open | - |
| 2026-10-15 07:24 | favourite | cs2 | Aurora Gaming | NIP | YES Aurora Gaming | 12 | 0.72 | 0.71 | 0.71 | won | $3.19 |
| 2026-10-15 07:24 | model-only | cs2 | NIP | Aurora Gaming | NO Aurora Gaming | 1 | 0.30 | 0.43 | 0.29 | lost | -$0.32 |
| 2026-10-15 06:53 | favourite | dota2 | Yangon Galacticos | Ivory | YES Yangon Galacticos | 10 | 0.84 | 0.83 | 0.83 | won | $1.50 |
| 2026-10-15 06:53 | model-only | dota2 | Ivory | Yangon Galacticos | NO Yangon Galacticos | 1 | 0.18 | 0.37 | 0.17 | lost | -$0.20 |
| 2026-10-15 06:53 | favourite | dota2 | Xipto Esports | InterActive Philippines | NO InterActive Philippines | 10 | 0.81 | 0.80 | 0.80 | lost | -$8.21 |
| 2026-10-15 06:53 | model-only | dota2 | InterActive Philippines | Xipto Esports | NO Xipto Esports | 66 | 0.21 | 0.38 | 0.20 | won | $51.37 |
| 2026-10-15 06:53 | favourite | cs2 | Vitality Academy | VP.Future 3 | YES Vitality Academy | 14 | 0.59 | 0.57 | 0.57 | open | - |
| 2026-10-15 06:53 | model-only | cs2 | VP.Future 3 | Vitality Academy | YES VP.Future 3 | 32 | 0.44 | 0.51 | 0.43 | open | - |
| 2026-10-15 06:53 | favourite | cs2 | 6666 | Bushido Wildcats | YES 6666 | 14 | 0.62 | 0.60 | 0.60 | won | $5.08 |
| 2026-10-15 06:53 | favourite | cs2 | Brute | mellren | YES Brute | 13 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-10-15 06:53 | model-only | cs2 | mellren | Brute | YES mellren | 2 | 0.38 | 0.55 | 0.38 | open | - |
| 2026-10-15 06:53 | favourite | cs2 | WBT Academy | Esport Academy Copenhagen | NO Esport Academy Copenhagen | 14 | 0.58 | 0.56 | 0.56 | won | $5.64 |
| 2026-10-15 05:53 | favourite | dota2 | salamit | Spirit Academy | YES salamit | 12 | 0.72 | 0.70 | 0.70 | lost | -$8.81 |

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

