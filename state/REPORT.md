# Paper trading report

Updated 2026-11-16 14:19 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,460 | +10.23% | 0 | - | 236 |
| benchmark | 219,806 | +9.90% | 0 | - | 237 |
| snake_abs_exit | 213,321 | +6.66% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,147 | +6.07% | 2 | 50% | 345 |
| oracle | 211,080 | +5.54% | 0 | - | 233 |
| intramonth | 210,977 | +5.49% | 0 | - | 235 |
| intraweek | 210,619 | +5.31% | 35 | 54% | 3,851 |
| snake_abs | 209,410 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,249 | +4.62% | 1 | 100% | 255 |
| random_hold | 207,697 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 205,458 | +2.73% | 14 | 50% | 2,496 |
| snake_anaconda | 203,813 | +1.91% | 3 | 33% | 374 |
| snake_viper_tick | 201,944 | +0.97% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,133 (-4.93%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,440 | +0.66% |
| intramonth | +920 | +0.44% |
| snake_viper_wild | +701 | +0.34% |
| snake_viper_tick | +689 | +0.34% |
| random_hold | +471 | +0.23% |
| benchmark | +467 | +0.21% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -1,079 | -0.53% |
| oracle | -2,017 | -0.95% |
| benchmark_smallcap | -2,646 | -1.30% |
| gold | -2,663 | -1.45% |
| snake_abs_conv | -3,118 | -1.47% |
| snake_abs | -3,130 | -1.47% |
| snake_abs_exit | -3,664 | -1.69% |
| snake_abs_exit_conv | -4,234 | -1.96% |
| intraweek | -5,526 | -2.56% |

Average per day so far: unified Rs +602, benchmark Rs +583, snake_abs_exit Rs +430, snake_abs_exit_conv Rs +392, oracle Rs +326, intramonth Rs +323, intraweek Rs +312, snake_abs_conv Rs +298, snake_abs Rs +294, random_hold Rs +226, snake_viper_wild Rs +210, snake_anaconda Rs +131, snake_viper_tick Rs +85, nifty_calls Rs +54, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -549

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.