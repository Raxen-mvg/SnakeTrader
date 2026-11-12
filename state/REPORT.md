# Paper trading report

Updated 2026-11-12 09:31 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,508 | +11.25% | 0 | - | 236 |
| benchmark | 220,831 | +10.41% | 0 | - | 237 |
| snake_abs_exit_conv | 220,590 | +10.29% | 2 | 50% | 345 |
| snake_abs_exit | 220,032 | +10.02% | 2 | 50% | 345 |
| snake_abs | 217,000 | +8.50% | 1 | 100% | 255 |
| snake_abs_conv | 216,838 | +8.42% | 1 | 100% | 255 |
| intraweek | 215,857 | +7.93% | 30 | 53% | 3,302 |
| oracle | 213,431 | +6.72% | 0 | - | 233 |
| intramonth | 212,955 | +6.48% | 0 | - | 235 |
| snake_viper_wild | 212,148 | +6.07% | 10 | 50% | 1,825 |
| snake_viper_tick | 208,504 | +4.25% | 9 | 44% | 1,639 |
| random_hold | 208,192 | +4.10% | 10 | 70% | 733 |
| snake_anaconda | 207,802 | +3.90% | 3 | 33% | 374 |
| benchmark_smallcap | 203,430 | +1.72% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,643 | -6.68% | 0 | - | 237 |

Combined allocator (virtual): Rs 193,127 (-3.44%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +5,406 | +2.62% |
| snake_viper_tick | +5,296 | +2.61% |
| snake_abs_exit | +3,870 | +1.79% |
| snake_anaconda | +3,679 | +1.80% |
| snake_abs_exit_conv | +3,438 | +1.58% |
| snake_abs_conv | +3,380 | +1.58% |
| snake_abs | +3,375 | +1.58% |
| intraweek | +2,724 | +1.28% |
| unified | +2,694 | +1.23% |
| benchmark_smallcap | +2,623 | +1.31% |
| intramonth | +1,959 | +0.93% |
| benchmark | +1,568 | +0.71% |
| oracle | +1,429 | +0.67% |
| random_hold | +1,081 | +0.52% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,943 | -1.55% |

Average per day so far: snake_abs_exit_conv Rs +710, unified Rs +703, snake_abs_exit Rs +691, benchmark Rs +651, snake_abs_conv Rs +581, snake_abs Rs +567, snake_viper_wild Rs +506, intraweek Rs +496, oracle Rs +420, snake_viper_tick Rs +405, intramonth Rs +405, snake_anaconda Rs +289, random_hold Rs +256, benchmark_smallcap Rs +122, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -417

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.