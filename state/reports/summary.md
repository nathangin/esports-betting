# Esports paper trading (fake money)

Updated 2026-11-10 13:23 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 647 | 57 | 590 | 209 | -$147.38 | -2.2% | -0.2c (640) | $852.62 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1047 | 90 | 957 | 631 | -$452.67 | -7.5% | -1.6c (1036) | $547.33 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2159 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5858 | 0.2017 |
| model | 0.6515 | 0.2301 |
| blend | 0.5861 | 0.2020 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1372 | 0.5942 | 0.6584 |
| dota2 | 363 | 0.5609 | 0.6399 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 103 | 0.6402 | 0.6754 |
| lol | 97 | 0.5820 | 0.7126 |
| r6 | 83 | 0.5710 | 0.6597 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-10 13:23 | favourite | valorant | Alter Ego x Kertanegara | GAS Esports | YES Alter Ego x Kertanegara | 9 | 0.54 | 0.50 | 0.50 | open | - |
| 2026-11-10 11:53 | model-only | dota2 | Xipto Esports | PlayTime | YES Xipto Esports | 36 | 0.46 | 0.54 | 0.46 | open | - |
| 2026-11-10 11:53 | model-only | dota2 | PuckChamp | CyberHero | NO CyberHero | 116 | 0.14 | 0.25 | 0.13 | open | - |
| 2026-11-10 11:53 | favourite | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 7 | 0.67 | 0.66 | 0.66 | open | - |
| 2026-11-10 11:53 | favourite | dota2 | InterActive Philippines | Yakult's Brothers | YES InterActive Philippines | 8 | 0.60 | 0.58 | 0.58 | open | - |
| 2026-11-10 11:53 | favourite | dota2 | HULIGANI | Amaru Gaming | NO Amaru Gaming | 6 | 0.88 | 0.85 | 0.85 | open | - |
| 2026-11-10 10:53 | favourite | cs2 | ex-Zero Tenacity | ILLYRIANS | NO ILLYRIANS | 7 | 0.70 | 0.70 | 0.70 | open | - |
| 2026-11-10 10:53 | model-only | cs2 | BakS eSports | Team ACES | NO Team ACES | 4 | 0.47 | 0.53 | 0.44 | open | - |
| 2026-11-10 10:53 | favourite | cs2 | Team ACES | BakS eSports | YES Team ACES | 1 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-11-10 10:53 | model-only | cs2 | ILLYRIANS | ex-Zero Tenacity | NO ex-Zero Tenacity | 3 | 0.30 | 0.37 | 0.30 | open | - |
| 2026-11-10 10:53 | favourite | cs2 | Leo Team | PsychoFace | YES Leo Team | 8 | 0.63 | 0.62 | 0.62 | open | - |
| 2026-11-10 10:53 | favourite | dota2 | LenS Team | Cooman Team | YES LenS Team | 8 | 0.62 | 0.59 | 0.59 | open | - |
| 2026-11-10 10:53 | model-only | dota2 | Level Up Academy | oveA | YES Level Up Academy | 32 | 0.49 | 0.55 | 0.48 | open | - |
| 2026-11-10 10:53 | favourite | dota2 | oveA | Level Up Academy | YES oveA | 10 | 0.52 | 0.52 | 0.52 | open | - |
| 2026-11-10 10:23 | favourite | cs2 | The Chosen Few | Passion Academy | YES The Chosen Few | 8 | 0.60 | 0.60 | 0.60 | won | $3.06 |
| 2026-11-10 10:23 | favourite | cs2 | FORZE Reload | MOUZ NXT | NO MOUZ NXT | 7 | 0.75 | 0.75 | 0.75 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | PlayTime | Nemiga Gaming | YES PlayTime | 7 | 0.75 | 0.75 | 0.75 | won | $1.65 |
| 2026-11-10 08:53 | favourite | dota2 | Team Allied | Time to Sleep | YES Team Allied | 7 | 0.76 | 0.75 | 0.75 | won | $1.59 |
| 2026-11-10 08:53 | favourite | dota2 | LEGION | Yellow Submarine | YES LEGION | 9 | 0.53 | 0.53 | 0.53 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | Nemiga Gaming | PlayTime | YES Nemiga Gaming | 32 | 0.26 | 0.31 | 0.25 | lost | -$8.76 |
| 2026-11-10 08:53 | model-only | dota2 | Yellow Submarine | LEGION | NO LEGION | 33 | 0.48 | 0.61 | 0.47 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | potn9ki | Xipto Esports | YES potn9ki | 76 | 0.14 | 0.28 | 0.14 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | Xipto Esports | potn9ki | YES Xipto Esports | 6 | 0.86 | 0.86 | 0.86 | open | - |
| 2026-11-10 08:53 | model-only | dota2 | Zenith | Team Synapse | NO Team Synapse | 111 | 0.14 | 0.23 | 0.13 | open | - |
| 2026-11-10 08:53 | favourite | dota2 | Team Synapse | Zenith | YES Team Synapse | 6 | 0.87 | 0.87 | 0.87 | open | - |

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

