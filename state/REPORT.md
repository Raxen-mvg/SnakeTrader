# Paper trading report

Updated 2026-11-27 14:55 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,180 | +12.09% | 0 | - | 236 |
| benchmark | 223,860 | +11.93% | 0 | - | 237 |
| oracle | 212,268 | +6.13% | 0 | - | 233 |
| intramonth | 211,511 | +5.75% | 0 | - | 235 |
| random_hold | 211,218 | +5.61% | 13 | 69% | 1,037 |
| intraweek | 207,510 | +3.75% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,697 | +3.35% | 2 | 50% | 345 |
| snake_abs_exit | 204,412 | +2.21% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,899 | -0.05% | 1 | 100% | 255 |
| snake_abs_conv | 199,715 | -0.14% | 1 | 100% | 255 |
| snake_anaconda | 193,346 | -3.33% | 3 | 33% | 374 |
| snake_viper_wild | 192,447 | -3.78% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,178 | -5.41% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,041 | -14.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,191 (-5.40%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,300 | +3.14% |
| gold | +5,047 | +3.04% |
| snake_abs_exit | +3,334 | +1.66% |
| random_hold | +2,624 | +1.26% |
| snake_abs_conv | +1,348 | +0.68% |
| snake_abs | +1,347 | +0.68% |
| unified | +1,102 | +0.49% |
| snake_anaconda | +1,049 | +0.55% |
| intramonth | +977 | +0.46% |
| benchmark_smallcap | +617 | +0.31% |
| intraweek | +462 | +0.22% |
| snake_viper_wild | +242 | +0.13% |
| snake_viper_tick | +237 | +0.13% |
| oracle | +33 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -2,127 | -0.94% |

Average per day so far: unified Rs +576, benchmark Rs +568, oracle Rs +292, intramonth Rs +274, random_hold Rs +267, intraweek Rs +179, snake_abs_exit_conv Rs +172, snake_abs_exit Rs +113, nifty_calls Rs +44, benchmark_smallcap Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -3, snake_abs_conv Rs -7, snake_anaconda Rs -180, snake_viper_wild Rs -222, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -349, gold Rs -690

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.