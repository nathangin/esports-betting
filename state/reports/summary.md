# Esports paper trading (fake money)

Updated 2026-11-09 09:40 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 623 | 54 | 569 | 202 | -$185.92 | -2.9% | -0.3c (612) | $814.08 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1004 | 83 | 921 | 609 | -$446.62 | -7.6% | -1.6c (990) | $553.38 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2091 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5847 | 0.2013 |
| model | 0.6513 | 0.2300 |
| blend | 0.5849 | 0.2015 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1333 | 0.5936 | 0.6579 |
| dota2 | 343 | 0.5589 | 0.6387 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 102 | 0.6397 | 0.6752 |
| lol | 95 | 0.5646 | 0.7154 |
| r6 | 77 | 0.5815 | 0.6664 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-09 08:50 | favourite | dota2 | Zero Tenacity | Spirit Academy | NO Spirit Academy | 7 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Spirit Academy | Zero Tenacity | YES Spirit Academy | 31 | 0.36 | 0.41 | 0.34 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Yellow Submarine | Xipto Esports | YES Yellow Submarine | 8 | 0.62 | 0.62 | 0.62 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Xipto Esports | Yellow Submarine | YES Xipto Esports | 25 | 0.38 | 0.49 | 0.38 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Froglings | Team Synapse | YES Froglings | 7 | 0.72 | 0.70 | 0.70 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | Power Rangers | Nemiga Gaming | NO Nemiga Gaming | 3 | 0.74 | 0.73 | 0.73 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Nemiga Gaming | Power Rangers | NO Power Rangers | 57 | 0.27 | 0.48 | 0.27 | open | - |
| 2026-11-09 08:50 | favourite | dota2 | HULIGANI | Xipto Esports | YES HULIGANI | 9 | 0.59 | 0.58 | 0.58 | open | - |
| 2026-11-09 08:50 | model-only | dota2 | Xipto Esports | HULIGANI | NO HULIGANI | 36 | 0.43 | 0.65 | 0.42 | open | - |
| 2026-11-09 07:50 | favourite | cs2 | Prestige | Sokerorg | YES Prestige | 9 | 0.56 | 0.55 | 0.55 | open | - |
| 2026-11-09 07:50 | favourite | cs2 | FORZE Reload | maybe | YES FORZE Reload | 7 | 0.71 | 0.70 | 0.70 | open | - |
| 2026-11-09 07:50 | favourite | cs2 | Walczaki | Noir Verse | YES Walczaki | 9 | 0.59 | 0.59 | 0.59 | open | - |
| 2026-11-09 07:50 | model-only | cs2 | TheChampionGG | STATE | YES TheChampionGG | 153 | 0.10 | 0.26 | 0.08 | open | - |
| 2026-11-09 04:24 | favourite | r6 | Team Liquid | Geekay Esports | NO Geekay Esports | 1 | 0.62 | 0.60 | 0.60 | won | $0.36 |
| 2026-11-09 04:24 | favourite | r6 | Fluxo W7M | EDward Gaming | NO EDward Gaming | 6 | 0.85 | 0.83 | 0.83 | won | $0.84 |
| 2026-11-09 01:24 | favourite | r6 | FaZe Clan | Falcons Esport | YES FaZe Clan | 9 | 0.57 | 0.57 | 0.57 | lost | -$5.29 |
| 2026-11-09 01:24 | favourite | r6 | 100 Thieves | ENTERPRISE Esports | NO ENTERPRISE Esports | 7 | 0.71 | 0.70 | 0.70 | won | $1.92 |
| 2026-11-09 01:24 | model-only | r6 | ENTERPRISE Esports | 100 Thieves | YES ENTERPRISE Esports | 52 | 0.30 | 0.52 | 0.30 | lost | -$16.37 |
| 2026-11-09 00:24 | favourite | r6 | M80 | Sharper Esport | YES M80 | 9 | 0.57 | 0.56 | 0.56 | open | - |
| 2026-11-09 00:24 | model-only | r6 | Sharper Esport | M80 | NO M80 | 12 | 0.47 | 0.55 | 0.44 | open | - |
| 2026-11-08 14:53 | favourite | cs2 | RED Canids Academy | BESTIA Academy | YES RED Canids Academy | 3 | 0.66 | 0.67 | 0.67 | won | $0.97 |
| 2026-11-08 13:53 | favourite | cs2 | SAW Youngsters | MASONIC | NO MASONIC | 3 | 0.54 | 0.54 | 0.53 | lost | -$1.68 |
| 2026-11-08 12:52 | model-only | cs2 | G2 Ares | PRIVATE | NO PRIVATE | 1 | 0.18 | 0.33 | 0.17 | lost | -$0.20 |
| 2026-11-08 12:52 | model-only | cs2 | 6yuBoJlbl | 9INE | NO 9INE | 10 | 0.36 | 0.53 | 0.35 | lost | -$3.77 |
| 2026-11-08 12:52 | favourite | cs2 | 9INE | 6yuBoJlbl | YES 9INE | 8 | 0.66 | 0.65 | 0.65 | won | $2.59 |

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

