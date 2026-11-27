# Paper trading report

Updated 2026-11-27 10:35 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,816 | +12.41% | 0 | - | 237 |
| unified | 222,761 | +11.38% | 0 | - | 236 |
| oracle | 212,378 | +6.19% | 0 | - | 233 |
| intramonth | 210,580 | +5.29% | 0 | - | 235 |
| random_hold | 209,963 | +4.98% | 13 | 69% | 1,037 |
| intraweek | 208,025 | +4.01% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,026 | +2.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,725 | +1.86% | 2 | 50% | 345 |
| benchmark_smallcap | 201,905 | +0.95% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,021 | +0.51% | 1 | 100% | 255 |
| snake_abs_conv | 200,841 | +0.42% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,460 | -2.77% | 3 | 33% | 374 |
| snake_viper_wild | 193,292 | -3.35% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,005 | -5.00% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,476 | -15.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,688 (-5.66%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,949 | +1.96% |
| snake_abs_exit_conv | +3,328 | +1.66% |
| gold | +2,482 | +1.50% |
| snake_abs_conv | +2,474 | +1.25% |
| snake_abs | +2,469 | +1.24% |
| snake_anaconda | +2,163 | +1.12% |
| random_hold | +1,369 | +0.66% |
| snake_viper_wild | +1,086 | +0.56% |
| benchmark_smallcap | +1,065 | +0.53% |
| snake_viper_tick | +1,064 | +0.56% |
| intraweek | +976 | +0.47% |
| oracle | +142 | +0.07% |
| intramonth | +47 | +0.02% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -318 | -0.14% |
| benchmark | -1,170 | -0.52% |

Average per day so far: benchmark Rs +591, unified Rs +542, oracle Rs +295, intramonth Rs +252, random_hold Rs +237, intraweek Rs +191, snake_abs_exit Rs +129, snake_abs_exit_conv Rs +96, benchmark_smallcap Rs +50, nifty_calls Rs +44, snake_abs Rs +26, snake_abs_conv Rs +22, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -150, snake_viper_wild Rs -197, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -322, gold Rs -751

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.