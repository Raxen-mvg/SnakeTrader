# Paper trading report

Updated 2026-11-25 12:34 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,257 | +12.63% | 0 | - | 236 |
| benchmark | 225,199 | +12.60% | 0 | - | 237 |
| intramonth | 213,327 | +6.66% | 0 | - | 235 |
| oracle | 212,697 | +6.35% | 0 | - | 233 |
| random_hold | 209,981 | +4.99% | 12 | 75% | 1,009 |
| intraweek | 208,236 | +4.12% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,303 | +1.15% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,918 | +0.96% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,806 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,623 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,428 | -0.29% | 0 | - | 237 |
| snake_viper_wild | 196,958 | -1.52% | 16 | 50% | 2,827 |
| snake_anaconda | 194,000 | -3.00% | 3 | 33% | 374 |
| snake_viper_tick | 193,603 | -3.20% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,498 | -17.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,550 (-5.23%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,726 | +1.68% |
| random_hold | +1,554 | +0.75% |
| unified | +972 | +0.43% |
| intramonth | +575 | +0.27% |
| benchmark_smallcap | +448 | +0.23% |
| oracle | +355 | +0.17% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,383 | -1.60% |
| snake_viper_tick | -4,089 | -2.07% |
| snake_viper_wild | -4,167 | -2.07% |
| snake_abs | -4,654 | -2.27% |
| snake_abs_conv | -4,680 | -2.28% |
| snake_anaconda | -4,703 | -2.37% |
| gold | -4,932 | -2.91% |
| snake_abs_exit_conv | -5,128 | -2.48% |
| snake_abs_exit | -5,192 | -2.50% |

Average per day so far: unified Rs +631, benchmark Rs +630, intramonth Rs +333, oracle Rs +317, random_hold Rs +250, intraweek Rs +206, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +52, nifty_calls Rs +46, snake_abs Rs +21, snake_abs_conv Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -95, snake_anaconda Rs -171, snake_viper_tick Rs -221, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.