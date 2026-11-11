# Esports paper trading (fake money)

Updated 2026-11-11 05:01 UTC. Model fitted 2026-11-09T19:54. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 654 | 52 | 602 | 211 | -$252.06 | -3.8% | -0.3c (646) | $747.94 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 1059 | 81 | 978 | 647 | -$436.25 | -7.1% | -1.6c (1048) | $563.75 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

2209 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5846 | 0.2012 |
| model | 0.6508 | 0.2298 |
| blend | 0.5848 | 0.2014 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1395 | 0.5930 | 0.6577 |
| dota2 | 380 | 0.5611 | 0.6383 |
| ow | 121 | 0.5304 | 0.5383 |
| valorant | 112 | 0.6294 | 0.6734 |
| lol | 97 | 0.5820 | 0.7126 |
| r6 | 84 | 0.5712 | 0.6603 |
| cod | 20 | 0.5911 | 0.6189 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-11 03:20 | favourite | cs2 | Vitality | Team Falcons | NO Team Falcons | 1 | 0.69 | 0.69 | 0.70 | open | - |
| 2026-11-11 03:20 | model-only | cs2 | Team Falcons | Vitality | NO Vitality | 48 | 0.30 | 0.40 | 0.30 | open | - |
| 2026-11-11 02:20 | favourite | r6 | DarkZero Esports | Weibo Gaming | YES DarkZero Esports | 8 | 0.66 | 0.65 | 0.65 | won | $2.59 |
| 2026-11-11 02:20 | model-only | r6 | Weibo Gaming | DarkZero Esports | YES Weibo Gaming | 41 | 0.35 | 0.52 | 0.35 | lost | -$15.01 |
| 2026-11-11 00:50 | favourite | cs2 | FURIA | Legacy | YES FURIA | 7 | 0.72 | 0.71 | 0.71 | won | $1.86 |
| 2026-11-10 20:50 | favourite | cs2 | QUINTESSENCIA | Rush | YES QUINTESSENCIA | 2 | 0.58 | 0.56 | 0.56 | lost | -$1.20 |
| 2026-11-10 16:54 | favourite | cs2 | BoyBand | KUUSAMO.gg | YES BoyBand | 1 | 0.54 | 0.54 | 0.54 | won | $0.44 |
| 2026-11-10 15:54 | model-only | cs2 | B8 Academy | los kogutos | YES B8 Academy | 23 | 0.27 | 0.48 | 0.24 | open | - |
| 2026-11-10 14:54 | favourite | cs2 | MEIA NOITE | BORRACHEIROS | NO BORRACHEIROS | 8 | 0.61 | 0.60 | 0.60 | won | $2.98 |
| 2026-11-10 14:54 | model-only | cs2 | BORRACHEIROS | MEIA NOITE | YES BORRACHEIROS | 38 | 0.40 | 0.57 | 0.40 | lost | -$15.84 |
| 2026-11-10 14:54 | model-only | dota2 | InterActive Philippines | CyberHero | NO CyberHero | 1 | 0.15 | 0.35 | 0.14 | lost | -$0.16 |
| 2026-11-10 14:54 | favourite | dota2 | CyberHero | InterActive Philippines | YES CyberHero | 6 | 0.87 | 0.86 | 0.86 | won | $0.73 |
| 2026-11-10 14:54 | favourite | dota2 | Froglings | Power Rangers | YES Froglings | 4 | 0.78 | 0.78 | 0.78 | lost | -$3.17 |
| 2026-11-10 13:53 | favourite | dota2 | Xipto Esports | Mena Warriors | NO Mena Warriors | 9 | 0.57 | 0.55 | 0.55 | open | - |
| 2026-11-10 13:53 | model-only | dota2 | Xipto Esports | Mena Warriors | NO Mena Warriors | 27 | 0.57 | 0.79 | 0.55 | open | - |
| 2026-11-10 13:53 | favourite | cs2 | G2 Ares | maybe | YES G2 Ares | 9 | 0.55 | 0.55 | 0.55 | lost | -$5.11 |
| 2026-11-10 13:53 | favourite | cs2 | Butterfly | Honvéd | YES Butterfly | 7 | 0.69 | 0.69 | 0.69 | won | $2.06 |
| 2026-11-10 13:53 | model-only | cs2 | Honvéd | Butterfly | YES Honvéd | 49 | 0.31 | 0.43 | 0.31 | lost | -$15.93 |
| 2026-11-10 13:53 | favourite | cs2 | FORZE Reload | ex-RUSTEC | NO ex-RUSTEC | 3 | 0.59 | 0.59 | 0.59 | won | $1.17 |
| 2026-11-10 13:23 | favourite | valorant | Alter Ego x Kertanegara | GAS Esports | YES Alter Ego x Kertanegara | 9 | 0.54 | 0.50 | 0.50 | open | - |
| 2026-11-10 11:53 | favourite | dota2 | Inner Circle | Zero Tenacity | YES Inner Circle | 7 | 0.67 | 0.66 | 0.66 | won | $2.20 |
| 2026-11-10 11:53 | favourite | dota2 | InterActive Philippines | Yakult's Brothers | YES InterActive Philippines | 8 | 0.60 | 0.58 | 0.58 | won | $3.06 |
| 2026-11-10 11:53 | favourite | dota2 | HULIGANI | Amaru Gaming | NO Amaru Gaming | 6 | 0.88 | 0.85 | 0.85 | won | $0.67 |
| 2026-11-10 11:53 | model-only | dota2 | PuckChamp | CyberHero | NO CyberHero | 116 | 0.14 | 0.25 | 0.13 | lost | -$17.22 |
| 2026-11-10 11:53 | model-only | dota2 | Xipto Esports | PlayTime | YES Xipto Esports | 36 | 0.46 | 0.54 | 0.46 | won | $18.81 |

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

