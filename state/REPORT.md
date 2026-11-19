# Paper trading report

Updated 2026-11-19 15:04 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,679 | +12.34% | 0 | - | 236 |
| benchmark | 222,231 | +11.12% | 0 | - | 237 |
| intramonth | 214,114 | +7.06% | 0 | - | 235 |
| snake_abs_exit | 213,609 | +6.80% | 2 | 50% | 345 |
| intraweek | 213,148 | +6.57% | 35 | 54% | 3,851 |
| oracle | 212,045 | +6.02% | 0 | - | 233 |
| snake_abs_exit_conv | 211,296 | +5.65% | 2 | 50% | 345 |
| snake_abs | 208,992 | +4.50% | 1 | 100% | 255 |
| snake_abs_conv | 208,882 | +4.44% | 1 | 100% | 255 |
| random_hold | 208,397 | +4.20% | 10 | 70% | 733 |
| snake_viper_wild | 207,139 | +3.57% | 16 | 50% | 2,827 |
| snake_anaconda | 203,677 | +1.84% | 3 | 33% | 374 |
| snake_viper_tick | 203,601 | +1.80% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,822 | -12.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,044 (-3.98%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,067 | +0.93% |
| benchmark_smallcap | +2,007 | +1.01% |
| benchmark | +1,935 | +0.88% |
| intramonth | +1,841 | +0.87% |
| random_hold | +1,465 | +0.71% |
| intraweek | +1,309 | +0.62% |
| oracle | +1,249 | +0.59% |
| snake_viper_wild | +99 | +0.05% |
| snake_viper_tick | +98 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -422 | -0.20% |
| snake_abs_conv | -443 | -0.21% |
| snake_abs | -444 | -0.21% |
| snake_anaconda | -724 | -0.35% |
| snake_abs_exit_conv | -1,087 | -0.51% |
| gold | -2,499 | -1.41% |

Average per day so far: unified Rs +667, benchmark Rs +601, snake_abs_exit Rs +400, intramonth Rs +381, intraweek Rs +355, snake_abs_exit_conv Rs +332, oracle Rs +326, snake_abs_conv Rs +261, snake_abs Rs +257, snake_viper_wild Rs +246, random_hold Rs +227, snake_viper_tick Rs +138, snake_anaconda Rs +115, nifty_calls Rs +50, benchmark_smallcap Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.