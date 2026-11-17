# Paper trading report

Updated 2026-11-17 14:54 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,772 | +10.89% | 0 | - | 237 |
| unified | 221,491 | +10.75% | 0 | - | 236 |
| intraweek | 214,204 | +7.10% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,631 | +6.82% | 2 | 50% | 345 |
| oracle | 212,670 | +6.33% | 0 | - | 233 |
| snake_abs_exit_conv | 212,078 | +6.04% | 2 | 50% | 345 |
| intramonth | 211,429 | +5.71% | 0 | - | 235 |
| snake_viper_wild | 209,339 | +4.67% | 14 | 50% | 2,496 |
| snake_abs | 208,883 | +4.44% | 1 | 100% | 255 |
| snake_abs_conv | 208,743 | +4.37% | 1 | 100% | 255 |
| random_hold | 208,320 | +4.16% | 10 | 70% | 733 |
| snake_viper_tick | 205,761 | +2.88% | 13 | 46% | 2,299 |
| snake_anaconda | 204,436 | +2.22% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,177 | +0.59% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,510 | -9.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,337 (-4.33%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,195 | +1.55% |
| snake_viper_tick | +3,142 | +1.55% |
| intraweek | +2,938 | +1.39% |
| benchmark | +1,691 | +0.77% |
| oracle | +647 | +0.30% |
| random_hold | +527 | +0.25% |
| benchmark_smallcap | +348 | +0.17% |
| unified | +54 | +0.02% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -190 | -0.09% |
| gold | -444 | -0.24% |
| snake_anaconda | -667 | -0.33% |
| snake_abs_exit | -779 | -0.36% |
| snake_abs_exit_conv | -1,139 | -0.53% |
| snake_abs_conv | -1,247 | -0.59% |
| snake_abs | -1,251 | -0.59% |

Average per day so far: benchmark Rs +622, unified Rs +614, snake_abs_exit Rs +426, intraweek Rs +406, snake_abs_exit_conv Rs +377, oracle Rs +362, snake_viper_wild Rs +346, intramonth Rs +327, snake_abs_conv Rs +273, snake_abs Rs +269, snake_viper_tick Rs +240, random_hold Rs +238, snake_anaconda Rs +148, nifty_calls Rs +52, benchmark_smallcap Rs +38, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -557

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.