# Paper trading report

Updated 2026-11-17 13:25 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,557 | +10.78% | 0 | - | 236 |
| benchmark | 221,427 | +10.71% | 0 | - | 237 |
| snake_abs_exit | 214,371 | +7.19% | 2 | 50% | 345 |
| intraweek | 214,095 | +7.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,699 | +6.35% | 2 | 50% | 345 |
| oracle | 212,111 | +6.06% | 0 | - | 233 |
| intramonth | 211,596 | +5.80% | 0 | - | 235 |
| snake_abs | 209,586 | +4.79% | 1 | 100% | 255 |
| snake_abs_conv | 209,449 | +4.72% | 1 | 100% | 255 |
| snake_viper_wild | 209,299 | +4.65% | 14 | 50% | 2,496 |
| random_hold | 207,452 | +3.73% | 10 | 70% | 733 |
| snake_viper_tick | 205,722 | +2.86% | 13 | 46% | 2,299 |
| snake_anaconda | 205,177 | +2.59% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,964 | +0.48% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,365 | -9.32% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,170 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,154 | +1.53% |
| snake_viper_tick | +3,102 | +1.53% |
| intraweek | +2,829 | +1.34% |
| benchmark | +1,346 | +0.61% |
| gold | +411 | +0.23% |
| benchmark_smallcap | +135 | +0.07% |
| unified | +119 | +0.05% |
| oracle | +88 | +0.04% |
| snake_anaconda | +74 | +0.04% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -23 | -0.01% |
| snake_abs_exit | -38 | -0.02% |
| random_hold | -341 | -0.16% |
| snake_abs_exit_conv | -519 | -0.24% |
| snake_abs_conv | -541 | -0.26% |
| snake_abs | -548 | -0.26% |

Average per day so far: unified Rs +616, benchmark Rs +612, snake_abs_exit Rs +449, intraweek Rs +403, snake_abs_exit_conv Rs +397, oracle Rs +346, snake_viper_wild Rs +344, intramonth Rs +331, snake_abs_conv Rs +295, snake_abs Rs +290, snake_viper_tick Rs +238, random_hold Rs +213, snake_anaconda Rs +173, nifty_calls Rs +52, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.