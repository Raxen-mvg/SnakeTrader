# Paper trading report

Updated 2026-11-26 12:08 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,094 | +13.05% | 0 | - | 237 |
| unified | 223,206 | +11.60% | 0 | - | 236 |
| oracle | 213,015 | +6.51% | 0 | - | 233 |
| intramonth | 210,368 | +5.18% | 0 | - | 235 |
| random_hold | 209,826 | +4.91% | 13 | 69% | 1,037 |
| intraweek | 208,443 | +4.22% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| snake_abs_exit | 200,700 | +0.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,195 | +0.10% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,430 | -0.79% | 1 | 100% | 255 |
| snake_abs_conv | 198,236 | -0.88% | 1 | 100% | 255 |
| snake_anaconda | 192,288 | -3.86% | 3 | 33% | 374 |
| snake_viper_wild | 192,177 | -3.91% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,913 | -5.54% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,912 | -17.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,762 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,973 | +0.99% |
| intraweek | +1,700 | +0.82% |
| gold | +1,315 | +0.80% |
| benchmark | +1,071 | +0.48% |
| random_hold | +334 | +0.16% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -780 | -0.36% |
| unified | -894 | -0.40% |
| intramonth | -1,325 | -0.63% |
| snake_abs_exit | -1,555 | -0.77% |
| snake_abs | -1,720 | -0.86% |
| snake_abs_conv | -1,736 | -0.87% |
| snake_abs_exit_conv | -1,781 | -0.88% |
| snake_anaconda | -2,265 | -1.16% |
| snake_viper_tick | -5,264 | -2.71% |
| snake_viper_wild | -5,367 | -2.72% |

Average per day so far: benchmark Rs +636, unified Rs +566, oracle Rs +317, intramonth Rs +253, random_hold Rs +240, intraweek Rs +206, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs_exit Rs +18, snake_abs_exit_conv Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -40, snake_abs_conv Rs -46, snake_anaconda Rs -214, snake_viper_wild Rs -237, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -370, gold Rs -831

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.