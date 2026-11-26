# Paper trading report

Updated 2026-11-26 15:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,071 | +13.04% | 0 | - | 237 |
| unified | 223,008 | +11.50% | 0 | - | 236 |
| oracle | 212,106 | +6.05% | 0 | - | 233 |
| intramonth | 210,478 | +5.24% | 0 | - | 235 |
| random_hold | 208,477 | +4.24% | 13 | 69% | 1,037 |
| intraweek | 206,939 | +3.47% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,425 | +0.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,782 | +0.39% | 2 | 50% | 345 |
| benchmark_smallcap | 200,336 | +0.17% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,927 | -0.54% | 1 | 100% | 255 |
| snake_abs_conv | 198,744 | -0.63% | 1 | 100% | 255 |
| snake_anaconda | 192,695 | -3.65% | 3 | 33% | 374 |
| snake_viper_wild | 192,652 | -3.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,378 | -5.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,142 | -16.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,232 (-5.88%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,545 | +0.94% |
| benchmark_smallcap | +1,525 | +0.77% |
| benchmark | +1,048 | +0.47% |
| intraweek | +196 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -830 | -0.41% |
| random_hold | -1,016 | -0.48% |
| unified | -1,092 | -0.49% |
| snake_abs_exit_conv | -1,194 | -0.59% |
| intramonth | -1,215 | -0.57% |
| snake_abs | -1,222 | -0.61% |
| snake_abs_conv | -1,228 | -0.61% |
| oracle | -1,689 | -0.79% |
| snake_anaconda | -1,858 | -0.95% |
| snake_viper_tick | -4,799 | -2.47% |
| snake_viper_wild | -4,891 | -2.48% |

Average per day so far: benchmark Rs +636, unified Rs +561, oracle Rs +295, intramonth Rs +256, random_hold Rs +207, intraweek Rs +169, nifty_calls Rs +45, snake_abs_exit Rs +38, snake_abs_exit_conv Rs +21, benchmark_smallcap Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -28, snake_abs_conv Rs -33, snake_anaconda Rs -203, snake_viper_wild Rs -223, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -354, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.