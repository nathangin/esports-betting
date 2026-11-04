# Esports paper trading (fake money)

Updated 2026-11-04 00:53 UTC. Model fitted 2026-11-02T19:35. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 517 | 37 | 480 | 166 | -$104.59 | -2.0% | -0.3c (509) | $895.41 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 839 | 56 | 783 | 511 | -$452.88 | -8.6% | -1.5c (831) | $547.12 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1746 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5817 | 0.2001 |
| model | 0.6517 | 0.2303 |
| blend | 0.5817 | 0.2002 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1152 | 0.5947 | 0.6609 |
| dota2 | 272 | 0.5415 | 0.6244 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 46 | 0.6128 | 0.6882 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-04 00:53 | favourite | cs2 | Team Falcons | Heroic | NO Heroic | 7 | 0.68 | 0.68 | 0.68 | open | - |
| 2026-11-04 00:53 | model-only | cs2 | Heroic | Team Falcons | NO Team Falcons | 51 | 0.33 | 0.52 | 0.32 | open | - |
| 2026-11-03 14:21 | model-only | cs2 | BoyBand | RoundsGG | YES BoyBand | 15 | 0.57 | 0.62 | 0.56 | won | $6.19 |
| 2026-11-03 13:51 | favourite | cs2 | Walczaki | SINQU | YES Walczaki | 6 | 0.58 | 0.58 | 0.58 | won | $2.41 |
| 2026-11-03 13:51 | model-only | cs2 | Walczaki | SINQU | YES Walczaki | 6 | 0.58 | 0.71 | 0.58 | won | $2.41 |
| 2026-11-03 13:51 | favourite | cs2 | Brute | Nexus | YES Brute | 9 | 0.60 | 0.59 | 0.59 | won | $3.44 |
| 2026-11-03 13:51 | favourite | cs2 | Leo Team | ILLYRIANS | NO ILLYRIANS | 8 | 0.61 | 0.58 | 0.58 | won | $2.98 |
| 2026-11-03 13:21 | favourite | dota2 | Daxak Team | Stray Team | YES Daxak Team | 8 | 0.67 | 0.65 | 0.65 | won | $2.51 |
| 2026-11-03 12:51 | model-only | cs2 | mellren | Lilmix | NO Lilmix | 26 | 0.61 | 0.75 | 0.58 | lost | -$16.30 |
| 2026-11-03 12:51 | favourite | cs2 | Acend | Four Magic | NO Four Magic | 1 | 0.85 | 0.85 | 0.85 | won | $0.14 |
| 2026-11-03 12:51 | favourite | cs2 | WRAITH PCIFIC | Falcons Force | YES WRAITH PCIFIC | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-03 12:51 | model-only | cs2 | KUUSAMO.gg | BakS eSports | NO BakS eSports | 155 | 0.11 | 0.26 | 0.10 | lost | -$18.12 |
| 2026-11-03 12:51 | favourite | cs2 | BakS eSports | KUUSAMO.gg | YES BakS eSports | 6 | 0.90 | 0.90 | 0.90 | won | $0.56 |
| 2026-11-03 12:51 | favourite | cs2 | Saint Sinners | Drama eSports | NO Drama eSports | 9 | 0.55 | 0.53 | 0.53 | open | - |
| 2026-11-03 12:51 | favourite | cs2 | mellren | Lilmix | NO Lilmix | 8 | 0.61 | 0.58 | 0.58 | lost | -$5.02 |
| 2026-11-03 12:51 | favourite | cs2 | Rebels Gaming | maybe | NO maybe | 6 | 0.83 | 0.83 | 0.83 | open | - |
| 2026-11-03 12:51 | model-only | cs2 | Drama eSports | Saint Sinners | YES Drama eSports | 35 | 0.50 | 0.64 | 0.47 | open | - |
| 2026-11-03 11:51 | model-only | dota2 | PuckChamp | Xipto Esports | YES PuckChamp | 98 | 0.14 | 0.20 | 0.13 | lost | -$14.55 |
| 2026-11-03 11:51 | favourite | dota2 | CyberHero | Nemiga Gaming | NO Nemiga Gaming | 7 | 0.69 | 0.69 | 0.69 | won | $2.06 |
| 2026-11-03 11:51 | favourite | cs2 | Rush | MIBR fe | NO MIBR fe | 9 | 0.57 | 0.57 | 0.57 | open | - |
| 2026-11-03 11:51 | favourite | dota2 | Xipto Esports | PuckChamp | YES Xipto Esports | 6 | 0.88 | 0.87 | 0.87 | won | $0.67 |
| 2026-11-03 10:51 | favourite | cs2 | Spirit Academy | PsychoFace | YES Spirit Academy | 9 | 0.55 | 0.54 | 0.53 | lost | -$5.11 |
| 2026-11-03 10:51 | model-only | cs2 | Spirit Academy | PsychoFace | YES Spirit Academy | 32 | 0.55 | 0.77 | 0.53 | lost | -$18.16 |
| 2026-11-03 10:51 | favourite | cs2 | GenOne | Lilmix | NO Lilmix | 2 | 0.79 | 0.76 | 0.76 | won | $0.39 |
| 2026-11-03 10:20 | favourite | cs2 | XI Esport | 9INE Academy | NO 9INE Academy | 7 | 0.73 | 0.72 | 0.72 | lost | -$5.21 |

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

