# Paper trading report

Updated 2026-11-26 10:20 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,642 | +12.82% | 0 | - | 237 |
| unified | 223,892 | +11.95% | 0 | - | 236 |
| oracle | 213,321 | +6.66% | 0 | - | 233 |
| intramonth | 211,162 | +5.58% | 0 | - | 235 |
| random_hold | 210,114 | +5.06% | 13 | 69% | 1,037 |
| intraweek | 208,057 | +4.03% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,141 | +1.57% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,490 | +1.25% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,818 | +0.41% | 0 | - | 237 |
| snake_abs | 200,496 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,321 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,380 | -2.81% | 3 | 33% | 374 |
| snake_viper_wild | 193,497 | -3.25% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,205 | -4.90% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,000 | -16.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,230 (-5.38%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,403 | +2.07% |
| benchmark_smallcap | +2,007 | +1.01% |
| intraweek | +1,314 | +0.64% |
| snake_abs_exit | +885 | +0.44% |
| random_hold | +622 | +0.30% |
| benchmark | +620 | +0.28% |
| snake_abs_exit_conv | +514 | +0.25% |
| snake_abs_conv | +349 | +0.17% |
| snake_abs | +346 | +0.17% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_anaconda | -173 | -0.09% |
| unified | -207 | -0.09% |
| oracle | -475 | -0.22% |
| intramonth | -531 | -0.25% |
| snake_viper_tick | -3,971 | -2.04% |
| snake_viper_wild | -4,047 | -2.05% |

Average per day so far: benchmark Rs +625, unified Rs +583, oracle Rs +325, intramonth Rs +272, random_hold Rs +247, intraweek Rs +197, snake_abs_exit Rs +83, snake_abs_exit_conv Rs +66, nifty_calls Rs +45, benchmark_smallcap Rs +22, snake_abs Rs +13, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -156, snake_viper_wild Rs -197, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -326, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.