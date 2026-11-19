# Paper trading report

Updated 2026-11-19 13:08 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,615 | +11.81% | 0 | - | 236 |
| benchmark | 221,649 | +10.82% | 0 | - | 237 |
| intramonth | 213,243 | +6.62% | 0 | - | 235 |
| snake_abs_exit | 212,542 | +6.27% | 2 | 50% | 345 |
| intraweek | 211,688 | +5.84% | 35 | 54% | 3,851 |
| oracle | 211,590 | +5.79% | 0 | - | 233 |
| snake_abs_exit_conv | 210,680 | +5.34% | 2 | 50% | 345 |
| snake_abs | 208,160 | +4.08% | 1 | 100% | 255 |
| snake_abs_conv | 208,026 | +4.01% | 1 | 100% | 255 |
| random_hold | 207,614 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,480 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,935 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 202,971 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,235 (-4.38%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,354 | +0.61% |
| benchmark_smallcap | +1,289 | +0.65% |
| unified | +1,003 | +0.45% |
| intramonth | +970 | +0.46% |
| oracle | +794 | +0.38% |
| random_hold | +681 | +0.33% |
| snake_viper_wild | +440 | +0.21% |
| snake_viper_tick | +431 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -152 | -0.07% |
| snake_abs | -1,276 | -0.61% |
| snake_abs_conv | -1,299 | -0.62% |
| snake_anaconda | -1,430 | -0.70% |
| snake_abs_exit | -1,490 | -0.70% |
| snake_abs_exit_conv | -1,704 | -0.80% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +638, benchmark Rs +585, snake_abs_exit Rs +369, intramonth Rs +358, intraweek Rs +316, snake_abs_exit_conv Rs +314, oracle Rs +313, snake_viper_wild Rs +258, snake_abs_conv Rs +236, snake_abs Rs +233, random_hold Rs +206, snake_viper_tick Rs +151, snake_anaconda Rs +93, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.