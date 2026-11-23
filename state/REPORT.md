# Paper trading report

Updated 2026-11-23 14:58 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,112 | +12.06% | 0 | - | 236 |
| benchmark | 221,833 | +10.92% | 0 | - | 237 |
| oracle | 211,902 | +5.95% | 0 | - | 233 |
| intramonth | 211,865 | +5.93% | 0 | - | 235 |
| intraweek | 211,788 | +5.89% | 40 | 55% | 4,400 |
| random_hold | 208,812 | +4.41% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,514 | +3.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,901 | +3.45% | 2 | 50% | 345 |
| snake_abs | 205,524 | +2.76% | 1 | 100% | 255 |
| snake_abs_conv | 205,345 | +2.67% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,532 | +0.77% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,876 | -0.06% | 0 | - | 237 |
| snake_anaconda | 198,436 | -0.78% | 3 | 33% | 374 |
| snake_viper_tick | 198,092 | -0.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,545 | -15.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,199 (-4.90%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,496 | +0.89% |
| snake_abs_exit_conv | +285 | +0.14% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -396 | -0.19% |
| snake_abs_conv | -437 | -0.21% |
| oracle | -577 | -0.27% |
| benchmark_smallcap | -1,031 | -0.51% |
| snake_abs_exit | -1,049 | -0.50% |
| snake_viper_tick | -1,280 | -0.64% |
| snake_viper_wild | -1,297 | -0.64% |
| snake_anaconda | -1,470 | -0.73% |
| random_hold | -1,948 | -0.92% |
| unified | -2,070 | -0.92% |
| intramonth | -3,139 | -1.46% |
| benchmark | -3,305 | -1.47% |
| intraweek | -3,925 | -1.82% |

Average per day so far: unified Rs +618, benchmark Rs +560, oracle Rs +305, intramonth Rs +304, intraweek Rs +302, random_hold Rs +226, snake_abs_exit Rs +209, snake_abs_exit_conv Rs +192, snake_abs Rs +149, snake_abs_conv Rs +148, snake_viper_wild Rs +49, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -4, snake_anaconda Rs -46, snake_viper_tick Rs -68, snake_nonews Rs -300, snake Rs -320, gold Rs -781

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.