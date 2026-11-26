# Paper trading report

Updated 2026-11-26 12:56 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,956 | +12.98% | 0 | - | 237 |
| unified | 223,436 | +11.72% | 0 | - | 236 |
| oracle | 213,296 | +6.65% | 0 | - | 233 |
| intramonth | 210,564 | +5.28% | 0 | - | 235 |
| random_hold | 209,942 | +4.97% | 13 | 69% | 1,037 |
| intraweek | 208,309 | +4.16% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,329 | +0.16% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,878 | -0.06% | 2 | 50% | 345 |
| snake_abs | 198,269 | -0.86% | 1 | 100% | 255 |
| snake_abs_conv | 198,069 | -0.97% | 1 | 100% | 255 |
| snake_anaconda | 192,024 | -3.99% | 3 | 33% | 374 |
| snake_viper_wild | 191,994 | -4.00% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,734 | -5.63% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,602 | -16.70% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,846 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,006 | +1.22% |
| benchmark_smallcap | +1,760 | +0.89% |
| intraweek | +1,566 | +0.76% |
| benchmark | +933 | +0.41% |
| random_hold | +450 | +0.21% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -499 | -0.23% |
| unified | -663 | -0.30% |
| intramonth | -1,129 | -0.53% |
| snake_abs | -1,880 | -0.94% |
| snake_abs_conv | -1,903 | -0.95% |
| snake_abs_exit | -1,927 | -0.95% |
| snake_abs_exit_conv | -2,098 | -1.04% |
| snake_anaconda | -2,529 | -1.30% |
| snake_viper_tick | -5,443 | -2.80% |
| snake_viper_wild | -5,549 | -2.81% |

Average per day so far: benchmark Rs +633, unified Rs +572, oracle Rs +324, intramonth Rs +258, random_hold Rs +242, intraweek Rs +203, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -3, snake_abs Rs -44, snake_abs_conv Rs -51, snake_anaconda Rs -222, snake_viper_wild Rs -243, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -376, gold Rs -815

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.