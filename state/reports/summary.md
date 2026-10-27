# Esports paper trading (fake money)

Updated 2026-10-27 11:14 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 395 | 39 | 356 | 117 | -$71.88 | -1.9% | -0.7c (389) | $928.12 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 614 | 49 | 565 | 375 | -$280.32 | -6.9% | -1.4c (607) | $719.68 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1322 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5794 | 0.1988 |
| model | 0.6572 | 0.2328 |
| blend | 0.5790 | 0.1988 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 856 | 0.5935 | 0.6647 |
| dota2 | 197 | 0.5507 | 0.6363 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 81 | 0.5680 | 0.7211 |
| valorant | 61 | 0.5606 | 0.6748 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-27 10:54 | favourite | cs2 | ex-RUSTEC | Spirit Academy | YES ex-RUSTEC | 13 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-10-27 10:54 | model-only | cs2 | Spirit Academy | ex-RUSTEC | NO ex-RUSTEC | 4 | 0.49 | 0.57 | 0.48 | open | - |
| 2026-10-27 10:54 | favourite | cs2 | Nuclear TigeRES | FOKUS | YES Nuclear TigeRES | 14 | 0.51 | 0.51 | 0.51 | open | - |
| 2026-10-27 10:24 | favourite | cs2 | gothboiclique | WonderKids | NO WonderKids | 1 | 0.77 | 0.78 | 0.78 | open | - |
| 2026-10-27 09:53 | model-only | cs2 | Alliance | FaZe | NO FaZe | 52 | 0.31 | 0.42 | 0.30 | open | - |
| 2026-10-27 09:53 | model-only | cs2 | Liquid | Aurora Gaming | NO Aurora Gaming | 58 | 0.28 | 0.37 | 0.28 | open | - |
| 2026-10-27 09:53 | favourite | cs2 | Aurora Gaming | Liquid | YES Aurora Gaming | 9 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-27 09:53 | model-only | cs2 | Nemiga | DENDELE CS | NO DENDELE CS | 27 | 0.60 | 0.69 | 0.59 | open | - |
| 2026-10-27 09:53 | favourite | cs2 | Nemiga | DENDELE CS | NO DENDELE CS | 12 | 0.60 | 0.59 | 0.59 | open | - |
| 2026-10-27 09:53 | favourite | cs2 | FaZe | Alliance | NO Alliance | 10 | 0.70 | 0.69 | 0.70 | open | - |
| 2026-10-27 09:53 | model-only | cs2 | magic | BIG | YES magic | 39 | 0.42 | 0.54 | 0.42 | open | - |
| 2026-10-27 09:53 | favourite | cs2 | BIG | magic | YES BIG | 12 | 0.58 | 0.58 | 0.58 | open | - |
| 2026-10-27 09:53 | favourite | valorant | Wolves Esports | World Sports Invictus Gaming | NO World Sports Invictus Gaming | 10 | 0.70 | 0.70 | 0.70 | open | - |
| 2026-10-27 07:53 | favourite | cs2 | Team Nemesis | Brute | NO Brute | 9 | 0.75 | 0.74 | 0.74 | lost | -$6.87 |
| 2026-10-27 07:53 | model-only | cs2 | Bread Eaters Esports | Prestige | YES Bread Eaters Esports | 14 | 0.30 | 0.40 | 0.28 | open | - |
| 2026-10-27 07:53 | favourite | cs2 | Prestige | Bread Eaters Esports | NO Bread Eaters Esports | 9 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-10-27 07:53 | model-only | cs2 | Brute | Team Nemesis | NO Team Nemesis | 62 | 0.26 | 0.39 | 0.26 | won | $45.04 |
| 2026-10-27 07:53 | model-only | dota2 | Mena Warriors | No Hoodwink | YES Mena Warriors | 70 | 0.23 | 0.41 | 0.23 | open | - |
| 2026-10-27 07:53 | favourite | cs2 | Revise | eternal premium | NO eternal premium | 12 | 0.57 | 0.54 | 0.54 | lost | -$7.05 |
| 2026-10-27 07:53 | favourite | valorant | Unsettled Resentment | Victory No Limits | YES Unsettled Resentment | 9 | 0.73 | 0.72 | 0.72 | open | - |
| 2026-10-27 06:53 | favourite | cs2 | B8 | K27 | YES B8 | 11 | 0.66 | 0.66 | 0.66 | lost | -$7.44 |
| 2026-10-27 06:53 | model-only | cs2 | K27 | B8 | NO B8 | 45 | 0.35 | 0.54 | 0.34 | won | $28.53 |
| 2026-10-27 02:53 | favourite | dota2 | Royal Bear | Cloud Dawning | NO Cloud Dawning | 2 | 0.84 | 0.84 | 0.84 | won | $0.30 |
| 2026-10-27 01:53 | favourite | cs2 | Abyssal | Rooster | YES Abyssal | 12 | 0.57 | 0.55 | 0.55 | lost | -$7.05 |
| 2026-10-27 01:53 | model-only | cs2 | Rooster | Abyssal | YES Rooster | 35 | 0.46 | 0.54 | 0.45 | won | $18.29 |

## Backtest on real Kalshi prices

8779 settled matches from 2026-05-28 to 2026-10-26, decided 60 min before scheduled start at the quoted bid/ask, with Kalshi's taker fee. Ratings, the win model and the blend only ever use earlier matches (weekly walk-forward refits).

| Strategy | Bets | Staked | P&L | ROI | 95% range | Hit rate | Closing-line value | Max drawdown |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| model + market blend | 24 | $444.79 | -$1.79 | -0.4% | -34.5% to +46.3% | 58% | +0.0c | 8% |
| model only | 2012 | $8,014.92 | -$990.92 | -12.4% | -20.6% to -4.1% | 33% | -0.6c | 99% |
| always the favourite (1% flat) | 4205 | $16,392.93 | -$775.93 | -4.7% | -7.0% to -2.5% | 67% | -1.6c | 81% |
| always the underdog (1% flat) | 3757 | $9,447.49 | -$982.49 | -10.4% | -15.7% to -4.8% | 31% | -1.3c | 98% |

Closing-line value: the market's probability at the scheduled start of the side bought, minus the price paid, averaged over bets. Around zero means the bets saw nothing the market did not price in by the start.

Forecast quality on the same 8554 matches (lower is better):

| Forecast | Log loss | Brier | Picks the winner |
|---|---:|---:|---:|
| market | 0.5736 | 0.1961 | 69.2% |
| model | 0.6609 | 0.2344 | 59.5% |
| blend | 0.5732 | 0.1960 | - |

Is the market's favourite priced right?

| Market favourite at | Matches | Average price | Won |
|---|---:|---:|---:|
| (0.499, 0.55] | 1402 | 0.525 | 0.529 |
| (0.55, 0.6] | 1444 | 0.577 | 0.551 |
| (0.6, 0.65] | 1325 | 0.626 | 0.629 |
| (0.65, 0.7] | 1152 | 0.676 | 0.702 |
| (0.7, 0.75] | 964 | 0.726 | 0.772 |
| (0.75, 0.8] | 823 | 0.776 | 0.810 |
| (0.8, 0.85] | 698 | 0.826 | 0.827 |
| (0.85, 0.9] | 521 | 0.877 | 0.902 |
| (0.9, 1.0] | 450 | 0.932 | 0.956 |

