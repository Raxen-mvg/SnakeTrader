# Paper trading report

Updated 2026-11-12 13:17 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,431 | +10.71% | 0 | - | 236 |
| benchmark | 220,050 | +10.03% | 0 | - | 237 |
| snake_abs_exit_conv | 218,627 | +9.31% | 2 | 50% | 345 |
| snake_abs_exit | 217,636 | +8.82% | 2 | 50% | 345 |
| snake_abs | 215,645 | +7.82% | 1 | 100% | 255 |
| snake_abs_conv | 215,473 | +7.74% | 1 | 100% | 255 |
| intraweek | 214,383 | +7.19% | 30 | 53% | 3,302 |
| oracle | 213,362 | +6.68% | 0 | - | 233 |
| intramonth | 212,021 | +6.01% | 0 | - | 235 |
| random_hold | 208,057 | +4.03% | 10 | 70% | 733 |
| snake_viper_wild | 207,343 | +3.67% | 10 | 50% | 1,825 |
| snake_anaconda | 206,408 | +3.20% | 3 | 33% | 374 |
| snake_viper_tick | 203,796 | +1.90% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,172 | +1.59% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,919 | -7.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,169 (-3.92%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,365 | +1.18% |
| snake_anaconda | +2,285 | +1.12% |
| snake_abs | +2,021 | +0.95% |
| snake_abs_conv | +2,015 | +0.94% |
| unified | +1,617 | +0.74% |
| snake_abs_exit_conv | +1,476 | +0.68% |
| snake_abs_exit | +1,474 | +0.68% |
| oracle | +1,359 | +0.64% |
| intraweek | +1,250 | +0.59% |
| intramonth | +1,025 | +0.49% |
| random_hold | +946 | +0.46% |
| benchmark | +788 | +0.36% |
| snake_viper_wild | +601 | +0.29% |
| snake_viper_tick | +587 | +0.29% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,666 | -1.93% |

Average per day so far: unified Rs +670, snake_abs_exit_conv Rs +642, benchmark Rs +627, snake_abs_exit Rs +608, snake_abs_conv Rs +534, snake_abs Rs +522, intraweek Rs +449, oracle Rs +418, intramonth Rs +376, snake_viper_wild Rs +306, random_hold Rs +252, snake_anaconda Rs +237, snake_viper_tick Rs +181, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -440

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.