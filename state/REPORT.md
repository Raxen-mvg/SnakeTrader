# Paper trading report

Updated 2026-11-19 14:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,558 | +11.78% | 0 | - | 236 |
| benchmark | 222,483 | +11.24% | 0 | - | 237 |
| snake_abs_exit | 213,563 | +6.78% | 2 | 50% | 345 |
| intramonth | 213,243 | +6.62% | 0 | - | 235 |
| intraweek | 211,944 | +5.97% | 35 | 54% | 3,851 |
| oracle | 211,396 | +5.70% | 0 | - | 233 |
| snake_abs_exit_conv | 211,277 | +5.64% | 2 | 50% | 345 |
| snake_abs | 209,141 | +4.57% | 1 | 100% | 255 |
| snake_abs_conv | 209,023 | +4.51% | 1 | 100% | 255 |
| random_hold | 207,921 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 207,676 | +3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,127 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,649 | +1.82% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,874 | +0.44% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,069 | -12.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,291 (-4.35%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,188 | +0.99% |
| benchmark_smallcap | +1,547 | +0.78% |
| random_hold | +989 | +0.48% |
| intramonth | +969 | +0.46% |
| unified | +946 | +0.42% |
| snake_viper_wild | +637 | +0.31% |
| snake_viper_tick | +624 | +0.31% |
| oracle | +600 | +0.28% |
| intraweek | +105 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -295 | -0.14% |
| snake_abs_conv | -302 | -0.14% |
| snake_abs_exit | -468 | -0.22% |
| snake_anaconda | -752 | -0.37% |
| snake_abs_exit_conv | -1,107 | -0.52% |
| gold | -2,252 | -1.27% |

Average per day so far: unified Rs +637, benchmark Rs +608, snake_abs_exit Rs +399, intramonth Rs +358, snake_abs_exit_conv Rs +332, intraweek Rs +323, oracle Rs +308, snake_abs_conv Rs +265, snake_viper_wild Rs +265, snake_abs Rs +261, random_hold Rs +214, snake_viper_tick Rs +159, snake_anaconda Rs +114, nifty_calls Rs +50, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -674

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.