# Paper trading report

Updated 2026-11-19 11:07 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,482 | +11.74% | 0 | - | 236 |
| benchmark | 220,915 | +10.46% | 0 | - | 237 |
| snake_abs_exit | 213,771 | +6.89% | 2 | 50% | 345 |
| intramonth | 213,069 | +6.54% | 0 | - | 235 |
| snake_abs_exit_conv | 211,877 | +5.94% | 2 | 50% | 345 |
| intraweek | 211,702 | +5.85% | 35 | 54% | 3,851 |
| oracle | 210,896 | +5.45% | 0 | - | 233 |
| snake_abs | 209,481 | +4.74% | 1 | 100% | 255 |
| snake_abs_conv | 209,357 | +4.68% | 1 | 100% | 255 |
| random_hold | 207,654 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 203,505 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,381 | +0.19% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,184 | -12.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,068 (-4.47%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,054 | +0.53% |
| unified | +870 | +0.39% |
| intramonth | +796 | +0.38% |
| random_hold | +722 | +0.35% |
| benchmark | +620 | +0.28% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| oracle | +100 | +0.05% |
| snake_abs | +45 | +0.02% |
| snake_abs_conv | +32 | +0.01% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -137 | -0.07% |
| snake_abs_exit | -260 | -0.12% |
| snake_abs_exit_conv | -507 | -0.24% |
| snake_anaconda | -896 | -0.44% |
| gold | -2,137 | -1.21% |

Average per day so far: unified Rs +635, benchmark Rs +565, snake_abs_exit Rs +405, intramonth Rs +353, snake_abs_exit_conv Rs +349, intraweek Rs +316, oracle Rs +294, snake_abs_conv Rs +275, snake_abs Rs +271, snake_viper_wild Rs +262, random_hold Rs +207, snake_viper_tick Rs +156, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +12, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -671

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.