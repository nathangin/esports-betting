# Esports paper trading (fake money)

Updated 2026-11-05 16:43 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 547 | 44 | 503 | 179 | -$5.66 | -0.1% | -0.3c (538) | $994.34 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 888 | 74 | 814 | 529 | -$480.87 | -8.9% | -1.5c (874) | $519.13 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1826 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5842 | 0.2012 |
| model | 0.6508 | 0.2299 |
| blend | 0.5845 | 0.2015 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1205 | 0.5968 | 0.6597 |
| dota2 | 289 | 0.5506 | 0.6276 |
| ow | 111 | 0.5147 | 0.5254 |
| lol | 91 | 0.5726 | 0.7204 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 48 | 0.6051 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-05 16:23 | favourite | cs2 | Al Ahli | SINQU | NO SINQU | 8 | 0.63 | 0.63 | 0.63 | open | - |
| 2026-11-05 16:23 | model-only | cs2 | Al Ahli | SINQU | NO SINQU | 25 | 0.63 | 0.76 | 0.63 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | Vitality Academy | Growth Lab Esports | YES Vitality Academy | 8 | 0.62 | 0.59 | 0.59 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | UNiTY esports | Monkeys | NO Monkeys | 5 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-11-05 15:53 | model-only | cs2 | Monkeys | UNiTY esports | YES Monkeys | 14 | 0.15 | 0.31 | 0.14 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | PARTIZAN | PENSIONERS | YES PARTIZAN | 6 | 0.58 | 0.54 | 0.54 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | IMAPROBLEM | Hermine Esports Club | NO Hermine Esports Club | 8 | 0.56 | 0.52 | 0.52 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | 99firepower 1utility | GamersLab Esports | YES 99firepower 1utility | 7 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-05 15:23 | favourite | cs2 | Revise | wnT | YES Revise | 5 | 0.51 | 0.50 | 0.50 | open | - |
| 2026-11-05 15:23 | model-only | cs2 | Revise | wnT | YES Revise | 5 | 0.51 | 0.58 | 0.50 | open | - |
| 2026-11-05 14:53 | favourite | dota2 | Xipto Esports | Zero Tenacity | YES Xipto Esports | 9 | 0.54 | 0.53 | 0.53 | open | - |
| 2026-11-05 14:53 | favourite | cs2 | JUMBO TEAM | RoundsGG | YES JUMBO TEAM | 7 | 0.65 | 0.62 | 0.62 | open | - |
| 2026-11-05 14:23 | favourite | cs2 | Prestige | KUUSAMO.gg | YES Prestige | 6 | 0.76 | 0.76 | 0.76 | open | - |
| 2026-11-05 14:23 | model-only | cs2 | KUUSAMO.gg | Prestige | NO Prestige | 77 | 0.25 | 0.33 | 0.24 | open | - |
| 2026-11-05 13:53 | favourite | cs2 | BASEMENT BOYS | Misa Esports | YES BASEMENT BOYS | 7 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-11-05 13:53 | model-only | cs2 | Misa Esports | BASEMENT BOYS | NO BASEMENT BOYS | 56 | 0.34 | 0.49 | 0.33 | open | - |
| 2026-11-05 13:53 | favourite | cs2 | ILLYRIANS | Honvéd | NO Honvéd | 7 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-11-05 13:53 | model-only | cs2 | Honvéd | ILLYRIANS | YES Honvéd | 12 | 0.33 | 0.45 | 0.33 | open | - |
| 2026-11-05 13:53 | favourite | cs2 | FORZE Reload | G2 Ares | YES FORZE Reload | 6 | 0.75 | 0.74 | 0.74 | open | - |
| 2026-11-05 12:53 | favourite | cs2 | Rebels Gaming | mellren | YES Rebels Gaming | 8 | 0.58 | 0.55 | 0.55 | won | $3.22 |
| 2026-11-05 11:53 | favourite | dota2 | GamerLegion | Yellow Submarine | YES GamerLegion | 6 | 0.72 | 0.71 | 0.71 | open | - |
| 2026-11-05 11:53 | model-only | dota2 | Time to Sleep | Team Lynx | NO Team Lynx | 106 | 0.17 | 0.31 | 0.17 | lost | -$19.07 |
| 2026-11-05 11:53 | favourite | dota2 | Team Lynx | Time to Sleep | YES Team Lynx | 2 | 0.84 | 0.83 | 0.83 | won | $0.30 |
| 2026-11-05 10:52 | favourite | cs2 | Fire Flux Esports | ILLYRIANS | YES Fire Flux Esports | 8 | 0.58 | 0.56 | 0.56 | won | $3.22 |
| 2026-11-05 10:22 | favourite | cs2 | ex-ENCE | Noir Verse | NO Noir Verse | 5 | 0.63 | 0.59 | 0.59 | open | - |

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

