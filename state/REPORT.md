# Paper trading report

Updated 2026-11-19 15:18 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,486 | +12.24% | 0 | - | 236 |
| benchmark | 222,452 | +11.23% | 0 | - | 237 |
| intramonth | 213,917 | +6.96% | 0 | - | 235 |
| snake_abs_exit | 213,246 | +6.62% | 2 | 50% | 345 |
| intraweek | 212,814 | +6.41% | 35 | 54% | 3,851 |
| oracle | 212,008 | +6.00% | 0 | - | 233 |
| snake_abs_exit_conv | 210,969 | +5.49% | 2 | 50% | 345 |
| snake_abs | 208,793 | +4.40% | 1 | 100% | 255 |
| snake_abs_conv | 208,673 | +4.34% | 1 | 100% | 255 |
| random_hold | 208,479 | +4.24% | 10 | 70% | 733 |
| snake_viper_wild | 207,523 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,977 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,318 | +1.66% | 3 | 33% | 374 |
| benchmark_smallcap | 201,883 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,707 | -12.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,923 (-4.04%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,556 | +1.28% |
| benchmark | +2,157 | +0.98% |
| unified | +1,875 | +0.84% |
| intramonth | +1,644 | +0.77% |
| random_hold | +1,546 | +0.75% |
| oracle | +1,212 | +0.57% |
| intraweek | +975 | +0.46% |
| snake_viper_wild | +483 | +0.23% |
| snake_viper_tick | +474 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -644 | -0.31% |
| snake_abs_conv | -652 | -0.31% |
| snake_abs_exit | -786 | -0.37% |
| snake_anaconda | -1,083 | -0.53% |
| snake_abs_exit_conv | -1,414 | -0.67% |
| gold | -2,614 | -1.47% |

Average per day so far: unified Rs +662, benchmark Rs +607, snake_abs_exit Rs +390, intramonth Rs +376, intraweek Rs +346, oracle Rs +325, snake_abs_exit_conv Rs +323, snake_viper_wild Rs +259, snake_abs_conv Rs +255, snake_abs Rs +251, random_hold Rs +229, snake_viper_tick Rs +153, snake_anaconda Rs +104, benchmark_smallcap Rs +57, nifty_calls Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -684

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.