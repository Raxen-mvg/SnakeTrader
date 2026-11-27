# Paper trading report

Updated 2026-11-27 15:07 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,910 | +11.96% | 0 | - | 236 |
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| oracle | 212,086 | +6.04% | 0 | - | 233 |
| intramonth | 211,449 | +5.72% | 0 | - | 235 |
| random_hold | 211,316 | +5.66% | 13 | 69% | 1,037 |
| intraweek | 208,161 | +4.08% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,529 | +3.26% | 2 | 50% | 345 |
| snake_abs_exit | 204,293 | +2.15% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,726 | +0.86% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,610 | -0.20% | 1 | 100% | 255 |
| snake_abs_conv | 199,424 | -0.29% | 1 | 100% | 255 |
| snake_anaconda | 193,165 | -3.42% | 3 | 33% | 374 |
| snake_viper_wild | 192,505 | -3.75% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,235 | -5.38% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,498 | -14.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,202 (-5.40%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,132 | +3.06% |
| gold | +4,505 | +2.71% |
| snake_abs_exit | +3,216 | +1.60% |
| random_hold | +2,722 | +1.30% |
| intraweek | +1,112 | +0.54% |
| snake_abs | +1,058 | +0.53% |
| snake_abs_conv | +1,058 | +0.53% |
| intramonth | +915 | +0.43% |
| benchmark_smallcap | +886 | +0.44% |
| snake_anaconda | +868 | +0.45% |
| unified | +832 | +0.37% |
| snake_viper_wild | +299 | +0.16% |
| snake_viper_tick | +294 | +0.15% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -149 | -0.07% |
| benchmark | -2,547 | -1.13% |

Average per day so far: unified Rs +569, benchmark Rs +558, oracle Rs +288, intramonth Rs +273, random_hold Rs +269, intraweek Rs +194, snake_abs_exit_conv Rs +167, snake_abs_exit Rs +110, benchmark_smallcap Rs +45, nifty_calls Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, snake_anaconda Rs -185, snake_viper_wild Rs -220, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -347, gold Rs -702

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.