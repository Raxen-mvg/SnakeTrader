# Paper trading report

Updated 2026-11-19 13:28 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,828 | +11.91% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,430 | +6.71% | 0 | - | 235 |
| snake_abs_exit | 213,005 | +6.50% | 2 | 50% | 345 |
| intraweek | 211,802 | +5.90% | 35 | 54% | 3,851 |
| oracle | 211,539 | +5.77% | 0 | - | 233 |
| snake_abs_exit_conv | 211,087 | +5.54% | 2 | 50% | 345 |
| snake_abs | 208,614 | +4.31% | 1 | 100% | 255 |
| snake_abs_conv | 208,491 | +4.25% | 1 | 100% | 255 |
| random_hold | 207,601 | +3.80% | 10 | 70% | 733 |
| snake_viper_wild | 207,480 | +3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,935 | +1.97% | 15 | 47% | 2,625 |
| snake_anaconda | 203,153 | +1.58% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,135 | -12.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,332 (-4.33%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,308 | +0.59% |
| benchmark_smallcap | +1,289 | +0.65% |
| unified | +1,216 | +0.55% |
| intramonth | +1,156 | +0.55% |
| oracle | +743 | +0.35% |
| random_hold | +669 | +0.32% |
| snake_viper_wild | +440 | +0.21% |
| snake_viper_tick | +431 | +0.21% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -37 | -0.02% |
| snake_abs | -822 | -0.39% |
| snake_abs_conv | -834 | -0.40% |
| snake_abs_exit | -1,027 | -0.48% |
| snake_anaconda | -1,248 | -0.61% |
| snake_abs_exit_conv | -1,296 | -0.61% |
| gold | -2,187 | -1.23% |

Average per day so far: unified Rs +644, benchmark Rs +584, snake_abs_exit Rs +382, intramonth Rs +363, snake_abs_exit_conv Rs +326, intraweek Rs +319, oracle Rs +312, snake_viper_wild Rs +258, snake_abs_conv Rs +250, snake_abs Rs +246, random_hold Rs +205, snake_viper_tick Rs +151, snake_anaconda Rs +99, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.