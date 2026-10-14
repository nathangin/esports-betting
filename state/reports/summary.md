# Esports paper trading (fake money)

Updated 2026-10-14 12:21 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 162 | 20 | 142 | 39 | -$235.16 | -13.2% | -0.8c (155) | $764.84 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 236 | 29 | 207 | 141 | -$112.34 | -7.3% | -1.0c (228) | $887.66 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

549 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5638 | 0.1916 |
| model | 0.6643 | 0.2357 |
| blend | 0.5624 | 0.1911 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 355 | 0.5800 | 0.6659 |
| dota2 | 67 | 0.5272 | 0.6552 |
| lol | 49 | 0.4974 | 0.7250 |
| ow | 36 | 0.4575 | 0.5342 |
| r6 | 28 | 0.6762 | 0.7223 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-14 12:21 | favourite | cs2 | Legacy | PARIVISION | YES Legacy | 2 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-14 11:51 | favourite | dota2 | Dawn Bulls | salamit | YES Dawn Bulls | 13 | 0.66 | 0.66 | 0.66 | open | - |
| 2026-10-14 11:51 | model-only | dota2 | salamit | Dawn Bulls | YES salamit | 11 | 0.35 | 0.42 | 0.34 | open | - |
| 2026-10-14 11:51 | favourite | cs2 | Blitzkrieg | realgotis22 | YES Blitzkrieg | 16 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-14 11:51 | model-only | cs2 | realgotis22 | Blitzkrieg | NO Blitzkrieg | 1 | 0.47 | 0.60 | 0.47 | open | - |
| 2026-10-14 11:51 | favourite | cs2 | 6yuBoJlbl | HyperSpirit | YES 6yuBoJlbl | 12 | 0.69 | 0.68 | 0.68 | open | - |
| 2026-10-14 11:51 | model-only | cs2 | HyperSpirit | 6yuBoJlbl | NO 6yuBoJlbl | 1 | 0.32 | 0.48 | 0.32 | open | - |
| 2026-10-14 11:51 | favourite | cs2 | Lynn Vision | Alter Ego | YES Lynn Vision | 12 | 0.71 | 0.70 | 0.71 | open | - |
| 2026-10-14 10:51 | favourite | ow | ENTER FORCE.36 | 99DIVINE | YES ENTER FORCE.36 | 15 | 0.57 | 0.54 | 0.54 | open | - |
| 2026-10-14 10:51 | favourite | dota2 | Team Resilience | Yakult's Brothers | NO Yakult's Brothers | 15 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | los kogutos | 6666 | YES los kogutos | 13 | 0.67 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | Team Falcons | NIP | YES Team Falcons | 12 | 0.74 | 0.74 | 0.74 | open | - |
| 2026-10-14 09:51 | model-only | cs2 | NIP | Team Falcons | YES NIP | 52 | 0.26 | 0.41 | 0.26 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | ex-RUSTEC | mellren | YES ex-RUSTEC | 13 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:51 | model-only | cs2 | mellren | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.39 | 0.52 | 0.38 | open | - |
| 2026-10-14 09:51 | favourite | cs2 | BakS eSports | Bushido Wildcats | YES BakS eSports | 15 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-10-14 09:21 | favourite | cs2 | EAC Extra | Bread Eaters Esports | YES EAC Extra | 14 | 0.62 | 0.62 | 0.62 | open | - |
| 2026-10-14 09:21 | model-only | cs2 | Bread Eaters Esports | EAC Extra | YES Bread Eaters Esports | 33 | 0.38 | 0.44 | 0.38 | open | - |
| 2026-10-14 08:50 | favourite | cs2 | Nuclear TigeRES | LPH Gaming | NO LPH Gaming | 10 | 0.87 | 0.86 | 0.86 | open | - |
| 2026-10-14 08:50 | model-only | cs2 | HOTU | fnatic | NO fnatic | 30 | 0.45 | 0.52 | 0.44 | won | $15.98 |
| 2026-10-14 08:50 | favourite | cs2 | fnatic | HOTU | YES fnatic | 15 | 0.56 | 0.56 | 0.56 | lost | -$8.66 |
| 2026-10-14 08:50 | model-only | cs2 | LPH Gaming | Nuclear TigeRES | YES LPH Gaming | 97 | 0.14 | 0.37 | 0.14 | open | - |
| 2026-10-14 08:50 | model-only | cs2 | Sashi Esport | Astralis | YES Sashi Esport | 90 | 0.15 | 0.36 | 0.15 | lost | -$14.31 |
| 2026-10-14 08:50 | favourite | cs2 | Astralis | Sashi Esport | YES Astralis | 10 | 0.86 | 0.85 | 0.85 | won | $1.31 |
| 2026-10-14 08:50 | favourite | dota2 | Team Lynx | Inner Circle | NO Inner Circle | 12 | 0.70 | 0.68 | 0.68 | won | $3.42 |

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

