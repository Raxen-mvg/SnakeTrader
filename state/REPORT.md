# Paper trading report

Updated 2026-11-19 12:43 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,690 | +11.85% | 0 | - | 236 |
| benchmark | 221,726 | +10.86% | 0 | - | 237 |
| intramonth | 213,303 | +6.65% | 0 | - | 235 |
| snake_abs_exit | 212,908 | +6.45% | 2 | 50% | 345 |
| intraweek | 211,508 | +5.75% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,986 | +5.49% | 2 | 50% | 345 |
| oracle | 210,884 | +5.44% | 0 | - | 233 |
| snake_abs | 208,652 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,524 | +4.26% | 1 | 100% | 255 |
| random_hold | 207,674 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 207,518 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,972 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 202,930 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,683 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,113 (-4.44%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,431 | +0.65% |
| benchmark_smallcap | +1,356 | +0.68% |
| unified | +1,079 | +0.48% |
| intramonth | +1,030 | +0.48% |
| random_hold | +742 | +0.36% |
| snake_viper_wild | +479 | +0.23% |
| snake_viper_tick | +469 | +0.23% |
| oracle | +88 | +0.04% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -332 | -0.16% |
| snake_abs | -784 | -0.37% |
| snake_abs_conv | -801 | -0.38% |
| snake_abs_exit | -1,124 | -0.53% |
| snake_abs_exit_conv | -1,397 | -0.66% |
| snake_anaconda | -1,471 | -0.72% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +640, benchmark Rs +587, snake_abs_exit Rs +380, intramonth Rs +360, snake_abs_exit_conv Rs +323, intraweek Rs +311, oracle Rs +294, snake_viper_wild Rs +259, snake_abs_conv Rs +251, snake_abs Rs +247, random_hold Rs +207, snake_viper_tick Rs +153, snake_anaconda Rs +92, nifty_calls Rs +50, benchmark_smallcap Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.