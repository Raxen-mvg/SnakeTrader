# Paper trading report

Updated 2026-11-19 12:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,655 | +11.83% | 0 | - | 236 |
| benchmark | 221,450 | +10.72% | 0 | - | 237 |
| snake_abs_exit | 213,507 | +6.75% | 2 | 50% | 345 |
| intramonth | 213,272 | +6.64% | 0 | - | 235 |
| intraweek | 211,651 | +5.83% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,637 | +5.82% | 2 | 50% | 345 |
| oracle | 210,978 | +5.49% | 0 | - | 233 |
| snake_abs | 209,110 | +4.55% | 1 | 100% | 255 |
| snake_abs_conv | 208,984 | +4.49% | 1 | 100% | 255 |
| snake_viper_wild | 207,705 | +3.85% | 16 | 50% | 2,827 |
| random_hold | 207,596 | +3.80% | 10 | 70% | 733 |
| snake_viper_tick | 204,156 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,375 | +1.69% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,135 | -12.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,148 (-4.43%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,233 | +0.62% |
| benchmark | +1,155 | +0.52% |
| unified | +1,043 | +0.47% |
| intramonth | +998 | +0.47% |
| snake_viper_wild | +666 | +0.32% |
| random_hold | +663 | +0.32% |
| snake_viper_tick | +652 | +0.32% |
| oracle | +182 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -188 | -0.09% |
| snake_abs | -326 | -0.16% |
| snake_abs_conv | -341 | -0.16% |
| snake_abs_exit | -525 | -0.24% |
| snake_abs_exit_conv | -747 | -0.35% |
| snake_anaconda | -1,026 | -0.50% |
| gold | -2,187 | -1.23% |

Average per day so far: unified Rs +639, benchmark Rs +580, snake_abs_exit Rs +397, intramonth Rs +359, snake_abs_exit_conv Rs +342, intraweek Rs +315, oracle Rs +297, snake_viper_wild Rs +266, snake_abs_conv Rs +264, snake_abs Rs +260, random_hold Rs +205, snake_viper_tick Rs +160, snake_anaconda Rs +105, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.