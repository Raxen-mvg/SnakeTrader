# Paper trading report

Updated 2026-11-27 11:34 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,051 | +12.03% | 0 | - | 237 |
| unified | 222,169 | +11.09% | 0 | - | 236 |
| oracle | 211,898 | +5.95% | 0 | - | 233 |
| intramonth | 210,315 | +5.16% | 0 | - | 235 |
| random_hold | 210,272 | +5.14% | 13 | 69% | 1,037 |
| intraweek | 207,726 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,493 | +2.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,132 | +2.07% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,636 | +0.82% | 0 | - | 237 |
| snake_abs | 200,983 | +0.49% | 1 | 100% | 255 |
| snake_abs_conv | 200,806 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,504 | -2.75% | 3 | 33% | 374 |
| snake_viper_wild | 193,436 | -3.28% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,146 | -4.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,150 | -15.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,444 (-5.78%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,415 | +2.20% |
| snake_abs_exit_conv | +3,735 | +1.86% |
| gold | +3,156 | +1.90% |
| snake_abs_conv | +2,439 | +1.23% |
| snake_abs | +2,430 | +1.22% |
| snake_anaconda | +2,207 | +1.15% |
| random_hold | +1,678 | +0.80% |
| snake_viper_wild | +1,230 | +0.64% |
| snake_viper_tick | +1,205 | +0.64% |
| benchmark_smallcap | +796 | +0.40% |
| intraweek | +677 | +0.33% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -218 | -0.10% |
| oracle | -337 | -0.16% |
| unified | -909 | -0.41% |
| benchmark | -1,935 | -0.86% |

Average per day so far: benchmark Rs +573, unified Rs +528, oracle Rs +283, intramonth Rs +246, random_hold Rs +245, intraweek Rs +184, snake_abs_exit Rs +141, snake_abs_exit_conv Rs +106, nifty_calls Rs +44, benchmark_smallcap Rs +43, snake_abs Rs +25, snake_abs_conv Rs +21, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -149, snake_viper_wild Rs -193, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -318, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.