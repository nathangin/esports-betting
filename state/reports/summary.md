# Esports paper trading (fake money)

Updated 2026-10-19 02:55 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 236 | 18 | 218 | 55 | -$490.08 | -19.9% | -0.9c (232) | $509.92 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 361 | 26 | 335 | 232 | -$90.64 | -3.7% | -1.4c (358) | $909.36 |

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
| 2026-10-18 20:54 | favourite | cs2 | Procyon Gaming | your end | YES Procyon Gaming | 5 | 0.89 | 0.88 | 0.88 | won | $0.51 |
| 2026-10-18 18:53 | favourite | cs2 | 6yuBoJlbl | HyperSpirit | YES 6yuBoJlbl | 2 | 0.65 | 0.62 | 0.62 | lost | -$1.34 |
| 2026-10-18 16:53 | model-only | lol | MVK Esports | Karmine Corp | NO Karmine Corp | 42 | 0.13 | 0.28 | 0.12 | lost | -$5.80 |
| 2026-10-18 15:53 | favourite | cs2 | Nuclear TigeRES | ex-RUSTEC | NO ex-RUSTEC | 12 | 0.67 | 0.65 | 0.65 | won | $3.77 |
| 2026-10-18 15:53 | favourite | cs2 | FORZE Reload | BakS eSports | NO BakS eSports | 14 | 0.60 | 0.58 | 0.58 | won | $5.36 |
| 2026-10-18 15:53 | model-only | cs2 | ex-RUSTEC | Nuclear TigeRES | YES ex-RUSTEC | 29 | 0.37 | 0.46 | 0.35 | lost | -$11.21 |
| 2026-10-18 15:53 | model-only | cs2 | BakS eSports | FORZE Reload | YES BakS eSports | 23 | 0.43 | 0.49 | 0.42 | lost | -$10.29 |
| 2026-10-18 15:53 | model-only | cs2 | mellren | UNiTY esports | YES mellren | 29 | 0.37 | 0.51 | 0.35 | lost | -$11.21 |
| 2026-10-18 15:53 | favourite | cs2 | UNiTY esports | mellren | NO mellren | 8 | 0.67 | 0.65 | 0.65 | won | $2.51 |
| 2026-10-18 14:53 | favourite | cs2 | Damajuana | A NATA | YES Damajuana | 16 | 0.52 | 0.51 | 0.51 | won | $7.40 |
| 2026-10-18 14:53 | model-only | cs2 | A NATA | Damajuana | YES A NATA | 20 | 0.51 | 0.61 | 0.49 | lost | -$10.55 |
| 2026-10-18 13:53 | favourite | dota2 | Power Rangers | Nemiga Gaming | YES Power Rangers | 14 | 0.58 | 0.58 | 0.58 | won | $5.64 |
| 2026-10-18 13:53 | favourite | cs2 | FURIA | BetBoom Team | NO BetBoom Team | 11 | 0.74 | 0.73 | 0.73 | won | $2.71 |
| 2026-10-18 13:53 | model-only | cs2 | BetBoom Team | FURIA | NO FURIA | 38 | 0.27 | 0.45 | 0.27 | lost | -$10.79 |
| 2026-10-18 12:53 | favourite | cs2 | Spirit Academy | mellren | YES Spirit Academy | 15 | 0.55 | 0.53 | 0.53 | won | $6.49 |
| 2026-10-18 12:53 | model-only | cs2 | Lavked | UPGRADE | YES Lavked | 28 | 0.36 | 0.45 | 0.35 | won | $17.46 |
| 2026-10-18 12:53 | favourite | cs2 | UPGRADE | Lavked | NO Lavked | 12 | 0.67 | 0.65 | 0.65 | lost | -$8.23 |
| 2026-10-18 12:53 | model-only | cs2 | mellren | Spirit Academy | YES mellren | 21 | 0.49 | 0.58 | 0.47 | lost | -$10.66 |
| 2026-10-18 12:53 | favourite | cs2 | Team Nemesis | EYEBALLERS | NO EYEBALLERS | 12 | 0.70 | 0.68 | 0.68 | won | $3.42 |
| 2026-10-18 12:53 | favourite | cs2 | ILLYRIANS | MORROW | YES ILLYRIANS | 13 | 0.65 | 0.62 | 0.62 | won | $4.34 |
| 2026-10-18 12:53 | model-only | cs2 | Brute | 33 | YES Brute | 26 | 0.38 | 0.56 | 0.35 | won | $15.69 |
| 2026-10-18 12:53 | favourite | cs2 | 33 | Brute | NO Brute | 4 | 0.68 | 0.65 | 0.65 | lost | -$2.79 |
| 2026-10-18 12:38 | favourite | cs2 | Phantom Academy | antidaun | NO antidaun | 10 | 0.85 | 0.83 | 0.83 | won | $1.41 |
| 2026-10-18 12:38 | favourite | cs2 | ex-6666 | Privateer Gaming | NO Privateer Gaming | 10 | 0.85 | 0.83 | 0.83 | won | $1.41 |
| 2026-10-18 12:38 | model-only | cs2 | Privateer Gaming | ex-6666 | YES Privateer Gaming | 1 | 0.18 | 0.38 | 0.17 | lost | -$0.20 |

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

