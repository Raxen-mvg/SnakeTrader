# Paper trading report

Updated 2026-11-17 10:54 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,849 | +10.92% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| snake_abs_exit | 215,719 | +7.86% | 2 | 50% | 345 |
| intraweek | 214,107 | +7.05% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,828 | +6.91% | 2 | 50% | 345 |
| oracle | 212,678 | +6.34% | 0 | - | 233 |
| intramonth | 211,694 | +5.85% | 0 | - | 235 |
| snake_abs | 210,382 | +5.19% | 1 | 100% | 255 |
| snake_abs_conv | 210,232 | +5.12% | 1 | 100% | 255 |
| random_hold | 208,260 | +4.13% | 10 | 70% | 733 |
| snake_viper_wild | 207,285 | +3.64% | 14 | 50% | 2,496 |
| snake_anaconda | 205,791 | +2.90% | 3 | 33% | 374 |
| snake_viper_tick | 203,741 | +1.87% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,107 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,694 | -9.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,484 (-4.26%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,841 | +1.34% |
| benchmark | +1,522 | +0.69% |
| snake_abs_exit | +1,310 | +0.61% |
| benchmark_smallcap | +1,278 | +0.64% |
| snake_viper_wild | +1,141 | +0.55% |
| snake_viper_tick | +1,121 | +0.55% |
| gold | +740 | +0.41% |
| snake_anaconda | +688 | +0.34% |
| oracle | +655 | +0.31% |
| snake_abs_exit_conv | +611 | +0.29% |
| random_hold | +467 | +0.23% |
| unified | +411 | +0.19% |
| snake_abs | +248 | +0.12% |
| snake_abs_conv | +243 | +0.12% |
| intramonth | +75 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +624, benchmark Rs +617, snake_abs_exit Rs +491, snake_abs_exit_conv Rs +432, intraweek Rs +403, oracle Rs +362, intramonth Rs +334, snake_abs_conv Rs +320, snake_abs Rs +315, snake_viper_wild Rs +270, random_hold Rs +236, snake_anaconda Rs +193, snake_viper_tick Rs +156, benchmark_smallcap Rs +68, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -523

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.