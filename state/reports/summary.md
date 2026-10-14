# Esports paper trading (fake money)

Updated 2026-10-14 10:06 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 159 | 23 | 136 | 35 | -$277.60 | -16.2% | -0.8c (152) | $722.40 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 229 | 29 | 200 | 138 | -$84.39 | -5.7% | -0.9c (221) | $915.61 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

541 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5625 | 0.1908 |
| model | 0.6642 | 0.2355 |
| blend | 0.5609 | 0.1903 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 350 | 0.5777 | 0.6650 |
| dota2 | 65 | 0.5205 | 0.6497 |
| lol | 49 | 0.4974 | 0.7250 |
| ow | 35 | 0.4688 | 0.5468 |
| r6 | 28 | 0.6762 | 0.7223 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-14 09:51 | favourite | cs2 | los kogutos | 6666 | YES los kogutos | 13 | 0.67 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | Team Falcons | NIP | YES Team Falcons | 12 | 0.74 | 0.74 | 0.74 | open | - |
| 2026-10-14 09:51 | model-only | cs2 | NIP | Team Falcons | YES NIP | 52 | 0.26 | 0.41 | 0.26 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | ex-RUSTEC | mellren | YES ex-RUSTEC | 13 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:51 | model-only | cs2 | mellren | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.39 | 0.52 | 0.38 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | BakS eSports | Bushido Wildcats | YES BakS eSports | 15 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-14 09:21 | favourite | cs2 | EAC Extra | Bread Eaters Esports | YES EAC Extra | 14 | 0.62 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:21 | model-only | cs2 | Bread Eaters Esports | EAC Extra | YES Bread Eaters Esports | 33 | 0.38 | 0.44 | 0.38 | open | - |
| 2026-10-14 08:50 | favourite | cs2 | Nuclear TigeRES | LPH Gaming | NO LPH Gaming | 10 | 0.87 | 0.86 | 0.86 | open | - |
| 2026-10-14 08:50 | model-only | cs2 | HOTU | fnatic | NO fnatic | 30 | 0.45 | 0.52 | 0.44 | open | - |
| 2026-10-14 08:50 | favourite | cs2 | fnatic | HOTU | YES fnatic | 15 | 0.56 | 0.56 | 0.56 | open | - |
| 2026-10-14 08:50 | model-only | cs2 | LPH Gaming | Nuclear TigeRES | YES LPH Gaming | 97 | 0.14 | 0.37 | 0.14 | open | - |
| 2026-10-14 08:50 | model-only | cs2 | Sashi Esport | Astralis | YES Sashi Esport | 90 | 0.15 | 0.36 | 0.15 | open | - |
| 2026-10-14 08:50 | favourite | cs2 | Astralis | Sashi Esport | YES Astralis | 10 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-14 08:50 | favourite | dota2 | Team Lynx | Inner Circle | NO Inner Circle | 12 | 0.70 | 0.68 | 0.68 | won | $3.42 |
| 2026-10-14 07:50 | favourite | lol | KT Rolster | BNK FEARX | NO BNK FEARX | 15 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-10-14 07:50 | model-only | lol | BNK FEARX | KT Rolster | NO KT Rolster | 33 | 0.42 | 0.49 | 0.41 | open | - |
| 2026-10-14 07:50 | favourite | dota2 | The Warriors | Shadow Dance | NO Shadow Dance | 10 | 0.85 | 0.83 | 0.83 | open | - |
| 2026-10-14 07:50 | favourite | dota2 | Kalmychata | Nemiga Gaming | YES Kalmychata | 14 | 0.62 | 0.62 | 0.62 | open | - |
| 2026-10-14 07:50 | favourite | cs2 | Rooster | MARKandLARRY | NO MARKandLARRY | 10 | 0.88 | 0.87 | 0.87 | open | - |
| 2026-10-14 07:20 | favourite | cs2 | Aurora Gaming | 9z | NO 9z | 12 | 0.74 | 0.73 | 0.73 | open | - |
| 2026-10-14 07:20 | model-only | cs2 | 9z | Aurora Gaming | YES 9z | 50 | 0.27 | 0.35 | 0.27 | open | - |
| 2026-10-14 06:50 | favourite | cs2 | Lavked | Gothic | NO Gothic | 16 | 0.52 | 0.51 | 0.51 | open | - |
| 2026-10-14 06:50 | model-only | cs2 | B8 Academy | ENJOY | YES B8 Academy | 34 | 0.40 | 0.50 | 0.39 | open | - |
| 2026-10-14 06:50 | favourite | cs2 | ENJOY | B8 Academy | NO B8 Academy | 14 | 0.62 | 0.61 | 0.61 | open | - |

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

