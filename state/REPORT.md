# Paper trading report

Updated 2026-11-23 12:09 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,290 | +12.14% | 0 | - | 236 |
| benchmark | 222,942 | +11.47% | 0 | - | 237 |
| intraweek | 213,009 | +6.50% | 40 | 55% | 4,400 |
| intramonth | 212,328 | +6.16% | 0 | - | 235 |
| oracle | 211,897 | +5.95% | 0 | - | 233 |
| random_hold | 209,894 | +4.95% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,925 | +3.46% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,566 | +2.78% | 2 | 50% | 345 |
| snake_abs | 204,471 | +2.24% | 1 | 100% | 255 |
| snake_abs_conv | 204,302 | +2.15% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,249 | +0.62% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_anaconda | 197,937 | -1.03% | 3 | 33% | 374 |
| snake_viper_tick | 197,815 | -1.09% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,071 | -14.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,439 (-4.78%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,022 | +1.20% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -581 | -0.27% |
| random_hold | -866 | -0.41% |
| snake_abs_exit_conv | -1,050 | -0.51% |
| benchmark_smallcap | -1,356 | -0.68% |
| snake_abs | -1,448 | -0.70% |
| snake_abs_conv | -1,481 | -0.72% |
| snake_viper_tick | -1,557 | -0.78% |
| snake_viper_wild | -1,580 | -0.78% |
| snake_abs_exit | -1,638 | -0.79% |
| unified | -1,892 | -0.84% |
| snake_anaconda | -1,968 | -0.98% |
| benchmark | -2,196 | -0.97% |
| intramonth | -2,676 | -1.25% |
| intraweek | -2,703 | -1.25% |

Average per day so far: unified Rs +623, benchmark Rs +588, intraweek Rs +334, intramonth Rs +316, oracle Rs +305, random_hold Rs +254, snake_abs_exit Rs +192, snake_abs_exit_conv Rs +155, snake_abs Rs +121, snake_abs_conv Rs +120, nifty_calls Rs +47, snake_viper_wild Rs +40, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -61, snake_viper_tick Rs -78, snake_nonews Rs -300, snake Rs -320, gold Rs -767

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.