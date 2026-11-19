# Paper trading report

Updated 2026-11-19 09:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,982 | +11.49% | 0 | - | 236 |
| benchmark | 219,308 | +9.65% | 0 | - | 237 |
| intramonth | 212,955 | +6.48% | 0 | - | 235 |
| snake_abs_exit | 212,532 | +6.27% | 2 | 50% | 345 |
| snake_abs_exit_conv | 210,979 | +5.49% | 2 | 50% | 345 |
| intraweek | 210,977 | +5.49% | 35 | 54% | 3,851 |
| oracle | 210,413 | +5.21% | 0 | - | 233 |
| snake_abs | 208,636 | +4.32% | 1 | 100% | 255 |
| snake_abs_conv | 208,508 | +4.25% | 1 | 100% | 255 |
| snake_viper_wild | 207,692 | +3.85% | 16 | 50% | 2,827 |
| random_hold | 206,807 | +3.40% | 10 | 70% | 733 |
| snake_viper_tick | 204,142 | +2.07% | 15 | 47% | 2,625 |
| snake_anaconda | 203,330 | +1.67% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,867 | -0.57% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,658 | -12.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,606 (-4.70%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +681 | +0.32% |
| snake_viper_wild | +653 | +0.32% |
| snake_viper_tick | +639 | +0.31% |
| unified | +370 | +0.17% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| random_hold | -125 | -0.06% |
| oracle | -383 | -0.18% |
| benchmark_smallcap | -460 | -0.23% |
| snake_abs | -801 | -0.38% |
| snake_abs_conv | -817 | -0.39% |
| intraweek | -862 | -0.41% |
| benchmark | -987 | -0.45% |
| snake_anaconda | -1,071 | -0.52% |
| snake_abs_exit_conv | -1,404 | -0.66% |
| snake_abs_exit | -1,500 | -0.70% |
| gold | -2,663 | -1.50% |

Average per day so far: unified Rs +621, benchmark Rs +522, snake_abs_exit Rs +369, intramonth Rs +350, snake_abs_exit_conv Rs +323, intraweek Rs +297, oracle Rs +281, snake_viper_wild Rs +265, snake_abs_conv Rs +250, snake_abs Rs +247, random_hold Rs +184, snake_viper_tick Rs +159, snake_anaconda Rs +104, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, snake_nonews Rs -317, snake Rs -337, gold Rs -685

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.