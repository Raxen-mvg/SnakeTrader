# Paper trading report

Updated 2026-11-19 15:30 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,615 | +12.31% | 0 | - | 236 |
| benchmark | 222,376 | +11.19% | 0 | - | 237 |
| intramonth | 214,008 | +7.00% | 0 | - | 235 |
| snake_abs_exit | 213,351 | +6.68% | 2 | 50% | 345 |
| intraweek | 212,889 | +6.45% | 35 | 54% | 3,851 |
| oracle | 212,089 | +6.04% | 0 | - | 233 |
| snake_abs_exit_conv | 211,064 | +5.53% | 2 | 50% | 345 |
| snake_abs | 208,980 | +4.49% | 1 | 100% | 255 |
| snake_abs_conv | 208,860 | +4.43% | 1 | 100% | 255 |
| random_hold | 208,453 | +4.23% | 10 | 70% | 733 |
| snake_viper_wild | 207,523 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,977 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,464 | +1.73% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,773 | -12.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,981 (-4.01%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,141 | +1.07% |
| benchmark | +2,081 | +0.94% |
| unified | +2,004 | +0.90% |
| intramonth | +1,734 | +0.82% |
| random_hold | +1,521 | +0.73% |
| oracle | +1,293 | +0.61% |
| intraweek | +1,050 | +0.49% |
| snake_viper_wild | +483 | +0.23% |
| snake_viper_tick | +474 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -457 | -0.22% |
| snake_abs_conv | -465 | -0.22% |
| snake_abs_exit | -681 | -0.32% |
| snake_anaconda | -937 | -0.46% |
| snake_abs_exit_conv | -1,319 | -0.62% |
| gold | -2,548 | -1.44% |

Average per day so far: unified Rs +665, benchmark Rs +605, snake_abs_exit Rs +393, intramonth Rs +379, intraweek Rs +348, oracle Rs +327, snake_abs_exit_conv Rs +325, snake_abs_conv Rs +261, snake_viper_wild Rs +259, snake_abs Rs +257, random_hold Rs +228, snake_viper_tick Rs +153, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +44, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -682

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.