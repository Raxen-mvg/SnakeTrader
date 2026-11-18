# Paper trading report

Updated 2026-11-18 14:03 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,535 | +11.27% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit | 213,915 | +6.96% | 2 | 50% | 345 |
| intraweek | 212,548 | +6.27% | 35 | 54% | 3,851 |
| oracle | 212,288 | +6.14% | 0 | - | 233 |
| intramonth | 212,273 | +6.14% | 0 | - | 235 |
| snake_abs_exit_conv | 212,078 | +6.04% | 2 | 50% | 345 |
| snake_abs | 209,218 | +4.61% | 1 | 100% | 255 |
| snake_abs_conv | 209,099 | +4.55% | 1 | 100% | 255 |
| random_hold | 207,306 | +3.65% | 10 | 70% | 733 |
| snake_viper_wild | 206,972 | +3.49% | 16 | 50% | 2,827 |
| snake_anaconda | 204,180 | +2.09% | 3 | 33% | 374 |
| snake_viper_tick | 203,437 | +1.72% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,239 | -11.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,131 (-4.43%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,097 | +0.49% |
| snake_abs_exit | +773 | +0.36% |
| intramonth | +731 | +0.35% |
| snake_abs_conv | +679 | +0.33% |
| snake_abs | +659 | +0.32% |
| snake_abs_exit_conv | +505 | +0.24% |
| snake_anaconda | +125 | +0.06% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -198 | -0.09% |
| intraweek | -775 | -0.36% |
| benchmark_smallcap | -1,020 | -0.51% |
| random_hold | -1,127 | -0.54% |
| benchmark | -1,339 | -0.60% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,443 | -1.17% |
| gold | -3,485 | -1.93% |

Average per day so far: unified Rs +626, benchmark Rs +563, snake_abs_exit Rs +422, snake_abs_exit_conv Rs +366, intraweek Rs +349, oracle Rs +341, intramonth Rs +341, snake_abs_conv Rs +276, snake_abs Rs +271, snake_viper_wild Rs +249, random_hold Rs +203, snake_viper_tick Rs +137, snake_anaconda Rs +135, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -14, snake_nonews Rs -326, snake Rs -347, gold Rs -632

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.