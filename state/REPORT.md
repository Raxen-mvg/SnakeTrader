# Paper trading report

Updated 2026-11-17 13:38 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,634 | +10.82% | 0 | - | 237 |
| unified | 221,589 | +10.79% | 0 | - | 236 |
| snake_abs_exit | 214,910 | +7.46% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,277 | +6.64% | 2 | 50% | 345 |
| intraweek | 213,270 | +6.63% | 35 | 54% | 3,851 |
| oracle | 212,230 | +6.12% | 0 | - | 233 |
| intramonth | 211,559 | +5.78% | 0 | - | 235 |
| snake_abs | 210,085 | +5.04% | 1 | 100% | 255 |
| snake_abs_conv | 209,948 | +4.97% | 1 | 100% | 255 |
| snake_viper_wild | 209,258 | +4.63% | 14 | 50% | 2,496 |
| random_hold | 207,382 | +3.69% | 10 | 70% | 733 |
| snake_anaconda | 205,760 | +2.88% | 3 | 33% | 374 |
| snake_viper_tick | 205,682 | +2.84% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,109 | +0.56% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,036 | -9.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,080 (-4.46%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,114 | +1.51% |
| snake_viper_tick | +3,062 | +1.51% |
| intraweek | +2,004 | +0.95% |
| benchmark | +1,553 | +0.71% |
| snake_anaconda | +657 | +0.32% |
| snake_abs_exit | +501 | +0.23% |
| benchmark_smallcap | +280 | +0.14% |
| oracle | +207 | +0.10% |
| unified | +152 | +0.07% |
| gold | +82 | +0.04% |
| snake_abs_exit_conv | +60 | +0.03% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_conv | -42 | -0.02% |
| snake_abs | -49 | -0.02% |
| intramonth | -60 | -0.03% |
| random_hold | -411 | -0.20% |

Average per day so far: benchmark Rs +618, unified Rs +617, snake_abs_exit Rs +466, snake_abs_exit_conv Rs +415, intraweek Rs +379, oracle Rs +349, snake_viper_wild Rs +343, intramonth Rs +330, snake_abs_conv Rs +311, snake_abs Rs +306, snake_viper_tick Rs +237, random_hold Rs +211, snake_anaconda Rs +192, nifty_calls Rs +52, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -542

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.