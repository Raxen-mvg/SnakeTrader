# Paper trading report

Updated 2026-11-18 12:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,428 | +11.21% | 0 | - | 236 |
| benchmark | 219,767 | +9.88% | 0 | - | 237 |
| intraweek | 213,051 | +6.53% | 35 | 54% | 3,851 |
| intramonth | 212,494 | +6.25% | 0 | - | 235 |
| snake_abs_exit | 212,304 | +6.15% | 2 | 50% | 345 |
| oracle | 211,505 | +5.75% | 0 | - | 233 |
| snake_abs_exit_conv | 210,444 | +5.22% | 2 | 50% | 345 |
| snake_abs | 207,640 | +3.82% | 1 | 100% | 255 |
| snake_abs_conv | 207,501 | +3.75% | 1 | 100% | 255 |
| random_hold | 207,001 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 206,651 | +3.33% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,123 | +1.56% | 15 | 47% | 2,625 |
| snake_anaconda | 202,460 | +1.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,923 | -0.54% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,976 | -11.51% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,945 (-4.53%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +989 | +0.45% |
| intramonth | +952 | +0.45% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -271 | -0.13% |
| snake_abs_exit | -838 | -0.39% |
| snake_abs | -918 | -0.44% |
| snake_abs_conv | -919 | -0.44% |
| oracle | -981 | -0.46% |
| snake_abs_exit_conv | -1,130 | -0.53% |
| random_hold | -1,431 | -0.69% |
| snake_anaconda | -1,595 | -0.78% |
| benchmark_smallcap | -1,648 | -0.82% |
| benchmark | -1,836 | -0.83% |
| snake_viper_tick | -2,714 | -1.32% |
| snake_viper_wild | -2,764 | -1.32% |
| gold | -3,748 | -2.07% |

Average per day so far: unified Rs +623, benchmark Rs +549, snake_abs_exit Rs +373, intraweek Rs +363, intramonth Rs +347, oracle Rs +320, snake_abs_exit_conv Rs +316, snake_viper_wild Rs +238, snake_abs_conv Rs +227, snake_abs Rs +225, random_hold Rs +194, snake_viper_tick Rs +125, snake_anaconda Rs +79, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.