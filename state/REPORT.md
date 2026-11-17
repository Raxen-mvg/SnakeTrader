# Paper trading report

Updated 2026-11-17 15:30 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| unified | 221,439 | +10.72% | 0 | - | 236 |
| intraweek | 213,323 | +6.66% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,142 | +6.57% | 2 | 50% | 345 |
| oracle | 212,486 | +6.24% | 0 | - | 233 |
| snake_abs_exit_conv | 211,574 | +5.79% | 2 | 50% | 345 |
| intramonth | 211,542 | +5.77% | 0 | - | 235 |
| snake_viper_wild | 209,415 | +4.71% | 14 | 50% | 2,496 |
| snake_abs | 208,559 | +4.28% | 1 | 100% | 255 |
| random_hold | 208,432 | +4.22% | 10 | 70% | 733 |
| snake_abs_conv | 208,420 | +4.21% | 1 | 100% | 255 |
| snake_viper_tick | 205,837 | +2.92% | 13 | 46% | 2,299 |
| snake_anaconda | 204,055 | +2.03% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,724 | -9.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,161 (-4.42%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,271 | +1.59% |
| snake_viper_tick | +3,217 | +1.59% |
| intraweek | +2,057 | +0.97% |
| benchmark | +1,522 | +0.69% |
| random_hold | +639 | +0.31% |
| oracle | +463 | +0.22% |
| unified | +1 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -77 | -0.04% |
| gold | -230 | -0.13% |
| benchmark_smallcap | -258 | -0.13% |
| snake_anaconda | -1,048 | -0.51% |
| snake_abs_exit | -1,268 | -0.59% |
| snake_abs_conv | -1,570 | -0.75% |
| snake_abs | -1,575 | -0.75% |
| snake_abs_exit_conv | -1,644 | -0.77% |

Average per day so far: benchmark Rs +617, unified Rs +613, snake_abs_exit Rs +411, intraweek Rs +381, snake_abs_exit_conv Rs +362, oracle Rs +357, snake_viper_wild Rs +349, intramonth Rs +330, snake_abs_conv Rs +263, snake_abs Rs +259, snake_viper_tick Rs +243, random_hold Rs +241, snake_anaconda Rs +135, nifty_calls Rs +52, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -551

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.