# Esports paper trading (fake money)

Updated 2026-10-13 16:22 UTC. Model fitted 2026-10-12T19:16. Every bet below is simulated: the trader only reads Kalshi's public market data and never places orders.

## Books

| Book | What it does | Bets | Open | Settled | Won | P&L | ROI | Closing-line value | Equity |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blend | model + market blend (the strategy under test) | 0 | 0 | 0 | 0 | $0.00 | - | - | $1,000.00 |
| model-only | Elo win model alone (control: ignores the market) | 146 | 13 | 133 | 34 | -$274.75 | -16.3% | -0.8c (141) | $725.25 |
| favourite | 1% flat on the market favourite (no-skill baseline) | 206 | 19 | 187 | 130 | -$87.11 | -6.2% | -0.8c (202) | $912.89 |

Each book started with $1,000 of fake money. ROI is P&L over money staked on settled bets. Closing-line value is the market's probability of the backed team near the start minus the price paid (bets with a snapshot); it shows skill long before P&L can.

97 bets on games outside the trial (ebasketballgame, esoccergame, mlbb) were voided and their stakes returned: Kalshi listed those series after the trial began (Oct 8-10 2026), they are not games the model was built or tested on, and most had no real order book. They are not counted above.

## Forecast scoring on the matches the trader looked at

512 finished matches. Lower is better; the market line is the bar to beat.

| Forecast | Log loss | Brier |
|---|---:|---:|
| market | 0.5629 | 0.1910 |
| model | 0.6639 | 0.2354 |
| blend | 0.5616 | 0.1905 |

| Game | Matches | Market log loss | Model log loss |
|---|---:|---:|---:|
| cs2 | 336 | 0.5803 | 0.6645 |
| dota2 | 55 | 0.5069 | 0.6436 |
| lol | 48 | 0.5033 | 0.7254 |
| ow | 34 | 0.4812 | 0.5596 |
| r6 | 25 | 0.6521 | 0.7187 |
| valorant | 14 | 0.6110 | 0.6746 |

## Latest bets

Prob is the book's probability that the backed team wins; Market is the market's (mid price) at the decision.

| Placed (UTC) | Book | Game | Backs | vs | Side | Qty | Price | Prob | Market | Status | P&L |
|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|
| 2026-10-13 15:52 | favourite | cs2 | Black Phoenix | 6666 | YES Black Phoenix | 1 | 0.77 | 0.72 | 0.72 | open | - |
| 2026-10-13 15:52 | favourite | cs2 | Spirit Academy Green | Fraternity | YES Spirit Academy Green | 12 | 0.70 | 0.69 | 0.69 | open | - |
| 2026-10-13 15:52 | model-only | cs2 | Fraternity | Spirit Academy Green | YES Fraternity | 3 | 0.32 | 0.43 | 0.31 | open | - |
| 2026-10-13 14:52 | favourite | r6 | G2 Esports | Geekay Esports | YES G2 Esports | 12 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-10-13 14:52 | model-only | r6 | Geekay Esports | G2 Esports | NO G2 Esports | 22 | 0.34 | 0.43 | 0.33 | open | - |
| 2026-10-13 14:52 | favourite | lol | Solary | Anubis Gaming | YES Solary | 10 | 0.85 | 0.83 | 0.83 | open | - |
| 2026-10-13 14:52 | favourite | lol | Galions | Movistar KOI Fénix | NO Movistar KOI Fénix | 10 | 0.82 | 0.81 | 0.81 | open | - |
| 2026-10-13 14:52 | favourite | dota2 | Dawn Bulls | Nemiga Gaming | YES Dawn Bulls | 5 | 0.78 | 0.79 | 0.79 | open | - |
| 2026-10-13 14:52 | favourite | cs2 | Procyon Gaming | Hacha Esports | YES Procyon Gaming | 10 | 0.86 | 0.85 | 0.85 | open | - |
| 2026-10-13 14:52 | favourite | cs2 | eternal premium | Revise | YES eternal premium | 16 | 0.54 | 0.51 | 0.51 | open | - |
| 2026-10-13 12:52 | model-only | cs2 | Saint Sinners | Walczaki | YES Saint Sinners | 31 | 0.47 | 0.53 | 0.47 | open | - |
| 2026-10-13 12:52 | favourite | cs2 | Walczaki | Saint Sinners | YES Walczaki | 17 | 0.52 | 0.53 | 0.53 | open | - |
| 2026-10-13 11:52 | favourite | dota2 | Power Rangers | The Warriors | YES Power Rangers | 13 | 0.68 | 0.67 | 0.67 | open | - |
| 2026-10-13 11:52 | model-only | dota2 | The Warriors | Power Rangers | YES The Warriors | 45 | 0.34 | 0.51 | 0.33 | open | - |
| 2026-10-13 11:52 | favourite | dota2 | Dawn Bulls | Spirit Academy | YES Dawn Bulls | 10 | 0.84 | 0.83 | 0.83 | won | $1.50 |
| 2026-10-13 11:52 | model-only | dota2 | Spirit Academy | Dawn Bulls | NO Dawn Bulls | 2 | 0.19 | 0.33 | 0.17 | lost | -$0.41 |
| 2026-10-13 11:52 | favourite | cs2 | QUINTESSENCIA | Martians | NO Martians | 11 | 0.76 | 0.75 | 0.75 | won | $2.49 |
| 2026-10-13 11:52 | model-only | cs2 | Martians | QUINTESSENCIA | YES Martians | 61 | 0.25 | 0.46 | 0.25 | lost | -$16.06 |
| 2026-10-13 11:52 | favourite | cs2 | Alter Ego | Just Swing | YES Alter Ego | 11 | 0.80 | 0.80 | 0.80 | won | $2.07 |
| 2026-10-13 11:52 | model-only | cs2 | Just Swing | Alter Ego | NO Alter Ego | 69 | 0.22 | 0.42 | 0.20 | lost | -$16.01 |
| 2026-10-13 10:51 | favourite | lol | Nothin'Here | essences | NO essences | 15 | 0.56 | 0.56 | 0.56 | won | $6.34 |
| 2026-10-13 10:51 | model-only | lol | Nothin'Here | essences | NO essences | 27 | 0.56 | 0.63 | 0.56 | won | $11.41 |
| 2026-10-13 10:51 | favourite | ow | 99DIVINE | Please Not Hero Ban | YES 99DIVINE | 2 | 0.89 | 0.86 | 0.86 | won | $0.20 |
| 2026-10-13 09:51 | favourite | cs2 | Bushido Wildcats | ILLYRIANS | YES Bushido Wildcats | 14 | 0.59 | 0.58 | 0.58 | lost | -$8.50 |
| 2026-10-13 09:21 | favourite | cs2 | Vitality Academy | RoundsGG | YES Vitality Academy | 16 | 0.54 | 0.53 | 0.53 | lost | -$8.92 |

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

