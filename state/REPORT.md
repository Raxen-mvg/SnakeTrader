# Paper trading report

Updated 2026-11-17 13:55 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,963 | +10.98% | 0 | - | 237 |
| unified | 221,687 | +10.84% | 0 | - | 236 |
| snake_abs_exit | 215,219 | +7.61% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,657 | +6.83% | 2 | 50% | 345 |
| intraweek | 213,402 | +6.70% | 35 | 54% | 3,851 |
| oracle | 212,361 | +6.18% | 0 | - | 233 |
| intramonth | 211,610 | +5.80% | 0 | - | 235 |
| snake_viper_wild | 210,714 | +5.36% | 14 | 50% | 2,496 |
| snake_abs | 210,480 | +5.24% | 1 | 100% | 255 |
| snake_abs_conv | 210,357 | +5.18% | 1 | 100% | 255 |
| random_hold | 207,657 | +3.83% | 10 | 70% | 733 |
| snake_viper_tick | 207,115 | +3.56% | 13 | 46% | 2,299 |
| snake_anaconda | 206,109 | +3.06% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,020 | +0.51% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,856 | -9.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,183 (-4.41%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +4,570 | +2.22% |
| snake_viper_tick | +4,495 | +2.22% |
| intraweek | +2,136 | +1.01% |
| benchmark | +1,882 | +0.85% |
| snake_anaconda | +1,006 | +0.49% |
| snake_abs_exit | +809 | +0.38% |
| snake_abs_exit_conv | +440 | +0.21% |
| snake_abs_conv | +367 | +0.17% |
| snake_abs | +347 | +0.17% |
| oracle | +338 | +0.16% |
| unified | +249 | +0.11% |
| benchmark_smallcap | +191 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -9 | -0.00% |
| gold | -99 | -0.06% |
| random_hold | -136 | -0.07% |

Average per day so far: benchmark Rs +628, unified Rs +620, snake_abs_exit Rs +476, snake_abs_exit_conv Rs +427, snake_viper_wild Rs +397, intraweek Rs +383, oracle Rs +353, intramonth Rs +332, snake_abs_conv Rs +324, snake_abs Rs +318, snake_viper_tick Rs +296, random_hold Rs +219, snake_anaconda Rs +204, nifty_calls Rs +52, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -547

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.