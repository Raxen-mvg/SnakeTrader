# Paper trading report

Updated 2026-11-26 10:06 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,390 | +12.70% | 0 | - | 237 |
| unified | 223,979 | +11.99% | 0 | - | 236 |
| oracle | 213,467 | +6.73% | 0 | - | 233 |
| intramonth | 211,529 | +5.76% | 0 | - | 235 |
| random_hold | 210,216 | +5.11% | 13 | 69% | 1,037 |
| intraweek | 208,415 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,424 | +1.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,781 | +1.39% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,793 | +0.40% | 1 | 100% | 255 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| snake_abs_conv | 200,617 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,286 | -1.86% | 16 | 50% | 2,827 |
| snake_anaconda | 194,970 | -2.52% | 3 | 33% | 374 |
| snake_viper_tick | 192,945 | -3.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,852 | -16.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,390 (-5.31%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,255 | +1.98% |
| benchmark_smallcap | +1,894 | +0.95% |
| intraweek | +1,672 | +0.81% |
| snake_abs_exit | +1,169 | +0.58% |
| snake_abs_exit_conv | +805 | +0.40% |
| random_hold | +723 | +0.34% |
| snake_abs_conv | +645 | +0.32% |
| snake_abs | +643 | +0.32% |
| snake_anaconda | +417 | +0.21% |
| benchmark | +367 | +0.16% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| unified | -120 | -0.05% |
| intramonth | -164 | -0.08% |
| oracle | -328 | -0.15% |
| snake_viper_tick | -1,231 | -0.63% |
| snake_viper_wild | -1,258 | -0.64% |

Average per day so far: benchmark Rs +619, unified Rs +585, oracle Rs +328, intramonth Rs +281, random_hold Rs +249, intraweek Rs +205, snake_abs_exit Rs +90, snake_abs_exit_conv Rs +73, nifty_calls Rs +45, snake_abs Rs +20, benchmark_smallcap Rs +19, snake_abs_conv Rs +16, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -113, snake_anaconda Rs -140, snake_viper_tick Rs -235, snake_nonews Rs -284, snake Rs -304, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.