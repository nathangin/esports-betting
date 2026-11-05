# Esports paper trading (fake money)

Updated 2026-11-05 11:53 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 541 | 41 | 500 | 178 | -$37.67 | -0.7% | -0.3c (533) | $962.33 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 874 | 65 | 809 | 525 | -$486.71 | -9.0% | -1.5c (864) | $513.29 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1813 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5833 | 0.2008 |
| model | 0.6512 | 0.2301 |
| blend | 0.5836 | 0.2011 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1198 | 0.5959 | 0.6596 |
| dota2 | 286 | 0.5501 | 0.6273 |
| ow | 108 | 0.5091 | 0.5315 |
| lol | 91 | 0.5726 | 0.7204 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 48 | 0.6051 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-05 11:53 | favourite | dota2 | Team Lynx | Time to Sleep | YES Team Lynx | 2 | 0.84 | 0.83 | 0.83 | open | - |
| 2026-11-05 11:53 | model-only | dota2 | Time to Sleep | Team Lynx | NO Team Lynx | 106 | 0.17 | 0.31 | 0.17 | open | - |
| 2026-11-05 11:53 | favourite | dota2 | GamerLegion | Yellow Submarine | YES GamerLegion | 6 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-11-05 10:52 | favourite | cs2 | Fire Flux Esports | ILLYRIANS | YES Fire Flux Esports | 8 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-11-05 10:22 | favourite | cs2 | ex-ENCE | Noir Verse | NO Noir Verse | 5 | 0.63 | 0.59 | 0.59 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | GenOne | maybe | NO maybe | 2 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-11-05 07:52 | model-only | cs2 | Honvéd | BakS eSports | NO BakS eSports | 17 | 0.15 | 0.39 | 0.15 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | BakS eSports | Honvéd | YES BakS eSports | 5 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | Walczaki | HyperSpirit | NO HyperSpirit | 8 | 0.55 | 0.54 | 0.54 | open | - |
| 2026-11-05 07:52 | model-only | cs2 | maybe | GenOne | NO GenOne | 73 | 0.25 | 0.48 | 0.24 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | megoshort | Bebop | NO Bebop | 9 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-11-05 07:52 | model-only | cs2 | QUAZAR | FOKUS | YES QUAZAR | 63 | 0.29 | 0.47 | 0.29 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | FOKUS | QUAZAR | NO QUAZAR | 4 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-11-05 07:52 | favourite | cs2 | STATE | NAVI Junior | YES STATE | 8 | 0.56 | 0.55 | 0.55 | won | $3.38 |
| 2026-11-04 18:20 | model-only | cs2 | Al Ahli | NoTime | YES Al Ahli | 8 | 0.58 | 0.63 | 0.55 | open | - |
| 2026-11-04 16:50 | model-only | cs2 | maybe | Prestige | YES maybe | 21 | 0.38 | 0.49 | 0.38 | won | $12.67 |
| 2026-11-04 16:50 | model-only | cs2 | INOX Division | Johnny Speeds | YES INOX Division | 34 | 0.52 | 0.62 | 0.50 | won | $15.72 |
| 2026-11-04 16:50 | model-only | cs2 | BOJONG | SINQU | YES BOJONG | 45 | 0.39 | 0.60 | 0.38 | won | $26.70 |
| 2026-11-04 15:50 | model-only | cs2 | Regnum4Games | BIG Academy | YES Regnum4Games | 80 | 0.22 | 0.46 | 0.22 | lost | -$18.57 |
| 2026-11-04 15:50 | model-only | cs2 | Monkeys | SINNERS Legacy | NO SINNERS Legacy | 45 | 0.39 | 0.50 | 0.36 | won | $26.70 |
| 2026-11-04 14:50 | favourite | cs2 | Fire Flux Esports | Spirit Academy Green | NO Spirit Academy Green | 7 | 0.61 | 0.58 | 0.58 | lost | -$4.39 |
| 2026-11-04 14:50 | model-only | cs2 | Spirit Academy Green | Fire Flux Esports | YES Spirit Academy Green | 2 | 0.44 | 0.50 | 0.42 | won | $1.08 |
| 2026-11-04 14:50 | model-only | dota2 | Spirit Academy | Xipto Esports | NO Xipto Esports | 1 | 0.28 | 0.32 | 0.28 | won | $0.70 |
| 2026-11-04 14:50 | model-only | dota2 | CyberHero | HULIGANI | YES CyberHero | 45 | 0.39 | 0.54 | 0.39 | lost | -$18.30 |
| 2026-11-04 14:20 | favourite | cs2 | HAVU | RoundsGG | YES HAVU | 6 | 0.83 | 0.82 | 0.82 | won | $0.96 |

## Backtest on real Kalshi prices

9155 settled matches from 2026-05-28 to 2026-11-02, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 26 | $481.86 | $33.14 | +6.9% | -29.7% to +53.7% | 62% | -0.4c | 8% |
| model only | 2020 | $9,242.02 | -$992.02 | -10.7% | -18.4% to -3.0% | 33% | -0.7c | 99% |
| always the favourite (1% flat) | 4414 | $17,347.39 | -$838.39 | -4.8% | -7.1% to -2.7% | 67% | -1.7c | 84% |
| always the underdog (1% flat) | 3784 | $8,995.47 | -$985.47 | -11.0% | -16.5% to -4.9% | 31% | -1.3c | 99% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8930 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5749 | 0.1968 | 68.9% |
| model | 0.6599 | 0.2340 | 59.6% |
| blend | 0.5747 | 0.1968 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1475 | 0.525 | 0.525 |
| (0.55, 0.6] | 1510 | 0.577 | 0.547 |
| (0.6, 0.65] | 1371 | 0.626 | 0.628 |
| (0.65, 0.7] | 1202 | 0.676 | 0.700 |
| (0.7, 0.75] | 1004 | 0.726 | 0.770 |
| (0.75, 0.8] | 855 | 0.776 | 0.807 |
| (0.8, 0.85] | 729 | 0.826 | 0.823 |
| (0.85, 0.9] | 536 | 0.877 | 0.903 |
| (0.9, 1.0] | 473 | 0.932 | 0.958 |

