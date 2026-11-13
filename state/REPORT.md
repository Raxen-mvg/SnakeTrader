# Paper trading report

Updated 2026-11-13 10:46 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,711 | +10.36% | 0 | - | 236 |
| benchmark | 220,173 | +10.09% | 0 | - | 237 |
| snake_abs_exit_conv | 217,224 | +8.61% | 2 | 50% | 345 |
| snake_abs_exit | 217,207 | +8.60% | 2 | 50% | 345 |
| intraweek | 216,124 | +8.06% | 30 | 53% | 3,302 |
| oracle | 213,849 | +6.92% | 0 | - | 233 |
| snake_abs | 213,137 | +6.57% | 1 | 100% | 255 |
| snake_abs_conv | 212,969 | +6.49% | 1 | 100% | 255 |
| intramonth | 211,469 | +5.74% | 0 | - | 235 |
| random_hold | 207,408 | +3.70% | 10 | 70% | 733 |
| snake_viper_wild | 206,723 | +3.36% | 14 | 50% | 2,496 |
| snake_anaconda | 205,107 | +2.55% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,188 | +1.59% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,374 | -7.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,244 (-3.88%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,466 | +0.68% |
| snake_viper_wild | +1,431 | +0.70% |
| snake_viper_tick | +1,406 | +0.70% |
| oracle | +733 | +0.34% |
| benchmark_smallcap | +493 | +0.24% |
| unified | +14 | +0.01% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -124 | -0.06% |
| snake_abs_exit | -235 | -0.11% |
| benchmark | -375 | -0.17% |
| random_hold | -646 | -0.31% |
| snake_anaconda | -821 | -0.40% |
| gold | -937 | -0.51% |
| snake_abs_exit_conv | -1,450 | -0.66% |
| snake_abs_conv | -2,566 | -1.19% |
| snake_abs | -2,575 | -1.19% |

Average per day so far: unified Rs +628, benchmark Rs +611, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +574, intraweek Rs +489, snake_abs_conv Rs +432, snake_abs Rs +424, oracle Rs +420, intramonth Rs +348, snake_viper_wild Rs +269, random_hold Rs +224, snake_anaconda Rs +182, snake_viper_tick Rs +145, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -474

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.