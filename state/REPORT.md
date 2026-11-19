# Paper trading report

Updated 2026-11-19 10:00 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,003 | +12.00% | 0 | - | 236 |
| benchmark | 220,471 | +10.24% | 0 | - | 237 |
| intramonth | 213,823 | +6.91% | 0 | - | 235 |
| snake_abs_exit | 213,729 | +6.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,922 | +5.96% | 2 | 50% | 345 |
| intraweek | 211,636 | +5.82% | 35 | 54% | 3,851 |
| oracle | 211,380 | +5.69% | 0 | - | 233 |
| snake_abs | 209,173 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,053 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,814 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 207,702 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,152 | +2.08% | 15 | 47% | 2,625 |
| snake_anaconda | 203,906 | +1.95% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,582 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,440 (-4.28%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,550 | +0.73% |
| unified | +1,391 | +0.62% |
| benchmark_smallcap | +1,256 | +0.63% |
| random_hold | +882 | +0.43% |
| snake_viper_wild | +662 | +0.32% |
| snake_viper_tick | +649 | +0.32% |
| oracle | +584 | +0.28% |
| benchmark | +176 | +0.08% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -203 | -0.10% |
| snake_abs | -263 | -0.13% |
| snake_abs_conv | -272 | -0.13% |
| snake_abs_exit | -303 | -0.14% |
| snake_abs_exit_conv | -462 | -0.22% |
| snake_anaconda | -495 | -0.24% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +649, benchmark Rs +553, snake_abs_exit Rs +404, intramonth Rs +374, snake_abs_exit_conv Rs +351, intraweek Rs +314, oracle Rs +308, snake_abs_conv Rs +266, snake_viper_wild Rs +266, snake_abs Rs +262, random_hold Rs +211, snake_viper_tick Rs +160, snake_anaconda Rs +122, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.