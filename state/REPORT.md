# Paper trading report

Updated 2026-11-19 11:18 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,598 | +11.80% | 0 | - | 236 |
| benchmark | 220,877 | +10.44% | 0 | - | 237 |
| snake_abs_exit | 213,713 | +6.86% | 2 | 50% | 345 |
| intramonth | 213,084 | +6.54% | 0 | - | 235 |
| snake_abs_exit_conv | 211,758 | +5.88% | 2 | 50% | 345 |
| intraweek | 211,723 | +5.86% | 35 | 54% | 3,851 |
| oracle | 210,916 | +5.46% | 0 | - | 233 |
| snake_abs | 209,193 | +4.60% | 1 | 100% | 255 |
| snake_abs_conv | 209,073 | +4.54% | 1 | 100% | 255 |
| random_hold | 207,585 | +3.79% | 10 | 70% | 733 |
| snake_viper_wild | 207,417 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,874 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,460 | +1.73% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,266 | -12.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,095 (-4.45%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,065 | +0.53% |
| unified | +987 | +0.44% |
| intramonth | +810 | +0.38% |
| random_hold | +652 | +0.32% |
| benchmark | +581 | +0.26% |
| snake_viper_wild | +378 | +0.18% |
| snake_viper_tick | +370 | +0.18% |
| oracle | +120 | +0.06% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -116 | -0.06% |
| snake_abs | -243 | -0.12% |
| snake_abs_conv | -251 | -0.12% |
| snake_abs_exit | -319 | -0.15% |
| snake_abs_exit_conv | -626 | -0.29% |
| snake_anaconda | -941 | -0.46% |
| gold | -2,055 | -1.16% |

Average per day so far: unified Rs +638, benchmark Rs +564, snake_abs_exit Rs +403, intramonth Rs +354, snake_abs_exit_conv Rs +346, intraweek Rs +317, oracle Rs +295, snake_abs_conv Rs +267, snake_abs Rs +263, snake_viper_wild Rs +256, random_hold Rs +205, snake_viper_tick Rs +149, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -668

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.