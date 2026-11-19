# Paper trading report

Updated 2026-11-19 11:00 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,458 | +11.73% | 0 | - | 236 |
| benchmark | 220,838 | +10.42% | 0 | - | 237 |
| snake_abs_exit | 213,655 | +6.83% | 2 | 50% | 345 |
| intramonth | 213,040 | +6.52% | 0 | - | 235 |
| snake_abs_exit_conv | 211,712 | +5.86% | 2 | 50% | 345 |
| intraweek | 211,425 | +5.71% | 35 | 54% | 3,851 |
| oracle | 210,753 | +5.38% | 0 | - | 233 |
| snake_abs | 209,422 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,295 | +4.65% | 1 | 100% | 255 |
| snake_viper_wild | 207,744 | +3.87% | 16 | 50% | 2,827 |
| random_hold | 207,451 | +3.73% | 10 | 70% | 733 |
| snake_viper_tick | 204,193 | +2.10% | 15 | 47% | 2,625 |
| snake_anaconda | 203,449 | +1.73% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,212 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,966 (-4.52%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +886 | +0.44% |
| unified | +847 | +0.38% |
| intramonth | +767 | +0.36% |
| snake_viper_wild | +704 | +0.34% |
| snake_viper_tick | +690 | +0.34% |
| benchmark | +543 | +0.25% |
| random_hold | +519 | +0.25% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_abs | -14 | -0.01% |
| snake_abs_conv | -29 | -0.01% |
| oracle | -43 | -0.02% |
| snake_abs_exit | -377 | -0.18% |
| intraweek | -415 | -0.20% |
| snake_abs_exit_conv | -672 | -0.32% |
| snake_anaconda | -952 | -0.47% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +634, benchmark Rs +563, snake_abs_exit Rs +402, intramonth Rs +352, snake_abs_exit_conv Rs +344, intraweek Rs +309, oracle Rs +291, snake_abs_conv Rs +273, snake_abs Rs +269, snake_viper_wild Rs +267, random_hold Rs +201, snake_viper_tick Rs +161, snake_anaconda Rs +108, nifty_calls Rs +50, benchmark_smallcap Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.