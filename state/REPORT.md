# Paper trading report

Updated 2026-11-19 09:17 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,145 | +11.57% | 0 | - | 236 |
| benchmark | 220,150 | +10.07% | 0 | - | 237 |
| intramonth | 212,805 | +6.40% | 0 | - | 235 |
| snake_abs_exit | 212,481 | +6.24% | 2 | 50% | 345 |
| intraweek | 211,893 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,193 | +5.60% | 0 | - | 233 |
| snake_abs_exit_conv | 210,815 | +5.41% | 2 | 50% | 345 |
| snake_abs | 207,964 | +3.98% | 1 | 100% | 255 |
| snake_abs_conv | 207,828 | +3.91% | 1 | 100% | 255 |
| random_hold | 207,151 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 207,083 | +3.54% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,546 | +1.77% | 15 | 47% | 2,625 |
| snake_anaconda | 202,910 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,215 | -0.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,214 | -12.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,913 (-4.54%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +533 | +0.24% |
| intramonth | +532 | +0.25% |
| oracle | +397 | +0.19% |
| random_hold | +218 | +0.10% |
| intraweek | +53 | +0.03% |
| snake_viper_wild | +43 | +0.02% |
| snake_viper_tick | +42 | +0.02% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -112 | -0.06% |
| benchmark | -145 | -0.07% |
| snake_abs | -1,472 | -0.70% |
| snake_anaconda | -1,491 | -0.73% |
| snake_abs_conv | -1,497 | -0.71% |
| snake_abs_exit | -1,550 | -0.72% |
| snake_abs_exit_conv | -1,568 | -0.74% |
| gold | -3,107 | -1.75% |

Average per day so far: unified Rs +626, benchmark Rs +545, snake_abs_exit Rs +367, intramonth Rs +346, intraweek Rs +321, snake_abs_exit_conv Rs +318, oracle Rs +303, snake_viper_wild Rs +244, snake_abs_conv Rs +230, snake_abs Rs +228, random_hold Rs +193, snake_viper_tick Rs +136, snake_anaconda Rs +91, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -24, snake_nonews Rs -317, snake Rs -337, gold Rs -697

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.