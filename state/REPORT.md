# Paper trading report

Updated 2026-11-19 14:49 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,243 | +12.12% | 0 | - | 236 |
| benchmark | 222,231 | +11.12% | 0 | - | 237 |
| snake_abs_exit | 213,763 | +6.88% | 2 | 50% | 345 |
| intramonth | 213,744 | +6.87% | 0 | - | 235 |
| intraweek | 211,872 | +5.94% | 35 | 54% | 3,851 |
| oracle | 211,678 | +5.84% | 0 | - | 233 |
| snake_abs_exit_conv | 211,400 | +5.70% | 2 | 50% | 345 |
| snake_abs | 209,187 | +4.59% | 1 | 100% | 255 |
| snake_abs_conv | 209,070 | +4.54% | 1 | 100% | 255 |
| random_hold | 208,311 | +4.16% | 10 | 70% | 733 |
| snake_viper_wild | 207,691 | +3.85% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,141 | +2.07% | 15 | 47% | 2,625 |
| snake_anaconda | 203,713 | +1.86% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,008 | +0.50% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,970 | -12.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,612 (-4.19%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,935 | +0.88% |
| benchmark_smallcap | +1,682 | +0.84% |
| unified | +1,632 | +0.73% |
| intramonth | +1,470 | +0.69% |
| random_hold | +1,379 | +0.67% |
| oracle | +882 | +0.42% |
| snake_viper_wild | +651 | +0.32% |
| snake_viper_tick | +638 | +0.31% |
| intraweek | +32 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -250 | -0.12% |
| snake_abs_conv | -255 | -0.12% |
| snake_abs_exit | -269 | -0.13% |
| snake_anaconda | -688 | -0.34% |
| snake_abs_exit_conv | -983 | -0.46% |
| gold | -2,351 | -1.33% |

Average per day so far: unified Rs +655, benchmark Rs +601, snake_abs_exit Rs +405, intramonth Rs +371, snake_abs_exit_conv Rs +335, intraweek Rs +321, oracle Rs +316, snake_abs_conv Rs +267, snake_viper_wild Rs +265, snake_abs Rs +262, random_hold Rs +225, snake_viper_tick Rs +159, snake_anaconda Rs +116, nifty_calls Rs +50, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.