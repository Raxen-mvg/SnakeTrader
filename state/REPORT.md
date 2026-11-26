# Paper trading report

Updated 2026-11-26 09:42 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,656 | +12.33% | 0 | - | 237 |
| unified | 223,884 | +11.94% | 0 | - | 236 |
| oracle | 213,637 | +6.82% | 0 | - | 233 |
| intramonth | 211,525 | +5.76% | 0 | - | 235 |
| random_hold | 210,496 | +5.25% | 13 | 69% | 1,037 |
| intraweek | 207,587 | +3.79% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,693 | +1.85% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,987 | +1.49% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,959 | +0.48% | 1 | 100% | 255 |
| snake_abs_conv | 200,783 | +0.39% | 1 | 100% | 255 |
| benchmark_smallcap | 200,425 | +0.21% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,761 | -1.62% | 16 | 50% | 2,827 |
| snake_anaconda | 195,322 | -2.34% | 3 | 33% | 374 |
| snake_viper_tick | 193,411 | -3.29% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,128 | -16.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,368 (-5.32%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,532 | +1.54% |
| benchmark_smallcap | +1,614 | +0.81% |
| snake_abs_exit | +1,438 | +0.71% |
| snake_abs_exit_conv | +1,012 | +0.50% |
| random_hold | +1,003 | +0.48% |
| intraweek | +844 | +0.41% |
| snake_abs_conv | +811 | +0.41% |
| snake_abs | +809 | +0.40% |
| snake_anaconda | +769 | +0.40% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -158 | -0.07% |
| intramonth | -168 | -0.08% |
| unified | -215 | -0.10% |
| benchmark | -367 | -0.16% |
| snake_viper_tick | -766 | -0.40% |
| snake_viper_wild | -782 | -0.40% |

Average per day so far: benchmark Rs +601, unified Rs +583, oracle Rs +333, intramonth Rs +281, random_hold Rs +256, intraweek Rs +185, snake_abs_exit Rs +97, snake_abs_exit_conv Rs +79, nifty_calls Rs +45, snake_abs Rs +25, snake_abs_conv Rs +21, benchmark_smallcap Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -98, snake_anaconda Rs -130, snake_viper_tick Rs -220, snake_nonews Rs -284, snake Rs -304, gold Rs -802

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.