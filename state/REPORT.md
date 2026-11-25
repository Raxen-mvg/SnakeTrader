# Paper trading report

Updated 2026-11-25 09:31 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,961 | +12.98% | 0 | - | 236 |
| benchmark | 224,809 | +12.40% | 0 | - | 237 |
| intramonth | 213,516 | +6.76% | 0 | - | 235 |
| oracle | 212,987 | +6.49% | 0 | - | 233 |
| intraweek | 211,744 | +5.87% | 40 | 55% | 4,400 |
| random_hold | 209,236 | +4.62% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,785 | +1.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,141 | +1.57% | 2 | 50% | 345 |
| snake_abs | 202,317 | +1.16% | 1 | 100% | 255 |
| snake_abs_conv | 202,139 | +1.07% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,044 | +0.02% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,535 | -0.23% | 16 | 50% | 2,827 |
| snake_viper_tick | 196,137 | -1.93% | 15 | 47% | 2,625 |
| snake_anaconda | 195,368 | -2.32% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,714 | -17.14% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,306 (-4.85%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,335 | +1.51% |
| unified | +1,676 | +0.75% |
| benchmark_smallcap | +1,065 | +0.54% |
| random_hold | +809 | +0.39% |
| intramonth | +765 | +0.36% |
| oracle | +645 | +0.30% |
| intraweek | +125 | +0.06% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,556 | -0.79% |
| snake_viper_wild | -1,589 | -0.79% |
| snake_abs | -3,144 | -1.53% |
| snake_abs_conv | -3,163 | -1.54% |
| snake_anaconda | -3,335 | -1.68% |
| snake_abs_exit | -3,710 | -1.79% |
| gold | -3,715 | -2.19% |
| snake_abs_exit_conv | -3,905 | -1.89% |

Average per day so far: unified Rs +649, benchmark Rs +620, intramonth Rs +338, oracle Rs +325, intraweek Rs +294, random_hold Rs +231, snake_abs_exit Rs +102, snake_abs_exit_conv Rs +85, snake_abs Rs +61, snake_abs_conv Rs +58, nifty_calls Rs +46, benchmark_smallcap Rs +1, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -15, snake_anaconda Rs -132, snake_viper_tick Rs -133, snake_nonews Rs -292, snake Rs -311, gold Rs -857

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.