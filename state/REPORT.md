# Paper trading report

Updated 2026-11-26 13:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,023 | +12.51% | 0 | - | 237 |
| unified | 223,156 | +11.58% | 0 | - | 236 |
| oracle | 212,700 | +6.35% | 0 | - | 233 |
| intramonth | 210,388 | +5.19% | 0 | - | 235 |
| random_hold | 209,165 | +4.58% | 13 | 69% | 1,037 |
| intraweek | 207,674 | +3.84% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,100 | +0.05% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,862 | -0.07% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,348 | -0.33% | 2 | 50% | 345 |
| snake_abs | 197,725 | -1.14% | 1 | 100% | 255 |
| snake_abs_conv | 197,518 | -1.24% | 1 | 100% | 255 |
| snake_viper_wild | 192,239 | -3.88% | 16 | 50% | 2,827 |
| snake_anaconda | 191,428 | -4.29% | 3 | 33% | 374 |
| snake_viper_tick | 188,974 | -5.51% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,402 (-5.80%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,463 | +0.89% |
| benchmark_smallcap | +1,289 | +0.65% |
| intraweek | +930 | +0.45% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -328 | -0.16% |
| unified | -944 | -0.42% |
| oracle | -1,095 | -0.51% |
| intramonth | -1,305 | -0.62% |
| snake_abs_exit | -2,393 | -1.18% |
| snake_abs | -2,425 | -1.21% |
| snake_abs_conv | -2,454 | -1.23% |
| snake_abs_exit_conv | -2,627 | -1.30% |
| snake_anaconda | -3,125 | -1.61% |
| snake_viper_tick | -5,203 | -2.68% |
| snake_viper_wild | -5,304 | -2.69% |

Average per day so far: benchmark Rs +610, unified Rs +565, oracle Rs +310, intramonth Rs +253, random_hold Rs +224, intraweek Rs +187, nifty_calls Rs +45, benchmark_smallcap Rs +3, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -4, snake_abs_exit_conv Rs -17, snake_abs Rs -58, snake_abs_conv Rs -65, snake_viper_wild Rs -235, snake_anaconda Rs -238, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.