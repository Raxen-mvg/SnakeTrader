# Paper trading report

Updated 2026-11-23 10:42 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,422 | +12.21% | 0 | - | 236 |
| benchmark | 223,462 | +11.73% | 0 | - | 237 |
| intraweek | 212,989 | +6.49% | 40 | 55% | 4,400 |
| intramonth | 212,288 | +6.14% | 0 | - | 235 |
| oracle | 211,321 | +5.66% | 0 | - | 233 |
| random_hold | 210,005 | +5.00% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,901 | +3.45% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,949 | +2.98% | 2 | 50% | 345 |
| snake_abs | 204,198 | +2.10% | 1 | 100% | 255 |
| snake_abs_conv | 204,047 | +2.02% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,111 | +0.06% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,540 | -0.23% | 0 | - | 237 |
| snake_anaconda | 197,878 | -1.06% | 3 | 33% | 374 |
| snake_viper_tick | 196,701 | -1.65% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,413 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,363 (-4.82%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,365 | +0.81% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -667 | -0.32% |
| random_hold | -754 | -0.36% |
| oracle | -1,157 | -0.55% |
| benchmark_smallcap | -1,368 | -0.68% |
| snake_abs_exit | -1,661 | -0.80% |
| benchmark | -1,675 | -0.74% |
| snake_abs | -1,722 | -0.84% |
| snake_abs_conv | -1,736 | -0.84% |
| unified | -1,760 | -0.78% |
| snake_anaconda | -2,027 | -1.01% |
| snake_viper_tick | -2,671 | -1.34% |
| intramonth | -2,716 | -1.26% |
| snake_viper_wild | -2,718 | -1.34% |
| intraweek | -2,723 | -1.26% |

Average per day so far: unified Rs +626, benchmark Rs +602, intraweek Rs +333, intramonth Rs +315, oracle Rs +290, random_hold Rs +257, snake_abs_exit Rs +192, snake_abs_exit_conv Rs +165, snake_abs Rs +113, snake_abs_conv Rs +112, nifty_calls Rs +47, snake_viper_wild Rs +4, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -62, snake_viper_tick Rs -118, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.