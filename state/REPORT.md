# Paper trading report

Updated 2026-11-12 13:06 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,615 | +10.81% | 0 | - | 236 |
| benchmark | 220,242 | +10.12% | 0 | - | 237 |
| snake_abs_exit_conv | 218,788 | +9.39% | 2 | 50% | 345 |
| snake_abs_exit | 217,714 | +8.86% | 2 | 50% | 345 |
| snake_abs | 215,727 | +7.86% | 1 | 100% | 255 |
| snake_abs_conv | 215,556 | +7.78% | 1 | 100% | 255 |
| intraweek | 214,706 | +7.35% | 30 | 53% | 3,302 |
| oracle | 213,590 | +6.79% | 0 | - | 233 |
| intramonth | 212,201 | +6.10% | 0 | - | 235 |
| random_hold | 208,080 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,285 | +3.64% | 10 | 50% | 1,825 |
| snake_anaconda | 206,480 | +3.24% | 3 | 33% | 374 |
| snake_viper_tick | 203,739 | +1.87% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,194 | +1.60% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,919 | -7.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,334 (-3.83%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,388 | +1.19% |
| snake_anaconda | +2,357 | +1.16% |
| snake_abs | +2,102 | +0.98% |
| snake_abs_conv | +2,098 | +0.98% |
| unified | +1,801 | +0.82% |
| snake_abs_exit_conv | +1,637 | +0.75% |
| oracle | +1,587 | +0.75% |
| intraweek | +1,573 | +0.74% |
| snake_abs_exit | +1,552 | +0.72% |
| intramonth | +1,205 | +0.57% |
| benchmark | +979 | +0.45% |
| random_hold | +969 | +0.47% |
| snake_viper_wild | +543 | +0.26% |
| snake_viper_tick | +530 | +0.26% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,666 | -1.93% |

Average per day so far: unified Rs +675, snake_abs_exit_conv Rs +648, benchmark Rs +633, snake_abs_exit Rs +611, snake_abs_conv Rs +536, snake_abs Rs +524, intraweek Rs +460, oracle Rs +425, intramonth Rs +381, snake_viper_wild Rs +304, random_hold Rs +252, snake_anaconda Rs +240, snake_viper_tick Rs +178, benchmark_smallcap Rs +114, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -440

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.