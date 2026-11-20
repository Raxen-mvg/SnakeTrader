# Paper trading report

Updated 2026-11-20 12:19 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,396 | +13.20% | 0 | - | 236 |
| benchmark | 223,699 | +11.85% | 0 | - | 237 |
| intramonth | 215,356 | +7.68% | 0 | - | 235 |
| intraweek | 214,792 | +7.40% | 35 | 54% | 3,851 |
| oracle | 212,666 | +6.33% | 0 | - | 233 |
| snake_abs_exit | 209,535 | +4.77% | 2 | 50% | 345 |
| random_hold | 208,993 | +4.50% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,566 | +3.78% | 2 | 50% | 345 |
| snake_abs | 206,703 | +3.35% | 1 | 100% | 255 |
| snake_abs_conv | 206,567 | +3.28% | 1 | 100% | 255 |
| snake_viper_wild | 206,279 | +3.14% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,758 | +1.38% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| snake_anaconda | 200,619 | +0.31% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,536 | -16.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,084 (-3.96%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,903 | +0.89% |
| unified | +1,781 | +0.79% |
| intramonth | +1,348 | +0.63% |
| benchmark | +1,323 | +0.59% |
| oracle | +577 | +0.27% |
| random_hold | +540 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -706 | -0.35% |
| snake_viper_tick | -1,219 | -0.60% |
| snake_viper_wild | -1,243 | -0.60% |
| snake_abs | -2,276 | -1.09% |
| snake_abs_conv | -2,293 | -1.10% |
| snake_anaconda | -2,845 | -1.40% |
| snake_abs_exit_conv | -3,499 | -1.66% |
| snake_abs_exit | -3,817 | -1.79% |
| gold | -8,236 | -4.71% |

Average per day so far: unified Rs +695, benchmark Rs +624, intramonth Rs +404, intraweek Rs +389, oracle Rs +333, snake_abs_exit Rs +272, random_hold Rs +237, snake_abs_exit_conv Rs +216, snake_viper_wild Rs +209, snake_abs_conv Rs +188, snake_abs Rs +186, snake_viper_tick Rs +102, nifty_calls Rs +48, benchmark_smallcap Rs +22, snake_anaconda Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.