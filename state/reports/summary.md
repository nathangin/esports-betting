# Esports paper trading (fake money)

Updated 2026-10-27 04:43 UTC. Model fitted 2026-10-26T16:12. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 386 | 33 | 353 | 114 | -$163.74 | -4.5% | -0.7c (381) | $836.26 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 601 | 41 | 560 | 374 | -$252.21 | -6.2% | -1.4c (597) | $747.79 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

1315 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5789 | 0.1986 |
| model | 0.6576 | 0.2330 |
| blend | 0.5784 | 0.1985 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 850 | 0.5924 | 0.6649 |
| dota2 | 196 | 0.5526 | 0.6386 |
| ow | 83 | 0.5090 | 0.5369 |
| lol | 81 | 0.5680 | 0.7211 |
| valorant | 61 | 0.5606 | 0.6748 |
| r6 | 44 | 0.6133 | 0.6886 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-27 02:53 | favourite | dota2 | Royal Bear | Cloud Dawning | NO Cloud Dawning | 2 | 0.84 | 0.84 | 0.84 | open | - |
| 2026-10-27 01:53 | favourite | cs2 | Abyssal | Rooster | YES Abyssal | 12 | 0.57 | 0.55 | 0.55 | open | - |
| 2026-10-27 01:53 | model-only | cs2 | Rooster | Abyssal | YES Rooster | 35 | 0.46 | 0.54 | 0.45 | open | - |
| 2026-10-26 19:52 | model-only | cs2 | QUINTESSENCIA | MEIA NOITE | YES QUINTESSENCIA | 1 | 0.43 | 0.57 | 0.40 | open | - |
| 2026-10-26 19:52 | model-only | cs2 | ARK E-sports | ALKA | NO ALKA | 1 | 0.21 | 0.41 | 0.19 | open | - |
| 2026-10-26 16:51 | model-only | cs2 | TTG Esports | Diamant Esports | YES TTG Esports | 5 | 0.59 | 0.70 | 0.59 | open | - |
| 2026-10-26 15:51 | favourite | cs2 | Natus Vincere | BetBoom Team | NO BetBoom Team | 6 | 0.63 | 0.62 | 0.62 | lost | -$3.88 |
| 2026-10-26 15:51 | favourite | cs2 | ECSTATIC | MASQ | YES ECSTATIC | 10 | 0.74 | 0.72 | 0.72 | lost | -$7.54 |
| 2026-10-26 15:51 | model-only | cs2 | MASQ | ECSTATIC | NO ECSTATIC | 6 | 0.30 | 0.51 | 0.28 | won | $4.11 |
| 2026-10-26 15:51 | favourite | cs2 | G2 | DENDELE CS | NO DENDELE CS | 10 | 0.75 | 0.74 | 0.74 | lost | -$7.64 |
| 2026-10-26 15:51 | model-only | cs2 | DENDELE CS | G2 | YES DENDELE CS | 56 | 0.26 | 0.43 | 0.26 | won | $40.68 |
| 2026-10-26 15:51 | favourite | cs2 | BIG Academy | Sissi State Punks | YES BIG Academy | 8 | 0.89 | 0.87 | 0.87 | won | $0.82 |
| 2026-10-26 15:21 | favourite | cs2 | Aurora Young Blood | Four Magic | YES Aurora Young Blood | 10 | 0.71 | 0.67 | 0.67 | won | $2.75 |
| 2026-10-26 15:21 | model-only | cs2 | DINERO | TTG Esports | YES DINERO | 1 | 0.25 | 0.43 | 0.27 | lost | -$0.27 |
| 2026-10-26 15:21 | favourite | cs2 | TTG Esports | DINERO | NO DINERO | 1 | 0.78 | 0.73 | 0.73 | won | $0.20 |
| 2026-10-26 13:51 | favourite | cs2 | Nuclear TigeRES | UNiTY esports | YES Nuclear TigeRES | 1 | 0.65 | 0.65 | 0.65 | won | $0.33 |
| 2026-10-26 13:51 | model-only | cs2 | UNiTY esports | Nuclear TigeRES | YES UNiTY esports | 42 | 0.35 | 0.55 | 0.35 | lost | -$15.37 |
| 2026-10-26 13:51 | favourite | cs2 | ILLYRIANS | HAVU | NO HAVU | 14 | 0.53 | 0.52 | 0.52 | won | $6.33 |
| 2026-10-26 12:51 | favourite | dota2 | PARIVISION | Team Spirit | YES PARIVISION | 12 | 0.64 | 0.64 | 0.64 | lost | -$7.88 |
| 2026-10-26 12:51 | model-only | dota2 | Team Spirit | PARIVISION | NO PARIVISION | 38 | 0.37 | 0.48 | 0.36 | won | $23.31 |
| 2026-10-26 12:51 | favourite | cs2 | Legacy | Liquid | YES Legacy | 11 | 0.71 | 0.70 | 0.70 | lost | -$7.97 |
| 2026-10-26 12:51 | model-only | cs2 | Liquid | Legacy | NO Legacy | 47 | 0.30 | 0.43 | 0.30 | won | $32.20 |
| 2026-10-26 12:51 | favourite | cs2 | Spirit | FURIA | NO FURIA | 12 | 0.64 | 0.64 | 0.64 | won | $4.12 |
| 2026-10-26 12:51 | model-only | cs2 | FURIA | Spirit | NO Spirit | 27 | 0.37 | 0.42 | 0.36 | lost | -$10.44 |
| 2026-10-26 10:50 | favourite | cs2 | Metizport | Brute | YES Metizport | 13 | 0.58 | 0.57 | 0.57 | lost | -$7.77 |

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

