# Paper trading report

Updated 2026-11-23 12:30 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,892 | +11.95% | 0 | - | 236 |
| benchmark | 222,827 | +11.41% | 0 | - | 237 |
| intraweek | 212,360 | +6.18% | 40 | 55% | 4,400 |
| oracle | 211,871 | +5.93% | 0 | - | 233 |
| intramonth | 211,747 | +5.87% | 0 | - | 235 |
| random_hold | 208,807 | +4.40% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,098 | +3.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,790 | +2.90% | 2 | 50% | 345 |
| snake_abs | 204,816 | +2.41% | 1 | 100% | 255 |
| snake_abs_conv | 204,654 | +2.33% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,148 | +0.57% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_anaconda | 198,339 | -0.83% | 3 | 33% | 374 |
| snake_viper_tick | 197,716 | -1.14% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,022 | -14.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,114 (-4.94%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,973 | +1.17% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -608 | -0.29% |
| snake_abs_exit_conv | -827 | -0.40% |
| snake_abs | -1,104 | -0.54% |
| snake_abs_conv | -1,129 | -0.55% |
| benchmark_smallcap | -1,300 | -0.65% |
| snake_abs_exit | -1,464 | -0.70% |
| snake_anaconda | -1,567 | -0.78% |
| snake_viper_tick | -1,656 | -0.83% |
| snake_viper_wild | -1,681 | -0.83% |
| random_hold | -1,952 | -0.93% |
| unified | -2,290 | -1.01% |
| benchmark | -2,310 | -1.03% |
| intramonth | -3,257 | -1.51% |
| intraweek | -3,352 | -1.55% |

Average per day so far: unified Rs +613, benchmark Rs +585, intraweek Rs +317, oracle Rs +304, intramonth Rs +301, random_hold Rs +226, snake_abs_exit Rs +197, snake_abs_exit_conv Rs +161, snake_abs Rs +130, snake_abs_conv Rs +129, nifty_calls Rs +47, snake_viper_wild Rs +37, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_anaconda Rs -49, snake_viper_tick Rs -82, snake_nonews Rs -300, snake Rs -320, gold Rs -769

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.