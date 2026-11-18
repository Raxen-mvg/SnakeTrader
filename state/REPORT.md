# Paper trading report

Updated 2026-11-18 13:34 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,964 | +11.48% | 0 | - | 236 |
| benchmark | 219,737 | +9.87% | 0 | - | 237 |
| intramonth | 212,740 | +6.37% | 0 | - | 235 |
| snake_abs_exit | 212,342 | +6.17% | 2 | 50% | 345 |
| oracle | 212,310 | +6.16% | 0 | - | 233 |
| intraweek | 212,254 | +6.13% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,665 | +5.33% | 2 | 50% | 345 |
| snake_abs | 207,638 | +3.82% | 1 | 100% | 255 |
| snake_abs_conv | 207,502 | +3.75% | 1 | 100% | 255 |
| random_hold | 207,007 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 206,497 | +3.25% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,972 | +1.49% | 15 | 47% | 2,625 |
| snake_anaconda | 202,772 | +1.39% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,617 | -11.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,150 (-4.42%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,525 | +0.69% |
| intramonth | +1,198 | +0.57% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -176 | -0.08% |
| snake_abs_exit | -800 | -0.38% |
| snake_abs_exit_conv | -908 | -0.43% |
| snake_abs_conv | -917 | -0.44% |
| snake_abs | -921 | -0.44% |
| intraweek | -1,068 | -0.50% |
| snake_anaconda | -1,283 | -0.63% |
| random_hold | -1,425 | -0.68% |
| benchmark_smallcap | -1,469 | -0.73% |
| benchmark | -1,867 | -0.84% |
| snake_viper_tick | -2,864 | -1.39% |
| snake_viper_wild | -2,918 | -1.39% |
| gold | -3,107 | -1.72% |

Average per day so far: unified Rs +638, benchmark Rs +548, snake_abs_exit Rs +374, intramonth Rs +354, oracle Rs +342, intraweek Rs +340, snake_abs_exit_conv Rs +323, snake_viper_wild Rs +232, snake_abs_conv Rs +227, snake_abs Rs +225, random_hold Rs +195, snake_viper_tick Rs +119, snake_anaconda Rs +89, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -28, snake_nonews Rs -326, snake Rs -347, gold Rs -622

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.