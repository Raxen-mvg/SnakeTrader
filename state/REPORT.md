# Paper trading report

Updated 2026-11-23 13:16 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,879 | +11.94% | 0 | - | 236 |
| benchmark | 222,445 | +11.22% | 0 | - | 237 |
| intraweek | 212,374 | +6.19% | 40 | 55% | 4,400 |
| intramonth | 212,076 | +6.04% | 0 | - | 235 |
| oracle | 211,635 | +5.82% | 0 | - | 233 |
| random_hold | 208,946 | +4.47% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,952 | +3.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,495 | +2.75% | 2 | 50% | 345 |
| snake_abs | 204,450 | +2.23% | 1 | 100% | 255 |
| snake_abs_conv | 204,287 | +2.14% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,894 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 198,075 | -0.96% | 3 | 33% | 374 |
| snake_viper_tick | 197,467 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,087 | -14.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,081 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,039 | +1.21% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -843 | -0.40% |
| snake_abs_exit_conv | -1,121 | -0.54% |
| snake_abs | -1,470 | -0.71% |
| snake_abs_conv | -1,496 | -0.73% |
| snake_abs_exit | -1,611 | -0.77% |
| benchmark_smallcap | -1,670 | -0.83% |
| random_hold | -1,814 | -0.86% |
| snake_anaconda | -1,831 | -0.92% |
| snake_viper_tick | -1,905 | -0.95% |
| snake_viper_wild | -1,935 | -0.95% |
| unified | -2,303 | -1.02% |
| benchmark | -2,693 | -1.20% |
| intramonth | -2,928 | -1.36% |
| intraweek | -3,338 | -1.55% |

Average per day so far: unified Rs +612, benchmark Rs +576, intraweek Rs +317, intramonth Rs +310, oracle Rs +298, random_hold Rs +229, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +153, snake_abs Rs +120, snake_abs_conv Rs +119, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -57, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.