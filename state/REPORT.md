# Paper trading report

Updated 2026-11-17 10:38 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,222 | +11.11% | 0 | - | 236 |
| benchmark | 221,527 | +10.76% | 0 | - | 237 |
| snake_abs_exit | 215,413 | +7.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,595 | +6.80% | 2 | 50% | 345 |
| intraweek | 213,504 | +6.75% | 35 | 54% | 3,851 |
| oracle | 212,468 | +6.23% | 0 | - | 233 |
| intramonth | 212,129 | +6.06% | 0 | - | 235 |
| snake_abs | 210,025 | +5.01% | 1 | 100% | 255 |
| snake_abs_conv | 209,877 | +4.94% | 1 | 100% | 255 |
| random_hold | 208,399 | +4.20% | 10 | 70% | 733 |
| snake_viper_wild | 207,179 | +3.59% | 14 | 50% | 2,496 |
| snake_anaconda | 205,562 | +2.78% | 3 | 33% | 374 |
| snake_viper_tick | 203,637 | +1.82% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,028 | +1.01% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,480 | -9.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,511 (-4.24%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,238 | +1.06% |
| benchmark | +1,446 | +0.66% |
| benchmark_smallcap | +1,199 | +0.60% |
| snake_viper_wild | +1,035 | +0.50% |
| snake_viper_tick | +1,017 | +0.50% |
| snake_abs_exit | +1,004 | +0.47% |
| unified | +784 | +0.35% |
| random_hold | +606 | +0.29% |
| gold | +526 | +0.29% |
| intramonth | +510 | +0.24% |
| snake_anaconda | +460 | +0.22% |
| oracle | +445 | +0.21% |
| snake_abs_exit_conv | +378 | +0.18% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -108 | -0.05% |
| snake_abs_conv | -113 | -0.05% |

Average per day so far: unified Rs +635, benchmark Rs +615, snake_abs_exit Rs +482, snake_abs_exit_conv Rs +425, intraweek Rs +386, oracle Rs +356, intramonth Rs +347, snake_abs_conv Rs +309, snake_abs Rs +304, snake_viper_wild Rs +266, random_hold Rs +240, snake_anaconda Rs +185, snake_viper_tick Rs +152, benchmark_smallcap Rs +65, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -529

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.