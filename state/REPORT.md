# Paper trading report

Updated 2026-11-19 13:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,744 | +11.87% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,357 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 212,997 | +6.50% | 2 | 50% | 345 |
| intraweek | 211,939 | +5.97% | 35 | 54% | 3,851 |
| oracle | 211,501 | +5.75% | 0 | - | 233 |
| snake_abs_exit_conv | 211,064 | +5.53% | 2 | 50% | 345 |
| snake_abs | 208,593 | +4.30% | 1 | 100% | 255 |
| snake_abs_conv | 208,467 | +4.23% | 1 | 100% | 255 |
| snake_viper_wild | 207,705 | +3.85% | 16 | 50% | 2,827 |
| random_hold | 207,619 | +3.81% | 10 | 70% | 733 |
| snake_viper_tick | 204,156 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,135 | +1.57% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,694 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,019 | -12.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,317 (-4.34%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,368 | +0.69% |
| benchmark | +1,308 | +0.59% |
| unified | +1,133 | +0.51% |
| intramonth | +1,083 | +0.51% |
| oracle | +705 | +0.33% |
| random_hold | +686 | +0.33% |
| snake_viper_wild | +666 | +0.32% |
| snake_viper_tick | +652 | +0.32% |
| intraweek | +100 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -843 | -0.40% |
| snake_abs_conv | -858 | -0.41% |
| snake_abs_exit | -1,034 | -0.48% |
| snake_anaconda | -1,266 | -0.62% |
| snake_abs_exit_conv | -1,319 | -0.62% |
| gold | -2,302 | -1.30% |

Average per day so far: unified Rs +642, benchmark Rs +584, snake_abs_exit Rs +382, intramonth Rs +361, snake_abs_exit_conv Rs +325, intraweek Rs +323, oracle Rs +311, snake_viper_wild Rs +266, snake_abs_conv Rs +249, snake_abs Rs +246, random_hold Rs +206, snake_viper_tick Rs +160, snake_anaconda Rs +98, nifty_calls Rs +50, benchmark_smallcap Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.