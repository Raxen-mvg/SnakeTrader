# Paper trading report

Updated 2026-11-26 14:02 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,985 | +12.49% | 0 | - | 237 |
| unified | 223,220 | +11.61% | 0 | - | 236 |
| oracle | 212,870 | +6.43% | 0 | - | 233 |
| intramonth | 210,443 | +5.22% | 0 | - | 235 |
| random_hold | 209,251 | +4.62% | 13 | 69% | 1,037 |
| intraweek | 207,583 | +3.79% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,033 | +0.02% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,869 | -0.07% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,331 | -0.34% | 2 | 50% | 345 |
| snake_abs | 197,691 | -1.16% | 1 | 100% | 255 |
| snake_abs_conv | 197,484 | -1.26% | 1 | 100% | 255 |
| snake_viper_wild | 192,239 | -3.88% | 16 | 50% | 2,827 |
| snake_anaconda | 191,394 | -4.30% | 3 | 33% | 374 |
| snake_viper_tick | 188,974 | -5.51% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,449 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,463 | +0.89% |
| benchmark_smallcap | +1,222 | +0.61% |
| intraweek | +840 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| benchmark | -38 | -0.02% |
| random_hold | -242 | -0.12% |
| unified | -880 | -0.39% |
| oracle | -925 | -0.43% |
| intramonth | -1,250 | -0.59% |
| snake_abs_exit | -2,387 | -1.18% |
| snake_abs | -2,459 | -1.23% |
| snake_abs_conv | -2,489 | -1.24% |
| snake_abs_exit_conv | -2,645 | -1.31% |
| snake_anaconda | -3,159 | -1.62% |
| snake_viper_tick | -5,203 | -2.68% |
| snake_viper_wild | -5,304 | -2.69% |

Average per day so far: benchmark Rs +609, unified Rs +566, oracle Rs +314, intramonth Rs +255, random_hold Rs +226, intraweek Rs +185, nifty_calls Rs +45, benchmark_smallcap Rs +1, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -3, snake_abs_exit_conv Rs -18, snake_abs Rs -59, snake_abs_conv Rs -66, snake_viper_wild Rs -235, snake_anaconda Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.