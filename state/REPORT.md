# Paper trading report

Updated 2026-11-06 09:38 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,672 | +7.34% | 0 | - | 236 |
| benchmark | 213,953 | +6.98% | 0 | - | 237 |
| intraweek | 210,280 | +5.14% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,893 | +4.95% | 1 | 100% | 255 |
| snake_abs_exit | 209,656 | +4.83% | 1 | 100% | 260 |
| snake_abs | 206,842 | +3.42% | 1 | 100% | 255 |
| snake_abs_conv | 206,674 | +3.34% | 1 | 100% | 255 |
| intramonth | 206,610 | +3.31% | 0 | - | 235 |
| oracle | 204,173 | +2.09% | 0 | - | 233 |
| random_hold | 203,717 | +1.86% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,464 | -0.77% | 3 | 33% | 702 |
| snake_anaconda | 197,099 | -1.45% | 3 | 33% | 374 |
| benchmark_smallcap | 195,246 | -2.38% | 0 | - | 237 |
| snake_viper_tick | 195,100 | -2.45% | 2 | 0% | 532 |
| gold | 190,226 | -4.89% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,422 (-6.29%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +861 | +0.41% |
| benchmark | +184 | +0.09% |
| oracle | +101 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -606 | -0.30% |
| unified | -1,311 | -0.61% |
| intramonth | -1,339 | -0.64% |
| benchmark_smallcap | -3,441 | -1.73% |
| gold | -3,995 | -2.06% |
| snake_abs | -4,846 | -2.29% |
| snake_abs_conv | -4,871 | -2.30% |
| snake_abs_exit_conv | -4,910 | -2.29% |
| snake_abs_exit | -5,003 | -2.33% |
| snake_anaconda | -5,380 | -2.66% |
| snake_viper_tick | -6,038 | -3.00% |
| snake_viper_wild | -6,192 | -3.03% |

Average per day so far: unified Rs +506, benchmark Rs +481, snake_abs_exit_conv Rs +381, snake_abs_exit Rs +371, intraweek Rs +354, snake_abs_conv Rs +257, snake_abs Rs +253, intramonth Rs +228, oracle Rs +144, random_hold Rs +128, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -73, snake_anaconda Rs -121, benchmark_smallcap Rs -190, snake_viper_tick Rs -272, gold Rs -337, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.