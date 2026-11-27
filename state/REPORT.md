# Paper trading report

Updated 2026-11-27 14:34 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,067 | +12.03% | 0 | - | 237 |
| unified | 223,792 | +11.90% | 0 | - | 236 |
| oracle | 212,020 | +6.01% | 0 | - | 233 |
| intramonth | 211,119 | +5.56% | 0 | - | 235 |
| random_hold | 210,963 | +5.48% | 13 | 69% | 1,037 |
| intraweek | 207,680 | +3.84% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,478 | +3.24% | 2 | 50% | 345 |
| snake_abs_exit | 204,147 | +2.07% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,468 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,593 | -0.20% | 1 | 100% | 255 |
| snake_abs_conv | 199,410 | -0.29% | 1 | 100% | 255 |
| snake_anaconda | 193,040 | -3.48% | 3 | 33% | 374 |
| snake_viper_wild | 192,462 | -3.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,192 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 171,025 | -14.49% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,989 (-5.51%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,081 | +3.04% |
| gold | +5,031 | +3.03% |
| snake_abs_exit | +3,070 | +1.53% |
| random_hold | +2,369 | +1.14% |
| snake_abs_conv | +1,044 | +0.53% |
| snake_abs | +1,041 | +0.52% |
| snake_anaconda | +744 | +0.39% |
| unified | +714 | +0.32% |
| intraweek | +631 | +0.30% |
| benchmark_smallcap | +628 | +0.31% |
| intramonth | +585 | +0.28% |
| snake_viper_wild | +256 | +0.13% |
| snake_viper_tick | +251 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -215 | -0.10% |
| benchmark | -1,920 | -0.85% |

Average per day so far: benchmark Rs +573, unified Rs +566, oracle Rs +286, intramonth Rs +265, random_hold Rs +261, intraweek Rs +183, snake_abs_exit_conv Rs +166, snake_abs_exit Rs +106, nifty_calls Rs +44, benchmark_smallcap Rs +39, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, snake_anaconda Rs -188, snake_viper_wild Rs -222, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -349, gold Rs -690

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.