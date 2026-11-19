# Paper trading report

Updated 2026-11-19 12:40 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,812 | +11.91% | 0 | - | 236 |
| benchmark | 221,718 | +10.86% | 0 | - | 237 |
| intramonth | 213,463 | +6.73% | 0 | - | 235 |
| snake_abs_exit | 212,921 | +6.46% | 2 | 50% | 345 |
| intraweek | 211,619 | +5.81% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,998 | +5.50% | 2 | 50% | 345 |
| oracle | 210,992 | +5.50% | 0 | - | 233 |
| snake_abs | 208,665 | +4.33% | 1 | 100% | 255 |
| snake_abs_conv | 208,536 | +4.27% | 1 | 100% | 255 |
| random_hold | 207,754 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,518 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,972 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 202,943 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,216 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,435 | +0.72% |
| benchmark | +1,423 | +0.65% |
| unified | +1,200 | +0.54% |
| intramonth | +1,190 | +0.56% |
| random_hold | +822 | +0.40% |
| snake_viper_wild | +479 | +0.23% |
| snake_viper_tick | +469 | +0.23% |
| oracle | +196 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -221 | -0.10% |
| snake_abs | -772 | -0.37% |
| snake_abs_conv | -789 | -0.38% |
| snake_abs_exit | -1,111 | -0.52% |
| snake_abs_exit_conv | -1,385 | -0.65% |
| snake_anaconda | -1,458 | -0.71% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +644, benchmark Rs +587, snake_abs_exit Rs +380, intramonth Rs +364, snake_abs_exit_conv Rs +323, intraweek Rs +314, oracle Rs +297, snake_viper_wild Rs +259, snake_abs_conv Rs +251, snake_abs Rs +248, random_hold Rs +210, snake_viper_tick Rs +153, snake_anaconda Rs +92, nifty_calls Rs +50, benchmark_smallcap Rs +23, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.