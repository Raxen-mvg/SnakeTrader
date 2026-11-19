# Paper trading report

Updated 2026-11-19 12:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,861 | +11.93% | 0 | - | 236 |
| benchmark | 221,458 | +10.73% | 0 | - | 237 |
| intramonth | 213,387 | +6.69% | 0 | - | 235 |
| snake_abs_exit | 213,096 | +6.55% | 2 | 50% | 345 |
| intraweek | 211,485 | +5.74% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,250 | +5.62% | 2 | 50% | 345 |
| oracle | 210,969 | +5.49% | 0 | - | 233 |
| snake_abs | 208,850 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,723 | +4.36% | 1 | 100% | 255 |
| snake_viper_wild | 207,667 | +3.83% | 16 | 50% | 2,827 |
| random_hold | 207,541 | +3.77% | 10 | 70% | 733 |
| snake_viper_tick | 204,118 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,119 | +1.56% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,871 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,172 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,278 | +0.64% |
| unified | +1,249 | +0.56% |
| benchmark | +1,163 | +0.53% |
| intramonth | +1,114 | +0.53% |
| snake_viper_wild | +627 | +0.30% |
| snake_viper_tick | +615 | +0.30% |
| random_hold | +609 | +0.29% |
| oracle | +173 | +0.08% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -354 | -0.17% |
| snake_abs | -586 | -0.28% |
| snake_abs_conv | -602 | -0.29% |
| snake_abs_exit | -936 | -0.44% |
| snake_abs_exit_conv | -1,133 | -0.53% |
| snake_anaconda | -1,282 | -0.63% |
| gold | -2,450 | -1.38% |

Average per day so far: unified Rs +645, benchmark Rs +580, snake_abs_exit Rs +385, intramonth Rs +362, snake_abs_exit_conv Rs +331, intraweek Rs +310, oracle Rs +296, snake_viper_wild Rs +264, snake_abs_conv Rs +257, snake_abs Rs +253, random_hold Rs +204, snake_viper_tick Rs +158, snake_anaconda Rs +97, nifty_calls Rs +50, benchmark_smallcap Rs +18, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.