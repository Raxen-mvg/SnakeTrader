# Paper trading report

Updated 2026-11-25 11:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,117 | +13.06% | 0 | - | 237 |
| unified | 225,443 | +12.72% | 0 | - | 236 |
| intramonth | 213,065 | +6.53% | 0 | - | 235 |
| oracle | 212,525 | +6.26% | 0 | - | 233 |
| random_hold | 209,418 | +4.71% | 12 | 75% | 1,009 |
| intraweek | 207,480 | +3.74% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,784 | +1.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,146 | +1.07% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,590 | +0.80% | 1 | 100% | 255 |
| snake_abs_conv | 201,403 | +0.70% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 196,953 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,266 | -2.87% | 3 | 33% | 374 |
| snake_viper_tick | 193,599 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,481 | -17.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,458 (-5.27%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,644 | +2.10% |
| unified | +1,158 | +0.52% |
| random_hold | +992 | +0.48% |
| benchmark_smallcap | +572 | +0.29% |
| intramonth | +314 | +0.15% |
| oracle | +183 | +0.09% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -3,871 | -1.88% |
| snake_abs_conv | -3,899 | -1.90% |
| snake_viper_tick | -4,094 | -2.07% |
| intraweek | -4,139 | -1.96% |
| snake_viper_wild | -4,171 | -2.07% |
| snake_anaconda | -4,437 | -2.23% |
| snake_abs_exit | -4,711 | -2.27% |
| snake_abs_exit_conv | -4,900 | -2.37% |
| gold | -4,948 | -2.92% |

Average per day so far: benchmark Rs +653, unified Rs +636, intramonth Rs +327, oracle Rs +313, random_hold Rs +235, intraweek Rs +187, snake_abs_exit Rs +75, snake_abs_exit_conv Rs +58, nifty_calls Rs +46, snake_abs Rs +42, snake_abs_conv Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -95, snake_anaconda Rs -164, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.