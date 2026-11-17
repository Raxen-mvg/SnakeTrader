# Paper trading report

Updated 2026-11-17 14:01 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| unified | 221,629 | +10.81% | 0 | - | 236 |
| snake_abs_exit | 213,895 | +6.95% | 2 | 50% | 345 |
| intraweek | 213,560 | +6.78% | 35 | 54% | 3,851 |
| oracle | 212,432 | +6.22% | 0 | - | 233 |
| snake_abs_exit_conv | 212,325 | +6.16% | 2 | 50% | 345 |
| intramonth | 211,461 | +5.73% | 0 | - | 235 |
| snake_abs | 209,183 | +4.59% | 1 | 100% | 255 |
| snake_viper_wild | 209,170 | +4.58% | 14 | 50% | 2,496 |
| snake_abs_conv | 209,041 | +4.52% | 1 | 100% | 255 |
| random_hold | 207,562 | +3.78% | 10 | 70% | 733 |
| snake_viper_tick | 205,595 | +2.80% | 13 | 46% | 2,299 |
| snake_anaconda | 204,777 | +2.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,087 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,921 | -9.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,164 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,026 | +1.47% |
| snake_viper_tick | +2,975 | +1.47% |
| intraweek | +2,294 | +1.09% |
| benchmark | +1,943 | +0.88% |
| oracle | +410 | +0.19% |
| benchmark_smallcap | +258 | +0.13% |
| unified | +191 | +0.09% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| gold | -33 | -0.02% |
| intramonth | -158 | -0.07% |
| random_hold | -231 | -0.11% |
| snake_anaconda | -326 | -0.16% |
| snake_abs_exit | -514 | -0.24% |
| snake_abs_exit_conv | -892 | -0.42% |
| snake_abs_conv | -949 | -0.45% |
| snake_abs | -951 | -0.45% |

Average per day so far: benchmark Rs +629, unified Rs +618, snake_abs_exit Rs +434, intraweek Rs +387, snake_abs_exit_conv Rs +385, oracle Rs +355, snake_viper_wild Rs +340, intramonth Rs +327, snake_abs_conv Rs +283, snake_abs Rs +278, snake_viper_tick Rs +233, random_hold Rs +216, snake_anaconda Rs +159, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -545

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.