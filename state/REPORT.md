# Paper trading report

Updated 2026-11-23 12:13 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,256 | +12.13% | 0 | - | 236 |
| benchmark | 223,041 | +11.52% | 0 | - | 237 |
| intraweek | 212,988 | +6.49% | 40 | 55% | 4,400 |
| intramonth | 212,163 | +6.08% | 0 | - | 235 |
| oracle | 211,872 | +5.94% | 0 | - | 233 |
| random_hold | 209,948 | +4.97% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,969 | +3.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,548 | +2.77% | 2 | 50% | 345 |
| snake_abs | 204,491 | +2.25% | 1 | 100% | 255 |
| snake_abs_conv | 204,321 | +2.16% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,249 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,686 | -0.16% | 0 | - | 237 |
| snake_anaconda | 197,955 | -1.02% | 3 | 33% | 374 |
| snake_viper_tick | 197,815 | -1.09% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,104 | -14.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,422 (-4.79%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,055 | +1.22% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -607 | -0.29% |
| random_hold | -811 | -0.39% |
| snake_abs_exit_conv | -1,068 | -0.52% |
| benchmark_smallcap | -1,222 | -0.61% |
| snake_abs | -1,429 | -0.69% |
| snake_abs_conv | -1,462 | -0.71% |
| snake_viper_tick | -1,557 | -0.78% |
| snake_viper_wild | -1,580 | -0.78% |
| snake_abs_exit | -1,593 | -0.76% |
| unified | -1,926 | -0.85% |
| snake_anaconda | -1,950 | -0.98% |
| benchmark | -2,096 | -0.93% |
| intraweek | -2,724 | -1.26% |
| intramonth | -2,841 | -1.32% |

Average per day so far: unified Rs +622, benchmark Rs +591, intraweek Rs +333, intramonth Rs +312, oracle Rs +304, random_hold Rs +255, snake_abs_exit Rs +194, snake_abs_exit_conv Rs +154, snake_abs Rs +121, snake_abs_conv Rs +120, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_anaconda Rs -60, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.