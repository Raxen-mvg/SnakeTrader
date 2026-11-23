# Paper trading report

Updated 2026-11-23 15:29 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,652 | +12.33% | 0 | - | 236 |
| benchmark | 221,511 | +10.76% | 0 | - | 237 |
| intramonth | 213,468 | +6.73% | 0 | - | 235 |
| oracle | 212,114 | +6.06% | 0 | - | 233 |
| intraweek | 211,379 | +5.69% | 40 | 55% | 4,400 |
| random_hold | 208,297 | +4.15% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,757 | +3.88% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,290 | +3.65% | 2 | 50% | 345 |
| snake_abs | 205,496 | +2.75% | 1 | 100% | 255 |
| snake_abs_conv | 205,351 | +2.67% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,500 | +0.25% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,630 | -0.18% | 0 | - | 237 |
| snake_anaconda | 198,927 | -0.54% | 3 | 33% | 374 |
| snake_viper_tick | 197,082 | -1.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,249 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,418 (-4.79%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,200 | +0.71% |
| snake_abs_exit_conv | +674 | +0.33% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -365 | -0.17% |
| snake_abs | -424 | -0.21% |
| snake_abs_conv | -432 | -0.21% |
| snake_abs_exit | -805 | -0.39% |
| snake_anaconda | -978 | -0.49% |
| benchmark_smallcap | -1,278 | -0.64% |
| unified | -1,530 | -0.68% |
| intramonth | -1,536 | -0.71% |
| snake_viper_tick | -2,290 | -1.15% |
| snake_viper_wild | -2,329 | -1.15% |
| random_hold | -2,463 | -1.17% |
| benchmark | -3,626 | -1.61% |
| intraweek | -4,333 | -2.01% |

Average per day so far: unified Rs +632, benchmark Rs +552, intramonth Rs +345, oracle Rs +311, intraweek Rs +292, snake_abs_exit Rs +215, random_hold Rs +213, snake_abs_exit_conv Rs +203, snake_abs_conv Rs +149, snake_abs Rs +149, nifty_calls Rs +47, snake_viper_wild Rs +16, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_anaconda Rs -32, snake_viper_tick Rs -104, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.