# Paper trading report

Updated 2026-11-26 12:46 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,079 | +13.04% | 0 | - | 237 |
| unified | 223,317 | +11.66% | 0 | - | 236 |
| oracle | 213,244 | +6.62% | 0 | - | 233 |
| intramonth | 210,369 | +5.18% | 0 | - | 235 |
| random_hold | 209,844 | +4.92% | 13 | 69% | 1,037 |
| intraweek | 208,211 | +4.11% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,269 | +0.13% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,844 | -0.08% | 2 | 50% | 345 |
| snake_abs | 198,181 | -0.91% | 1 | 100% | 255 |
| snake_abs_conv | 197,981 | -1.01% | 1 | 100% | 255 |
| snake_anaconda | 191,934 | -4.03% | 3 | 33% | 374 |
| snake_viper_wild | 191,841 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,584 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,471 | -16.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,760 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,874 | +1.14% |
| benchmark_smallcap | +1,760 | +0.89% |
| intraweek | +1,468 | +0.71% |
| benchmark | +1,056 | +0.47% |
| random_hold | +351 | +0.17% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -551 | -0.26% |
| unified | -783 | -0.35% |
| intramonth | -1,325 | -0.63% |
| snake_abs | -1,969 | -0.98% |
| snake_abs_exit | -1,987 | -0.98% |
| snake_abs_conv | -1,991 | -1.00% |
| snake_abs_exit_conv | -2,132 | -1.06% |
| snake_anaconda | -2,619 | -1.35% |
| snake_viper_tick | -5,593 | -2.88% |
| snake_viper_wild | -5,703 | -2.89% |

Average per day so far: benchmark Rs +636, unified Rs +569, oracle Rs +323, intramonth Rs +253, random_hold Rs +240, intraweek Rs +200, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -4, snake_abs Rs -47, snake_abs_conv Rs -53, snake_anaconda Rs -224, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -381, gold Rs -818

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.