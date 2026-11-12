# Paper trading report

Updated 2026-11-12 12:00 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,747 | +10.87% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 219,121 | +9.56% | 2 | 50% | 345 |
| snake_abs_exit | 218,174 | +9.09% | 2 | 50% | 345 |
| snake_abs | 216,116 | +8.06% | 1 | 100% | 255 |
| snake_abs_conv | 215,945 | +7.97% | 1 | 100% | 255 |
| intraweek | 215,163 | +7.58% | 30 | 53% | 3,302 |
| oracle | 213,362 | +6.68% | 0 | - | 233 |
| intramonth | 212,061 | +6.03% | 0 | - | 235 |
| random_hold | 208,083 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,774 | +3.89% | 10 | 50% | 1,825 |
| snake_anaconda | 206,662 | +3.33% | 3 | 33% | 374 |
| snake_viper_tick | 204,218 | +2.11% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,295 | +1.65% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,314 | -6.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,455 (-3.77%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,539 | +1.24% |
| snake_abs | +2,491 | +1.17% |
| benchmark_smallcap | +2,489 | +1.24% |
| snake_abs_conv | +2,487 | +1.17% |
| intraweek | +2,030 | +0.95% |
| snake_abs_exit | +2,012 | +0.93% |
| snake_abs_exit_conv | +1,970 | +0.91% |
| unified | +1,933 | +0.88% |
| oracle | +1,359 | +0.64% |
| benchmark | +1,117 | +0.51% |
| intramonth | +1,065 | +0.51% |
| snake_viper_wild | +1,032 | +0.50% |
| snake_viper_tick | +1,010 | +0.50% |
| random_hold | +972 | +0.47% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,272 | -1.73% |

Average per day so far: unified Rs +680, snake_abs_exit_conv Rs +659, benchmark Rs +637, snake_abs_exit Rs +627, snake_abs_conv Rs +550, snake_abs Rs +537, intraweek Rs +474, oracle Rs +418, intramonth Rs +377, snake_viper_wild Rs +324, random_hold Rs +253, snake_anaconda Rs +247, snake_viper_tick Rs +201, benchmark_smallcap Rs +118, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -428

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.