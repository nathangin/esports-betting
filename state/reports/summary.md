# Esports paper trading (fake money)

Updated 2026-11-05 07:32 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 537 | 37 | 500 | 178 | -$37.67 | -0.7% | -0.3c (530) | $962.33 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 864 | 56 | 808 | 524 | -$490.09 | -9.1% | -1.5c (856) | $509.91 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1811 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5832 | 0.2008 |
| model | 0.6513 | 0.2301 |
| blend | 0.5835 | 0.2010 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1197 | 0.5959 | 0.6597 |
| dota2 | 285 | 0.5494 | 0.6269 |
| ow | 108 | 0.5091 | 0.5315 |
| lol | 91 | 0.5726 | 0.7204 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 48 | 0.6051 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-04 18:20 | model-only | cs2 | Al Ahli | NoTime | YES Al Ahli | 8 | 0.58 | 0.63 | 0.55 | open | - |
| 2026-11-04 16:50 | model-only | cs2 | maybe | Prestige | YES maybe | 21 | 0.38 | 0.49 | 0.38 | won | $12.67 |
| 2026-11-04 16:50 | model-only | cs2 | INOX Division | Johnny Speeds | YES INOX Division | 34 | 0.52 | 0.62 | 0.50 | won | $15.72 |
| 2026-11-04 16:50 | model-only | cs2 | BOJONG | SINQU | YES BOJONG | 45 | 0.39 | 0.60 | 0.38 | won | $26.70 |
| 2026-11-04 15:50 | model-only | cs2 | Regnum4Games | BIG Academy | YES Regnum4Games | 80 | 0.22 | 0.46 | 0.22 | lost | -$18.57 |
| 2026-11-04 15:50 | model-only | cs2 | Monkeys | SINNERS Legacy | NO SINNERS Legacy | 45 | 0.39 | 0.50 | 0.36 | won | $26.70 |
| 2026-11-04 14:50 | model-only | dota2 | CyberHero | HULIGANI | YES CyberHero | 45 | 0.39 | 0.54 | 0.39 | lost | -$18.30 |
| 2026-11-04 14:50 | model-only | cs2 | Spirit Academy Green | Fire Flux Esports | YES Spirit Academy Green | 2 | 0.44 | 0.50 | 0.42 | won | $1.08 |
| 2026-11-04 14:50 | favourite | cs2 | Fire Flux Esports | Spirit Academy Green | NO Spirit Academy Green | 7 | 0.61 | 0.58 | 0.58 | lost | -$4.39 |
| 2026-11-04 14:50 | model-only | dota2 | Spirit Academy | Xipto Esports | NO Xipto Esports | 1 | 0.28 | 0.32 | 0.28 | won | $0.70 |
| 2026-11-04 14:20 | favourite | cs2 | HAVU | RoundsGG | YES HAVU | 6 | 0.83 | 0.82 | 0.82 | won | $0.96 |
| 2026-11-04 14:20 | model-only | cs2 | RoundsGG | HAVU | NO HAVU | 99 | 0.18 | 0.32 | 0.18 | lost | -$18.85 |
| 2026-11-04 13:50 | favourite | cs2 | Noir Verse | KUUSAMO.gg | NO KUUSAMO.gg | 8 | 0.64 | 0.64 | 0.64 | lost | -$5.25 |
| 2026-11-04 13:50 | favourite | cs2 | ex-Zero Tenacity | Honvéd | YES ex-Zero Tenacity | 6 | 0.79 | 0.78 | 0.78 | lost | -$4.81 |
| 2026-11-04 13:50 | model-only | cs2 | Honvéd | ex-Zero Tenacity | NO ex-Zero Tenacity | 4 | 0.22 | 0.27 | 0.22 | won | $3.07 |
| 2026-11-04 13:24 | favourite | dota2 | iLTW TEAM | rostikfacekid TEAM | YES iLTW TEAM | 8 | 0.65 | 0.63 | 0.63 | lost | -$5.33 |
| 2026-11-04 12:54 | model-only | cs2 | Lilmix | mellren | NO mellren | 1 | 0.18 | 0.28 | 0.17 | lost | -$0.20 |
| 2026-11-04 12:54 | model-only | cs2 | maybe | WRAITH PCIFIC | YES maybe | 53 | 0.34 | 0.42 | 0.34 | lost | -$18.86 |
| 2026-11-04 12:54 | favourite | cs2 | WRAITH PCIFIC | maybe | NO maybe | 7 | 0.67 | 0.67 | 0.67 | won | $2.20 |
| 2026-11-04 12:54 | favourite | cs2 | mellren | Lilmix | NO Lilmix | 6 | 0.85 | 0.83 | 0.83 | won | $0.84 |
| 2026-11-04 12:54 | model-only | cs2 | Drama eSports | Saint Sinners | YES Drama eSports | 36 | 0.50 | 0.61 | 0.49 | won | $17.37 |
| 2026-11-04 12:54 | favourite | cs2 | Saint Sinners | Drama eSports | NO Drama eSports | 9 | 0.53 | 0.51 | 0.51 | lost | -$4.93 |
| 2026-11-04 11:54 | favourite | dota2 | GamerLegion | OG | YES GamerLegion | 10 | 0.51 | 0.50 | 0.50 | won | $4.72 |
| 2026-11-04 11:54 | favourite | dota2 | Zero Tenacity | angry birds | NO angry birds | 8 | 0.64 | 0.62 | 0.62 | lost | -$5.25 |
| 2026-11-04 11:54 | model-only | dota2 | angry birds | Zero Tenacity | YES angry birds | 7 | 0.39 | 0.51 | 0.38 | won | $4.15 |

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

