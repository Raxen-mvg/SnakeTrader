# Paper trading report

Updated 2026-11-11 13:04 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,792 | +10.40% | 0 | - | 237 |
| unified | 220,584 | +10.29% | 0 | - | 236 |
| snake_abs_exit_conv | 218,096 | +9.05% | 2 | 50% | 345 |
| snake_abs_exit | 216,995 | +8.50% | 2 | 50% | 345 |
| snake_abs | 214,595 | +7.30% | 1 | 100% | 255 |
| snake_abs_conv | 214,440 | +7.22% | 1 | 100% | 255 |
| intraweek | 213,721 | +6.86% | 30 | 53% | 3,302 |
| oracle | 211,958 | +5.98% | 0 | - | 233 |
| intramonth | 211,484 | +5.74% | 0 | - | 235 |
| random_hold | 207,053 | +3.53% | 9 | 67% | 709 |
| snake_anaconda | 204,862 | +2.43% | 3 | 33% | 374 |
| snake_viper_wild | 204,610 | +2.31% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| snake_viper_tick | 201,121 | +0.56% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,996 | -5.00% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,430 (-4.29%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,180 | +3.64% |
| snake_viper_tick | +7,044 | +3.63% |
| snake_abs_exit_conv | +6,187 | +2.92% |
| snake_anaconda | +5,395 | +2.71% |
| snake_abs_exit | +5,011 | +2.36% |
| snake_abs_conv | +4,963 | +2.37% |
| snake_abs | +4,948 | +2.36% |
| benchmark_smallcap | +3,228 | +1.63% |
| benchmark | +2,700 | +1.24% |
| random_hold | +2,092 | +1.02% |
| oracle | +2,040 | +0.97% |
| intramonth | +875 | +0.41% |
| unified | +837 | +0.38% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -820 | -0.38% |
| gold | -2,137 | -1.11% |

Average per day so far: benchmark Rs +671, unified Rs +664, snake_abs_exit_conv Rs +646, snake_abs_exit Rs +607, snake_abs_conv Rs +516, snake_abs Rs +503, intraweek Rs +443, oracle Rs +386, intramonth Rs +370, random_hold Rs +228, snake_viper_wild Rs +200, snake_anaconda Rs +187, nifty_calls Rs +59, snake_viper_tick Rs +56, benchmark_smallcap Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -323, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.