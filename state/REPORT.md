# Paper trading report

Updated 2026-11-13 10:28 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,486 | +10.24% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 216,758 | +8.38% | 2 | 50% | 345 |
| intraweek | 216,495 | +8.25% | 30 | 53% | 3,302 |
| snake_abs_exit | 216,329 | +8.16% | 2 | 50% | 345 |
| oracle | 213,908 | +6.95% | 0 | - | 233 |
| snake_abs | 213,142 | +6.57% | 1 | 100% | 255 |
| snake_abs_conv | 212,972 | +6.49% | 1 | 100% | 255 |
| intramonth | 211,359 | +5.68% | 0 | - | 235 |
| random_hold | 207,272 | +3.64% | 10 | 70% | 733 |
| snake_viper_wild | 206,596 | +3.30% | 14 | 50% | 2,496 |
| snake_anaconda | 205,109 | +2.55% | 3 | 33% | 374 |
| benchmark_smallcap | 203,575 | +1.79% | 0 | - | 237 |
| snake_viper_tick | 203,062 | +1.53% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,374 | -7.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,266 (-3.87%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,837 | +0.86% |
| snake_viper_wild | +1,303 | +0.64% |
| snake_viper_tick | +1,281 | +0.64% |
| oracle | +793 | +0.37% |
| benchmark_smallcap | +370 | +0.18% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -211 | -0.10% |
| intramonth | -234 | -0.11% |
| benchmark | -627 | -0.28% |
| random_hold | -782 | -0.38% |
| snake_anaconda | -818 | -0.40% |
| gold | -937 | -0.51% |
| snake_abs_exit | -1,113 | -0.51% |
| snake_abs_exit_conv | -1,916 | -0.88% |
| snake_abs_conv | -2,563 | -1.19% |
| snake_abs | -2,569 | -1.19% |

Average per day so far: unified Rs +621, benchmark Rs +604, snake_abs_exit_conv Rs +559, snake_abs_exit Rs +544, intraweek Rs +500, snake_abs_conv Rs +432, snake_abs Rs +424, oracle Rs +421, intramonth Rs +344, snake_viper_wild Rs +264, random_hold Rs +220, snake_anaconda Rs +182, snake_viper_tick Rs +139, benchmark_smallcap Rs +123, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -474

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.