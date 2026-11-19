# Paper trading report

Updated 2026-11-19 14:55 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,414 | +12.21% | 0 | - | 236 |
| benchmark | 222,292 | +11.15% | 0 | - | 237 |
| intramonth | 213,930 | +6.96% | 0 | - | 235 |
| snake_abs_exit | 213,533 | +6.77% | 2 | 50% | 345 |
| intraweek | 212,144 | +6.07% | 35 | 54% | 3,851 |
| oracle | 211,821 | +5.91% | 0 | - | 233 |
| snake_abs_exit_conv | 211,227 | +5.61% | 2 | 50% | 345 |
| snake_abs | 208,838 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,719 | +4.36% | 1 | 100% | 255 |
| random_hold | 208,286 | +4.14% | 10 | 70% | 733 |
| snake_viper_wild | 207,667 | +3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,118 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,504 | +1.75% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,822 | -12.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,755 (-4.12%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,074 | +1.04% |
| benchmark | +1,997 | +0.91% |
| unified | +1,803 | +0.81% |
| intramonth | +1,656 | +0.78% |
| random_hold | +1,354 | +0.65% |
| oracle | +1,025 | +0.49% |
| snake_viper_wild | +627 | +0.30% |
| snake_viper_tick | +615 | +0.30% |
| intraweek | +305 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -498 | -0.23% |
| snake_abs | -598 | -0.29% |
| snake_abs_conv | -606 | -0.29% |
| snake_anaconda | -897 | -0.44% |
| snake_abs_exit_conv | -1,157 | -0.55% |
| gold | -2,499 | -1.41% |

Average per day so far: unified Rs +660, benchmark Rs +602, snake_abs_exit Rs +398, intramonth Rs +376, snake_abs_exit_conv Rs +330, intraweek Rs +328, oracle Rs +319, snake_viper_wild Rs +264, snake_abs_conv Rs +256, snake_abs Rs +253, random_hold Rs +224, snake_viper_tick Rs +158, snake_anaconda Rs +110, nifty_calls Rs +50, benchmark_smallcap Rs +42, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.