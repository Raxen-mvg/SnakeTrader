# Paper trading report

Updated 2026-11-18 10:30 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,381 | +11.19% | 0 | - | 236 |
| benchmark | 220,341 | +10.17% | 0 | - | 237 |
| intraweek | 214,811 | +7.41% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,761 | +6.38% | 2 | 50% | 345 |
| intramonth | 212,318 | +6.16% | 0 | - | 235 |
| oracle | 212,224 | +6.11% | 0 | - | 233 |
| snake_abs_exit_conv | 211,118 | +5.56% | 2 | 50% | 345 |
| snake_abs | 208,120 | +4.06% | 1 | 100% | 255 |
| snake_abs_conv | 207,977 | +3.99% | 1 | 100% | 255 |
| random_hold | 207,436 | +3.72% | 10 | 70% | 733 |
| snake_viper_wild | 207,121 | +3.56% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,583 | +1.79% | 15 | 47% | 2,625 |
| snake_anaconda | 202,942 | +1.47% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,932 | -0.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,535 | -11.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,426 (-4.29%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,488 | +0.70% |
| unified | +942 | +0.43% |
| intramonth | +776 | +0.37% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -262 | -0.12% |
| snake_abs_exit | -381 | -0.18% |
| snake_abs | -438 | -0.21% |
| snake_abs_conv | -442 | -0.21% |
| snake_abs_exit_conv | -455 | -0.21% |
| benchmark_smallcap | -639 | -0.32% |
| random_hold | -996 | -0.48% |
| snake_anaconda | -1,113 | -0.55% |
| benchmark | -1,262 | -0.57% |
| snake_viper_tick | -2,253 | -1.09% |
| snake_viper_wild | -2,294 | -1.09% |
| gold | -3,189 | -1.76% |

Average per day so far: unified Rs +622, benchmark Rs +565, intraweek Rs +411, snake_abs_exit Rs +387, intramonth Rs +342, oracle Rs +340, snake_abs_exit_conv Rs +337, snake_viper_wild Rs +254, snake_abs_conv Rs +242, snake_abs Rs +239, random_hold Rs +207, snake_viper_tick Rs +143, snake_anaconda Rs +95, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -2, snake_nonews Rs -326, snake Rs -347, gold Rs -624

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.