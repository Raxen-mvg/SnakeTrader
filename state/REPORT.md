# Paper trading report

Updated 2026-11-23 14:01 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,948 | +11.97% | 0 | - | 236 |
| benchmark | 222,215 | +11.11% | 0 | - | 237 |
| intraweek | 212,400 | +6.20% | 40 | 55% | 4,400 |
| intramonth | 212,029 | +6.01% | 0 | - | 235 |
| oracle | 211,509 | +5.75% | 0 | - | 233 |
| random_hold | 208,924 | +4.46% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,932 | +3.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,714 | +2.86% | 2 | 50% | 345 |
| snake_abs | 204,689 | +2.35% | 1 | 100% | 255 |
| snake_abs_conv | 204,516 | +2.26% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,865 | +0.43% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,428 | -0.29% | 0 | - | 237 |
| snake_anaconda | 197,827 | -1.09% | 3 | 33% | 374 |
| snake_viper_tick | 197,439 | -1.28% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,381 | -15.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,088 (-4.96%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,332 | +0.79% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -903 | -0.44% |
| oracle | -970 | -0.46% |
| snake_abs | -1,231 | -0.60% |
| snake_abs_conv | -1,267 | -0.62% |
| benchmark_smallcap | -1,480 | -0.74% |
| snake_abs_exit | -1,630 | -0.78% |
| random_hold | -1,835 | -0.87% |
| snake_viper_tick | -1,933 | -0.97% |
| snake_viper_wild | -1,964 | -0.97% |
| snake_anaconda | -2,079 | -1.04% |
| unified | -2,234 | -0.99% |
| benchmark | -2,922 | -1.30% |
| intramonth | -2,975 | -1.38% |
| intraweek | -3,312 | -1.53% |

Average per day so far: unified Rs +614, benchmark Rs +570, intraweek Rs +318, intramonth Rs +308, oracle Rs +295, random_hold Rs +229, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +159, snake_abs Rs +127, snake_abs_conv Rs +125, nifty_calls Rs +47, snake_viper_wild Rs +28, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_anaconda Rs -64, snake_viper_tick Rs -91, snake_nonews Rs -300, snake Rs -320, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.