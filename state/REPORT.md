# Paper trading report

Updated 2026-11-12 12:03 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,718 | +10.86% | 0 | - | 236 |
| benchmark | 220,402 | +10.20% | 0 | - | 237 |
| snake_abs_exit_conv | 219,284 | +9.64% | 2 | 50% | 345 |
| snake_abs_exit | 218,293 | +9.15% | 2 | 50% | 345 |
| snake_abs | 216,308 | +8.15% | 1 | 100% | 255 |
| snake_abs_conv | 216,137 | +8.07% | 1 | 100% | 255 |
| intraweek | 215,116 | +7.56% | 30 | 53% | 3,302 |
| oracle | 213,374 | +6.69% | 0 | - | 233 |
| intramonth | 212,025 | +6.01% | 0 | - | 235 |
| random_hold | 208,087 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,971 | +3.98% | 10 | 50% | 1,825 |
| snake_anaconda | 206,860 | +3.43% | 3 | 33% | 374 |
| snake_viper_tick | 204,411 | +2.21% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,239 | +1.62% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,116 | -6.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,471 (-3.76%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,737 | +1.34% |
| snake_abs | +2,683 | +1.26% |
| snake_abs_conv | +2,679 | +1.25% |
| benchmark_smallcap | +2,433 | +1.21% |
| snake_abs_exit_conv | +2,133 | +0.98% |
| snake_abs_exit | +2,131 | +0.99% |
| intraweek | +1,983 | +0.93% |
| unified | +1,904 | +0.87% |
| oracle | +1,371 | +0.65% |
| snake_viper_wild | +1,229 | +0.59% |
| snake_viper_tick | +1,202 | +0.59% |
| benchmark | +1,140 | +0.52% |
| intramonth | +1,028 | +0.49% |
| random_hold | +976 | +0.47% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,469 | -1.83% |

Average per day so far: unified Rs +679, snake_abs_exit_conv Rs +665, benchmark Rs +638, snake_abs_exit Rs +631, snake_abs_conv Rs +556, snake_abs Rs +544, intraweek Rs +472, oracle Rs +418, intramonth Rs +376, snake_viper_wild Rs +332, snake_anaconda Rs +254, random_hold Rs +253, snake_viper_tick Rs +210, benchmark_smallcap Rs +116, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.