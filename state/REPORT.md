# Paper trading report

Updated 2026-11-05 12:01 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,088 | +9.04% | 0 | - | 236 |
| snake_abs_exit_conv | 213,891 | +6.95% | 1 | 100% | 255 |
| snake_abs_exit | 213,583 | +6.79% | 1 | 100% | 260 |
| benchmark | 212,699 | +6.35% | 0 | - | 237 |
| intraweek | 210,837 | +5.42% | 25 | 48% | 2,757 |
| snake_abs | 210,777 | +5.39% | 1 | 100% | 255 |
| snake_abs_conv | 210,641 | +5.32% | 1 | 100% | 255 |
| intramonth | 209,952 | +4.98% | 0 | - | 235 |
| snake_viper_wild | 206,801 | +3.40% | 3 | 33% | 702 |
| random_hold | 206,733 | +3.37% | 8 | 62% | 649 |
| oracle | 204,232 | +2.12% | 0 | - | 233 |
| snake_viper_tick | 203,244 | +1.62% | 2 | 0% | 532 |
| snake_anaconda | 202,076 | +1.04% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| gold | 194,402 | -2.80% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,090 (-4.95%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,940 | +1.89% |
| unified | +3,648 | +1.70% |
| random_hold | +3,424 | +1.68% |
| gold | +3,009 | +1.57% |
| intramonth | +2,936 | +1.42% |
| benchmark_smallcap | +2,545 | +1.29% |
| oracle | +2,440 | +1.21% |
| intraweek | +1,139 | +0.54% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,117 | -0.53% |
| snake_abs_exit_conv | -1,124 | -0.52% |
| snake_abs | -1,126 | -0.53% |
| snake_abs_exit | -1,318 | -0.61% |
| snake_anaconda | -1,744 | -0.86% |
| snake_viper_tick | -2,156 | -1.05% |
| snake_viper_wild | -2,229 | -1.07% |

Average per day so far: unified Rs +646, snake_abs_exit_conv Rs +556, snake_abs_exit Rs +543, benchmark Rs +454, snake_abs_conv Rs +426, snake_abs Rs +415, intraweek Rs +387, intramonth Rs +355, snake_viper_wild Rs +340, random_hold Rs +240, snake_viper_tick Rs +191, oracle Rs +151, snake_anaconda Rs +90, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -33, gold Rs -200, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.