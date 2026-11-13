# Paper trading report

Updated 2026-11-13 09:58 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,226 | +10.61% | 0 | - | 236 |
| benchmark | 219,997 | +10.00% | 0 | - | 237 |
| snake_abs_exit_conv | 217,354 | +8.68% | 2 | 50% | 345 |
| snake_abs_exit | 216,773 | +8.39% | 2 | 50% | 345 |
| intraweek | 215,354 | +7.68% | 30 | 53% | 3,302 |
| oracle | 214,241 | +7.12% | 0 | - | 233 |
| snake_abs | 213,473 | +6.74% | 1 | 100% | 255 |
| snake_abs_conv | 213,305 | +6.65% | 1 | 100% | 255 |
| intramonth | 211,902 | +5.95% | 0 | - | 235 |
| random_hold | 207,680 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 205,480 | +2.74% | 14 | 50% | 2,496 |
| snake_anaconda | 204,502 | +2.25% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 201,966 | +0.98% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,029 | -7.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,305 (-3.85%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,125 | +0.53% |
| intraweek | +696 | +0.32% |
| unified | +529 | +0.24% |
| benchmark_smallcap | +493 | +0.24% |
| intramonth | +309 | +0.15% |
| snake_viper_wild | +187 | +0.09% |
| snake_viper_tick | +185 | +0.09% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -374 | -0.18% |
| benchmark | -551 | -0.25% |
| snake_abs_exit | -669 | -0.31% |
| gold | -1,282 | -0.69% |
| snake_abs_exit_conv | -1,320 | -0.60% |
| snake_anaconda | -1,425 | -0.69% |
| snake_abs_conv | -2,230 | -1.03% |
| snake_abs | -2,238 | -1.04% |

Average per day so far: unified Rs +643, benchmark Rs +606, snake_abs_exit_conv Rs +578, snake_abs_exit Rs +559, intraweek Rs +465, snake_abs_conv Rs +444, snake_abs Rs +435, oracle Rs +432, intramonth Rs +361, random_hold Rs +233, snake_viper_wild Rs +219, snake_anaconda Rs +161, benchmark_smallcap Rs +128, snake_viper_tick Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -484

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.