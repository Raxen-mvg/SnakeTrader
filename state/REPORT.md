# Paper trading report

Updated 2026-11-05 10:14 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,950 | +9.47% | 0 | - | 236 |
| snake_abs_exit_conv | 215,719 | +7.86% | 1 | 100% | 255 |
| snake_abs_exit | 215,463 | +7.73% | 1 | 100% | 260 |
| snake_abs | 212,594 | +6.30% | 1 | 100% | 255 |
| snake_abs_conv | 212,442 | +6.22% | 1 | 100% | 255 |
| benchmark | 212,339 | +6.17% | 0 | - | 237 |
| intramonth | 210,778 | +5.39% | 0 | - | 235 |
| intraweek | 210,736 | +5.37% | 25 | 48% | 2,757 |
| random_hold | 206,915 | +3.46% | 8 | 62% | 649 |
| snake_viper_wild | 205,962 | +2.98% | 3 | 33% | 702 |
| oracle | 204,596 | +2.30% | 0 | - | 233 |
| snake_anaconda | 202,751 | +1.38% | 3 | 33% | 374 |
| snake_viper_tick | 202,435 | +1.22% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,585 | -0.21% | 0 | - | 237 |
| gold | 195,241 | -2.38% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,657 (-4.67%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,511 | +2.10% |
| gold | +3,847 | +2.01% |
| intramonth | +3,762 | +1.82% |
| random_hold | +3,606 | +1.77% |
| benchmark | +3,580 | +1.72% |
| benchmark_smallcap | +2,915 | +1.48% |
| oracle | +2,804 | +1.39% |
| intraweek | +1,038 | +0.49% |
| snake_abs_exit_conv | +704 | +0.33% |
| snake_abs | +691 | +0.33% |
| snake_abs_conv | +684 | +0.32% |
| snake_abs_exit | +563 | +0.26% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -1,069 | -0.52% |
| snake_viper_tick | -2,965 | -1.44% |
| snake_viper_wild | -3,068 | -1.47% |

Average per day so far: unified Rs +677, snake_abs_exit_conv Rs +629, snake_abs_exit Rs +619, snake_abs_conv Rs +498, snake_abs Rs +484, benchmark Rs +441, intramonth Rs +385, intraweek Rs +383, snake_viper_wild Rs +298, random_hold Rs +247, oracle Rs +164, snake_viper_tick Rs +143, snake_anaconda Rs +120, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -17, gold Rs -170, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.