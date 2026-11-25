# Paper trading report

Updated 2026-11-25 10:59 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,665 | +12.83% | 0 | - | 237 |
| unified | 225,296 | +12.65% | 0 | - | 236 |
| intramonth | 213,065 | +6.53% | 0 | - | 235 |
| oracle | 212,141 | +6.07% | 0 | - | 233 |
| random_hold | 209,736 | +4.87% | 12 | 75% | 1,009 |
| intraweek | 208,442 | +4.22% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,657 | +0.83% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,184 | +0.59% | 2 | 50% | 345 |
| snake_abs | 200,958 | +0.48% | 1 | 100% | 255 |
| snake_abs_conv | 200,765 | +0.38% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 195,369 | -2.32% | 16 | 50% | 2,827 |
| snake_anaconda | 193,272 | -3.36% | 3 | 33% | 374 |
| snake_viper_tick | 192,048 | -3.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,402 | -17.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,367 (-5.32%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,192 | +1.89% |
| random_hold | +1,310 | +0.63% |
| unified | +1,010 | +0.45% |
| benchmark_smallcap | +572 | +0.29% |
| intramonth | +314 | +0.15% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -201 | -0.10% |
| intraweek | -3,177 | -1.50% |
| gold | -4,028 | -2.38% |
| snake_abs | -4,503 | -2.19% |
| snake_abs_conv | -4,537 | -2.21% |
| snake_anaconda | -5,431 | -2.73% |
| snake_viper_tick | -5,645 | -2.85% |
| snake_viper_wild | -5,755 | -2.86% |
| snake_abs_exit | -5,838 | -2.81% |
| snake_abs_exit_conv | -5,862 | -2.83% |

Average per day so far: benchmark Rs +642, unified Rs +632, intramonth Rs +327, oracle Rs +304, random_hold Rs +243, intraweek Rs +211, nifty_calls Rs +46, snake_abs_exit Rs +45, snake_abs_exit_conv Rs +32, snake_abs Rs +25, snake_abs_conv Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -145, snake_anaconda Rs -192, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.