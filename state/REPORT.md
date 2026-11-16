# Paper trading report

Updated 2026-11-16 09:35 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,448 | +10.22% | 0 | - | 237 |
| unified | 219,498 | +9.75% | 0 | - | 236 |
| intraweek | 215,263 | +7.63% | 35 | 54% | 3,851 |
| snake_abs_exit | 214,678 | +7.34% | 2 | 50% | 345 |
| oracle | 213,535 | +6.77% | 0 | - | 233 |
| snake_abs_exit_conv | 213,346 | +6.67% | 2 | 50% | 345 |
| snake_abs | 210,434 | +5.22% | 1 | 100% | 255 |
| intramonth | 210,346 | +5.17% | 0 | - | 235 |
| snake_abs_conv | 210,265 | +5.13% | 1 | 100% | 255 |
| random_hold | 207,688 | +3.84% | 10 | 70% | 733 |
| snake_anaconda | 204,471 | +2.24% | 3 | 33% | 374 |
| snake_viper_wild | 203,850 | +1.93% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,849 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,363 | +0.18% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,401 | -8.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,506 (-4.25%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,109 | +0.51% |
| unified | +478 | +0.22% |
| random_hold | +462 | +0.22% |
| oracle | +437 | +0.20% |
| intramonth | +289 | +0.14% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -421 | -0.20% |
| intraweek | -882 | -0.41% |
| snake_viper_tick | -892 | -0.44% |
| snake_viper_wild | -908 | -0.44% |
| benchmark_smallcap | -1,020 | -0.50% |
| gold | -1,595 | -0.87% |
| snake_abs_conv | -2,101 | -0.99% |
| snake_abs | -2,106 | -0.99% |
| snake_abs_exit | -2,307 | -1.06% |
| snake_abs_exit_conv | -3,035 | -1.40% |

Average per day so far: benchmark Rs +601, unified Rs +573, snake_abs_exit Rs +473, intraweek Rs +449, snake_abs_exit_conv Rs +431, oracle Rs +398, snake_abs_conv Rs +331, snake_abs Rs +326, intramonth Rs +304, random_hold Rs +226, snake_anaconda Rs +154, snake_viper_wild Rs +148, benchmark_smallcap Rs +62, nifty_calls Rs +54, snake_viper_tick Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -518

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.