# Paper trading report

Updated 2026-11-25 12:04 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,857 | +12.93% | 0 | - | 237 |
| unified | 225,361 | +12.68% | 0 | - | 236 |
| intramonth | 213,071 | +6.54% | 0 | - | 235 |
| oracle | 212,651 | +6.33% | 0 | - | 233 |
| random_hold | 210,131 | +5.07% | 12 | 75% | 1,009 |
| intraweek | 207,886 | +3.94% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,297 | +1.15% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,735 | +0.87% | 2 | 50% | 345 |
| snake_abs | 201,071 | +0.54% | 1 | 100% | 255 |
| snake_abs_conv | 200,881 | +0.44% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,708 | -0.15% | 0 | - | 237 |
| snake_viper_wild | 196,694 | -1.65% | 16 | 50% | 2,827 |
| snake_anaconda | 193,861 | -3.07% | 3 | 33% | 374 |
| snake_viper_tick | 193,345 | -3.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,564 | -17.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,534 (-5.23%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,383 | +1.98% |
| random_hold | +1,705 | +0.82% |
| unified | +1,076 | +0.48% |
| benchmark_smallcap | +729 | +0.37% |
| intramonth | +320 | +0.15% |
| oracle | +309 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,733 | -1.76% |
| snake_viper_tick | -4,348 | -2.20% |
| snake_abs | -4,390 | -2.14% |
| snake_abs_conv | -4,421 | -2.15% |
| snake_viper_wild | -4,431 | -2.20% |
| snake_anaconda | -4,842 | -2.44% |
| gold | -4,866 | -2.87% |
| snake_abs_exit | -5,198 | -2.50% |
| snake_abs_exit_conv | -5,310 | -2.56% |

Average per day so far: benchmark Rs +646, unified Rs +634, intramonth Rs +327, oracle Rs +316, random_hold Rs +253, intraweek Rs +197, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +47, nifty_calls Rs +46, snake_abs Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_viper_wild Rs -103, snake_anaconda Rs -175, snake_viper_tick Rs -229, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.