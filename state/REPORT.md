# Paper trading report

Updated 2026-11-27 11:25 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,929 | +11.96% | 0 | - | 237 |
| unified | 222,255 | +11.13% | 0 | - | 236 |
| oracle | 211,678 | +5.84% | 0 | - | 233 |
| random_hold | 210,324 | +5.16% | 13 | 69% | 1,037 |
| intramonth | 210,068 | +5.03% | 0 | - | 235 |
| intraweek | 207,697 | +3.85% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,949 | +2.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,843 | +1.92% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,423 | +0.71% | 0 | - | 237 |
| snake_abs | 200,801 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,623 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,257 | -2.87% | 3 | 33% | 374 |
| snake_viper_wild | 193,474 | -3.26% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,184 | -4.91% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,167 | -15.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,372 (-5.81%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,871 | +1.93% |
| snake_abs_exit_conv | +3,446 | +1.72% |
| gold | +3,173 | +1.91% |
| snake_abs_conv | +2,256 | +1.14% |
| snake_abs | +2,249 | +1.13% |
| snake_anaconda | +1,961 | +1.02% |
| random_hold | +1,730 | +0.83% |
| snake_viper_wild | +1,269 | +0.66% |
| snake_viper_tick | +1,243 | +0.66% |
| intraweek | +648 | +0.31% |
| benchmark_smallcap | +583 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -465 | -0.22% |
| oracle | -558 | -0.26% |
| unified | -824 | -0.37% |
| benchmark | -2,058 | -0.91% |

Average per day so far: benchmark Rs +570, unified Rs +530, oracle Rs +278, random_hold Rs +246, intramonth Rs +240, intraweek Rs +183, snake_abs_exit Rs +127, snake_abs_exit_conv Rs +99, nifty_calls Rs +44, benchmark_smallcap Rs +37, snake_abs Rs +20, snake_abs_conv Rs +16, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -155, snake_viper_wild Rs -192, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -317, gold Rs -734

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.