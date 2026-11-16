# Paper trading report

Updated 2026-11-16 10:14 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,263 | +10.63% | 0 | - | 236 |
| benchmark | 220,616 | +10.31% | 0 | - | 237 |
| intraweek | 214,530 | +7.26% | 35 | 54% | 3,851 |
| snake_abs_exit | 214,076 | +7.04% | 2 | 50% | 345 |
| oracle | 213,776 | +6.89% | 0 | - | 233 |
| snake_abs_exit_conv | 212,666 | +6.33% | 2 | 50% | 345 |
| intramonth | 211,540 | +5.77% | 0 | - | 235 |
| snake_abs | 209,859 | +4.93% | 1 | 100% | 255 |
| snake_abs_conv | 209,689 | +4.84% | 1 | 100% | 255 |
| random_hold | 208,525 | +4.26% | 10 | 70% | 733 |
| snake_anaconda | 204,185 | +2.09% | 3 | 33% | 374 |
| snake_viper_wild | 203,575 | +1.79% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,093 | +0.05% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,286 | -8.86% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,935 (-4.03%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,243 | +1.02% |
| intramonth | +1,483 | +0.71% |
| random_hold | +1,299 | +0.63% |
| benchmark | +1,278 | +0.58% |
| oracle | +678 | +0.32% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -707 | -0.34% |
| benchmark_smallcap | -964 | -0.47% |
| snake_viper_tick | -1,161 | -0.58% |
| snake_viper_wild | -1,182 | -0.58% |
| intraweek | -1,615 | -0.75% |
| gold | -1,710 | -0.93% |
| snake_abs_conv | -2,678 | -1.26% |
| snake_abs | -2,681 | -1.26% |
| snake_abs_exit | -2,909 | -1.34% |
| snake_abs_exit_conv | -3,716 | -1.72% |

Average per day so far: unified Rs +625, benchmark Rs +606, snake_abs_exit Rs +454, intraweek Rs +427, snake_abs_exit_conv Rs +409, oracle Rs +405, intramonth Rs +339, snake_abs_conv Rs +313, snake_abs Rs +308, random_hold Rs +251, snake_anaconda Rs +144, snake_viper_wild Rs +138, benchmark_smallcap Rs +64, nifty_calls Rs +54, snake_viper_tick Rs +4, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -521

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.