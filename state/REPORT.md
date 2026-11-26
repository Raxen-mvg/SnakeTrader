# Paper trading report

Updated 2026-11-26 14:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,926 | +12.96% | 0 | - | 237 |
| unified | 223,013 | +11.51% | 0 | - | 236 |
| oracle | 212,340 | +6.17% | 0 | - | 233 |
| intramonth | 210,376 | +5.19% | 0 | - | 235 |
| random_hold | 208,778 | +4.39% | 13 | 69% | 1,037 |
| intraweek | 207,413 | +3.71% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,013 | +0.51% | 2 | 50% | 345 |
| benchmark_smallcap | 200,941 | +0.47% | 0 | - | 237 |
| snake_abs_exit_conv | 200,283 | +0.14% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,589 | -0.71% | 1 | 100% | 255 |
| snake_abs_conv | 198,395 | -0.80% | 1 | 100% | 255 |
| snake_viper_wild | 192,287 | -3.86% | 16 | 50% | 2,827 |
| snake_anaconda | 192,204 | -3.90% | 3 | 33% | 374 |
| snake_viper_tick | 189,021 | -5.49% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,240 | -16.88% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,367 (-5.82%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,130 | +1.07% |
| gold | +1,644 | +1.00% |
| benchmark | +903 | +0.40% |
| intraweek | +670 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -715 | -0.34% |
| unified | -1,087 | -0.48% |
| snake_abs_exit | -1,243 | -0.61% |
| intramonth | -1,317 | -0.62% |
| oracle | -1,455 | -0.68% |
| snake_abs | -1,561 | -0.78% |
| snake_abs_conv | -1,577 | -0.79% |
| snake_abs_exit_conv | -1,693 | -0.84% |
| snake_anaconda | -2,349 | -1.21% |
| snake_viper_tick | -5,156 | -2.65% |
| snake_viper_wild | -5,256 | -2.66% |

Average per day so far: benchmark Rs +632, unified Rs +561, oracle Rs +301, intramonth Rs +253, random_hold Rs +214, intraweek Rs +181, nifty_calls Rs +45, snake_abs_exit Rs +27, benchmark_smallcap Rs +25, snake_abs_exit_conv Rs +7, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -36, snake_abs_conv Rs -42, snake_anaconda Rs -217, snake_viper_wild Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -366, gold Rs -823

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.