# Paper trading report

Updated 2026-11-25 09:56 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,468 | +12.73% | 0 | - | 236 |
| benchmark | 224,816 | +12.41% | 0 | - | 237 |
| oracle | 213,026 | +6.51% | 0 | - | 233 |
| intramonth | 212,954 | +6.48% | 0 | - | 235 |
| intraweek | 209,830 | +4.92% | 40 | 55% | 4,400 |
| random_hold | 209,820 | +4.91% | 12 | 75% | 1,009 |
| snake_abs_exit | 201,963 | +0.98% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,352 | +0.68% | 2 | 50% | 345 |
| snake_abs | 200,888 | +0.44% | 1 | 100% | 255 |
| snake_abs_conv | 200,692 | +0.35% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,562 | -0.22% | 0 | - | 237 |
| snake_viper_wild | 198,820 | -0.59% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,437 | -2.28% | 15 | 47% | 2,625 |
| snake_anaconda | 193,696 | -3.15% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,583 | -17.21% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,728 (-5.14%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,343 | +1.51% |
| random_hold | +1,393 | +0.67% |
| unified | +1,182 | +0.53% |
| oracle | +684 | +0.32% |
| benchmark_smallcap | +583 | +0.29% |
| intramonth | +203 | +0.10% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -1,789 | -0.84% |
| snake_viper_tick | -2,256 | -1.14% |
| snake_viper_wild | -2,304 | -1.15% |
| gold | -3,847 | -2.27% |
| snake_abs | -4,573 | -2.23% |
| snake_abs_conv | -4,611 | -2.25% |
| snake_anaconda | -5,007 | -2.52% |
| snake_abs_exit | -5,532 | -2.67% |
| snake_abs_exit_conv | -5,694 | -2.75% |

Average per day so far: unified Rs +637, benchmark Rs +620, oracle Rs +326, intramonth Rs +324, intraweek Rs +246, random_hold Rs +245, snake_abs_exit Rs +53, nifty_calls Rs +46, snake_abs_exit_conv Rs +37, snake_abs Rs +23, snake_abs_conv Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -12, snake_viper_wild Rs -37, snake_viper_tick Rs -157, snake_anaconda Rs -180, snake_nonews Rs -292, snake Rs -311, gold Rs -860

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.