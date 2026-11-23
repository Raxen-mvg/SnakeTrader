# Paper trading report

Updated 2026-11-23 10:06 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,285 | +12.64% | 0 | - | 236 |
| benchmark | 223,676 | +11.84% | 0 | - | 237 |
| intraweek | 213,058 | +6.53% | 40 | 55% | 4,400 |
| intramonth | 213,002 | +6.50% | 0 | - | 235 |
| oracle | 211,279 | +5.64% | 0 | - | 233 |
| random_hold | 210,157 | +5.08% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,158 | +4.08% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,599 | +3.30% | 2 | 50% | 345 |
| snake_abs | 205,455 | +2.73% | 1 | 100% | 255 |
| snake_abs_conv | 205,308 | +2.65% | 1 | 100% | 255 |
| snake_viper_wild | 203,717 | +1.86% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,241 | +0.12% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,831 | -0.08% | 0 | - | 237 |
| snake_anaconda | 199,322 | -0.34% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,265 | -15.37% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,864 (-4.57%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,217 | +0.72% |
| snake_viper_wild | +888 | +0.44% |
| snake_viper_tick | +870 | +0.44% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit_conv | -17 | -0.01% |
| snake_abs_exit | -404 | -0.19% |
| snake_abs | -465 | -0.23% |
| snake_abs_conv | -475 | -0.23% |
| snake_anaconda | -583 | -0.29% |
| random_hold | -602 | -0.29% |
| unified | -897 | -0.40% |
| benchmark_smallcap | -1,076 | -0.54% |
| oracle | -1,199 | -0.56% |
| benchmark | -1,461 | -0.65% |
| intramonth | -2,002 | -0.93% |
| intraweek | -2,654 | -1.23% |

Average per day so far: unified Rs +648, benchmark Rs +607, intraweek Rs +335, intramonth Rs +333, oracle Rs +289, random_hold Rs +260, snake_abs_exit Rs +227, snake_abs_exit_conv Rs +183, snake_abs_conv Rs +147, snake_abs Rs +147, snake_viper_wild Rs +120, nifty_calls Rs +47, snake_viper_tick Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -5, snake_anaconda Rs -20, snake_nonews Rs -300, snake Rs -320, gold Rs -788

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.