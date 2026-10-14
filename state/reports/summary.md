# Esports paper trading (fake money)

Updated 2026-10-14 22:42 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 165 | 13 | 152 | 41 | -$261.56 | -14.0% | -0.7c (162) | $738.44 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 236 | 14 | 222 | 152 | -$108.67 | -6.6% | -1.0c (234) | $891.33 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

594 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5611 | 0.1902 |
| model | 0.6607 | 0.2339 |
| blend | 0.5593 | 0.1896 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 383 | 0.5719 | 0.6633 |
| dota2 | 78 | 0.5396 | 0.6437 |
| lol | 51 | 0.4986 | 0.7236 |
| ow | 38 | 0.4673 | 0.5439 |
| r6 | 28 | 0.6762 | 0.7223 |
| valorant | 16 | 0.6269 | 0.6492 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-14 12:51 | model-only | cs2 | Ryvex | WRAITH PCIFIC | YES Ryvex | 63 | 0.18 | 0.39 | 0.17 | lost | -$12.00 |
| 2026-10-14 12:51 | model-only | cs2 | Just_Players | FOKUS | NO FOKUS | 2 | 0.24 | 0.44 | 0.23 | lost | -$0.51 |
| 2026-10-14 12:51 | model-only | cs2 | FORZE Reload | 33 | YES FORZE Reload | 29 | 0.50 | 0.57 | 0.48 | won | $13.99 |
| 2026-10-14 12:21 | favourite | cs2 | Legacy | PARIVISION | YES Legacy | 2 | 0.58 | 0.58 | 0.58 | won | $0.80 |
| 2026-10-14 11:51 | favourite | dota2 | Dawn Bulls | salamit | YES Dawn Bulls | 13 | 0.66 | 0.66 | 0.66 | won | $4.21 |
| 2026-10-14 11:51 | model-only | dota2 | salamit | Dawn Bulls | YES salamit | 11 | 0.35 | 0.42 | 0.34 | lost | -$4.03 |
| 2026-10-14 11:51 | favourite | cs2 | Blitzkrieg | realgotis22 | YES Blitzkrieg | 16 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-10-14 11:51 | model-only | cs2 | realgotis22 | Blitzkrieg | NO Blitzkrieg | 1 | 0.47 | 0.60 | 0.47 | open | - |
| 2026-10-14 11:51 | favourite | cs2 | 6yuBoJlbl | HyperSpirit | YES 6yuBoJlbl | 12 | 0.69 | 0.68 | 0.68 | won | $3.54 |
| 2026-10-14 11:51 | model-only | cs2 | HyperSpirit | 6yuBoJlbl | NO 6yuBoJlbl | 1 | 0.32 | 0.48 | 0.32 | lost | -$0.34 |
| 2026-10-14 11:51 | favourite | cs2 | Lynn Vision | Alter Ego | YES Lynn Vision | 12 | 0.71 | 0.70 | 0.71 | won | $3.30 |
| 2026-10-14 10:51 | favourite | dota2 | Team Resilience | Yakult's Brothers | NO Yakult's Brothers | 15 | 0.59 | 0.59 | 0.59 | won | $5.89 |
| 2026-10-14 10:51 | favourite | ow | ENTER FORCE.36 | 99DIVINE | YES ENTER FORCE.36 | 15 | 0.57 | 0.54 | 0.54 | lost | -$8.81 |
| 2026-10-14 09:51 | favourite | cs2 | los kogutos | 6666 | YES los kogutos | 13 | 0.67 | 0.62 | 0.62 | lost | -$8.92 |
| 2026-10-14 09:51 | favourite | cs2 | Team Falcons | NIP | YES Team Falcons | 12 | 0.74 | 0.74 | 0.74 | won | $2.95 |
| 2026-10-14 09:51 | model-only | cs2 | NIP | Team Falcons | YES NIP | 52 | 0.26 | 0.41 | 0.26 | lost | -$14.23 |
| 2026-10-14 09:51 | favourite | cs2 | ex-RUSTEC | mellren | YES ex-RUSTEC | 13 | 0.64 | 0.62 | 0.62 | won | $4.47 |
| 2026-10-14 09:51 | model-only | cs2 | mellren | ex-RUSTEC | NO ex-RUSTEC | 1 | 0.39 | 0.52 | 0.38 | lost | -$0.41 |
| 2026-10-14 09:51 | favourite | cs2 | BakS eSports | Bushido Wildcats | YES BakS eSports | 15 | 0.58 | 0.57 | 0.57 | won | $6.04 |
| 2026-10-14 09:21 | favourite | cs2 | EAC Extra | Bread Eaters Esports | YES EAC Extra | 14 | 0.62 | 0.62 | 0.62 | lost | -$8.92 |
| 2026-10-14 09:21 | model-only | cs2 | Bread Eaters Esports | EAC Extra | YES Bread Eaters Esports | 33 | 0.38 | 0.44 | 0.38 | won | $19.91 |
| 2026-10-14 08:50 | favourite | cs2 | Nuclear TigeRES | LPH Gaming | NO LPH Gaming | 10 | 0.87 | 0.86 | 0.86 | won | $1.22 |
| 2026-10-14 08:50 | model-only | cs2 | HOTU | fnatic | NO fnatic | 30 | 0.45 | 0.52 | 0.44 | won | $15.98 |
| 2026-10-14 08:50 | favourite | cs2 | fnatic | HOTU | YES fnatic | 15 | 0.56 | 0.56 | 0.56 | lost | -$8.66 |
| 2026-10-14 08:50 | model-only | cs2 | LPH Gaming | Nuclear TigeRES | YES LPH Gaming | 97 | 0.14 | 0.37 | 0.14 | lost | -$14.40 |

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

