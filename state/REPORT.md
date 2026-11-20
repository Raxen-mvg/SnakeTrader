# Paper trading report

Updated 2026-11-20 13:38 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,445 | +13.22% | 0 | - | 236 |
| benchmark | 224,227 | +12.11% | 0 | - | 237 |
| intraweek | 215,344 | +7.67% | 35 | 54% | 3,851 |
| intramonth | 215,334 | +7.67% | 0 | - | 235 |
| oracle | 212,627 | +6.31% | 0 | - | 233 |
| random_hold | 209,575 | +4.79% | 11 | 73% | 979 |
| snake_abs_exit | 209,354 | +4.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,333 | +3.67% | 2 | 50% | 345 |
| snake_abs | 206,521 | +3.26% | 1 | 100% | 255 |
| snake_abs_conv | 206,392 | +3.20% | 1 | 100% | 255 |
| snake_viper_wild | 204,026 | +2.01% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,188 | +0.59% | 0 | - | 237 |
| snake_anaconda | 200,637 | +0.32% | 3 | 33% | 374 |
| snake_viper_tick | 200,545 | +0.27% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,506 | -16.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,114 (-3.94%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,455 | +1.15% |
| benchmark | +1,851 | +0.83% |
| unified | +1,830 | +0.81% |
| intramonth | +1,326 | +0.62% |
| random_hold | +1,122 | +0.54% |
| oracle | +538 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -280 | -0.14% |
| snake_abs | -2,458 | -1.18% |
| snake_abs_conv | -2,468 | -1.18% |
| snake_anaconda | -2,826 | -1.39% |
| snake_viper_tick | -3,432 | -1.68% |
| snake_viper_wild | -3,497 | -1.69% |
| snake_abs_exit_conv | -3,732 | -1.77% |
| snake_abs_exit | -3,997 | -1.87% |
| gold | -7,266 | -4.16% |

Average per day so far: unified Rs +696, benchmark Rs +638, intraweek Rs +404, intramonth Rs +404, oracle Rs +332, snake_abs_exit Rs +267, random_hold Rs +252, snake_abs_exit_conv Rs +210, snake_abs_conv Rs +183, snake_abs Rs +181, snake_viper_wild Rs +134, nifty_calls Rs +48, benchmark_smallcap Rs +35, snake_viper_tick Rs +20, snake_anaconda Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -855

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.