# Paper trading report

Updated 2026-11-19 14:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,832 | +11.92% | 0 | - | 236 |
| benchmark | 222,391 | +11.20% | 0 | - | 237 |
| snake_abs_exit | 213,714 | +6.86% | 2 | 50% | 345 |
| intramonth | 213,327 | +6.66% | 0 | - | 235 |
| intraweek | 211,976 | +5.99% | 35 | 54% | 3,851 |
| oracle | 211,864 | +5.93% | 0 | - | 233 |
| snake_abs_exit_conv | 211,394 | +5.70% | 2 | 50% | 345 |
| snake_abs | 209,225 | +4.61% | 1 | 100% | 255 |
| snake_abs_conv | 209,107 | +4.55% | 1 | 100% | 255 |
| random_hold | 207,888 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,676 | +3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,127 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,898 | +1.95% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,907 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,987 | -12.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,464 (-4.27%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,096 | +0.95% |
| benchmark_smallcap | +1,581 | +0.79% |
| unified | +1,220 | +0.55% |
| oracle | +1,068 | +0.51% |
| intramonth | +1,054 | +0.50% |
| random_hold | +956 | +0.46% |
| snake_viper_wild | +637 | +0.31% |
| snake_viper_tick | +624 | +0.31% |
| intraweek | +136 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -212 | -0.10% |
| snake_abs_conv | -218 | -0.10% |
| snake_abs_exit | -318 | -0.15% |
| snake_anaconda | -503 | -0.25% |
| snake_abs_exit_conv | -989 | -0.47% |
| gold | -2,334 | -1.32% |

Average per day so far: unified Rs +644, benchmark Rs +605, snake_abs_exit Rs +403, intramonth Rs +360, snake_abs_exit_conv Rs +335, intraweek Rs +324, oracle Rs +321, snake_abs_conv Rs +268, snake_viper_wild Rs +265, snake_abs Rs +264, random_hold Rs +213, snake_viper_tick Rs +159, snake_anaconda Rs +122, nifty_calls Rs +50, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.