# Paper trading report

Updated 2026-11-26 09:56 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,260 | +12.63% | 0 | - | 237 |
| unified | 224,004 | +12.00% | 0 | - | 236 |
| oracle | 213,956 | +6.98% | 0 | - | 233 |
| intramonth | 211,608 | +5.80% | 0 | - | 235 |
| random_hold | 210,311 | +5.16% | 13 | 69% | 1,037 |
| intraweek | 208,449 | +4.22% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,513 | +1.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,876 | +1.44% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,786 | +0.39% | 1 | 100% | 255 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| snake_abs_conv | 200,613 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 195,830 | -2.08% | 16 | 50% | 2,827 |
| snake_anaconda | 195,112 | -2.44% | 3 | 33% | 374 |
| snake_viper_tick | 192,499 | -3.75% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,408 | -16.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,514 (-5.24%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,811 | +1.71% |
| benchmark_smallcap | +1,861 | +0.94% |
| intraweek | +1,705 | +0.82% |
| snake_abs_exit | +1,257 | +0.62% |
| snake_abs_exit_conv | +900 | +0.45% |
| random_hold | +818 | +0.39% |
| snake_abs_conv | +641 | +0.32% |
| snake_abs | +636 | +0.32% |
| snake_anaconda | +559 | +0.29% |
| benchmark | +237 | +0.10% |
| oracle | +161 | +0.07% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intramonth | -85 | -0.04% |
| unified | -96 | -0.04% |
| snake_viper_tick | -1,678 | -0.86% |
| snake_viper_wild | -1,714 | -0.87% |

Average per day so far: benchmark Rs +616, unified Rs +585, oracle Rs +340, intramonth Rs +283, random_hold Rs +251, intraweek Rs +206, snake_abs_exit Rs +92, snake_abs_exit_conv Rs +76, nifty_calls Rs +45, snake_abs Rs +20, benchmark_smallcap Rs +18, snake_abs_conv Rs +16, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -126, snake_anaconda Rs -136, snake_viper_tick Rs -250, snake_nonews Rs -284, snake Rs -304, gold Rs -795

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.