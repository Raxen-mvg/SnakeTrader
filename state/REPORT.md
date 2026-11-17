# Paper trading report

Updated 2026-11-17 14:47 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,817 | +10.91% | 0 | - | 237 |
| unified | 221,091 | +10.55% | 0 | - | 236 |
| intraweek | 213,934 | +6.97% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,422 | +6.71% | 2 | 50% | 345 |
| oracle | 212,383 | +6.19% | 0 | - | 233 |
| snake_abs_exit_conv | 211,889 | +5.94% | 2 | 50% | 345 |
| intramonth | 211,050 | +5.53% | 0 | - | 235 |
| snake_viper_wild | 209,778 | +4.89% | 14 | 50% | 2,496 |
| snake_abs | 208,688 | +4.34% | 1 | 100% | 255 |
| snake_abs_conv | 208,553 | +4.28% | 1 | 100% | 255 |
| random_hold | 207,936 | +3.97% | 10 | 70% | 733 |
| snake_viper_tick | 206,193 | +3.10% | 13 | 46% | 2,299 |
| snake_anaconda | 204,108 | +2.05% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,154 | +0.58% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,625 | -9.69% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,041 (-4.48%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,633 | +1.76% |
| snake_viper_tick | +3,573 | +1.76% |
| intraweek | +2,668 | +1.26% |
| benchmark | +1,737 | +0.79% |
| oracle | +360 | +0.17% |
| benchmark_smallcap | +325 | +0.16% |
| random_hold | +143 | +0.07% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| gold | -329 | -0.18% |
| unified | -346 | -0.16% |
| intramonth | -569 | -0.27% |
| snake_abs_exit | -988 | -0.46% |
| snake_anaconda | -995 | -0.48% |
| snake_abs_exit_conv | -1,329 | -0.62% |
| snake_abs_conv | -1,437 | -0.68% |
| snake_abs | -1,446 | -0.69% |

Average per day so far: benchmark Rs +623, unified Rs +603, snake_abs_exit Rs +419, intraweek Rs +398, snake_abs_exit_conv Rs +372, snake_viper_wild Rs +362, oracle Rs +354, intramonth Rs +316, snake_abs_conv Rs +267, snake_abs Rs +263, snake_viper_tick Rs +258, random_hold Rs +227, snake_anaconda Rs +137, nifty_calls Rs +52, benchmark_smallcap Rs +37, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -554

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.