# Paper trading report

Updated 2026-11-27 11:04 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,418 | +12.21% | 0 | - | 237 |
| unified | 222,433 | +11.22% | 0 | - | 236 |
| oracle | 212,140 | +6.07% | 0 | - | 233 |
| intramonth | 210,229 | +5.11% | 0 | - | 235 |
| random_hold | 210,016 | +5.01% | 13 | 69% | 1,037 |
| intraweek | 207,688 | +3.84% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,480 | +2.74% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,185 | +2.09% | 2 | 50% | 345 |
| benchmark_smallcap | 202,073 | +1.04% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,101 | +0.55% | 1 | 100% | 255 |
| snake_abs_conv | 200,923 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,671 | -2.67% | 3 | 33% | 374 |
| snake_viper_wild | 193,527 | -3.24% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,236 | -4.88% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,525 (-5.74%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,402 | +2.19% |
| snake_abs_exit_conv | +3,788 | +1.89% |
| gold | +3,239 | +1.95% |
| snake_abs_conv | +2,557 | +1.29% |
| snake_abs | +2,548 | +1.28% |
| snake_anaconda | +2,374 | +1.24% |
| random_hold | +1,422 | +0.68% |
| snake_viper_wild | +1,322 | +0.69% |
| snake_viper_tick | +1,295 | +0.69% |
| benchmark_smallcap | +1,233 | +0.61% |
| intraweek | +639 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -96 | -0.04% |
| intramonth | -305 | -0.14% |
| unified | -646 | -0.29% |
| benchmark | -1,568 | -0.69% |

Average per day so far: benchmark Rs +581, unified Rs +534, oracle Rs +289, intramonth Rs +244, random_hold Rs +238, intraweek Rs +183, snake_abs_exit Rs +141, snake_abs_exit_conv Rs +107, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -144, snake_viper_wild Rs -190, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -315, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.