# Paper trading report

Updated 2026-11-13 10:01 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,128 | +10.56% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 217,506 | +8.75% | 2 | 50% | 345 |
| snake_abs_exit | 216,967 | +8.48% | 2 | 50% | 345 |
| intraweek | 215,095 | +7.55% | 30 | 53% | 3,302 |
| oracle | 214,168 | +7.08% | 0 | - | 233 |
| snake_abs | 213,588 | +6.79% | 1 | 100% | 255 |
| snake_abs_conv | 213,423 | +6.71% | 1 | 100% | 255 |
| intramonth | 211,791 | +5.90% | 0 | - | 235 |
| random_hold | 207,516 | +3.76% | 10 | 70% | 733 |
| snake_viper_wild | 205,387 | +2.69% | 14 | 50% | 2,496 |
| snake_anaconda | 205,031 | +2.52% | 3 | 33% | 374 |
| benchmark_smallcap | 203,901 | +1.95% | 0 | - | 237 |
| snake_viper_tick | 201,875 | +0.94% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,177 | -7.91% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,200 (-3.90%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,053 | +0.49% |
| benchmark_smallcap | +695 | +0.34% |
| intraweek | +437 | +0.20% |
| unified | +432 | +0.20% |
| intramonth | +198 | +0.09% |
| snake_viper_wild | +94 | +0.05% |
| snake_viper_tick | +93 | +0.05% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -475 | -0.22% |
| random_hold | -538 | -0.26% |
| benchmark | -627 | -0.28% |
| snake_anaconda | -896 | -0.43% |
| gold | -1,134 | -0.61% |
| snake_abs_exit_conv | -1,168 | -0.53% |
| snake_abs_conv | -2,112 | -0.98% |
| snake_abs | -2,123 | -0.98% |

Average per day so far: unified Rs +640, benchmark Rs +604, snake_abs_exit_conv Rs +584, snake_abs_exit Rs +566, intraweek Rs +457, snake_abs_conv Rs +447, snake_abs Rs +438, oracle Rs +429, intramonth Rs +357, random_hold Rs +228, snake_viper_wild Rs +215, snake_anaconda Rs +180, benchmark_smallcap Rs +135, snake_viper_tick Rs +85, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -479

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.