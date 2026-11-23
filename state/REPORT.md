# Paper trading report

Updated 2026-11-23 12:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,830 | +11.91% | 0 | - | 236 |
| benchmark | 222,674 | +11.34% | 0 | - | 237 |
| intraweek | 212,372 | +6.19% | 40 | 55% | 4,400 |
| intramonth | 211,807 | +5.90% | 0 | - | 235 |
| oracle | 211,678 | +5.84% | 0 | - | 233 |
| random_hold | 208,649 | +4.32% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,511 | +3.26% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,280 | +2.64% | 2 | 50% | 345 |
| snake_abs | 204,100 | +2.05% | 1 | 100% | 255 |
| snake_abs_conv | 203,932 | +1.97% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,903 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_anaconda | 197,733 | -1.13% | 3 | 33% | 374 |
| snake_viper_tick | 197,476 | -1.26% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,531 | -14.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,961 (-5.02%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,482 | +1.48% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -801 | -0.38% |
| snake_abs_exit_conv | -1,336 | -0.65% |
| benchmark_smallcap | -1,469 | -0.73% |
| snake_abs | -1,820 | -0.88% |
| snake_abs_conv | -1,851 | -0.90% |
| snake_viper_tick | -1,895 | -0.95% |
| snake_viper_wild | -1,926 | -0.95% |
| snake_abs_exit | -2,051 | -0.98% |
| random_hold | -2,111 | -1.00% |
| snake_anaconda | -2,172 | -1.09% |
| unified | -2,352 | -1.04% |
| benchmark | -2,463 | -1.09% |
| intramonth | -3,197 | -1.49% |
| intraweek | -3,340 | -1.55% |

Average per day so far: unified Rs +611, benchmark Rs +581, intraweek Rs +317, intramonth Rs +303, oracle Rs +299, random_hold Rs +222, snake_abs_exit Rs +181, snake_abs_exit_conv Rs +147, snake_abs Rs +111, snake_abs_conv Rs +109, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -67, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -756

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.