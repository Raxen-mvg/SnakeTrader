# Paper trading report

Updated 2026-11-20 09:59 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,363 | +12.68% | 0 | - | 236 |
| benchmark | 222,812 | +11.41% | 0 | - | 237 |
| intramonth | 214,496 | +7.25% | 0 | - | 235 |
| intraweek | 213,924 | +6.96% | 35 | 54% | 3,851 |
| oracle | 212,701 | +6.35% | 0 | - | 233 |
| snake_abs_exit | 210,678 | +5.34% | 2 | 50% | 345 |
| random_hold | 209,033 | +4.52% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,438 | +4.22% | 2 | 50% | 345 |
| snake_abs | 207,122 | +3.56% | 1 | 100% | 255 |
| snake_abs_conv | 206,985 | +3.49% | 1 | 100% | 255 |
| snake_viper_wild | 205,641 | +2.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,135 | +1.07% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,432 | +0.72% | 3 | 33% | 374 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,468 | -17.27% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,824 (-4.09%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,035 | +0.49% |
| unified | +748 | +0.33% |
| oracle | +613 | +0.29% |
| random_hold | +580 | +0.28% |
| intramonth | +488 | +0.23% |
| benchmark | +436 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -796 | -0.40% |
| snake_viper_tick | -1,842 | -0.90% |
| snake_abs | -1,858 | -0.89% |
| snake_abs_conv | -1,875 | -0.90% |
| snake_viper_wild | -1,882 | -0.91% |
| snake_anaconda | -2,031 | -1.00% |
| snake_abs_exit_conv | -2,626 | -1.24% |
| snake_abs_exit | -2,673 | -1.25% |
| gold | -9,305 | -5.32% |

Average per day so far: unified Rs +667, benchmark Rs +600, intramonth Rs +381, intraweek Rs +366, oracle Rs +334, snake_abs_exit Rs +305, snake_abs_exit_conv Rs +241, random_hold Rs +238, snake_abs_conv Rs +200, snake_abs Rs +198, snake_viper_wild Rs +188, snake_viper_tick Rs +79, nifty_calls Rs +48, snake_anaconda Rs +43, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -909

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.