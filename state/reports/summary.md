# Esports paper trading (fake money)

Updated 2026-11-12 15:05 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 688 | 60 | 628 | 216 | -$377.93 | -5.4% | -0.2c (678) | $622.07 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1101 | 89 | 1012 | 666 | -$485.46 | -7.7% | -1.6c (1090) | $514.54 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2293 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5823 | 0.2003 |
| model | 0.6513 | 0.2301 |
| blend | 0.5822 | 0.2004 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1438 | 0.5924 | 0.6578 |
| dota2 | 402 | 0.5600 | 0.6395 |
| ow | 128 | 0.5051 | 0.5379 |
| valorant | 120 | 0.6349 | 0.6783 |
| lol | 99 | 0.5729 | 0.7176 |
| r6 | 86 | 0.5672 | 0.6601 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-12 14:54 | model-only | cs2 | Team Recrent | Team Jerry | YES Team Recrent | 24 | 0.45 | 0.53 | 0.44 | open | - |
| 2026-11-12 14:54 | model-only | cs2 | Isurus | ex-Yawara | YES Isurus | 29 | 0.41 | 0.53 | 0.41 | open | - |
| 2026-11-12 13:54 | model-only | cs2 | The Last Resort | BakS eSports | NO BakS eSports | 1 | 0.16 | 0.27 | 0.16 | open | - |
| 2026-11-12 12:54 | favourite | cs2 | 6yuBoJlbl | Drama eSports | NO Drama eSports | 4 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-11-12 12:54 | favourite | cs2 | Lavked | DNK | NO DNK | 6 | 0.77 | 0.77 | 0.77 | open | - |
| 2026-11-12 11:54 | model-only | dota2 | Team Allied | CyberHero | YES Team Allied | 110 | 0.11 | 0.25 | 0.11 | open | - |
| 2026-11-12 11:54 | favourite | cs2 | Axorfy Gaming | MEIA NOITE | YES Axorfy Gaming | 1 | 0.62 | 0.60 | 0.60 | open | - |
| 2026-11-12 11:54 | model-only | cs2 | MEIA NOITE | Axorfy Gaming | NO Axorfy Gaming | 14 | 0.42 | 0.52 | 0.40 | open | - |
| 2026-11-12 11:54 | model-only | dota2 | GamerLegion | Aurora | NO Aurora | 41 | 0.30 | 0.53 | 0.29 | open | - |
| 2026-11-12 11:54 | model-only | dota2 | Nemiga Gaming | Power Rangers | YES Nemiga Gaming | 26 | 0.39 | 0.48 | 0.38 | won | $15.42 |
| 2026-11-12 11:24 | favourite | cs2 | Team Buster | Team korya_mc | YES Team Buster | 9 | 0.56 | 0.54 | 0.54 | open | - |
| 2026-11-12 10:54 | model-only | dota2 | old blood | Xipto Esports | NO Xipto Esports | 110 | 0.11 | 0.26 | 0.08 | lost | -$12.86 |
| 2026-11-12 10:54 | favourite | cs2 | GenOne | Leo Team | NO Leo Team | 1 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-11-12 10:54 | model-only | cs2 | Leo Team | GenOne | NO GenOne | 3 | 0.48 | 0.57 | 0.48 | open | - |
| 2026-11-12 10:54 | favourite | cs2 | FORZE Reload | Butterfly | NO Butterfly | 9 | 0.57 | 0.56 | 0.56 | lost | -$5.29 |
| 2026-11-12 08:24 | model-only | cs2 | G2 | Spirit | NO Spirit | 16 | 0.27 | 0.32 | 0.27 | lost | -$4.55 |
| 2026-11-12 07:54 | favourite | cs2 | NAVI Junior | MOUZ NXT | NO MOUZ NXT | 9 | 0.57 | 0.57 | 0.57 | lost | -$5.29 |
| 2026-11-12 07:54 | model-only | cs2 | DNK | Ducks | YES DNK | 32 | 0.29 | 0.35 | 0.28 | lost | -$9.75 |
| 2026-11-12 07:54 | model-only | cs2 | ILLYRIANS | Phantom | NO Phantom | 1 | 0.21 | 0.45 | 0.21 | lost | -$0.23 |
| 2026-11-12 07:54 | favourite | cs2 | Phantom | ILLYRIANS | NO ILLYRIANS | 6 | 0.79 | 0.79 | 0.79 | won | $1.19 |
| 2026-11-12 07:54 | model-only | cs2 | NAVI Junior | MOUZ NXT | NO MOUZ NXT | 22 | 0.57 | 0.68 | 0.57 | lost | -$12.92 |
| 2026-11-12 07:54 | favourite | cs2 | Ducks | DNK | NO DNK | 7 | 0.72 | 0.71 | 0.72 | won | $1.86 |
| 2026-11-12 07:54 | favourite | cs2 | MASONIC | The Last Resort | YES MASONIC | 8 | 0.60 | 0.59 | 0.59 | lost | -$4.94 |
| 2026-11-12 07:54 | model-only | cs2 | TheChampionGG | NAVI Junior | NO NAVI Junior | 56 | 0.22 | 0.36 | 0.21 | open | - |
| 2026-11-12 07:54 | favourite | cs2 | NAVI Junior | TheChampionGG | YES NAVI Junior | 1 | 0.80 | 0.79 | 0.79 | open | - |

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

