# Paper trading report

Updated 2026-11-18 12:46 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,166 | +11.08% | 0 | - | 236 |
| benchmark | 219,836 | +9.92% | 0 | - | 237 |
| intraweek | 213,061 | +6.53% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,484 | +6.24% | 2 | 50% | 345 |
| intramonth | 212,306 | +6.15% | 0 | - | 235 |
| oracle | 211,633 | +5.82% | 0 | - | 233 |
| snake_abs_exit_conv | 210,718 | +5.36% | 2 | 50% | 345 |
| snake_abs | 207,771 | +3.89% | 1 | 100% | 255 |
| snake_abs_conv | 207,633 | +3.82% | 1 | 100% | 255 |
| random_hold | 206,931 | +3.47% | 10 | 70% | 733 |
| snake_viper_wild | 206,795 | +3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,264 | +1.63% | 15 | 47% | 2,625 |
| snake_anaconda | 202,677 | +1.34% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,091 | -0.45% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,943 | -11.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,903 (-4.55%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +764 | +0.36% |
| unified | +728 | +0.33% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraweek | -262 | -0.12% |
| snake_abs_exit | -658 | -0.31% |
| snake_abs_conv | -786 | -0.38% |
| snake_abs | -787 | -0.38% |
| oracle | -853 | -0.40% |
| snake_abs_exit_conv | -856 | -0.41% |
| snake_anaconda | -1,378 | -0.68% |
| benchmark_smallcap | -1,480 | -0.74% |
| random_hold | -1,501 | -0.72% |
| benchmark | -1,767 | -0.80% |
| snake_viper_tick | -2,573 | -1.25% |
| snake_viper_wild | -2,620 | -1.25% |
| gold | -3,781 | -2.09% |

Average per day so far: unified Rs +616, benchmark Rs +551, snake_abs_exit Rs +378, intraweek Rs +363, intramonth Rs +342, snake_abs_exit_conv Rs +325, oracle Rs +323, snake_viper_wild Rs +243, snake_abs_conv Rs +231, snake_abs Rs +229, random_hold Rs +193, snake_viper_tick Rs +131, snake_anaconda Rs +86, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -28, snake_nonews Rs -326, snake Rs -347, gold Rs -640

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.