# Paper trading report

Updated 2026-11-17 13:09 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,492 | +10.75% | 0 | - | 236 |
| benchmark | 221,427 | +10.71% | 0 | - | 237 |
| snake_abs_exit | 214,286 | +7.14% | 2 | 50% | 345 |
| intraweek | 213,626 | +6.81% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,598 | +6.30% | 2 | 50% | 345 |
| oracle | 211,901 | +5.95% | 0 | - | 233 |
| intramonth | 211,342 | +5.67% | 0 | - | 235 |
| snake_abs | 209,509 | +4.75% | 1 | 100% | 255 |
| snake_abs_conv | 209,371 | +4.68% | 1 | 100% | 255 |
| snake_viper_wild | 208,421 | +4.21% | 14 | 50% | 2,496 |
| random_hold | 207,388 | +3.69% | 10 | 70% | 733 |
| snake_anaconda | 205,027 | +2.51% | 3 | 33% | 374 |
| snake_viper_tick | 204,860 | +2.43% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,020 | +0.51% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,382 | -9.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,985 (-4.51%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,360 | +1.12% |
| snake_viper_wild | +2,277 | +1.10% |
| snake_viper_tick | +2,240 | +1.10% |
| benchmark | +1,346 | +0.61% |
| gold | +427 | +0.24% |
| benchmark_smallcap | +191 | +0.10% |
| unified | +54 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_anaconda | -76 | -0.04% |
| oracle | -122 | -0.06% |
| snake_abs_exit | -124 | -0.06% |
| intramonth | -277 | -0.13% |
| random_hold | -406 | -0.20% |
| snake_abs_conv | -619 | -0.29% |
| snake_abs_exit_conv | -619 | -0.29% |
| snake_abs | -625 | -0.30% |

Average per day so far: unified Rs +614, benchmark Rs +612, snake_abs_exit Rs +446, snake_abs_exit_conv Rs +394, intraweek Rs +389, oracle Rs +340, intramonth Rs +324, snake_viper_wild Rs +312, snake_abs_conv Rs +293, snake_abs Rs +288, random_hold Rs +211, snake_viper_tick Rs +202, snake_anaconda Rs +168, nifty_calls Rs +52, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.