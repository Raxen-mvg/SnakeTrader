# Paper trading report

Updated 2026-11-19 14:34 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,921 | +11.96% | 0 | - | 236 |
| benchmark | 222,399 | +11.20% | 0 | - | 237 |
| snake_abs_exit | 213,655 | +6.83% | 2 | 50% | 345 |
| intramonth | 213,415 | +6.71% | 0 | - | 235 |
| intraweek | 212,038 | +6.02% | 35 | 54% | 3,851 |
| oracle | 211,876 | +5.94% | 0 | - | 233 |
| snake_abs_exit_conv | 211,337 | +5.67% | 2 | 50% | 345 |
| snake_abs | 209,172 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,053 | +4.53% | 1 | 100% | 255 |
| random_hold | 207,936 | +3.97% | 10 | 70% | 733 |
| snake_viper_wild | 207,676 | +3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,127 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,846 | +1.92% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,874 | +0.44% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,036 | -12.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,511 (-4.24%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,104 | +0.95% |
| benchmark_smallcap | +1,547 | +0.78% |
| unified | +1,309 | +0.59% |
| intramonth | +1,141 | +0.54% |
| oracle | +1,080 | +0.51% |
| random_hold | +1,003 | +0.48% |
| snake_viper_wild | +637 | +0.31% |
| snake_viper_tick | +624 | +0.31% |
| intraweek | +199 | +0.09% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -265 | -0.13% |
| snake_abs_conv | -272 | -0.13% |
| snake_abs_exit | -377 | -0.18% |
| snake_anaconda | -555 | -0.27% |
| snake_abs_exit_conv | -1,047 | -0.49% |
| gold | -2,285 | -1.29% |

Average per day so far: unified Rs +647, benchmark Rs +605, snake_abs_exit Rs +402, intramonth Rs +363, snake_abs_exit_conv Rs +333, intraweek Rs +325, oracle Rs +321, snake_abs_conv Rs +266, snake_viper_wild Rs +265, snake_abs Rs +262, random_hold Rs +214, snake_viper_tick Rs +159, snake_anaconda Rs +120, nifty_calls Rs +50, benchmark_smallcap Rs +26, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -675

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.