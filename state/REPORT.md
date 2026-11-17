# Paper trading report

Updated 2026-11-17 11:37 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,143 | +11.07% | 0 | - | 236 |
| benchmark | 221,902 | +10.95% | 0 | - | 237 |
| snake_abs_exit | 215,305 | +7.65% | 2 | 50% | 345 |
| intraweek | 213,942 | +6.97% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,485 | +6.74% | 2 | 50% | 345 |
| oracle | 212,436 | +6.22% | 0 | - | 233 |
| intramonth | 212,150 | +6.08% | 0 | - | 235 |
| snake_abs | 210,079 | +5.04% | 1 | 100% | 255 |
| snake_abs_conv | 209,931 | +4.96% | 1 | 100% | 255 |
| random_hold | 207,898 | +3.95% | 10 | 70% | 733 |
| snake_viper_wild | 207,694 | +3.85% | 14 | 50% | 2,496 |
| snake_anaconda | 205,563 | +2.78% | 3 | 33% | 374 |
| snake_viper_tick | 204,143 | +2.07% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,230 | +1.11% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,316 | -9.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,523 (-4.24%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,676 | +1.27% |
| benchmark | +1,821 | +0.83% |
| snake_viper_wild | +1,549 | +0.75% |
| snake_viper_tick | +1,523 | +0.75% |
| benchmark_smallcap | +1,401 | +0.70% |
| snake_abs_exit | +896 | +0.42% |
| unified | +706 | +0.32% |
| intramonth | +531 | +0.25% |
| snake_anaconda | +460 | +0.22% |
| oracle | +413 | +0.20% |
| gold | +362 | +0.20% |
| snake_abs_exit_conv | +267 | +0.12% |
| random_hold | +105 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -54 | -0.03% |
| snake_abs_conv | -59 | -0.03% |

Average per day so far: unified Rs +633, benchmark Rs +626, snake_abs_exit Rs +478, snake_abs_exit_conv Rs +421, intraweek Rs +398, oracle Rs +355, intramonth Rs +347, snake_abs_conv Rs +310, snake_abs Rs +305, snake_viper_wild Rs +285, random_hold Rs +226, snake_anaconda Rs +185, snake_viper_tick Rs +173, benchmark_smallcap Rs +72, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -534

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.