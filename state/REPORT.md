# Paper trading report

Updated 2026-11-18 14:38 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,247 | +11.12% | 0 | - | 236 |
| benchmark | 220,234 | +10.12% | 0 | - | 237 |
| snake_abs_exit | 214,383 | +7.19% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,708 | +6.35% | 2 | 50% | 345 |
| oracle | 212,152 | +6.08% | 0 | - | 233 |
| intramonth | 211,974 | +5.99% | 0 | - | 235 |
| intraweek | 211,790 | +5.89% | 35 | 54% | 3,851 |
| snake_abs | 209,846 | +4.92% | 1 | 100% | 255 |
| snake_abs_conv | 209,740 | +4.87% | 1 | 100% | 255 |
| random_hold | 206,988 | +3.49% | 10 | 70% | 733 |
| snake_viper_wild | 206,934 | +3.47% | 16 | 50% | 2,827 |
| snake_anaconda | 205,040 | +2.52% | 3 | 33% | 374 |
| snake_viper_tick | 203,400 | +1.70% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,596 | -0.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,239 | -11.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,885 (-4.56%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +1,320 | +0.63% |
| snake_abs | +1,287 | +0.62% |
| snake_abs_exit | +1,241 | +0.58% |
| snake_abs_exit_conv | +1,134 | +0.54% |
| snake_anaconda | +985 | +0.48% |
| unified | +808 | +0.36% |
| intramonth | +431 | +0.20% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -334 | -0.16% |
| benchmark_smallcap | -975 | -0.49% |
| benchmark | -1,369 | -0.62% |
| random_hold | -1,444 | -0.69% |
| intraweek | -1,533 | -0.72% |
| snake_viper_tick | -2,437 | -1.18% |
| snake_viper_wild | -2,481 | -1.19% |
| gold | -3,485 | -1.93% |

Average per day so far: unified Rs +618, benchmark Rs +562, snake_abs_exit Rs +436, snake_abs_exit_conv Rs +385, oracle Rs +338, intramonth Rs +333, intraweek Rs +327, snake_abs_conv Rs +295, snake_abs Rs +290, snake_viper_wild Rs +248, random_hold Rs +194, snake_anaconda Rs +163, snake_viper_tick Rs +136, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -13, snake_nonews Rs -326, snake Rs -347, gold Rs -632

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.