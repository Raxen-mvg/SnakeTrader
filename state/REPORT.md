# Paper trading report

Updated 2026-11-17 11:20 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,230 | +11.12% | 0 | - | 236 |
| benchmark | 221,925 | +10.96% | 0 | - | 237 |
| snake_abs_exit | 215,636 | +7.82% | 2 | 50% | 345 |
| intraweek | 214,243 | +7.12% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,544 | +6.77% | 2 | 50% | 345 |
| oracle | 212,801 | +6.40% | 0 | - | 233 |
| intramonth | 212,225 | +6.11% | 0 | - | 235 |
| snake_abs | 210,015 | +5.01% | 1 | 100% | 255 |
| snake_abs_conv | 209,865 | +4.93% | 1 | 100% | 255 |
| random_hold | 208,134 | +4.07% | 10 | 70% | 733 |
| snake_viper_wild | 207,730 | +3.87% | 14 | 50% | 2,496 |
| snake_anaconda | 205,467 | +2.73% | 3 | 33% | 374 |
| snake_viper_tick | 204,179 | +2.09% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,387 | +1.19% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,694 | -9.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,707 (-4.15%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,977 | +1.41% |
| benchmark | +1,844 | +0.84% |
| snake_viper_wild | +1,586 | +0.77% |
| snake_viper_tick | +1,559 | +0.77% |
| benchmark_smallcap | +1,558 | +0.78% |
| snake_abs_exit | +1,226 | +0.57% |
| unified | +792 | +0.36% |
| oracle | +778 | +0.37% |
| gold | +740 | +0.41% |
| intramonth | +606 | +0.29% |
| snake_anaconda | +364 | +0.18% |
| random_hold | +341 | +0.16% |
| snake_abs_exit_conv | +327 | +0.15% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -118 | -0.06% |
| snake_abs_conv | -125 | -0.06% |

Average per day so far: unified Rs +635, benchmark Rs +626, snake_abs_exit Rs +489, snake_abs_exit_conv Rs +423, intraweek Rs +407, oracle Rs +366, intramonth Rs +349, snake_abs_conv Rs +308, snake_abs Rs +303, snake_viper_wild Rs +286, random_hold Rs +232, snake_anaconda Rs +182, snake_viper_tick Rs +174, benchmark_smallcap Rs +77, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -523

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.