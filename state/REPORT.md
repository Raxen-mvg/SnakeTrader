# Paper trading report

Updated 2026-11-17 15:22 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,657 | +10.83% | 0 | - | 237 |
| unified | 221,399 | +10.70% | 0 | - | 236 |
| snake_abs_exit | 213,665 | +6.83% | 2 | 50% | 345 |
| intraweek | 213,318 | +6.66% | 35 | 54% | 3,851 |
| oracle | 212,626 | +6.31% | 0 | - | 233 |
| snake_abs_exit_conv | 212,103 | +6.05% | 2 | 50% | 345 |
| intramonth | 211,588 | +5.79% | 0 | - | 235 |
| snake_viper_wild | 209,607 | +4.80% | 14 | 50% | 2,496 |
| snake_abs | 208,882 | +4.44% | 1 | 100% | 255 |
| snake_abs_conv | 208,749 | +4.37% | 1 | 100% | 255 |
| random_hold | 208,501 | +4.25% | 10 | 70% | 733 |
| snake_viper_tick | 206,025 | +3.01% | 13 | 46% | 2,299 |
| snake_anaconda | 204,603 | +2.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,212 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,823 | -9.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,195 (-4.40%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,462 | +1.68% |
| snake_viper_tick | +3,405 | +1.68% |
| intraweek | +2,053 | +0.97% |
| benchmark | +1,576 | +0.72% |
| random_hold | +707 | +0.34% |
| oracle | +603 | +0.28% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intramonth | -31 | -0.01% |
| unified | -38 | -0.02% |
| gold | -132 | -0.07% |
| snake_anaconda | -500 | -0.24% |
| benchmark_smallcap | -617 | -0.31% |
| snake_abs_exit | -745 | -0.35% |
| snake_abs_exit_conv | -1,114 | -0.52% |
| snake_abs_conv | -1,241 | -0.59% |
| snake_abs | -1,252 | -0.60% |

Average per day so far: benchmark Rs +619, unified Rs +611, snake_abs_exit Rs +427, intraweek Rs +381, snake_abs_exit_conv Rs +378, oracle Rs +361, snake_viper_wild Rs +356, intramonth Rs +331, snake_abs_conv Rs +273, snake_abs Rs +269, snake_viper_tick Rs +251, random_hold Rs +243, snake_anaconda Rs +153, nifty_calls Rs +52, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.