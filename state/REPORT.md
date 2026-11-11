# Paper trading report

Updated 2026-11-11 12:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,647 | +10.32% | 0 | - | 237 |
| unified | 220,554 | +10.28% | 0 | - | 236 |
| snake_abs_exit_conv | 217,490 | +8.74% | 2 | 50% | 345 |
| snake_abs_exit | 216,326 | +8.16% | 2 | 50% | 345 |
| snake_abs | 213,979 | +6.99% | 1 | 100% | 255 |
| snake_abs_conv | 213,825 | +6.91% | 1 | 100% | 255 |
| intraweek | 213,647 | +6.82% | 30 | 53% | 3,302 |
| oracle | 211,971 | +5.99% | 0 | - | 233 |
| intramonth | 211,453 | +5.73% | 0 | - | 235 |
| random_hold | 206,942 | +3.47% | 9 | 67% | 709 |
| snake_anaconda | 204,283 | +2.14% | 3 | 33% | 374 |
| snake_viper_wild | 204,099 | +2.05% | 10 | 50% | 1,825 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,300 | +0.65% | 0 | - | 237 |
| snake_viper_tick | 200,621 | +0.31% | 9 | 44% | 1,639 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,144 | -4.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,334 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +6,669 | +3.38% |
| snake_viper_tick | +6,544 | +3.37% |
| snake_abs_exit_conv | +5,581 | +2.63% |
| snake_anaconda | +4,817 | +2.42% |
| snake_abs_conv | +4,347 | +2.08% |
| snake_abs_exit | +4,342 | +2.05% |
| snake_abs | +4,333 | +2.07% |
| benchmark_smallcap | +3,128 | +1.58% |
| benchmark | +2,555 | +1.17% |
| oracle | +2,053 | +0.98% |
| random_hold | +1,982 | +0.97% |
| intramonth | +844 | +0.40% |
| unified | +807 | +0.37% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -895 | -0.42% |
| gold | -1,989 | -1.03% |

Average per day so far: benchmark Rs +666, unified Rs +663, snake_abs_exit_conv Rs +625, snake_abs_exit Rs +583, snake_abs_conv Rs +494, snake_abs Rs +482, intraweek Rs +440, oracle Rs +386, intramonth Rs +369, random_hold Rs +224, snake_viper_wild Rs +178, snake_anaconda Rs +165, nifty_calls Rs +59, benchmark_smallcap Rs +48, snake_viper_tick Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -318, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.