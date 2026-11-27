# Paper trading report

Updated 2026-11-27 10:06 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,489 | +12.74% | 0 | - | 237 |
| unified | 223,064 | +11.53% | 0 | - | 236 |
| oracle | 212,498 | +6.25% | 0 | - | 233 |
| intramonth | 210,713 | +5.36% | 0 | - | 235 |
| random_hold | 210,056 | +5.03% | 13 | 69% | 1,037 |
| intraweek | 208,470 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,553 | +2.78% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,505 | +2.25% | 2 | 50% | 345 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,592 | +0.80% | 1 | 100% | 255 |
| snake_abs_conv | 201,416 | +0.71% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,262 | -2.37% | 3 | 33% | 374 |
| snake_viper_wild | 193,415 | -3.29% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,126 | -4.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,575 | -15.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,870 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,475 | +2.23% |
| snake_abs_exit_conv | +4,108 | +2.05% |
| snake_abs_conv | +3,050 | +1.54% |
| snake_abs | +3,040 | +1.53% |
| snake_anaconda | +2,966 | +1.54% |
| gold | +2,581 | +1.55% |
| random_hold | +1,462 | +0.70% |
| intraweek | +1,421 | +0.69% |
| benchmark_smallcap | +1,289 | +0.64% |
| snake_viper_wild | +1,210 | +0.63% |
| snake_viper_tick | +1,184 | +0.63% |
| oracle | +263 | +0.12% |
| intramonth | +180 | +0.09% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -14 | -0.01% |
| benchmark | -497 | -0.22% |

Average per day so far: benchmark Rs +607, unified Rs +549, oracle Rs +298, intramonth Rs +255, random_hold Rs +239, intraweek Rs +202, snake_abs_exit Rs +142, snake_abs_exit_conv Rs +116, benchmark_smallcap Rs +56, nifty_calls Rs +44, snake_abs Rs +40, snake_abs_conv Rs +36, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -128, snake_viper_wild Rs -194, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -319, gold Rs -748

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.