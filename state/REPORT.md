# Paper trading report

Updated 2026-11-17 12:43 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,001 | +11.00% | 0 | - | 237 |
| unified | 221,768 | +10.88% | 0 | - | 236 |
| snake_abs_exit | 214,222 | +7.11% | 2 | 50% | 345 |
| intraweek | 213,310 | +6.66% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,483 | +6.24% | 2 | 50% | 345 |
| oracle | 212,186 | +6.09% | 0 | - | 233 |
| intramonth | 211,613 | +5.81% | 0 | - | 235 |
| snake_abs | 209,415 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,267 | +4.63% | 1 | 100% | 255 |
| random_hold | 207,596 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 207,586 | +3.79% | 14 | 50% | 2,496 |
| snake_anaconda | 204,932 | +2.47% | 3 | 33% | 374 |
| snake_viper_tick | 204,037 | +2.02% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,446 | +0.72% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,300 | -9.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,140 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,045 | +0.97% |
| benchmark | +1,920 | +0.87% |
| snake_viper_wild | +1,441 | +0.70% |
| snake_viper_tick | +1,417 | +0.70% |
| benchmark_smallcap | +617 | +0.31% |
| gold | +345 | +0.19% |
| unified | +330 | +0.15% |
| oracle | +163 | +0.08% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -6 | -0.00% |
| snake_anaconda | -170 | -0.08% |
| snake_abs_exit | -187 | -0.09% |
| random_hold | -197 | -0.10% |
| snake_abs | -719 | -0.34% |
| snake_abs_conv | -723 | -0.34% |
| snake_abs_exit_conv | -734 | -0.34% |

Average per day so far: benchmark Rs +629, unified Rs +622, snake_abs_exit Rs +444, snake_abs_exit_conv Rs +390, intraweek Rs +380, oracle Rs +348, intramonth Rs +332, snake_abs_conv Rs +290, snake_abs Rs +285, snake_viper_wild Rs +281, random_hold Rs +217, snake_viper_tick Rs +168, snake_anaconda Rs +164, nifty_calls Rs +52, benchmark_smallcap Rs +47, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.