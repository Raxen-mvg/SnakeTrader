# Paper trading report

Updated 2026-11-17 10:02 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,785 | +11.39% | 0 | - | 236 |
| benchmark | 221,205 | +10.60% | 0 | - | 237 |
| snake_abs_exit | 215,186 | +7.59% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,834 | +6.92% | 2 | 50% | 345 |
| oracle | 212,993 | +6.50% | 0 | - | 233 |
| intramonth | 212,785 | +6.39% | 0 | - | 235 |
| intraweek | 212,407 | +6.20% | 35 | 54% | 3,851 |
| snake_abs | 210,316 | +5.16% | 1 | 100% | 255 |
| snake_abs_conv | 210,166 | +5.08% | 1 | 100% | 255 |
| random_hold | 207,886 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 206,656 | +3.33% | 14 | 50% | 2,496 |
| snake_anaconda | 205,663 | +2.83% | 3 | 33% | 374 |
| snake_viper_tick | 203,123 | +1.56% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,995 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,938 | -9.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,674 (-4.16%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,347 | +0.61% |
| benchmark_smallcap | +1,166 | +0.58% |
| intramonth | +1,166 | +0.55% |
| intraweek | +1,141 | +0.54% |
| benchmark | +1,125 | +0.51% |
| oracle | +970 | +0.46% |
| snake_abs_exit | +777 | +0.36% |
| snake_abs_exit_conv | +617 | +0.29% |
| snake_anaconda | +560 | +0.27% |
| snake_viper_wild | +512 | +0.25% |
| snake_viper_tick | +503 | +0.25% |
| snake_abs | +183 | +0.09% |
| snake_abs_conv | +176 | +0.08% |
| random_hold | +92 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -16 | -0.01% |

Average per day so far: unified Rs +651, benchmark Rs +606, snake_abs_exit Rs +475, snake_abs_exit_conv Rs +432, oracle Rs +371, intramonth Rs +365, intraweek Rs +354, snake_abs_conv Rs +318, snake_abs Rs +313, snake_viper_wild Rs +247, random_hold Rs +225, snake_anaconda Rs +189, snake_viper_tick Rs +130, benchmark_smallcap Rs +64, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -545

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.