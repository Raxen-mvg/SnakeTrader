# Paper trading report

Updated 2026-11-17 14:05 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,986 | +10.99% | 0 | - | 237 |
| unified | 221,597 | +10.80% | 0 | - | 236 |
| snake_abs_exit | 213,589 | +6.79% | 2 | 50% | 345 |
| intraweek | 213,379 | +6.69% | 35 | 54% | 3,851 |
| oracle | 212,360 | +6.18% | 0 | - | 233 |
| snake_abs_exit_conv | 211,993 | +6.00% | 2 | 50% | 345 |
| intramonth | 211,467 | +5.73% | 0 | - | 235 |
| snake_viper_wild | 209,120 | +4.56% | 14 | 50% | 2,496 |
| snake_abs | 208,900 | +4.45% | 1 | 100% | 255 |
| snake_abs_conv | 208,759 | +4.38% | 1 | 100% | 255 |
| random_hold | 207,544 | +3.77% | 10 | 70% | 733 |
| snake_viper_tick | 205,546 | +2.77% | 13 | 46% | 2,299 |
| snake_anaconda | 204,465 | +2.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,087 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,987 | -9.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,110 (-4.45%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +2,976 | +1.44% |
| snake_viper_tick | +2,926 | +1.44% |
| intraweek | +2,113 | +1.00% |
| benchmark | +1,905 | +0.87% |
| oracle | +337 | +0.16% |
| benchmark_smallcap | +258 | +0.13% |
| unified | +159 | +0.07% |
| gold | +33 | +0.02% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -151 | -0.07% |
| random_hold | -249 | -0.12% |
| snake_anaconda | -638 | -0.31% |
| snake_abs_exit | -821 | -0.38% |
| snake_abs_exit_conv | -1,225 | -0.57% |
| snake_abs_conv | -1,231 | -0.59% |
| snake_abs | -1,233 | -0.59% |

Average per day so far: benchmark Rs +628, unified Rs +617, snake_abs_exit Rs +425, intraweek Rs +382, snake_abs_exit_conv Rs +375, oracle Rs +353, snake_viper_wild Rs +338, intramonth Rs +328, snake_abs_conv Rs +274, snake_abs Rs +270, snake_viper_tick Rs +231, random_hold Rs +216, snake_anaconda Rs +149, nifty_calls Rs +52, benchmark_smallcap Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -543

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.