# Paper trading report

Updated 2026-11-27 10:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 222,939 | +11.47% | 0 | - | 236 |
| oracle | 212,461 | +6.23% | 0 | - | 233 |
| intramonth | 210,602 | +5.30% | 0 | - | 235 |
| random_hold | 210,065 | +5.03% | 13 | 69% | 1,037 |
| intraweek | 208,423 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,669 | +2.83% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,570 | +2.29% | 2 | 50% | 345 |
| benchmark_smallcap | 202,107 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,551 | +0.78% | 1 | 100% | 255 |
| snake_abs_conv | 201,375 | +0.69% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,275 | -2.36% | 3 | 33% | 374 |
| snake_viper_wild | 193,262 | -3.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,975 | -5.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,641 | -15.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,818 (-5.59%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,592 | +2.28% |
| snake_abs_exit_conv | +4,173 | +2.08% |
| snake_abs_conv | +3,009 | +1.52% |
| snake_abs | +2,999 | +1.51% |
| snake_anaconda | +2,979 | +1.55% |
| gold | +2,647 | +1.59% |
| random_hold | +1,471 | +0.70% |
| intraweek | +1,374 | +0.66% |
| benchmark_smallcap | +1,267 | +0.63% |
| snake_viper_wild | +1,056 | +0.55% |
| snake_viper_tick | +1,034 | +0.55% |
| oracle | +226 | +0.11% |
| intramonth | +69 | +0.03% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -140 | -0.06% |
| benchmark | -329 | -0.15% |

Average per day so far: benchmark Rs +611, unified Rs +546, oracle Rs +297, intramonth Rs +252, random_hold Rs +240, intraweek Rs +201, snake_abs_exit Rs +145, snake_abs_exit_conv Rs +117, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +39, snake_abs_conv Rs +35, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -128, snake_viper_wild Rs -198, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -323, gold Rs -747

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.