# Paper trading report

Updated 2026-11-26 12:11 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,140 | +13.07% | 0 | - | 237 |
| unified | 223,191 | +11.60% | 0 | - | 236 |
| oracle | 212,843 | +6.42% | 0 | - | 233 |
| intramonth | 210,363 | +5.18% | 0 | - | 235 |
| random_hold | 209,885 | +4.94% | 13 | 69% | 1,037 |
| intraweek | 208,520 | +4.26% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,824 | +0.41% | 2 | 50% | 345 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| snake_abs_exit_conv | 200,247 | +0.12% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,520 | -0.74% | 1 | 100% | 255 |
| snake_abs_conv | 198,326 | -0.84% | 1 | 100% | 255 |
| snake_anaconda | 192,305 | -3.85% | 3 | 33% | 374 |
| snake_viper_wild | 192,273 | -3.86% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,007 | -5.50% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,945 | -17.03% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,750 (-5.63%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,973 | +0.99% |
| intraweek | +1,777 | +0.86% |
| gold | +1,348 | +0.82% |
| benchmark | +1,117 | +0.50% |
| random_hold | +392 | +0.19% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -909 | -0.41% |
| oracle | -953 | -0.45% |
| intramonth | -1,330 | -0.63% |
| snake_abs_exit | -1,431 | -0.71% |
| snake_abs | -1,630 | -0.81% |
| snake_abs_conv | -1,646 | -0.82% |
| snake_abs_exit_conv | -1,729 | -0.86% |
| snake_anaconda | -2,248 | -1.16% |
| snake_viper_tick | -5,170 | -2.66% |
| snake_viper_wild | -5,271 | -2.67% |

Average per day so far: benchmark Rs +638, unified Rs +566, oracle Rs +313, intramonth Rs +253, random_hold Rs +241, intraweek Rs +208, nifty_calls Rs +45, snake_abs_exit Rs +22, benchmark_smallcap Rs +21, snake_abs_exit_conv Rs +7, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -38, snake_abs_conv Rs -44, snake_anaconda Rs -214, snake_viper_wild Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -366, gold Rs -831

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.