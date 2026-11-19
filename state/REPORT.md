# Paper trading report

Updated 2026-11-19 12:54 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,810 | +11.90% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,474 | +6.74% | 0 | - | 235 |
| snake_abs_exit | 213,075 | +6.54% | 2 | 50% | 345 |
| intraweek | 211,919 | +5.96% | 35 | 54% | 3,851 |
| oracle | 211,664 | +5.83% | 0 | - | 233 |
| snake_abs_exit_conv | 211,189 | +5.59% | 2 | 50% | 345 |
| snake_abs | 208,709 | +4.36% | 1 | 100% | 255 |
| snake_abs_conv | 208,585 | +4.29% | 1 | 100% | 255 |
| random_hold | 207,878 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,388 | +3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,845 | +1.92% | 15 | 47% | 2,625 |
| snake_anaconda | 203,508 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,200 | -12.40% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,416 (-4.29%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,379 | +0.69% |
| benchmark | +1,308 | +0.59% |
| intramonth | +1,201 | +0.57% |
| unified | +1,198 | +0.54% |
| random_hold | +946 | +0.46% |
| oracle | +868 | +0.41% |
| snake_viper_wild | +349 | +0.17% |
| snake_viper_tick | +342 | +0.17% |
| intraweek | +79 | +0.04% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -727 | -0.35% |
| snake_abs_conv | -739 | -0.35% |
| snake_anaconda | -893 | -0.44% |
| snake_abs_exit | -957 | -0.45% |
| snake_abs_exit_conv | -1,194 | -0.56% |
| gold | -2,121 | -1.20% |

Average per day so far: unified Rs +644, benchmark Rs +584, snake_abs_exit Rs +385, intramonth Rs +364, snake_abs_exit_conv Rs +329, intraweek Rs +322, oracle Rs +315, snake_viper_wild Rs +255, snake_abs_conv Rs +253, snake_abs Rs +249, random_hold Rs +213, snake_viper_tick Rs +148, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -670

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.