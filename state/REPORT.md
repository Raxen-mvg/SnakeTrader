# Paper trading report

Updated 2026-11-23 14:52 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,055 | +12.03% | 0 | - | 236 |
| benchmark | 221,680 | +10.84% | 0 | - | 237 |
| oracle | 211,961 | +5.98% | 0 | - | 233 |
| intramonth | 211,918 | +5.96% | 0 | - | 235 |
| intraweek | 211,911 | +5.96% | 40 | 55% | 4,400 |
| random_hold | 208,856 | +4.43% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,306 | +3.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,704 | +3.35% | 2 | 50% | 345 |
| snake_abs | 205,110 | +2.56% | 1 | 100% | 255 |
| snake_abs_conv | 204,935 | +2.47% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,379 | +0.69% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,887 | -0.06% | 0 | - | 237 |
| snake_anaconda | 198,208 | -0.90% | 3 | 33% | 374 |
| snake_viper_tick | 197,942 | -1.03% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,660 | -15.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,182 (-4.91%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,611 | +0.96% |
| snake_abs_exit_conv | +87 | +0.04% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -518 | -0.24% |
| snake_abs | -810 | -0.39% |
| snake_abs_conv | -848 | -0.41% |
| benchmark_smallcap | -1,020 | -0.51% |
| snake_abs_exit | -1,256 | -0.60% |
| snake_viper_tick | -1,430 | -0.72% |
| snake_viper_wild | -1,451 | -0.71% |
| snake_anaconda | -1,697 | -0.85% |
| random_hold | -1,904 | -0.90% |
| unified | -2,126 | -0.94% |
| intramonth | -3,086 | -1.44% |
| benchmark | -3,458 | -1.54% |
| intraweek | -3,801 | -1.76% |

Average per day so far: unified Rs +617, benchmark Rs +556, oracle Rs +307, intramonth Rs +306, intraweek Rs +305, random_hold Rs +227, snake_abs_exit Rs +203, snake_abs_exit_conv Rs +186, snake_abs Rs +138, snake_abs_conv Rs +137, nifty_calls Rs +47, snake_viper_wild Rs +44, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -3, snake_anaconda Rs -53, snake_viper_tick Rs -74, snake_nonews Rs -300, snake Rs -320, gold Rs -778

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.