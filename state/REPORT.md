# Paper trading report

Updated 2026-11-27 10:56 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,640 | +12.32% | 0 | - | 237 |
| unified | 222,781 | +11.39% | 0 | - | 236 |
| oracle | 212,333 | +6.17% | 0 | - | 233 |
| intramonth | 210,569 | +5.28% | 0 | - | 235 |
| random_hold | 210,053 | +5.03% | 13 | 69% | 1,037 |
| intraweek | 207,707 | +3.85% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,259 | +2.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,127 | +2.06% | 2 | 50% | 345 |
| benchmark_smallcap | 202,096 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,172 | +0.59% | 1 | 100% | 255 |
| snake_abs_conv | 200,992 | +0.50% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,649 | -2.68% | 3 | 33% | 374 |
| snake_viper_wild | 193,513 | -3.24% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,222 | -4.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,117 | -15.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,685 (-5.66%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,182 | +2.08% |
| snake_abs_exit_conv | +3,730 | +1.86% |
| gold | +3,124 | +1.88% |
| snake_abs_conv | +2,626 | +1.32% |
| snake_abs | +2,619 | +1.32% |
| snake_anaconda | +2,352 | +1.22% |
| random_hold | +1,459 | +0.70% |
| snake_viper_wild | +1,307 | +0.68% |
| snake_viper_tick | +1,281 | +0.68% |
| benchmark_smallcap | +1,256 | +0.62% |
| intraweek | +659 | +0.32% |
| oracle | +97 | +0.05% |
| intramonth | +35 | +0.02% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -297 | -0.13% |
| benchmark | -1,346 | -0.60% |

Average per day so far: benchmark Rs +587, unified Rs +542, oracle Rs +294, intramonth Rs +252, random_hold Rs +239, intraweek Rs +184, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +106, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +29, snake_abs_conv Rs +25, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -145, snake_viper_wild Rs -191, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -315, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.