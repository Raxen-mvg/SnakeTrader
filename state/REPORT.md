# Paper trading report

Updated 2026-11-23 09:49 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,388 | +12.69% | 0 | - | 236 |
| benchmark | 223,738 | +11.87% | 0 | - | 237 |
| intraweek | 213,362 | +6.68% | 40 | 55% | 4,400 |
| intramonth | 213,213 | +6.61% | 0 | - | 235 |
| oracle | 211,779 | +5.89% | 0 | - | 233 |
| random_hold | 210,662 | +5.33% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,252 | +4.13% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,653 | +3.33% | 2 | 50% | 345 |
| snake_abs | 205,922 | +2.96% | 1 | 100% | 255 |
| snake_abs_conv | 205,770 | +2.88% | 1 | 100% | 255 |
| snake_viper_wild | 203,645 | +1.82% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,171 | +0.09% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,899 | -0.05% | 0 | - | 237 |
| snake_anaconda | 199,558 | -0.22% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,265 | -15.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,124 (-4.44%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,217 | +0.72% |
| snake_viper_wild | +816 | +0.40% |
| snake_viper_tick | +799 | +0.40% |
| snake_abs_exit_conv | +37 | +0.02% |
| snake_abs | +2 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_abs_conv | -13 | -0.01% |
| random_hold | -97 | -0.05% |
| snake_abs_exit | -310 | -0.15% |
| snake_anaconda | -347 | -0.17% |
| oracle | -699 | -0.33% |
| unified | -793 | -0.35% |
| benchmark_smallcap | -1,009 | -0.50% |
| benchmark | -1,400 | -0.62% |
| intramonth | -1,791 | -0.83% |
| intraweek | -2,350 | -1.09% |

Average per day so far: unified Rs +651, benchmark Rs +609, intraweek Rs +343, intramonth Rs +339, oracle Rs +302, random_hold Rs +273, snake_abs_exit Rs +229, snake_abs_exit_conv Rs +185, snake_abs_conv Rs +160, snake_abs Rs +160, snake_viper_wild Rs +118, nifty_calls Rs +47, snake_viper_tick Rs +6, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -3, snake_anaconda Rs -13, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.