# Esports paper trading (fake money)

Updated 2026-10-19 09:20 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 242 | 24 | 218 | 55 | -$490.08 | -19.9% | -0.9c (237) | $509.92 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 373 | 38 | 335 | 232 | -$90.64 | -3.7% | -1.4c (369) | $909.36 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

810 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5690 | 0.1939 |
| model | 0.6533 | 0.2308 |
| blend | 0.5682 | 0.1936 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 496 | 0.5756 | 0.6562 |
| dota2 | 138 | 0.5537 | 0.6492 |
| ow | 60 | 0.4906 | 0.5267 |
| lol | 59 | 0.5497 | 0.7082 |
| r6 | 35 | 0.6531 | 0.7263 |
| valorant | 22 | 0.6473 | 0.6972 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-19 09:20 | favourite | cs2 | The Chosen Few | SANCTUM | YES The Chosen Few | 12 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-19 09:20 | model-only | cs2 | SANCTUM | The Chosen Few | YES SANCTUM | 33 | 0.29 | 0.51 | 0.28 | open | - |
| 2026-10-19 07:50 | favourite | dota2 | Yellow Submarine | Zero Tenacity | YES Yellow Submarine | 10 | 0.87 | 0.86 | 0.86 | open | - |
| 2026-10-19 07:50 | model-only | dota2 | Zero Tenacity | Yellow Submarine | NO Yellow Submarine | 64 | 0.15 | 0.27 | 0.14 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | BIG | PRIVATE | YES BIG | 12 | 0.69 | 0.69 | 0.69 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | Nexus | WBT Academy | YES Nexus | 15 | 0.57 | 0.55 | 0.55 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | Infinite | Insiders Esport | YES Infinite | 11 | 0.80 | 0.79 | 0.79 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | BC.Game Esports | Drama eSports | YES BC.Game Esports | 10 | 0.85 | 0.84 | 0.84 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | BASEMENT BOYS | aimclub | NO aimclub | 13 | 0.64 | 0.62 | 0.62 | open | - |
| 2026-10-19 07:50 | model-only | cs2 | aimclub | BASEMENT BOYS | YES aimclub | 1 | 0.40 | 0.48 | 0.38 | open | - |
| 2026-10-19 07:50 | favourite | cs2 | Apogee Esports | Spirit Academy | YES Apogee Esports | 12 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-10-19 06:50 | model-only | cs2 | Copenhagen Wolves | Prestige | YES Copenhagen Wolves | 18 | 0.53 | 0.59 | 0.51 | open | - |
| 2026-10-19 06:50 | favourite | cs2 | FORZE Reload | GenOne | YES FORZE Reload | 12 | 0.71 | 0.69 | 0.69 | open | - |
| 2026-10-19 06:50 | favourite | cs2 | WRAITH PCIFIC | ILLYRIANS | YES WRAITH PCIFIC | 14 | 0.59 | 0.57 | 0.57 | open | - |
| 2026-10-19 06:50 | model-only | cs2 | GenOne | FORZE Reload | NO FORZE Reload | 30 | 0.32 | 0.44 | 0.31 | open | - |
| 2026-10-19 06:50 | favourite | cs2 | Copenhagen Wolves | Prestige | YES Copenhagen Wolves | 16 | 0.53 | 0.51 | 0.51 | open | - |
| 2026-10-19 06:50 | favourite | cs2 | Sokerorg | EAC Extra | YES Sokerorg | 13 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-10-19 06:50 | model-only | cs2 | EAC Extra | Sokerorg | NO Sokerorg | 4 | 0.35 | 0.55 | 0.34 | open | - |
| 2026-10-18 20:54 | favourite | cs2 | Procyon Gaming | your end | YES Procyon Gaming | 5 | 0.89 | 0.88 | 0.88 | won | $0.51 |
| 2026-10-18 18:53 | favourite | cs2 | 6yuBoJlbl | HyperSpirit | YES 6yuBoJlbl | 2 | 0.65 | 0.62 | 0.62 | lost | -$1.34 |
| 2026-10-18 16:53 | model-only | lol | MVK Esports | Karmine Corp | NO Karmine Corp | 42 | 0.13 | 0.28 | 0.12 | lost | -$5.80 |
| 2026-10-18 15:53 | favourite | cs2 | Nuclear TigeRES | ex-RUSTEC | NO ex-RUSTEC | 12 | 0.67 | 0.65 | 0.65 | won | $3.77 |
| 2026-10-18 15:53 | model-only | cs2 | BakS eSports | FORZE Reload | YES BakS eSports | 23 | 0.43 | 0.49 | 0.42 | lost | -$10.29 |
| 2026-10-18 15:53 | favourite | cs2 | FORZE Reload | BakS eSports | NO BakS eSports | 14 | 0.60 | 0.58 | 0.58 | won | $5.36 |
| 2026-10-18 15:53 | model-only | cs2 | ex-RUSTEC | Nuclear TigeRES | YES ex-RUSTEC | 29 | 0.37 | 0.46 | 0.35 | lost | -$11.21 |

## Backtest on real Kalshi prices

7979 settled matches from 2026-05-28 to 2026-10-12, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $439.42 | -$30.42 | -6.9% | -43.8% to +40.9% | 54% | -0.0c | 10% |
| model only | 1968 | $8,857.80 | -$985.80 | -11.1% | -19.2% to -3.2% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 3824 | $15,776.22 | -$733.22 | -4.6% | -7.0% to -2.2% | 67% | -1.5c | 81% |
| always the underdog (1% flat) | 3731 | $8,550.73 | -$978.73 | -11.4% | -17.1% to -5.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 7754 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5731 | 0.1959 | 69.2% |
| model | 0.6615 | 0.2347 | 59.5% |
| blend | 0.5727 | 0.1958 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1281 | 0.525 | 0.522 |
| (0.55, 0.6] | 1311 | 0.577 | 0.548 |
| (0.6, 0.65] | 1192 | 0.626 | 0.638 |
| (0.65, 0.7] | 1041 | 0.676 | 0.701 |
| (0.7, 0.75] | 880 | 0.726 | 0.773 |
| (0.75, 0.8] | 755 | 0.776 | 0.812 |
| (0.8, 0.85] | 636 | 0.826 | 0.824 |
| (0.85, 0.9] | 478 | 0.877 | 0.902 |
| (0.9, 1.0] | 405 | 0.932 | 0.956 |

