# Paper trading report

Updated 2026-11-26 15:22 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,040 | +13.02% | 0 | - | 237 |
| unified | 223,075 | +11.54% | 0 | - | 236 |
| oracle | 212,060 | +6.03% | 0 | - | 233 |
| intramonth | 210,510 | +5.25% | 0 | - | 235 |
| random_hold | 208,513 | +4.26% | 13 | 69% | 1,037 |
| intraweek | 207,146 | +3.57% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,313 | +0.66% | 2 | 50% | 345 |
| benchmark_smallcap | 200,851 | +0.43% | 0 | - | 237 |
| snake_abs_exit_conv | 200,668 | +0.33% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,822 | -0.59% | 1 | 100% | 255 |
| snake_abs_conv | 198,637 | -0.68% | 1 | 100% | 255 |
| snake_viper_wild | 192,652 | -3.67% | 16 | 50% | 2,827 |
| snake_anaconda | 192,587 | -3.71% | 3 | 33% | 374 |
| snake_viper_tick | 189,378 | -5.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,977 | -17.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,296 (-5.85%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,040 | +1.03% |
| gold | +1,381 | +0.84% |
| benchmark | +1,017 | +0.45% |
| intraweek | +403 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -942 | -0.47% |
| random_hold | -980 | -0.47% |
| unified | -1,025 | -0.46% |
| intramonth | -1,183 | -0.56% |
| snake_abs_exit_conv | -1,307 | -0.65% |
| snake_abs | -1,328 | -0.66% |
| snake_abs_conv | -1,336 | -0.67% |
| oracle | -1,735 | -0.81% |
| snake_anaconda | -1,966 | -1.01% |
| snake_viper_tick | -4,799 | -2.47% |
| snake_viper_wild | -4,891 | -2.48% |

Average per day so far: benchmark Rs +635, unified Rs +563, oracle Rs +294, intramonth Rs +256, random_hold Rs +208, intraweek Rs +174, nifty_calls Rs +45, snake_abs_exit Rs +35, benchmark_smallcap Rs +23, snake_abs_exit_conv Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -30, snake_abs_conv Rs -36, snake_anaconda Rs -206, snake_viper_wild Rs -223, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -354, gold Rs -830

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.