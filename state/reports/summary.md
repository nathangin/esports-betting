# Esports paper trading (fake money)

Updated 2026-11-11 13:07 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 665 | 60 | 605 | 212 | -$268.32 | -4.0% | -0.3c (657) | $731.68 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1078 | 95 | 983 | 650 | -$445.75 | -7.3% | -1.5c (1067) | $554.25 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2218 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5840 | 0.2009 |
| model | 0.6509 | 0.2299 |
| blend | 0.5841 | 0.2011 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1398 | 0.5932 | 0.6581 |
| dota2 | 381 | 0.5616 | 0.6380 |
| ow | 124 | 0.5192 | 0.5394 |
| valorant | 112 | 0.6294 | 0.6734 |
| lol | 97 | 0.5820 | 0.7126 |
| r6 | 86 | 0.5672 | 0.6601 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-11 11:51 | model-only | dota2 | Zero Tenacity | CyberHero | NO CyberHero | 6 | 0.13 | 0.23 | 0.12 | open | - |
| 2026-11-11 11:51 | model-only | dota2 | PuckChamp | HULIGANI | YES PuckChamp | 3 | 0.18 | 0.40 | 0.19 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | Nexus | MOUZ NXT | YES Nexus | 3 | 0.78 | 0.78 | 0.78 | open | - |
| 2026-11-11 10:51 | model-only | cs2 | MOUZ NXT | Nexus | NO Nexus | 59 | 0.23 | 0.31 | 0.22 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | GenOne | Inner Circle Academy | NO Inner Circle Academy | 10 | 0.54 | 0.54 | 0.54 | open | - |
| 2026-11-11 10:51 | model-only | cs2 | Inner Circle Academy | GenOne | NO GenOne | 29 | 0.47 | 0.54 | 0.46 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | Ducks | ex-Sashi Academy | NO ex-Sashi Academy | 2 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | Phantom | Drama eSports | YES Phantom | 6 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-11-11 10:51 | model-only | cs2 | Drama eSports | Phantom | NO Phantom | 75 | 0.18 | 0.41 | 0.17 | open | - |
| 2026-11-11 10:21 | favourite | cs2 | EYEBALLERS | Esport Academy Copenhagen | NO Esport Academy Copenhagen | 8 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-11-11 10:21 | model-only | cs2 | Esport Academy Copenhagen | EYEBALLERS | YES Esport Academy Copenhagen | 42 | 0.32 | 0.46 | 0.32 | open | - |
| 2026-11-11 10:21 | favourite | cs2 | Lunacy Team | G2 Ares | YES Lunacy Team | 9 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-11-11 08:51 | favourite | dota2 | InterActive Philippines | Zero Tenacity | NO Zero Tenacity | 9 | 0.60 | 0.60 | 0.60 | open | - |
| 2026-11-11 08:51 | favourite | dota2 | HULIGANI | Yakult's Brothers | YES HULIGANI | 6 | 0.87 | 0.85 | 0.85 | open | - |
| 2026-11-11 08:51 | model-only | dota2 | Yakult's Brothers | HULIGANI | YES Yakult's Brothers | 2 | 0.16 | 0.39 | 0.15 | open | - |
| 2026-11-11 08:51 | favourite | dota2 | PlayTime | Team Synapse | YES PlayTime | 7 | 0.79 | 0.77 | 0.77 | open | - |
| 2026-11-11 08:51 | favourite | dota2 | PuckChamp | Spirit Academy | NO Spirit Academy | 10 | 0.53 | 0.53 | 0.53 | lost | -$5.48 |
| 2026-11-11 08:51 | model-only | dota2 | Spirit Academy | PuckChamp | NO PuckChamp | 28 | 0.49 | 0.59 | 0.47 | won | $13.79 |
| 2026-11-11 08:51 | favourite | dota2 | LEGION | Xipto Esports | YES LEGION | 8 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-11 08:51 | favourite | dota2 | CyberHero | Inner Circle | YES CyberHero | 8 | 0.65 | 0.65 | 0.65 | open | - |
| 2026-11-11 08:21 | favourite | cs2 | MOUZ | G2 | NO G2 | 7 | 0.78 | 0.78 | 0.78 | lost | -$5.55 |
| 2026-11-11 07:51 | model-only | cs2 | 9INE Academy | Teletubisie | NO Teletubisie | 3 | 0.15 | 0.32 | 0.15 | open | - |
| 2026-11-11 07:51 | model-only | cs2 | UPGRADE | Butterfly | YES UPGRADE | 33 | 0.34 | 0.40 | 0.33 | open | - |
| 2026-11-11 07:51 | favourite | cs2 | ex-RUSTEC | Sokerorg | YES ex-RUSTEC | 9 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-11-11 07:51 | favourite | cs2 | Butterfly | UPGRADE | NO UPGRADE | 2 | 0.67 | 0.67 | 0.67 | open | - |

## Backtest on real Kalshi prices

9586 settled matches from 2026-05-28 to 2026-11-09, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2015 | $9,315.01 | -$992.01 | -10.6% | -18.8% to -2.6% | 32% | -0.6c | 99% |
| always the favourite (1% flat) | 4643 | $17,908.06 | -$833.06 | -4.7% | -6.9% to -2.4% | 67% | -1.8c | 84% |
| always the underdog (1% flat) | 3790 | $8,967.07 | -$986.07 | -11.0% | -16.9% to -5.1% | 31% | -1.2c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 9361 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5754 | 0.1970 | 68.9% |
| model | 0.6596 | 0.2339 | 59.6% |
| blend | 0.5751 | 0.1970 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1567 | 0.525 | 0.523 |
| (0.55, 0.6] | 1580 | 0.577 | 0.551 |
| (0.6, 0.65] | 1426 | 0.626 | 0.626 |
| (0.65, 0.7] | 1257 | 0.676 | 0.699 |
| (0.7, 0.75] | 1053 | 0.726 | 0.769 |
| (0.75, 0.8] | 889 | 0.776 | 0.805 |
| (0.8, 0.85] | 761 | 0.826 | 0.825 |
| (0.85, 0.9] | 562 | 0.877 | 0.902 |
| (0.9, 1.0] | 491 | 0.932 | 0.959 |

