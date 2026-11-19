# Paper trading report

Updated 2026-11-19 13:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,812 | +11.91% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,438 | +6.72% | 0 | - | 235 |
| snake_abs_exit | 212,754 | +6.38% | 2 | 50% | 345 |
| intraweek | 211,911 | +5.96% | 35 | 54% | 3,851 |
| oracle | 211,504 | +5.75% | 0 | - | 233 |
| snake_abs_exit_conv | 210,851 | +5.43% | 2 | 50% | 345 |
| snake_abs | 208,389 | +4.19% | 1 | 100% | 255 |
| snake_abs_conv | 208,262 | +4.13% | 1 | 100% | 255 |
| random_hold | 207,615 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,393 | +3.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,850 | +1.93% | 15 | 47% | 2,625 |
| snake_anaconda | 202,924 | +1.46% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,118 | -12.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,329 (-4.34%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,308 | +0.59% |
| benchmark_smallcap | +1,233 | +0.62% |
| unified | +1,201 | +0.54% |
| intramonth | +1,165 | +0.55% |
| oracle | +708 | +0.34% |
| random_hold | +682 | +0.33% |
| snake_viper_wild | +354 | +0.17% |
| snake_viper_tick | +347 | +0.17% |
| intraweek | +72 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -1,048 | -0.50% |
| snake_abs_conv | -1,063 | -0.51% |
| snake_abs_exit | -1,278 | -0.60% |
| snake_anaconda | -1,477 | -0.72% |
| snake_abs_exit_conv | -1,532 | -0.72% |
| gold | -2,203 | -1.24% |

Average per day so far: unified Rs +644, benchmark Rs +584, snake_abs_exit Rs +375, intramonth Rs +363, intraweek Rs +322, snake_abs_exit_conv Rs +319, oracle Rs +311, snake_viper_wild Rs +255, snake_abs_conv Rs +243, snake_abs Rs +240, random_hold Rs +206, snake_viper_tick Rs +148, snake_anaconda Rs +91, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.