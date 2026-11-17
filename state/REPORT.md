# Paper trading report

Updated 2026-11-17 13:51 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,833 | +10.92% | 0 | - | 237 |
| unified | 221,609 | +10.80% | 0 | - | 236 |
| snake_abs_exit | 214,824 | +7.41% | 2 | 50% | 345 |
| intraweek | 213,414 | +6.71% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,233 | +6.62% | 2 | 50% | 345 |
| oracle | 212,221 | +6.11% | 0 | - | 233 |
| intramonth | 211,527 | +5.76% | 0 | - | 235 |
| snake_abs | 210,063 | +5.03% | 1 | 100% | 255 |
| snake_abs_conv | 209,924 | +4.96% | 1 | 100% | 255 |
| snake_viper_wild | 209,225 | +4.61% | 14 | 50% | 2,496 |
| random_hold | 207,592 | +3.80% | 10 | 70% | 733 |
| snake_viper_tick | 205,650 | +2.83% | 13 | 46% | 2,299 |
| snake_anaconda | 205,617 | +2.81% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,031 | +0.52% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,823 | -9.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,110 (-4.44%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,081 | +1.50% |
| snake_viper_tick | +3,030 | +1.50% |
| intraweek | +2,148 | +1.02% |
| benchmark | +1,752 | +0.80% |
| snake_anaconda | +514 | +0.25% |
| snake_abs_exit | +414 | +0.19% |
| benchmark_smallcap | +202 | +0.10% |
| oracle | +198 | +0.09% |
| unified | +171 | +0.08% |
| snake_abs_exit_conv | +15 | +0.01% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_conv | -65 | -0.03% |
| snake_abs | -70 | -0.03% |
| intramonth | -92 | -0.04% |
| gold | -132 | -0.07% |
| random_hold | -202 | -0.10% |

Average per day so far: benchmark Rs +624, unified Rs +617, snake_abs_exit Rs +463, snake_abs_exit_conv Rs +414, intraweek Rs +383, oracle Rs +349, snake_viper_wild Rs +342, intramonth Rs +329, snake_abs_conv Rs +310, snake_abs Rs +305, snake_viper_tick Rs +235, random_hold Rs +217, snake_anaconda Rs +187, nifty_calls Rs +52, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.