# Esports paper trading (fake money)

Updated 2026-11-12 17:50 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 691 | 58 | 633 | 218 | -$305.37 | -4.4% | -0.2c (683) | $694.63 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1105 | 89 | 1016 | 668 | -$489.72 | -7.8% | -1.6c (1092) | $510.28 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2310 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5821 | 0.2002 |
| model | 0.6515 | 0.2301 |
| blend | 0.5820 | 0.2003 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1448 | 0.5911 | 0.6568 |
| dota2 | 408 | 0.5636 | 0.6439 |
| ow | 128 | 0.5051 | 0.5379 |
| valorant | 121 | 0.6354 | 0.6780 |
| lol | 99 | 0.5729 | 0.7176 |
| r6 | 86 | 0.5672 | 0.6601 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-12 17:50 | favourite | cs2 | tao toma | Procyon Gaming | YES tao toma | 1 | 0.64 | 0.64 | 0.64 | open | - |
| 2026-11-12 17:35 | favourite | cs2 | Team Bratishkin | Team Recrent | YES Team Bratishkin | 8 | 0.58 | 0.57 | 0.57 | open | - |
| 2026-11-12 16:50 | model-only | cs2 | Spirit Academy | ex-RUSTEC | YES Spirit Academy | 7 | 0.55 | 0.60 | 0.55 | open | - |
| 2026-11-12 16:50 | model-only | cs2 | maybe | Team ACES | NO Team ACES | 1 | 0.26 | 0.41 | 0.25 | open | - |
| 2026-11-12 16:50 | model-only | cs2 | Spirit HU | ENRAGE | NO ENRAGE | 44 | 0.30 | 0.42 | 0.29 | open | - |
| 2026-11-12 15:50 | favourite | cs2 | Fire Flux Esports | Banger Gang | NO Banger Gang | 1 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-11-12 15:50 | favourite | cs2 | TTG Esports | DINERO | NO DINERO | 1 | 0.78 | 0.78 | 0.78 | open | - |
| 2026-11-12 14:54 | model-only | cs2 | Team Recrent | Team Jerry | YES Team Recrent | 24 | 0.45 | 0.53 | 0.44 | open | - |
| 2026-11-12 14:54 | model-only | cs2 | Isurus | ex-Yawara | YES Isurus | 29 | 0.41 | 0.53 | 0.41 | open | - |
| 2026-11-12 13:54 | model-only | cs2 | The Last Resort | BakS eSports | NO BakS eSports | 1 | 0.16 | 0.27 | 0.16 | lost | -$0.17 |
| 2026-11-12 12:54 | favourite | cs2 | 6yuBoJlbl | Drama eSports | NO Drama eSports | 4 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-11-12 12:54 | favourite | cs2 | Lavked | DNK | NO DNK | 6 | 0.77 | 0.77 | 0.77 | won | $1.30 |
| 2026-11-12 11:54 | model-only | dota2 | Team Allied | CyberHero | YES Team Allied | 110 | 0.11 | 0.25 | 0.11 | won | $97.14 |
| 2026-11-12 11:54 | model-only | cs2 | MEIA NOITE | Axorfy Gaming | NO Axorfy Gaming | 14 | 0.42 | 0.52 | 0.40 | open | - |
| 2026-11-12 11:54 | favourite | cs2 | Axorfy Gaming | MEIA NOITE | YES Axorfy Gaming | 1 | 0.62 | 0.60 | 0.60 | open | - |
| 2026-11-12 11:54 | model-only | dota2 | GamerLegion | Aurora | NO Aurora | 41 | 0.30 | 0.53 | 0.29 | lost | -$12.91 |
| 2026-11-12 11:54 | model-only | dota2 | Nemiga Gaming | Power Rangers | YES Nemiga Gaming | 26 | 0.39 | 0.48 | 0.38 | won | $15.42 |
| 2026-11-12 11:24 | favourite | cs2 | Team Buster | Team korya_mc | YES Team Buster | 9 | 0.56 | 0.54 | 0.54 | lost | -$5.20 |
| 2026-11-12 10:54 | model-only | dota2 | old blood | Xipto Esports | NO Xipto Esports | 110 | 0.11 | 0.26 | 0.08 | lost | -$12.86 |
| 2026-11-12 10:54 | favourite | cs2 | GenOne | Leo Team | NO Leo Team | 1 | 0.52 | 0.52 | 0.52 | lost | -$0.54 |
| 2026-11-12 10:54 | model-only | cs2 | Leo Team | GenOne | NO GenOne | 3 | 0.48 | 0.57 | 0.48 | won | $1.50 |
| 2026-11-12 10:54 | favourite | cs2 | FORZE Reload | Butterfly | NO Butterfly | 9 | 0.57 | 0.56 | 0.56 | lost | -$5.29 |
| 2026-11-12 08:24 | model-only | cs2 | G2 | Spirit | NO Spirit | 16 | 0.27 | 0.32 | 0.27 | lost | -$4.55 |
| 2026-11-12 07:54 | favourite | cs2 | NAVI Junior | MOUZ NXT | NO MOUZ NXT | 9 | 0.57 | 0.57 | 0.57 | lost | -$5.29 |
| 2026-11-12 07:54 | model-only | cs2 | DNK | Ducks | YES DNK | 32 | 0.29 | 0.35 | 0.28 | lost | -$9.75 |

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

