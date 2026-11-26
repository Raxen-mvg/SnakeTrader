# Paper trading report

Updated 2026-11-26 10:09 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,375 | +12.69% | 0 | - | 237 |
| unified | 224,175 | +12.09% | 0 | - | 236 |
| oracle | 213,508 | +6.75% | 0 | - | 233 |
| intramonth | 211,619 | +5.81% | 0 | - | 235 |
| random_hold | 210,298 | +5.15% | 13 | 69% | 1,037 |
| intraweek | 208,465 | +4.23% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,414 | +1.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,744 | +1.37% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| snake_abs | 200,650 | +0.33% | 1 | 100% | 255 |
| snake_abs_conv | 200,476 | +0.24% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,262 | -1.87% | 16 | 50% | 2,827 |
| snake_anaconda | 194,946 | -2.53% | 3 | 33% | 374 |
| snake_viper_tick | 192,922 | -3.54% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,917 | -16.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,454 (-5.27%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,321 | +2.02% |
| benchmark_smallcap | +1,894 | +0.95% |
| intraweek | +1,722 | +0.83% |
| snake_abs_exit | +1,158 | +0.57% |
| random_hold | +805 | +0.38% |
| snake_abs_exit_conv | +768 | +0.38% |
| snake_abs_conv | +504 | +0.25% |
| snake_abs | +500 | +0.25% |
| snake_anaconda | +393 | +0.20% |
| benchmark | +352 | +0.16% |
| unified | +75 | +0.03% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intramonth | -74 | -0.04% |
| oracle | -287 | -0.13% |
| snake_viper_tick | -1,255 | -0.65% |
| snake_viper_wild | -1,282 | -0.65% |

Average per day so far: benchmark Rs +619, unified Rs +590, oracle Rs +329, intramonth Rs +283, random_hold Rs +251, intraweek Rs +206, snake_abs_exit Rs +90, snake_abs_exit_conv Rs +72, nifty_calls Rs +45, benchmark_smallcap Rs +19, snake_abs Rs +17, snake_abs_conv Rs +13, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -113, snake_anaconda Rs -140, snake_viper_tick Rs -236, snake_nonews Rs -284, snake Rs -304, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.