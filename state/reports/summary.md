# Esports paper trading (fake money)

Updated 2026-11-11 15:07 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 670 | 60 | 610 | 213 | -$296.47 | -4.4% | -0.3c (658) | $703.53 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1086 | 93 | 993 | 656 | -$458.96 | -7.4% | -1.5c (1071) | $541.04 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2231 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5836 | 0.2008 |
| model | 0.6513 | 0.2301 |
| blend | 0.5837 | 0.2010 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1403 | 0.5928 | 0.6579 |
| dota2 | 386 | 0.5616 | 0.6402 |
| ow | 125 | 0.5158 | 0.5392 |
| valorant | 114 | 0.6305 | 0.6776 |
| lol | 97 | 0.5820 | 0.7126 |
| r6 | 86 | 0.5672 | 0.6601 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-11 14:52 | model-only | dota2 | Xipto Esports | Froglings | NO Froglings | 34 | 0.39 | 0.56 | 0.39 | open | - |
| 2026-11-11 14:52 | favourite | dota2 | angry birds | Power Rangers | YES angry birds | 8 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-11-11 14:52 | model-only | dota2 | angry birds | Power Rangers | YES angry birds | 23 | 0.58 | 0.68 | 0.57 | open | - |
| 2026-11-11 14:52 | favourite | cs2 | QUINTESSENCIA | underw0rld | YES QUINTESSENCIA | 1 | 0.78 | 0.78 | 0.78 | open | - |
| 2026-11-11 14:52 | model-only | cs2 | underw0rld | QUINTESSENCIA | NO QUINTESSENCIA | 6 | 0.23 | 0.46 | 0.22 | open | - |
| 2026-11-11 14:52 | favourite | cs2 | Fire Flux Esports | RoundsGG | YES Fire Flux Esports | 6 | 0.78 | 0.76 | 0.76 | open | - |
| 2026-11-11 14:22 | favourite | cs2 | KUUSAMO.gg | SINQU | YES KUUSAMO.gg | 8 | 0.61 | 0.60 | 0.60 | open | - |
| 2026-11-11 14:22 | model-only | cs2 | SINQU | KUUSAMO.gg | NO KUUSAMO.gg | 3 | 0.40 | 0.49 | 0.40 | open | - |
| 2026-11-11 13:52 | favourite | cs2 | 33 | ex-INOX Division | NO ex-INOX Division | 10 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-11-11 13:52 | favourite | cs2 | FORZE Reload | MASONIC | YES FORZE Reload | 6 | 0.85 | 0.84 | 0.84 | open | - |
| 2026-11-11 13:52 | model-only | cs2 | MASONIC | FORZE Reload | NO FORZE Reload | 83 | 0.16 | 0.33 | 0.16 | open | - |
| 2026-11-11 13:52 | favourite | cs2 | BBL | 33 | YES BBL | 8 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-11-11 13:52 | favourite | cs2 | BakS eSports | Nexus | YES BakS eSports | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-11 11:51 | model-only | dota2 | PuckChamp | HULIGANI | YES PuckChamp | 3 | 0.18 | 0.40 | 0.19 | open | - |
| 2026-11-11 11:51 | model-only | dota2 | Zero Tenacity | CyberHero | NO CyberHero | 6 | 0.13 | 0.23 | 0.12 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | Nexus | MOUZ NXT | YES Nexus | 3 | 0.78 | 0.78 | 0.78 | won | $0.62 |
| 2026-11-11 10:51 | model-only | cs2 | MOUZ NXT | Nexus | NO Nexus | 59 | 0.23 | 0.31 | 0.22 | lost | -$14.31 |
| 2026-11-11 10:51 | favourite | cs2 | GenOne | Inner Circle Academy | NO Inner Circle Academy | 10 | 0.54 | 0.54 | 0.54 | lost | -$5.58 |
| 2026-11-11 10:51 | model-only | cs2 | Inner Circle Academy | GenOne | NO GenOne | 29 | 0.47 | 0.54 | 0.46 | won | $14.86 |
| 2026-11-11 10:51 | favourite | cs2 | Ducks | ex-Sashi Academy | NO ex-Sashi Academy | 2 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-11 10:51 | favourite | cs2 | Phantom | Drama eSports | YES Phantom | 6 | 0.83 | 0.83 | 0.83 | won | $0.96 |
| 2026-11-11 10:51 | model-only | cs2 | Drama eSports | Phantom | NO Phantom | 75 | 0.18 | 0.41 | 0.17 | lost | -$14.28 |
| 2026-11-11 10:21 | favourite | cs2 | Lunacy Team | G2 Ares | YES Lunacy Team | 9 | 0.58 | 0.57 | 0.57 | lost | -$5.38 |
| 2026-11-11 10:21 | favourite | cs2 | EYEBALLERS | Esport Academy Copenhagen | NO Esport Academy Copenhagen | 8 | 0.69 | 0.69 | 0.69 | won | $2.36 |
| 2026-11-11 10:21 | model-only | cs2 | Esport Academy Copenhagen | EYEBALLERS | YES Esport Academy Copenhagen | 42 | 0.32 | 0.46 | 0.32 | lost | -$14.08 |

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

