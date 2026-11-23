# Paper trading report

Updated 2026-11-23 09:17 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,493 | +13.25% | 0 | - | 236 |
| benchmark | 225,780 | +12.89% | 0 | - | 237 |
| intraweek | 216,766 | +8.38% | 35 | 54% | 3,851 |
| intramonth | 214,788 | +7.39% | 0 | - | 235 |
| oracle | 213,078 | +6.54% | 0 | - | 233 |
| random_hold | 212,428 | +6.21% | 11 | 73% | 979 |
| snake_abs_exit | 208,818 | +4.41% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,211 | +3.61% | 2 | 50% | 345 |
| snake_abs | 205,785 | +2.89% | 1 | 100% | 255 |
| snake_abs_conv | 205,647 | +2.82% | 1 | 100% | 255 |
| snake_viper_wild | 203,847 | +1.92% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| snake_viper_tick | 200,368 | +0.18% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,893 | -0.05% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,690 | -15.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,469 (-3.77%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| random_hold | +1,669 | +0.79% |
| intraweek | +1,054 | +0.49% |
| snake_viper_wild | +1,018 | +0.50% |
| snake_viper_tick | +996 | +0.50% |
| benchmark | +643 | +0.28% |
| gold | +641 | +0.38% |
| oracle | +599 | +0.28% |
| snake_abs_exit_conv | +595 | +0.29% |
| benchmark_smallcap | +560 | +0.28% |
| unified | +311 | +0.14% |
| snake_abs_exit | +256 | +0.12% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_anaconda | -12 | -0.01% |
| snake_abs | -135 | -0.07% |
| snake_abs_conv | -136 | -0.07% |
| intramonth | -216 | -0.10% |

Average per day so far: unified Rs +679, benchmark Rs +661, intraweek Rs +430, intramonth Rs +379, oracle Rs +335, random_hold Rs +319, snake_abs_exit Rs +245, snake_abs_exit_conv Rs +200, snake_abs_conv Rs +157, snake_abs Rs +156, snake_viper_wild Rs +124, nifty_calls Rs +47, benchmark_smallcap Rs +42, snake_viper_tick Rs +13, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_anaconda Rs -3, snake_nonews Rs -300, snake Rs -320, gold Rs -803

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.