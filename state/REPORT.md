# Paper trading report

Updated 2026-11-17 11:30 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,952 | +10.98% | 0 | - | 236 |
| benchmark | 221,879 | +10.94% | 0 | - | 237 |
| snake_abs_exit | 215,716 | +7.86% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,742 | +6.87% | 2 | 50% | 345 |
| intraweek | 213,641 | +6.82% | 35 | 54% | 3,851 |
| oracle | 212,244 | +6.12% | 0 | - | 233 |
| intramonth | 211,943 | +5.97% | 0 | - | 235 |
| snake_abs | 210,232 | +5.12% | 1 | 100% | 255 |
| snake_abs_conv | 210,083 | +5.04% | 1 | 100% | 255 |
| random_hold | 207,876 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,620 | +3.81% | 14 | 50% | 2,496 |
| snake_anaconda | 205,719 | +2.86% | 3 | 33% | 374 |
| snake_viper_tick | 204,070 | +2.04% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,141 | +1.07% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,530 | -9.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,352 (-4.32%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,375 | +1.12% |
| benchmark | +1,798 | +0.82% |
| snake_viper_wild | +1,476 | +0.72% |
| snake_viper_tick | +1,451 | +0.72% |
| benchmark_smallcap | +1,312 | +0.65% |
| snake_abs_exit | +1,307 | +0.61% |
| snake_anaconda | +616 | +0.30% |
| gold | +575 | +0.32% |
| snake_abs_exit_conv | +525 | +0.25% |
| unified | +514 | +0.23% |
| intramonth | +324 | +0.15% |
| oracle | +221 | +0.10% |
| snake_abs | +98 | +0.05% |
| snake_abs_conv | +94 | +0.04% |
| random_hold | +83 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +627, benchmark Rs +625, snake_abs_exit Rs +491, snake_abs_exit_conv Rs +429, intraweek Rs +390, oracle Rs +350, intramonth Rs +341, snake_abs_conv Rs +315, snake_abs Rs +310, snake_viper_wild Rs +282, random_hold Rs +225, snake_anaconda Rs +191, snake_viper_tick Rs +170, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -528

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.