# Paper trading report

Updated 2026-11-13 10:25 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,480 | +10.24% | 0 | - | 236 |
| benchmark | 219,989 | +9.99% | 0 | - | 237 |
| snake_abs_exit_conv | 216,931 | +8.47% | 2 | 50% | 345 |
| snake_abs_exit | 216,542 | +8.27% | 2 | 50% | 345 |
| intraweek | 216,500 | +8.25% | 30 | 53% | 3,302 |
| oracle | 214,018 | +7.01% | 0 | - | 233 |
| snake_abs | 213,303 | +6.65% | 1 | 100% | 255 |
| snake_abs_conv | 213,133 | +6.57% | 1 | 100% | 255 |
| intramonth | 211,224 | +5.61% | 0 | - | 235 |
| random_hold | 207,364 | +3.68% | 10 | 70% | 733 |
| snake_viper_wild | 206,508 | +3.25% | 14 | 50% | 2,496 |
| snake_anaconda | 205,250 | +2.62% | 3 | 33% | 374 |
| benchmark_smallcap | 203,587 | +1.79% | 0 | - | 237 |
| snake_viper_tick | 202,976 | +1.49% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,226 | -7.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,286 (-3.86%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,842 | +0.86% |
| snake_viper_wild | +1,215 | +0.59% |
| snake_viper_tick | +1,194 | +0.59% |
| oracle | +903 | +0.42% |
| benchmark_smallcap | +381 | +0.19% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -216 | -0.10% |
| intramonth | -369 | -0.17% |
| benchmark | -558 | -0.25% |
| snake_anaconda | -678 | -0.33% |
| random_hold | -690 | -0.33% |
| snake_abs_exit | -901 | -0.41% |
| gold | -1,085 | -0.59% |
| snake_abs_exit_conv | -1,743 | -0.80% |
| snake_abs_conv | -2,402 | -1.11% |
| snake_abs | -2,408 | -1.12% |

Average per day so far: unified Rs +621, benchmark Rs +606, snake_abs_exit_conv Rs +564, snake_abs_exit Rs +551, intraweek Rs +500, snake_abs_conv Rs +438, snake_abs Rs +429, oracle Rs +425, intramonth Rs +340, snake_viper_wild Rs +260, random_hold Rs +223, snake_anaconda Rs +187, snake_viper_tick Rs +135, benchmark_smallcap Rs +124, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -478

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.