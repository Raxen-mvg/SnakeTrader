# Paper trading report

Updated 2026-11-27 13:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,013 | +12.01% | 0 | - | 237 |
| unified | 223,428 | +11.71% | 0 | - | 236 |
| oracle | 211,993 | +6.00% | 0 | - | 233 |
| intramonth | 210,912 | +5.46% | 0 | - | 235 |
| random_hold | 210,790 | +5.39% | 13 | 69% | 1,037 |
| intraweek | 208,485 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,640 | +2.32% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,370 | +2.19% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,434 | +0.72% | 0 | - | 237 |
| snake_abs | 200,361 | +0.18% | 1 | 100% | 255 |
| snake_abs_conv | 200,178 | +0.09% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,733 | -3.13% | 3 | 33% | 374 |
| snake_viper_wild | 192,140 | -3.93% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,877 | -5.56% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,512 | -15.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,932 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,973 | +1.98% |
| snake_abs_exit | +3,562 | +1.77% |
| gold | +3,518 | +2.12% |
| random_hold | +2,196 | +1.05% |
| snake_abs_conv | +1,812 | +0.91% |
| snake_abs | +1,809 | +0.91% |
| snake_anaconda | +1,437 | +0.75% |
| intraweek | +1,436 | +0.69% |
| benchmark_smallcap | +594 | +0.30% |
| intramonth | +379 | +0.18% |
| unified | +349 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -64 | -0.03% |
| snake_viper_wild | -66 | -0.03% |
| oracle | -242 | -0.11% |
| benchmark | -1,974 | -0.87% |

Average per day so far: benchmark Rs +572, unified Rs +558, oracle Rs +286, intramonth Rs +260, random_hold Rs +257, intraweek Rs +202, snake_abs_exit Rs +119, snake_abs_exit_conv Rs +112, nifty_calls Rs +44, benchmark_smallcap Rs +38, snake_abs Rs +9, snake_abs_conv Rs +5, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -169, snake_viper_wild Rs -231, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -359, gold Rs -726

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.