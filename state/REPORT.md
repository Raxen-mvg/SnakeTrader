# Paper trading report

Updated 2026-11-13 10:40 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,523 | +10.26% | 0 | - | 236 |
| benchmark | 219,997 | +10.00% | 0 | - | 237 |
| snake_abs_exit_conv | 217,214 | +8.61% | 2 | 50% | 345 |
| snake_abs_exit | 217,105 | +8.55% | 2 | 50% | 345 |
| intraweek | 216,172 | +8.09% | 30 | 53% | 3,302 |
| oracle | 213,661 | +6.83% | 0 | - | 233 |
| snake_abs | 213,312 | +6.66% | 1 | 100% | 255 |
| snake_abs_conv | 213,144 | +6.57% | 1 | 100% | 255 |
| intramonth | 211,323 | +5.66% | 0 | - | 235 |
| random_hold | 207,371 | +3.69% | 10 | 70% | 733 |
| snake_viper_wild | 206,781 | +3.39% | 14 | 50% | 2,496 |
| snake_anaconda | 205,223 | +2.61% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 203,245 | +1.62% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,472 | -7.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,172 (-3.91%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,514 | +0.70% |
| snake_viper_wild | +1,489 | +0.72% |
| snake_viper_tick | +1,463 | +0.72% |
| oracle | +546 | +0.26% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -173 | -0.08% |
| intramonth | -271 | -0.13% |
| snake_abs_exit | -337 | -0.15% |
| benchmark | -551 | -0.25% |
| random_hold | -683 | -0.33% |
| snake_anaconda | -705 | -0.34% |
| gold | -838 | -0.45% |
| snake_abs_exit_conv | -1,460 | -0.67% |
| snake_abs_conv | -2,391 | -1.11% |
| snake_abs | -2,399 | -1.11% |

Average per day so far: unified Rs +622, benchmark Rs +606, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +570, intraweek Rs +490, snake_abs_conv Rs +438, snake_abs Rs +429, oracle Rs +414, intramonth Rs +343, snake_viper_wild Rs +271, random_hold Rs +223, snake_anaconda Rs +187, snake_viper_tick Rs +147, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -471

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.