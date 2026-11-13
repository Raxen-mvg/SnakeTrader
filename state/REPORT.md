# Paper trading report

Updated 2026-11-13 10:22 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,557 | +10.28% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 216,876 | +8.44% | 2 | 50% | 345 |
| intraweek | 216,571 | +8.29% | 30 | 53% | 3,302 |
| snake_abs_exit | 216,543 | +8.27% | 2 | 50% | 345 |
| oracle | 213,939 | +6.97% | 0 | - | 233 |
| snake_abs | 213,093 | +6.55% | 1 | 100% | 255 |
| snake_abs_conv | 212,925 | +6.46% | 1 | 100% | 255 |
| intramonth | 211,129 | +5.56% | 0 | - | 235 |
| random_hold | 207,347 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 206,508 | +3.25% | 14 | 50% | 2,496 |
| snake_anaconda | 205,170 | +2.58% | 3 | 33% | 374 |
| benchmark_smallcap | 203,699 | +1.85% | 0 | - | 237 |
| snake_viper_tick | 202,976 | +1.49% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,292 | -7.85% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,278 (-3.86%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,913 | +0.89% |
| snake_viper_wild | +1,215 | +0.59% |
| snake_viper_tick | +1,194 | +0.59% |
| oracle | +824 | +0.39% |
| benchmark_smallcap | +493 | +0.24% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -140 | -0.06% |
| intramonth | -465 | -0.22% |
| benchmark | -627 | -0.28% |
| random_hold | -707 | -0.34% |
| snake_anaconda | -757 | -0.37% |
| snake_abs_exit | -899 | -0.41% |
| gold | -1,019 | -0.55% |
| snake_abs_exit_conv | -1,798 | -0.82% |
| snake_abs_conv | -2,610 | -1.21% |
| snake_abs | -2,619 | -1.21% |

Average per day so far: unified Rs +623, benchmark Rs +604, snake_abs_exit_conv Rs +563, snake_abs_exit Rs +551, intraweek Rs +502, snake_abs_conv Rs +431, oracle Rs +422, snake_abs Rs +422, intramonth Rs +337, snake_viper_wild Rs +260, random_hold Rs +223, snake_anaconda Rs +185, snake_viper_tick Rs +135, benchmark_smallcap Rs +128, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -476

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.