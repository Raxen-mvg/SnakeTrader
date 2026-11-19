# Paper trading report

Updated 2026-11-19 13:40 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,819 | +11.91% | 0 | - | 236 |
| benchmark | 221,779 | +10.89% | 0 | - | 237 |
| intramonth | 213,339 | +6.67% | 0 | - | 235 |
| snake_abs_exit | 213,077 | +6.54% | 2 | 50% | 345 |
| intraweek | 211,969 | +5.98% | 35 | 54% | 3,851 |
| oracle | 211,500 | +5.75% | 0 | - | 233 |
| snake_abs_exit_conv | 211,121 | +5.56% | 2 | 50% | 345 |
| snake_abs | 208,632 | +4.32% | 1 | 100% | 255 |
| snake_abs_conv | 208,509 | +4.25% | 1 | 100% | 255 |
| random_hold | 207,758 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,422 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,878 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,204 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,594 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,102 | -12.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,343 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,484 | +0.67% |
| benchmark_smallcap | +1,267 | +0.64% |
| unified | +1,207 | +0.54% |
| intramonth | +1,066 | +0.50% |
| random_hold | +825 | +0.40% |
| oracle | +704 | +0.33% |
| snake_viper_wild | +383 | +0.18% |
| snake_viper_tick | +375 | +0.18% |
| intraweek | +129 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -805 | -0.38% |
| snake_abs_conv | -816 | -0.39% |
| snake_abs_exit | -955 | -0.45% |
| snake_anaconda | -1,197 | -0.59% |
| snake_abs_exit_conv | -1,262 | -0.59% |
| gold | -2,219 | -1.25% |

Average per day so far: unified Rs +644, benchmark Rs +589, snake_abs_exit Rs +385, intramonth Rs +361, snake_abs_exit_conv Rs +327, intraweek Rs +323, oracle Rs +311, snake_viper_wild Rs +256, snake_abs_conv Rs +250, snake_abs Rs +247, random_hold Rs +210, snake_viper_tick Rs +149, snake_anaconda Rs +100, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -673

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.