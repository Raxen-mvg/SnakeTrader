# Paper trading report

Updated 2026-11-26 14:33 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,543 | +12.77% | 0 | - | 237 |
| unified | 223,137 | +11.57% | 0 | - | 236 |
| oracle | 212,702 | +6.35% | 0 | - | 233 |
| intramonth | 210,482 | +5.24% | 0 | - | 235 |
| random_hold | 209,136 | +4.57% | 13 | 69% | 1,037 |
| intraweek | 207,966 | +3.98% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| snake_abs_exit | 200,018 | +0.01% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,390 | -0.30% | 2 | 50% | 345 |
| snake_abs | 197,734 | -1.13% | 1 | 100% | 255 |
| snake_abs_conv | 197,528 | -1.24% | 1 | 100% | 255 |
| snake_viper_wild | 192,225 | -3.89% | 16 | 50% | 2,827 |
| snake_anaconda | 191,412 | -4.29% | 3 | 33% | 374 |
| snake_viper_tick | 188,960 | -5.52% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,323 | -16.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,490 (-5.76%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,962 | +0.99% |
| gold | +1,726 | +1.05% |
| intraweek | +1,223 | +0.59% |
| benchmark | +520 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -357 | -0.17% |
| unified | -963 | -0.43% |
| oracle | -1,093 | -0.51% |
| intramonth | -1,211 | -0.57% |
| snake_abs_exit | -2,237 | -1.11% |
| snake_abs | -2,415 | -1.21% |
| snake_abs_conv | -2,444 | -1.22% |
| snake_abs_exit_conv | -2,586 | -1.28% |
| snake_anaconda | -3,141 | -1.61% |
| snake_viper_tick | -5,217 | -2.69% |
| snake_viper_wild | -5,319 | -2.69% |

Average per day so far: benchmark Rs +623, unified Rs +564, oracle Rs +310, intramonth Rs +256, random_hold Rs +223, intraweek Rs +194, nifty_calls Rs +45, benchmark_smallcap Rs +21, snake_abs_exit Rs +0, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -16, snake_abs Rs -58, snake_abs_conv Rs -65, snake_viper_wild Rs -236, snake_anaconda Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -368, gold Rs -821

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.