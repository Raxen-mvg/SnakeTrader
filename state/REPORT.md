# Paper trading report

Updated 2026-11-13 11:37 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,485 | +10.24% | 0 | - | 236 |
| benchmark | 219,446 | +9.72% | 0 | - | 237 |
| snake_abs_exit | 216,577 | +8.29% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,512 | +8.26% | 2 | 50% | 345 |
| intraweek | 216,049 | +8.03% | 30 | 53% | 3,302 |
| oracle | 213,468 | +6.73% | 0 | - | 233 |
| snake_abs | 212,742 | +6.37% | 1 | 100% | 255 |
| snake_abs_conv | 212,571 | +6.29% | 1 | 100% | 255 |
| intramonth | 211,208 | +5.60% | 0 | - | 235 |
| random_hold | 207,228 | +3.61% | 10 | 70% | 733 |
| snake_viper_wild | 205,889 | +2.94% | 14 | 50% | 2,496 |
| snake_anaconda | 204,796 | +2.40% | 3 | 33% | 374 |
| benchmark_smallcap | 203,306 | +1.65% | 0 | - | 237 |
| snake_viper_tick | 202,367 | +1.18% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,749 | -8.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,022 (-3.99%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,391 | +0.65% |
| snake_viper_wild | +596 | +0.29% |
| snake_viper_tick | +586 | +0.29% |
| oracle | +353 | +0.17% |
| benchmark_smallcap | +101 | +0.05% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -211 | -0.10% |
| intramonth | -385 | -0.18% |
| random_hold | -826 | -0.40% |
| snake_abs_exit | -866 | -0.40% |
| benchmark | -1,102 | -0.50% |
| snake_anaconda | -1,131 | -0.55% |
| gold | -1,562 | -0.84% |
| snake_abs_exit_conv | -2,162 | -0.99% |
| snake_abs_conv | -2,964 | -1.38% |
| snake_abs | -2,970 | -1.38% |

Average per day so far: unified Rs +621, benchmark Rs +589, snake_abs_exit Rs +553, snake_abs_exit_conv Rs +550, intraweek Rs +486, snake_abs_conv Rs +419, snake_abs Rs +411, oracle Rs +408, intramonth Rs +340, snake_viper_wild Rs +236, random_hold Rs +219, snake_anaconda Rs +171, benchmark_smallcap Rs +114, snake_viper_tick Rs +108, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -492

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.