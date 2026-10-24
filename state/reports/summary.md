# Esports paper trading (fake money)

Updated 2026-10-24 09:04 UTC. Model fitted 2026-10-19T16:33. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 336 | 33 | 303 | 91 | -$369.71 | -11.7% | -0.9c (330) | $630.29 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 524 | 47 | 477 | 327 | -$162.63 | -4.6% | -1.4c (518) | $837.37 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1139 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5716 | 0.1953 |
| model | 0.6568 | 0.2326 |
| blend | 0.5703 | 0.1949 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 745 | 0.5861 | 0.6630 |
| dota2 | 174 | 0.5504 | 0.6482 |
| lol | 68 | 0.5539 | 0.7164 |
| ow | 64 | 0.4642 | 0.5092 |
| valorant | 48 | 0.5544 | 0.6714 |
| r6 | 40 | 0.6166 | 0.6957 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-24 08:54 | favourite | cs2 | MOUZ | Liquid | YES MOUZ | 9 | 0.85 | 0.85 | 0.85 | open | - |
| 2026-10-24 08:54 | model-only | cs2 | Liquid | MOUZ | YES Liquid | 80 | 0.15 | 0.32 | 0.15 | open | - |
| 2026-10-24 08:54 | favourite | cs2 | Spirit | BetBoom Team | YES Spirit | 10 | 0.79 | 0.79 | 0.79 | open | - |
| 2026-10-24 08:54 | model-only | cs2 | BetBoom Team | Spirit | YES BetBoom Team | 58 | 0.21 | 0.34 | 0.21 | open | - |
| 2026-10-24 07:54 | favourite | valorant | Nova Esports | KeepBest Gaming | NO KeepBest Gaming | 11 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-24 07:54 | favourite | r6 | CAG by VARREL | SCARZ | NO SCARZ | 12 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-10-24 07:54 | model-only | r6 | SCARZ | CAG by VARREL | NO CAG by VARREL | 20 | 0.33 | 0.44 | 0.32 | open | - |
| 2026-10-24 07:54 | favourite | ow | SEIJI ESPORTS | Poker Face | NO Poker Face | 1 | 0.63 | 0.59 | 0.59 | open | - |
| 2026-10-24 07:54 | favourite | dota2 | Team Lynx | Nemiga Gaming | YES Team Lynx | 3 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-10-24 07:54 | model-only | dota2 | Team Lynx | Nemiga Gaming | YES Team Lynx | 3 | 0.59 | 0.80 | 0.59 | open | - |
| 2026-10-24 06:54 | model-only | cs2 | ex-Zero Tenacity | Nuclear TigeRES | YES ex-Zero Tenacity | 33 | 0.37 | 0.47 | 0.36 | open | - |
| 2026-10-24 06:54 | favourite | cs2 | 9INE Academy | Bread Eaters Esports | NO Bread Eaters Esports | 13 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-10-24 06:54 | model-only | cs2 | ex-6666 | FOKUS | YES ex-6666 | 50 | 0.24 | 0.33 | 0.23 | open | - |
| 2026-10-24 06:54 | favourite | cs2 | FOKUS | ex-6666 | NO ex-6666 | 10 | 0.78 | 0.77 | 0.77 | open | - |
| 2026-10-24 06:54 | model-only | dota2 | GamerLegion | 1win | NO 1win | 30 | 0.40 | 0.52 | 0.40 | open | - |
| 2026-10-24 06:54 | favourite | cs2 | Nuclear TigeRES | ex-Zero Tenacity | NO ex-Zero Tenacity | 12 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-10-24 06:54 | favourite | cs2 | Noir Verse | Ryvex | YES Noir Verse | 11 | 0.72 | 0.69 | 0.69 | open | - |
| 2026-10-24 06:54 | favourite | dota2 | 1win | GamerLegion | NO GamerLegion | 5 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-10-24 05:54 | favourite | cs2 | FUT Esports | TYLOO | YES FUT Esports | 10 | 0.79 | 0.78 | 0.78 | won | $1.98 |
| 2026-10-24 05:54 | model-only | cs2 | TYLOO | FUT Esports | YES TYLOO | 55 | 0.22 | 0.36 | 0.22 | lost | -$12.77 |
| 2026-10-24 05:54 | favourite | cs2 | Aurora Gaming | TheMongolz | YES Aurora Gaming | 11 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-24 05:54 | model-only | cs2 | TheMongolz | Aurora Gaming | NO Aurora Gaming | 39 | 0.31 | 0.40 | 0.31 | open | - |
| 2026-10-24 01:54 | favourite | cs2 | Chinggis Warriors | Rare Atom | NO Rare Atom | 1 | 0.65 | 0.65 | 0.65 | won | $0.33 |
| 2026-10-24 01:54 | model-only | cs2 | Rare Atom | Chinggis Warriors | NO Chinggis Warriors | 33 | 0.37 | 0.50 | 0.35 | lost | -$12.75 |
| 2026-10-24 01:54 | model-only | dota2 | Resp Gaming | Team Nemesis Academy | NO Team Nemesis Academy | 14 | 0.53 | 0.68 | 0.51 | won | $6.33 |

## Backtest on real Kalshi prices

8346 settled matches from 2026-05-28 to 2026-10-19, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 23 | $422.99 | -$10.99 | -2.6% | -39.0% to +46.3% | 57% | -0.0c | 8% |
| model only | 1998 | $8,526.95 | -$990.95 | -11.6% | -20.1% to -3.0% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4018 | $16,341.50 | -$762.50 | -4.7% | -6.9% to -2.4% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3742 | $8,889.87 | -$982.87 | -11.1% | -16.6% to -5.4% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8121 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5723 | 0.1955 | 69.3% |
| model | 0.6605 | 0.2343 | 59.6% |
| blend | 0.5719 | 0.1954 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1335 | 0.525 | 0.524 |
| (0.55, 0.6] | 1359 | 0.577 | 0.550 |
| (0.6, 0.65] | 1254 | 0.626 | 0.635 |
| (0.65, 0.7] | 1092 | 0.676 | 0.702 |
| (0.7, 0.75] | 921 | 0.726 | 0.773 |
| (0.75, 0.8] | 786 | 0.776 | 0.812 |
| (0.8, 0.85] | 668 | 0.826 | 0.826 |
| (0.85, 0.9] | 503 | 0.877 | 0.903 |
| (0.9, 1.0] | 428 | 0.932 | 0.956 |

