# Paper trading report

Updated 2026-11-19 14:10 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,497 | +11.75% | 0 | - | 236 |
| benchmark | 222,139 | +11.07% | 0 | - | 237 |
| intramonth | 213,122 | +6.56% | 0 | - | 235 |
| snake_abs_exit | 212,919 | +6.46% | 2 | 50% | 345 |
| intraweek | 211,890 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,361 | +5.68% | 0 | - | 233 |
| snake_abs_exit_conv | 210,654 | +5.33% | 2 | 50% | 345 |
| snake_abs | 208,552 | +4.28% | 1 | 100% | 255 |
| snake_abs_conv | 208,422 | +4.21% | 1 | 100% | 255 |
| random_hold | 207,871 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,542 | +3.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,996 | +2.00% | 15 | 47% | 2,625 |
| snake_anaconda | 203,047 | +1.52% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,052 | -12.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,206 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,844 | +0.84% |
| benchmark_smallcap | +1,457 | +0.73% |
| random_hold | +939 | +0.45% |
| unified | +885 | +0.40% |
| intramonth | +849 | +0.40% |
| oracle | +565 | +0.27% |
| snake_viper_wild | +503 | +0.24% |
| snake_viper_tick | +493 | +0.24% |
| intraweek | +51 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -885 | -0.42% |
| snake_abs_conv | -903 | -0.43% |
| snake_abs_exit | -1,113 | -0.52% |
| snake_anaconda | -1,354 | -0.66% |
| snake_abs_exit_conv | -1,729 | -0.81% |
| gold | -2,269 | -1.28% |

Average per day so far: unified Rs +635, benchmark Rs +598, snake_abs_exit Rs +380, intramonth Rs +355, intraweek Rs +321, snake_abs_exit_conv Rs +313, oracle Rs +307, snake_viper_wild Rs +260, snake_abs_conv Rs +248, snake_abs Rs +244, random_hold Rs +213, snake_viper_tick Rs +154, snake_anaconda Rs +95, nifty_calls Rs +50, benchmark_smallcap Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -674

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.