# Paper trading report

Updated 2026-11-25 14:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,770 | +12.38% | 0 | - | 237 |
| unified | 224,522 | +12.26% | 0 | - | 236 |
| oracle | 212,868 | +6.43% | 0 | - | 233 |
| intramonth | 211,929 | +5.96% | 0 | - | 235 |
| random_hold | 209,780 | +4.89% | 12 | 75% | 1,009 |
| intraweek | 207,165 | +3.58% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,221 | +1.11% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,897 | +0.95% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,417 | +0.21% | 1 | 100% | 255 |
| snake_abs_conv | 200,231 | +0.12% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,991 | -0.51% | 0 | - | 237 |
| snake_viper_wild | 197,649 | -1.18% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,280 | -2.86% | 15 | 47% | 2,625 |
| snake_anaconda | 193,968 | -3.02% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,073 | -17.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,099 (-5.45%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,297 | +1.49% |
| random_hold | +1,353 | +0.65% |
| oracle | +525 | +0.25% |
| unified | +237 | +0.11% |
| benchmark_smallcap | +11 | +0.01% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -822 | -0.39% |
| snake_viper_tick | -3,412 | -1.73% |
| snake_viper_wild | -3,475 | -1.73% |
| gold | -4,357 | -2.57% |
| intraweek | -4,454 | -2.10% |
| snake_anaconda | -4,735 | -2.38% |
| snake_abs | -5,043 | -2.46% |
| snake_abs_conv | -5,072 | -2.47% |
| snake_abs_exit_conv | -5,149 | -2.49% |
| snake_abs_exit | -5,274 | -2.54% |

Average per day so far: benchmark Rs +619, unified Rs +613, oracle Rs +322, intramonth Rs +298, random_hold Rs +244, intraweek Rs +179, snake_abs_exit Rs +60, snake_abs_exit_conv Rs +51, nifty_calls Rs +46, snake_abs Rs +11, snake_abs_conv Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -28, snake_viper_wild Rs -73, snake_anaconda Rs -172, snake_viper_tick Rs -197, snake_nonews Rs -292, snake Rs -311, gold Rs -873

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.