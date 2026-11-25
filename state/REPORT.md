# Paper trading report

Updated 2026-11-25 12:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,543 | +12.77% | 0 | - | 237 |
| unified | 225,459 | +12.73% | 0 | - | 236 |
| intramonth | 213,632 | +6.82% | 0 | - | 235 |
| oracle | 212,784 | +6.39% | 0 | - | 233 |
| random_hold | 210,134 | +5.07% | 12 | 75% | 1,009 |
| intraweek | 208,206 | +4.10% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,342 | +1.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,950 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,864 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,680 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_viper_wild | 196,958 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,057 | -2.97% | 3 | 33% | 374 |
| snake_viper_tick | 193,603 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,383 | -17.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,655 (-5.17%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,070 | +1.84% |
| random_hold | +1,707 | +0.82% |
| unified | +1,174 | +0.52% |
| intramonth | +881 | +0.41% |
| benchmark_smallcap | +460 | +0.23% |
| oracle | +442 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,413 | -1.61% |
| snake_viper_tick | -4,089 | -2.07% |
| snake_viper_wild | -4,167 | -2.07% |
| snake_abs | -4,597 | -2.24% |
| snake_abs_conv | -4,623 | -2.25% |
| snake_anaconda | -4,647 | -2.34% |
| gold | -5,047 | -2.98% |
| snake_abs_exit_conv | -5,096 | -2.46% |
| snake_abs_exit | -5,153 | -2.48% |

Average per day so far: benchmark Rs +639, unified Rs +636, intramonth Rs +341, oracle Rs +320, random_hold Rs +253, intraweek Rs +205, snake_abs_exit Rs +63, snake_abs_exit_conv Rs +53, nifty_calls Rs +46, snake_abs Rs +23, snake_abs_conv Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -95, snake_anaconda Rs -170, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -890

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.