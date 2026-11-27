# Paper trading report

Updated 2026-11-27 10:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,275 | +12.64% | 0 | - | 237 |
| unified | 222,878 | +11.44% | 0 | - | 236 |
| oracle | 212,344 | +6.17% | 0 | - | 233 |
| intramonth | 210,666 | +5.33% | 0 | - | 235 |
| random_hold | 210,108 | +5.05% | 13 | 69% | 1,037 |
| intraweek | 208,363 | +4.18% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,226 | +2.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,934 | +1.97% | 2 | 50% | 345 |
| benchmark_smallcap | 202,062 | +1.03% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,093 | +0.55% | 1 | 100% | 255 |
| snake_abs_conv | 200,911 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,431 | -2.79% | 3 | 33% | 374 |
| snake_viper_wild | 193,566 | -3.22% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,273 | -4.86% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,361 | -15.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,789 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,149 | +2.06% |
| snake_abs_exit_conv | +3,537 | +1.76% |
| snake_abs_conv | +2,545 | +1.28% |
| snake_abs | +2,541 | +1.28% |
| gold | +2,367 | +1.43% |
| snake_anaconda | +2,134 | +1.11% |
| random_hold | +1,514 | +0.73% |
| snake_viper_wild | +1,360 | +0.71% |
| snake_viper_tick | +1,332 | +0.70% |
| intraweek | +1,314 | +0.64% |
| benchmark_smallcap | +1,222 | +0.61% |
| intramonth | +133 | +0.06% |
| oracle | +108 | +0.05% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -200 | -0.09% |
| benchmark | -711 | -0.32% |

Average per day so far: benchmark Rs +602, unified Rs +545, oracle Rs +294, intramonth Rs +254, random_hold Rs +241, intraweek Rs +199, snake_abs_exit Rs +134, snake_abs_exit_conv Rs +101, benchmark_smallcap Rs +54, nifty_calls Rs +44, snake_abs Rs +27, snake_abs_conv Rs +23, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -151, snake_viper_wild Rs -189, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -314, gold Rs -753

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.