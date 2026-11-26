# Paper trading report

Updated 2026-11-26 13:34 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,306 | +12.65% | 0 | - | 237 |
| unified | 223,179 | +11.59% | 0 | - | 236 |
| oracle | 213,095 | +6.55% | 0 | - | 233 |
| intramonth | 210,562 | +5.28% | 0 | - | 235 |
| random_hold | 209,200 | +4.60% | 13 | 69% | 1,037 |
| intraweek | 207,852 | +3.93% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,212 | +0.11% | 0 | - | 237 |
| snake_abs_exit | 200,101 | +0.05% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,505 | -0.25% | 2 | 50% | 345 |
| snake_abs | 197,874 | -1.06% | 1 | 100% | 255 |
| snake_abs_conv | 197,669 | -1.17% | 1 | 100% | 255 |
| snake_viper_wild | 192,201 | -3.90% | 16 | 50% | 2,827 |
| snake_anaconda | 191,555 | -4.22% | 3 | 33% | 374 |
| snake_viper_tick | 188,936 | -5.53% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,208 | -16.90% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,545 (-5.73%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,611 | +0.98% |
| benchmark_smallcap | +1,401 | +0.70% |
| intraweek | +1,109 | +0.54% |
| benchmark | +283 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -292 | -0.14% |
| oracle | -701 | -0.33% |
| unified | -921 | -0.41% |
| intramonth | -1,131 | -0.53% |
| snake_abs_exit | -2,155 | -1.06% |
| snake_abs | -2,276 | -1.14% |
| snake_abs_conv | -2,304 | -1.15% |
| snake_abs_exit_conv | -2,471 | -1.22% |
| snake_anaconda | -2,998 | -1.54% |
| snake_viper_tick | -5,240 | -2.70% |
| snake_viper_wild | -5,343 | -2.70% |

Average per day so far: benchmark Rs +617, unified Rs +565, oracle Rs +319, intramonth Rs +258, random_hold Rs +224, intraweek Rs +192, nifty_calls Rs +45, benchmark_smallcap Rs +6, snake_abs_exit Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -13, snake_abs Rs -55, snake_abs_conv Rs -61, snake_anaconda Rs -235, snake_viper_wild Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -369, gold Rs -824

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.