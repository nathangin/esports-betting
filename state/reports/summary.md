# Esports paper trading (fake money)

Updated 2026-11-05 18:24 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 556 | 49 | 507 | 181 | -$35.64 | -0.6% | -0.3c (547) | $964.36 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 897 | 73 | 824 | 537 | -$475.13 | -8.7% | -1.6c (888) | $524.87 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1838 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5841 | 0.2011 |
| model | 0.6504 | 0.2296 |
| blend | 0.5844 | 0.2014 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1217 | 0.5964 | 0.6590 |
| dota2 | 289 | 0.5506 | 0.6276 |
| ow | 111 | 0.5147 | 0.5254 |
| lol | 91 | 0.5726 | 0.7204 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 48 | 0.6051 | 0.6885 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-05 18:23 | favourite | cs2 | Inner Circle Prospect | aimers | NO aimers | 1 | 0.61 | 0.59 | 0.59 | open | - |
| 2026-11-05 17:53 | model-only | cs2 | Damajuana | RED Canids Academy | YES Damajuana | 1 | 0.16 | 0.21 | 0.15 | open | - |
| 2026-11-05 17:53 | model-only | cs2 | Regnum4Games | Privateer Gaming | YES Regnum4Games | 5 | 0.49 | 0.59 | 0.48 | open | - |
| 2026-11-05 17:23 | favourite | cs2 | Gremio Esports | QUINTESSENCIA | NO QUINTESSENCIA | 1 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-11-05 17:23 | model-only | cs2 | QUINTESSENCIA | Gremio Esports | NO Gremio Esports | 22 | 0.50 | 0.64 | 0.49 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | Johnny Speeds | Drama eSports | NO Drama eSports | 7 | 0.66 | 0.65 | 0.65 | open | - |
| 2026-11-05 16:53 | model-only | cs2 | The Chosen Few | BANGARANGA | NO BANGARANGA | 54 | 0.34 | 0.46 | 0.33 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | BANGARANGA | The Chosen Few | NO The Chosen Few | 7 | 0.67 | 0.67 | 0.67 | open | - |
| 2026-11-05 16:53 | model-only | cs2 | Nordic Valor | BoyBand | NO BoyBand | 16 | 0.30 | 0.46 | 0.30 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | BoyBand | Nordic Valor | YES BoyBand | 7 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | Brute | GenOne | YES Brute | 1 | 0.67 | 0.66 | 0.66 | won | $0.31 |
| 2026-11-05 16:53 | model-only | cs2 | Drama eSports | Johnny Speeds | YES Drama eSports | 51 | 0.36 | 0.55 | 0.35 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | IMAPROBLEM | Glitchtech Esports | NO Glitchtech Esports | 8 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-11-05 16:53 | model-only | cs2 | maybe | KUUSAMO.gg | NO KUUSAMO.gg | 30 | 0.62 | 0.68 | 0.61 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | maybe | KUUSAMO.gg | NO KUUSAMO.gg | 8 | 0.62 | 0.61 | 0.61 | open | - |
| 2026-11-05 16:53 | model-only | cs2 | megoshort | Butterfly | NO Butterfly | 87 | 0.21 | 0.41 | 0.20 | open | - |
| 2026-11-05 16:53 | favourite | cs2 | Butterfly | megoshort | YES Butterfly | 5 | 0.81 | 0.80 | 0.80 | open | - |
| 2026-11-05 16:53 | model-only | cs2 | Spirit HU | Phantom Academy | NO Phantom Academy | 115 | 0.16 | 0.35 | 0.15 | open | - |
| 2026-11-05 16:23 | favourite | cs2 | Al Ahli | SINQU | NO SINQU | 8 | 0.63 | 0.63 | 0.63 | open | - |
| 2026-11-05 16:23 | model-only | cs2 | Al Ahli | SINQU | NO SINQU | 25 | 0.63 | 0.76 | 0.63 | open | - |
| 2026-11-05 15:53 | model-only | cs2 | Monkeys | UNiTY esports | YES Monkeys | 14 | 0.15 | 0.31 | 0.14 | open | - |
| 2026-11-05 15:53 | favourite | cs2 | 99firepower 1utility | GamersLab Esports | YES 99firepower 1utility | 7 | 0.66 | 0.65 | 0.65 | won | $2.27 |
| 2026-11-05 15:53 | favourite | cs2 | IMAPROBLEM | Hermine Esports Club | NO Hermine Esports Club | 8 | 0.56 | 0.52 | 0.52 | lost | -$4.62 |
| 2026-11-05 15:53 | favourite | cs2 | PARTIZAN | PENSIONERS | YES PARTIZAN | 6 | 0.58 | 0.54 | 0.54 | won | $2.41 |
| 2026-11-05 15:53 | favourite | cs2 | Vitality Academy | Growth Lab Esports | YES Vitality Academy | 8 | 0.62 | 0.59 | 0.59 | won | $2.90 |

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

