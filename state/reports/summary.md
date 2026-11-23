# Esports paper trading (fake money)

Updated 2026-11-23 12:59 UTC. Model fitted 2026-11-16T19:41. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 749 | 54 | 695 | 245 | -$244.02 | -3.2% | -0.2c (741) | $755.98 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1119 | 86 | 1033 | 678 | -$496.26 | -7.9% | -1.5c (1108) | $503.74 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2546 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5868 | 0.2021 |
| model | 0.6550 | 0.2318 |
| blend | 0.5868 | 0.2022 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1596 | 0.5959 | 0.6606 |
| dota2 | 456 | 0.5709 | 0.6454 |
| valorant | 148 | 0.6195 | 0.6930 |
| ow | 132 | 0.5132 | 0.5386 |
| lol | 101 | 0.5763 | 0.7125 |
| r6 | 93 | 0.5699 | 0.6553 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-15 14:54 | model-only | cs2 | OLDBOYS- | Fire Flux Esports | NO Fire Flux Esports | 38 | 0.37 | 0.60 | 0.36 | won | $23.31 |
| 2026-11-15 13:53 | model-only | cs2 | FORZE Reload | Nexus | YES FORZE Reload | 4 | 0.50 | 0.56 | 0.50 | won | $1.93 |
| 2026-11-15 13:53 | model-only | cs2 | Butterfly | BakS eSports | NO BakS eSports | 22 | 0.49 | 0.57 | 0.49 | lost | -$11.17 |
| 2026-11-15 13:53 | model-only | cs2 | Axorfy Gaming | Galorys | NO Galorys | 7 | 0.37 | 0.44 | 0.37 | lost | -$2.71 |
| 2026-11-15 13:23 | model-only | dota2 | InterActive Philippines | Nemiga Gaming | YES InterActive Philippines | 36 | 0.39 | 0.56 | 0.38 | lost | -$14.64 |
| 2026-11-15 12:08 | model-only | cs2 | Team leva2k | Team Buster | YES Team leva2k | 6 | 0.49 | 0.60 | 0.48 | won | $2.95 |
| 2026-11-15 12:08 | model-only | cs2 | Team cutierover | Team Bratishkin | NO Team Bratishkin | 41 | 0.32 | 0.52 | 0.30 | lost | -$13.75 |
| 2026-11-15 11:53 | model-only | dota2 | Team Allied | Zero Tenacity | NO Zero Tenacity | 25 | 0.53 | 0.60 | 0.53 | lost | -$13.69 |
| 2026-11-15 10:53 | model-only | cs2 | Omega | Iberian Soul | NO Iberian Soul | 43 | 0.30 | 0.37 | 0.30 | won | $29.46 |
| 2026-11-15 10:53 | model-only | cs2 | Brute | ex-INOX Division | YES Brute | 4 | 0.57 | 0.64 | 0.56 | lost | -$2.35 |
| 2026-11-15 10:53 | model-only | cs2 | Eternal Fire | 100 Thieves | YES Eternal Fire | 29 | 0.46 | 0.54 | 0.46 | lost | -$13.85 |
| 2026-11-15 10:53 | model-only | cs2 | The Last Resort | Leo Team | NO Leo Team | 60 | 0.19 | 0.35 | 0.18 | won | $47.95 |
| 2026-11-15 10:53 | model-only | dota2 | potn9ki | Xipto Esports | YES potn9ki | 34 | 0.20 | 0.24 | 0.17 | lost | -$7.19 |
| 2026-11-15 10:23 | model-only | cs2 | G2 Ares | WW Team | YES G2 Ares | 3 | 0.42 | 0.53 | 0.41 | won | $1.68 |
| 2026-11-15 08:53 | model-only | dota2 | GamerLegion | PARIVISION | YES GamerLegion | 101 | 0.13 | 0.37 | 0.12 | lost | -$13.93 |
| 2026-11-15 08:53 | model-only | cs2 | Team cutierover | Team Jerry | NO Team Jerry | 4 | 0.30 | 0.55 | 0.30 | won | $2.74 |
| 2026-11-15 07:52 | model-only | cs2 | The Chosen Few | NAVI Junior | NO NAVI Junior | 10 | 0.21 | 0.40 | 0.20 | lost | -$2.22 |
| 2026-11-15 07:52 | model-only | cs2 | Virtus.pro | Hype Tech | NO Hype Tech | 1 | 0.63 | 0.69 | 0.63 | won | $0.35 |
| 2026-11-15 07:52 | model-only | cs2 | FORZE Reload | PRIVATE | YES FORZE Reload | 34 | 0.39 | 0.52 | 0.39 | won | $20.17 |
| 2026-11-15 07:52 | model-only | cs2 | fnatic | FaZe | NO FaZe | 28 | 0.47 | 0.55 | 0.47 | won | $14.35 |
| 2026-11-15 07:52 | model-only | cs2 | Drama eSports | ex-RUSTEC | YES Drama eSports | 49 | 0.27 | 0.39 | 0.26 | lost | -$13.91 |
| 2026-11-15 06:52 | model-only | cs2 | FURIA | Spirit | YES FURIA | 32 | 0.41 | 0.51 | 0.41 | won | $18.33 |
| 2026-11-14 22:37 | model-only | cs2 | arroba | ALKA | YES arroba | 1 | 0.38 | 0.53 | 0.37 | lost | -$0.40 |
| 2026-11-14 17:51 | model-only | lol | Bilibili Gaming | Gen.G | YES Bilibili Gaming | 32 | 0.39 | 0.47 | 0.39 | won | $18.98 |
| 2026-11-14 17:51 | model-only | dota2 | Team Allied | Team Synapse | YES Team Allied | 1 | 0.36 | 0.41 | 0.34 | won | $0.62 |

## Backtest on real Kalshi prices

10025 settled matches from 2026-05-28 to 2026-11-16, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 28 | $524.99 | $56.01 | +10.7% | -23.7% to +53.5% | 64% | -1.1c | 8% |
| model only | 1973 | $7,977.91 | -$990.91 | -12.4% | -21.3% to -3.7% | 33% | -0.5c | 99% |
| always the favourite (1% flat) | 4839 | $18,787.58 | -$832.58 | -4.4% | -6.6% to -2.4% | 67% | -1.8c | 84% |
| always the underdog (1% flat) | 3796 | $8,474.47 | -$986.47 | -11.6% | -17.2% to -6.2% | 30% | -1.3c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 9800 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5765 | 0.1974 | 68.7% |
| model | 0.6600 | 0.2340 | 59.6% |
| blend | 0.5763 | 0.1974 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1658 | 0.524 | 0.521 |
| (0.55, 0.6] | 1658 | 0.577 | 0.552 |
| (0.6, 0.65] | 1495 | 0.626 | 0.625 |
| (0.65, 0.7] | 1312 | 0.676 | 0.697 |
| (0.7, 0.75] | 1094 | 0.726 | 0.771 |
| (0.75, 0.8] | 927 | 0.776 | 0.806 |
| (0.8, 0.85] | 788 | 0.826 | 0.829 |
| (0.85, 0.9] | 585 | 0.877 | 0.899 |
| (0.9, 1.0] | 508 | 0.932 | 0.957 |

