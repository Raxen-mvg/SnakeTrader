# Paper trading report

Updated 2026-11-19 13:34 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,815 | +11.91% | 0 | - | 236 |
| benchmark | 221,695 | +10.85% | 0 | - | 237 |
| intramonth | 213,361 | +6.68% | 0 | - | 235 |
| snake_abs_exit | 213,159 | +6.58% | 2 | 50% | 345 |
| intraweek | 211,837 | +5.92% | 35 | 54% | 3,851 |
| oracle | 211,461 | +5.73% | 0 | - | 233 |
| snake_abs_exit_conv | 211,174 | +5.59% | 2 | 50% | 345 |
| snake_abs | 208,695 | +4.35% | 1 | 100% | 255 |
| snake_abs_conv | 208,573 | +4.29% | 1 | 100% | 255 |
| random_hold | 207,718 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,480 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,935 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 203,239 | +1.62% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,069 | -12.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,322 (-4.34%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,400 | +0.64% |
| benchmark_smallcap | +1,345 | +0.68% |
| unified | +1,204 | +0.54% |
| intramonth | +1,088 | +0.51% |
| random_hold | +786 | +0.38% |
| oracle | +665 | +0.32% |
| snake_viper_wild | +440 | +0.21% |
| snake_viper_tick | +431 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -3 | -0.00% |
| snake_abs | -741 | -0.35% |
| snake_abs_conv | -752 | -0.36% |
| snake_abs_exit | -873 | -0.41% |
| snake_anaconda | -1,162 | -0.57% |
| snake_abs_exit_conv | -1,209 | -0.57% |
| gold | -2,252 | -1.27% |

Average per day so far: unified Rs +644, benchmark Rs +586, snake_abs_exit Rs +387, intramonth Rs +361, snake_abs_exit_conv Rs +329, intraweek Rs +320, oracle Rs +310, snake_viper_wild Rs +258, snake_abs_conv Rs +252, snake_abs Rs +248, random_hold Rs +209, snake_viper_tick Rs +151, snake_anaconda Rs +101, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -674

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.