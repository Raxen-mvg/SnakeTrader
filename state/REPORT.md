# Paper trading report

Updated 2026-11-17 12:00 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| unified | 222,261 | +11.13% | 0 | - | 236 |
| snake_abs_exit | 215,029 | +7.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,223 | +6.61% | 2 | 50% | 345 |
| intraweek | 212,644 | +6.32% | 35 | 54% | 3,851 |
| oracle | 212,229 | +6.12% | 0 | - | 233 |
| intramonth | 212,132 | +6.07% | 0 | - | 235 |
| snake_abs | 209,846 | +4.92% | 1 | 100% | 255 |
| snake_abs_conv | 209,698 | +4.85% | 1 | 100% | 255 |
| random_hold | 208,033 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,329 | +3.67% | 14 | 50% | 2,496 |
| snake_anaconda | 205,388 | +2.69% | 3 | 33% | 374 |
| snake_viper_tick | 203,784 | +1.89% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,275 | +1.14% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,431 | -9.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,312 (-4.34%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,211 | +1.00% |
| benchmark_smallcap | +1,446 | +0.72% |
| intraweek | +1,378 | +0.65% |
| snake_viper_wild | +1,185 | +0.57% |
| snake_viper_tick | +1,164 | +0.57% |
| unified | +823 | +0.37% |
| snake_abs_exit | +620 | +0.29% |
| intramonth | +513 | +0.24% |
| gold | +477 | +0.26% |
| snake_anaconda | +285 | +0.14% |
| random_hold | +240 | +0.12% |
| oracle | +206 | +0.10% |
| snake_abs_exit_conv | +6 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -287 | -0.14% |
| snake_abs_conv | -292 | -0.14% |

Average per day so far: benchmark Rs +637, unified Rs +636, snake_abs_exit Rs +470, snake_abs_exit_conv Rs +413, intraweek Rs +361, oracle Rs +349, intramonth Rs +347, snake_abs_conv Rs +303, snake_abs Rs +298, snake_viper_wild Rs +271, random_hold Rs +230, snake_anaconda Rs +180, snake_viper_tick Rs +158, benchmark_smallcap Rs +73, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.