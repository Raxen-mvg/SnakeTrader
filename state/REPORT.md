# Paper trading report

Updated 2026-11-19 14:07 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,782 | +11.89% | 0 | - | 236 |
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| intramonth | 213,360 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 212,944 | +6.47% | 2 | 50% | 345 |
| intraweek | 211,908 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,563 | +5.78% | 0 | - | 233 |
| snake_abs_exit_conv | 210,674 | +5.34% | 2 | 50% | 345 |
| snake_abs | 208,605 | +4.30% | 1 | 100% | 255 |
| snake_abs_conv | 208,475 | +4.24% | 1 | 100% | 255 |
| random_hold | 207,906 | +3.95% | 10 | 70% | 733 |
| snake_viper_wild | 207,542 | +3.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,996 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,101 | +1.55% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,840 | +0.42% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,118 | -12.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,359 (-4.32%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,729 | +0.79% |
| benchmark_smallcap | +1,513 | +0.76% |
| unified | +1,171 | +0.53% |
| intramonth | +1,086 | +0.51% |
| random_hold | +973 | +0.47% |
| oracle | +767 | +0.36% |
| snake_viper_wild | +503 | +0.24% |
| snake_viper_tick | +493 | +0.24% |
| intraweek | +69 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -832 | -0.40% |
| snake_abs_conv | -850 | -0.41% |
| snake_abs_exit | -1,088 | -0.51% |
| snake_anaconda | -1,300 | -0.64% |
| snake_abs_exit_conv | -1,709 | -0.81% |
| gold | -2,203 | -1.24% |

Average per day so far: unified Rs +643, benchmark Rs +595, snake_abs_exit Rs +381, intramonth Rs +361, intraweek Rs +322, snake_abs_exit_conv Rs +314, oracle Rs +313, snake_viper_wild Rs +260, snake_abs_conv Rs +249, snake_abs Rs +246, random_hold Rs +214, snake_viper_tick Rs +154, snake_anaconda Rs +97, nifty_calls Rs +50, benchmark_smallcap Rs +25, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.