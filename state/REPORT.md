# Paper trading report

Updated 2026-11-18 11:34 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,254 | +11.63% | 0 | - | 236 |
| benchmark | 220,364 | +10.18% | 0 | - | 237 |
| intraweek | 214,254 | +7.13% | 35 | 54% | 3,851 |
| intramonth | 213,070 | +6.54% | 0 | - | 235 |
| oracle | 212,809 | +6.40% | 0 | - | 233 |
| snake_abs_exit | 212,725 | +6.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 211,151 | +5.58% | 2 | 50% | 345 |
| snake_abs | 208,122 | +4.06% | 1 | 100% | 255 |
| snake_abs_conv | 207,986 | +3.99% | 1 | 100% | 255 |
| random_hold | 207,509 | +3.75% | 10 | 70% | 733 |
| snake_viper_wild | 206,972 | +3.49% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,437 | +1.72% | 15 | 47% | 2,625 |
| snake_anaconda | 203,199 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,596 | -0.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,420 | -11.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,751 (-4.12%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,816 | +0.82% |
| intramonth | +1,528 | +0.72% |
| intraweek | +931 | +0.44% |
| oracle | +322 | +0.15% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -417 | -0.20% |
| snake_abs_exit_conv | -423 | -0.20% |
| snake_abs_conv | -434 | -0.21% |
| snake_abs | -436 | -0.21% |
| snake_anaconda | -856 | -0.42% |
| random_hold | -923 | -0.44% |
| benchmark_smallcap | -975 | -0.49% |
| benchmark | -1,239 | -0.56% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,443 | -1.17% |
| gold | -3,304 | -1.83% |

Average per day so far: unified Rs +646, benchmark Rs +566, intraweek Rs +396, snake_abs_exit Rs +386, intramonth Rs +363, oracle Rs +356, snake_abs_exit_conv Rs +338, snake_viper_wild Rs +249, snake_abs_conv Rs +242, snake_abs Rs +239, random_hold Rs +209, snake_viper_tick Rs +137, snake_anaconda Rs +103, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -13, snake_nonews Rs -326, snake Rs -347, gold Rs -627

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.