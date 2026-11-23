# Paper trading report

Updated 2026-11-23 09:42 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,035 | +12.52% | 0 | - | 236 |
| benchmark | 223,875 | +11.94% | 0 | - | 237 |
| intraweek | 213,416 | +6.71% | 40 | 55% | 4,400 |
| intramonth | 212,611 | +6.31% | 0 | - | 235 |
| oracle | 211,599 | +5.80% | 0 | - | 233 |
| random_hold | 210,762 | +5.38% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,457 | +4.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,016 | +3.51% | 2 | 50% | 345 |
| snake_abs | 205,566 | +2.78% | 1 | 100% | 255 |
| snake_abs_conv | 205,424 | +2.71% | 1 | 100% | 255 |
| snake_viper_wild | 203,717 | +1.86% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,241 | +0.12% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,887 | -0.06% | 0 | - | 237 |
| snake_anaconda | 199,766 | -0.12% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,904 | -15.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,983 (-4.51%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +888 | +0.44% |
| snake_viper_tick | +870 | +0.44% |
| gold | +855 | +0.51% |
| snake_abs_exit_conv | +400 | +0.19% |
| random_hold | +2 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -105 | -0.05% |
| snake_anaconda | -139 | -0.07% |
| snake_abs | -354 | -0.17% |
| snake_abs_conv | -359 | -0.17% |
| oracle | -879 | -0.41% |
| benchmark_smallcap | -1,020 | -0.51% |
| unified | -1,147 | -0.51% |
| benchmark | -1,262 | -0.56% |
| intraweek | -2,296 | -1.06% |
| intramonth | -2,393 | -1.11% |

Average per day so far: unified Rs +642, benchmark Rs +612, intraweek Rs +344, intramonth Rs +323, oracle Rs +297, random_hold Rs +276, snake_abs_exit Rs +235, snake_abs_exit_conv Rs +195, snake_abs_conv Rs +151, snake_abs Rs +150, snake_viper_wild Rs +120, nifty_calls Rs +47, snake_viper_tick Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -3, snake_anaconda Rs -7, snake_nonews Rs -300, snake Rs -320, gold Rs -797

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.