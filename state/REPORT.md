# Paper trading report

Updated 2026-11-17 12:07 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,246 | +11.12% | 0 | - | 237 |
| unified | 222,133 | +11.07% | 0 | - | 236 |
| snake_abs_exit | 215,078 | +7.54% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,277 | +6.64% | 2 | 50% | 345 |
| intraweek | 212,317 | +6.16% | 35 | 54% | 3,851 |
| oracle | 212,263 | +6.13% | 0 | - | 233 |
| intramonth | 211,976 | +5.99% | 0 | - | 235 |
| snake_abs | 209,901 | +4.95% | 1 | 100% | 255 |
| snake_abs_conv | 209,753 | +4.88% | 1 | 100% | 255 |
| random_hold | 207,785 | +3.89% | 10 | 70% | 733 |
| snake_viper_wild | 207,329 | +3.67% | 14 | 50% | 2,496 |
| snake_anaconda | 205,472 | +2.74% | 3 | 33% | 374 |
| snake_viper_tick | 203,784 | +1.89% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,219 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,250 | -9.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,197 (-4.40%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,165 | +0.98% |
| benchmark_smallcap | +1,390 | +0.69% |
| snake_viper_wild | +1,185 | +0.57% |
| snake_viper_tick | +1,164 | +0.57% |
| intraweek | +1,051 | +0.50% |
| unified | +696 | +0.31% |
| snake_abs_exit | +669 | +0.31% |
| snake_anaconda | +369 | +0.18% |
| intramonth | +357 | +0.17% |
| gold | +296 | +0.16% |
| oracle | +240 | +0.11% |
| snake_abs_exit_conv | +60 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -8 | -0.00% |
| snake_abs | -232 | -0.11% |
| snake_abs_conv | -236 | -0.11% |

Average per day so far: benchmark Rs +636, unified Rs +632, snake_abs_exit Rs +471, snake_abs_exit_conv Rs +415, intraweek Rs +352, oracle Rs +350, intramonth Rs +342, snake_abs_conv Rs +305, snake_abs Rs +300, snake_viper_wild Rs +271, random_hold Rs +222, snake_anaconda Rs +182, snake_viper_tick Rs +158, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -536

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.