# Paper trading report

Updated 2026-11-26 11:43 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 223,177 | +11.59% | 0 | - | 236 |
| oracle | 213,066 | +6.53% | 0 | - | 233 |
| intramonth | 210,432 | +5.22% | 0 | - | 235 |
| random_hold | 209,737 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 208,649 | +4.33% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 200,702 | +0.35% | 2 | 50% | 345 |
| benchmark_smallcap | 200,504 | +0.25% | 0 | - | 237 |
| snake_abs_exit_conv | 200,142 | +0.07% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,428 | -0.79% | 1 | 100% | 255 |
| snake_abs_conv | 198,238 | -0.88% | 1 | 100% | 255 |
| snake_anaconda | 192,309 | -3.85% | 3 | 33% | 374 |
| snake_viper_wild | 192,023 | -3.99% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,763 | -5.62% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,306 | -16.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,757 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,906 | +0.92% |
| gold | +1,710 | +1.04% |
| benchmark_smallcap | +1,693 | +0.85% |
| benchmark | +635 | +0.28% |
| random_hold | +244 | +0.12% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -729 | -0.34% |
| unified | -922 | -0.41% |
| intramonth | -1,261 | -0.60% |
| snake_abs_exit | -1,553 | -0.77% |
| snake_abs | -1,721 | -0.86% |
| snake_abs_conv | -1,735 | -0.87% |
| snake_abs_exit_conv | -1,834 | -0.91% |
| snake_anaconda | -2,244 | -1.15% |
| snake_viper_tick | -5,414 | -2.79% |
| snake_viper_wild | -5,520 | -2.79% |

Average per day so far: benchmark Rs +626, unified Rs +565, oracle Rs +319, intramonth Rs +254, random_hold Rs +237, intraweek Rs +211, nifty_calls Rs +45, snake_abs_exit Rs +18, benchmark_smallcap Rs +14, snake_abs_exit_conv Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -40, snake_abs_conv Rs -46, snake_anaconda Rs -214, snake_viper_wild Rs -242, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -375, gold Rs -822

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.