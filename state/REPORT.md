# Paper trading report

Updated 2026-11-23 11:41 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,371 | +12.19% | 0 | - | 236 |
| benchmark | 223,133 | +11.57% | 0 | - | 237 |
| intraweek | 213,023 | +6.51% | 40 | 55% | 4,400 |
| intramonth | 212,455 | +6.23% | 0 | - | 235 |
| oracle | 211,377 | +5.69% | 0 | - | 233 |
| random_hold | 210,158 | +5.08% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,396 | +3.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,327 | +3.16% | 2 | 50% | 345 |
| snake_abs | 204,831 | +2.42% | 1 | 100% | 255 |
| snake_abs_conv | 204,666 | +2.33% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,532 | +0.77% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,630 | -0.18% | 0 | - | 237 |
| snake_anaconda | 198,298 | -0.85% | 3 | 33% | 374 |
| snake_viper_tick | 198,092 | -0.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,907 | -15.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,511 (-4.74%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,858 | +1.10% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -290 | -0.14% |
| random_hold | -602 | -0.28% |
| snake_abs | -1,089 | -0.53% |
| oracle | -1,101 | -0.52% |
| snake_abs_conv | -1,117 | -0.54% |
| snake_abs_exit | -1,167 | -0.56% |
| benchmark_smallcap | -1,278 | -0.64% |
| snake_viper_tick | -1,280 | -0.64% |
| snake_viper_wild | -1,297 | -0.64% |
| snake_anaconda | -1,607 | -0.80% |
| unified | -1,811 | -0.80% |
| benchmark | -2,004 | -0.89% |
| intramonth | -2,549 | -1.19% |
| intraweek | -2,689 | -1.25% |

Average per day so far: unified Rs +625, benchmark Rs +593, intraweek Rs +334, intramonth Rs +319, oracle Rs +292, random_hold Rs +260, snake_abs_exit Rs +205, snake_abs_exit_conv Rs +176, snake_abs Rs +131, snake_abs_conv Rs +130, snake_viper_wild Rs +49, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_anaconda Rs -50, snake_viper_tick Rs -68, snake_nonews Rs -300, snake Rs -320, gold Rs -772

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.