# Esports paper trading (fake money)

Updated 2026-11-02 17:23 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 1 | 0 | 1 | 1 | $10.02 | +50.2% | +4.0c (1) | $1,010.02 |
| model-only | Elo win model alone (control: ignores the market) | 496 | 40 | 456 | 154 | -$83.99 | -1.7% | -0.3c (488) | $916.01 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 809 | 60 | 749 | 491 | -$413.48 | -8.1% | -1.5c (797) | $586.52 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1658 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5823 | 0.2003 |
| model | 0.6520 | 0.2305 |
| blend | 0.5824 | 0.2005 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 1084 | 0.5934 | 0.6604 |
| dota2 | 254 | 0.5518 | 0.6294 |
| ow | 105 | 0.5083 | 0.5287 |
| lol | 89 | 0.5778 | 0.7239 |
| valorant | 82 | 0.6127 | 0.6718 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-11-02 16:53 | favourite | cs2 | STATE | ECSTATIC | NO ECSTATIC | 4 | 0.77 | 0.76 | 0.76 | open | - |
| 2026-11-02 16:53 | favourite | cs2 | ILLYRIANS | Sokerorg | YES ILLYRIANS | 9 | 0.58 | 0.56 | 0.56 | open | - |
| 2026-11-02 16:53 | favourite | cs2 | ex-ENCE | SINQU | YES ex-ENCE | 6 | 0.89 | 0.88 | 0.88 | open | - |
| 2026-11-02 16:53 | favourite | cs2 | LPH Gaming | eSuba | NO eSuba | 8 | 0.65 | 0.64 | 0.64 | open | - |
| 2026-11-02 16:53 | model-only | cs2 | eSuba | LPH Gaming | NO LPH Gaming | 11 | 0.36 | 0.48 | 0.36 | open | - |
| 2026-11-02 16:53 | favourite | cs2 | KUUSAMO.gg | BOJONG | NO BOJONG | 8 | 0.66 | 0.64 | 0.64 | open | - |
| 2026-11-02 16:53 | model-only | cs2 | BOJONG | KUUSAMO.gg | YES BOJONG | 47 | 0.38 | 0.51 | 0.36 | open | - |
| 2026-11-02 15:53 | favourite | cs2 | PARTIZAN | Regnum4Games | YES PARTIZAN | 10 | 0.53 | 0.52 | 0.52 | open | - |
| 2026-11-02 15:53 | model-only | cs2 | XI Esport | ECSTATIC | NO ECSTATIC | 14 | 0.58 | 0.66 | 0.55 | open | - |
| 2026-11-02 15:53 | favourite | cs2 | XI Esport | ECSTATIC | NO ECSTATIC | 9 | 0.58 | 0.55 | 0.55 | open | - |
| 2026-11-02 15:53 | favourite | cs2 | MASONIC | MASQ | NO MASQ | 7 | 0.76 | 0.73 | 0.73 | open | - |
| 2026-11-02 15:53 | model-only | cs2 | Regnum4Games | PARTIZAN | NO PARTIZAN | 36 | 0.50 | 0.63 | 0.48 | open | - |
| 2026-11-02 15:53 | favourite | cs2 | STATE | EAC Extra | NO EAC Extra | 7 | 0.79 | 0.78 | 0.78 | open | - |
| 2026-11-02 15:53 | model-only | cs2 | EAC Extra | STATE | YES EAC Extra | 14 | 0.24 | 0.41 | 0.23 | open | - |
| 2026-11-02 15:53 | model-only | cs2 | Vitality Academy | Young TigeRES | YES Vitality Academy | 73 | 0.24 | 0.34 | 0.22 | open | - |
| 2026-11-02 15:53 | favourite | cs2 | Young TigeRES | Vitality Academy | YES Young TigeRES | 3 | 0.78 | 0.78 | 0.78 | open | - |
| 2026-11-02 14:23 | favourite | cs2 | HAVU | Nordic Valor | YES HAVU | 6 | 0.87 | 0.86 | 0.86 | open | - |
| 2026-11-02 13:53 | favourite | cs2 | Spirit Academy | Noir Verse | NO Noir Verse | 7 | 0.83 | 0.80 | 0.80 | open | - |
| 2026-11-02 13:53 | model-only | cs2 | Misa Esports | PsychoFace | YES Misa Esports | 38 | 0.47 | 0.69 | 0.46 | lost | -$18.53 |
| 2026-11-02 13:53 | favourite | cs2 | PsychoFace | Misa Esports | NO Misa Esports | 10 | 0.54 | 0.54 | 0.54 | won | $4.42 |
| 2026-11-02 13:53 | favourite | cs2 | Saint Sinners | Lilmix | NO Lilmix | 7 | 0.74 | 0.72 | 0.72 | open | - |
| 2026-11-02 13:53 | model-only | cs2 | Lilmix | Saint Sinners | YES Lilmix | 57 | 0.30 | 0.37 | 0.28 | open | - |
| 2026-11-02 11:52 | favourite | dota2 | OG | Yellow Submarine | YES OG | 8 | 0.73 | 0.73 | 0.73 | lost | -$5.96 |
| 2026-11-02 10:52 | favourite | dota2 | HellNight- | potn9ki | YES HellNight- | 10 | 0.56 | 0.54 | 0.54 | lost | -$5.78 |
| 2026-11-02 10:52 | favourite | cs2 | Leo Team | Saint Sinners | NO Saint Sinners | 9 | 0.62 | 0.63 | 0.63 | won | $3.27 |

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

