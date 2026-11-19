# Paper trading report

Updated 2026-11-19 13:31 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,807 | +11.90% | 0 | - | 236 |
| benchmark | 221,680 | +10.84% | 0 | - | 237 |
| intramonth | 213,393 | +6.70% | 0 | - | 235 |
| snake_abs_exit | 213,202 | +6.60% | 2 | 50% | 345 |
| intraweek | 211,809 | +5.90% | 35 | 54% | 3,851 |
| oracle | 211,568 | +5.78% | 0 | - | 233 |
| snake_abs_exit_conv | 211,189 | +5.59% | 2 | 50% | 345 |
| snake_abs | 208,743 | +4.37% | 1 | 100% | 255 |
| snake_abs_conv | 208,620 | +4.31% | 1 | 100% | 255 |
| random_hold | 207,666 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 207,480 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,935 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 203,280 | +1.64% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,937 | -12.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,336 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,385 | +0.63% |
| benchmark_smallcap | +1,233 | +0.62% |
| unified | +1,196 | +0.54% |
| intramonth | +1,120 | +0.53% |
| oracle | +772 | +0.37% |
| random_hold | +734 | +0.35% |
| snake_viper_wild | +440 | +0.21% |
| snake_viper_tick | +431 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -31 | -0.01% |
| snake_abs | -694 | -0.33% |
| snake_abs_conv | -705 | -0.34% |
| snake_abs_exit | -829 | -0.39% |
| snake_anaconda | -1,121 | -0.55% |
| snake_abs_exit_conv | -1,194 | -0.56% |
| gold | -2,384 | -1.34% |

Average per day so far: unified Rs +643, benchmark Rs +586, snake_abs_exit Rs +388, intramonth Rs +362, snake_abs_exit_conv Rs +329, intraweek Rs +319, oracle Rs +313, snake_viper_wild Rs +258, snake_abs_conv Rs +254, snake_abs Rs +250, random_hold Rs +207, snake_viper_tick Rs +151, snake_anaconda Rs +102, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -677

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.