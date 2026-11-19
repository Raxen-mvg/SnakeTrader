# Paper trading report

Updated 2026-11-19 14:16 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,498 | +11.75% | 0 | - | 236 |
| benchmark | 222,215 | +11.11% | 0 | - | 237 |
| snake_abs_exit | 213,196 | +6.60% | 2 | 50% | 345 |
| intramonth | 213,144 | +6.57% | 0 | - | 235 |
| intraweek | 211,899 | +5.95% | 35 | 54% | 3,851 |
| oracle | 211,336 | +5.67% | 0 | - | 233 |
| snake_abs_exit_conv | 210,917 | +5.46% | 2 | 50% | 345 |
| snake_abs | 208,833 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,706 | +4.35% | 1 | 100% | 255 |
| random_hold | 207,955 | +3.98% | 10 | 70% | 733 |
| snake_viper_wild | 207,652 | +3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,104 | +2.05% | 15 | 47% | 2,625 |
| snake_anaconda | 203,319 | +1.66% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,904 | -12.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,221 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,920 | +0.87% |
| benchmark_smallcap | +1,345 | +0.68% |
| random_hold | +1,022 | +0.49% |
| unified | +886 | +0.40% |
| intramonth | +871 | +0.41% |
| snake_viper_wild | +613 | +0.30% |
| snake_viper_tick | +601 | +0.29% |
| oracle | +540 | +0.26% |
| intraweek | +60 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -604 | -0.29% |
| snake_abs_conv | -619 | -0.29% |
| snake_abs_exit | -836 | -0.39% |
| snake_anaconda | -1,082 | -0.53% |
| snake_abs_exit_conv | -1,467 | -0.69% |
| gold | -2,417 | -1.36% |

Average per day so far: unified Rs +635, benchmark Rs +600, snake_abs_exit Rs +388, intramonth Rs +355, intraweek Rs +322, snake_abs_exit_conv Rs +321, oracle Rs +306, snake_viper_wild Rs +264, snake_abs_conv Rs +256, snake_abs Rs +252, random_hold Rs +215, snake_viper_tick Rs +158, snake_anaconda Rs +104, nifty_calls Rs +50, benchmark_smallcap Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -678

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.