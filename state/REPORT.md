# Paper trading report

Updated 2026-11-12 12:17 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,441 | +10.72% | 0 | - | 236 |
| benchmark | 220,012 | +10.01% | 0 | - | 237 |
| snake_abs_exit_conv | 219,363 | +9.68% | 2 | 50% | 345 |
| snake_abs_exit | 218,385 | +9.19% | 2 | 50% | 345 |
| snake_abs | 216,257 | +8.13% | 1 | 100% | 255 |
| snake_abs_conv | 216,095 | +8.05% | 1 | 100% | 255 |
| intraweek | 214,924 | +7.46% | 30 | 53% | 3,302 |
| oracle | 213,402 | +6.70% | 0 | - | 233 |
| intramonth | 211,740 | +5.87% | 0 | - | 235 |
| random_hold | 208,010 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 207,513 | +3.76% | 10 | 50% | 1,825 |
| snake_anaconda | 207,026 | +3.51% | 3 | 33% | 374 |
| snake_viper_tick | 203,963 | +1.98% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,161 | +1.58% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,067 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,350 (-3.83%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,903 | +1.42% |
| snake_abs_conv | +2,637 | +1.24% |
| snake_abs | +2,633 | +1.23% |
| benchmark_smallcap | +2,354 | +1.17% |
| snake_abs_exit | +2,223 | +1.03% |
| snake_abs_exit_conv | +2,212 | +1.02% |
| intraweek | +1,791 | +0.84% |
| unified | +1,627 | +0.74% |
| oracle | +1,399 | +0.66% |
| random_hold | +900 | +0.43% |
| snake_viper_wild | +771 | +0.37% |
| snake_viper_tick | +754 | +0.37% |
| benchmark | +750 | +0.34% |
| intramonth | +743 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,518 | -1.86% |

Average per day so far: unified Rs +670, snake_abs_exit_conv Rs +668, snake_abs_exit Rs +634, benchmark Rs +625, snake_abs_conv Rs +555, snake_abs Rs +542, intraweek Rs +466, oracle Rs +419, intramonth Rs +367, snake_viper_wild Rs +313, snake_anaconda Rs +260, random_hold Rs +250, snake_viper_tick Rs +189, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.