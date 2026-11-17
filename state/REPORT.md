# Paper trading report

Updated 2026-11-17 10:35 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,983 | +10.99% | 0 | - | 236 |
| benchmark | 221,542 | +10.77% | 0 | - | 237 |
| snake_abs_exit | 215,511 | +7.75% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,621 | +6.81% | 2 | 50% | 345 |
| intraweek | 213,412 | +6.71% | 35 | 54% | 3,851 |
| oracle | 212,335 | +6.17% | 0 | - | 233 |
| intramonth | 211,952 | +5.98% | 0 | - | 235 |
| snake_abs | 210,044 | +5.02% | 1 | 100% | 255 |
| snake_abs_conv | 209,895 | +4.95% | 1 | 100% | 255 |
| random_hold | 208,304 | +4.15% | 10 | 70% | 733 |
| snake_viper_wild | 206,924 | +3.46% | 14 | 50% | 2,496 |
| snake_anaconda | 205,558 | +2.78% | 3 | 33% | 374 |
| snake_viper_tick | 203,386 | +1.69% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,816 | +0.91% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,415 | -9.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,370 (-4.32%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,146 | +1.02% |
| benchmark | +1,461 | +0.66% |
| snake_abs_exit | +1,102 | +0.51% |
| benchmark_smallcap | +986 | +0.49% |
| snake_viper_wild | +780 | +0.38% |
| snake_viper_tick | +766 | +0.38% |
| unified | +546 | +0.25% |
| random_hold | +511 | +0.25% |
| gold | +460 | +0.25% |
| snake_anaconda | +456 | +0.22% |
| snake_abs_exit_conv | +404 | +0.19% |
| intramonth | +333 | +0.16% |
| oracle | +312 | +0.15% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -89 | -0.04% |
| snake_abs_conv | -95 | -0.04% |

Average per day so far: unified Rs +628, benchmark Rs +615, snake_abs_exit Rs +485, snake_abs_exit_conv Rs +426, intraweek Rs +383, oracle Rs +352, intramonth Rs +341, snake_abs_conv Rs +309, snake_abs Rs +304, snake_viper_wild Rs +256, random_hold Rs +237, snake_anaconda Rs +185, snake_viper_tick Rs +141, benchmark_smallcap Rs +59, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.