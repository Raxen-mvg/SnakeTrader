# Paper trading report

Updated 2026-11-25 15:23 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,893 | +12.45% | 0 | - | 237 |
| unified | 224,079 | +12.04% | 0 | - | 236 |
| oracle | 214,010 | +7.00% | 0 | - | 233 |
| intramonth | 211,816 | +5.91% | 0 | - | 235 |
| random_hold | 209,548 | +4.77% | 12 | 75% | 1,009 |
| intraweek | 206,581 | +3.29% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,091 | +1.05% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,787 | +0.89% | 2 | 50% | 345 |
| snake_abs | 200,104 | +0.05% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,924 | -0.04% | 1 | 100% | 255 |
| benchmark_smallcap | 198,766 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 197,337 | -1.33% | 16 | 50% | 2,827 |
| snake_anaconda | 194,468 | -2.77% | 3 | 33% | 374 |
| snake_viper_tick | 193,975 | -3.01% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,432 | -17.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,067 (-5.47%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,420 | +1.54% |
| oracle | +1,667 | +0.79% |
| random_hold | +1,121 | +0.54% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -206 | -0.09% |
| benchmark_smallcap | -213 | -0.11% |
| intramonth | -935 | -0.44% |
| snake_viper_tick | -3,718 | -1.88% |
| snake_viper_wild | -3,787 | -1.88% |
| snake_anaconda | -4,235 | -2.13% |
| gold | -4,998 | -2.95% |
| intraweek | -5,038 | -2.38% |
| snake_abs_exit_conv | -5,259 | -2.54% |
| snake_abs | -5,357 | -2.61% |
| snake_abs_conv | -5,378 | -2.62% |
| snake_abs_exit | -5,404 | -2.60% |

Average per day so far: benchmark Rs +622, unified Rs +602, oracle Rs +350, intramonth Rs +295, random_hold Rs +239, intraweek Rs +165, snake_abs_exit Rs +57, snake_abs_exit_conv Rs +48, nifty_calls Rs +46, snake_abs Rs +3, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -2, benchmark_smallcap Rs -34, snake_viper_wild Rs -83, snake_anaconda Rs -158, snake_viper_tick Rs -208, snake_nonews Rs -292, snake Rs -311, gold Rs -889

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.