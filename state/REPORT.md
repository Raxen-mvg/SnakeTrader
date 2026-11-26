# Paper trading report

Updated 2026-11-26 13:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,864 | +12.93% | 0 | - | 237 |
| unified | 223,449 | +11.72% | 0 | - | 236 |
| oracle | 213,460 | +6.73% | 0 | - | 233 |
| intramonth | 210,610 | +5.30% | 0 | - | 235 |
| random_hold | 209,981 | +4.99% | 13 | 69% | 1,037 |
| intraweek | 208,612 | +4.31% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,815 | -0.09% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,249 | -0.38% | 2 | 50% | 345 |
| snake_abs | 197,623 | -1.19% | 1 | 100% | 255 |
| snake_abs_conv | 197,418 | -1.29% | 1 | 100% | 255 |
| snake_viper_wild | 191,793 | -4.10% | 16 | 50% | 2,827 |
| snake_anaconda | 191,421 | -4.29% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,537 | -5.73% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,339 | -16.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,874 (-5.56%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,869 | +0.90% |
| benchmark_smallcap | +1,850 | +0.93% |
| gold | +1,743 | +1.06% |
| benchmark | +842 | +0.37% |
| random_hold | +488 | +0.23% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -335 | -0.16% |
| unified | -651 | -0.29% |
| intramonth | -1,083 | -0.51% |
| snake_abs_exit | -2,441 | -1.21% |
| snake_abs | -2,527 | -1.26% |
| snake_abs_conv | -2,554 | -1.28% |
| snake_abs_exit_conv | -2,727 | -1.35% |
| snake_anaconda | -3,132 | -1.61% |
| snake_viper_tick | -5,640 | -2.90% |
| snake_viper_wild | -5,751 | -2.91% |

Average per day so far: benchmark Rs +631, unified Rs +572, oracle Rs +328, intramonth Rs +259, random_hold Rs +243, intraweek Rs +210, nifty_calls Rs +45, benchmark_smallcap Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -5, snake_abs_exit_conv Rs -20, snake_abs Rs -61, snake_abs_conv Rs -68, snake_anaconda Rs -238, snake_viper_wild Rs -249, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -382, gold Rs -821

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.