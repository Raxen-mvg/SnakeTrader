# Paper trading report

Updated 2026-11-26 12:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,079 | +13.04% | 0 | - | 237 |
| unified | 223,380 | +11.69% | 0 | - | 236 |
| oracle | 213,278 | +6.64% | 0 | - | 233 |
| intramonth | 210,483 | +5.24% | 0 | - | 235 |
| random_hold | 209,834 | +4.92% | 13 | 69% | 1,037 |
| intraweek | 208,182 | +4.09% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,349 | +0.17% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,937 | -0.03% | 2 | 50% | 345 |
| snake_abs | 198,282 | -0.86% | 1 | 100% | 255 |
| snake_abs_conv | 198,083 | -0.96% | 1 | 100% | 255 |
| snake_anaconda | 192,036 | -3.98% | 3 | 33% | 374 |
| snake_viper_wild | 191,932 | -4.03% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,673 | -5.66% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,795 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.17% |
| benchmark_smallcap | +1,760 | +0.89% |
| intraweek | +1,439 | +0.70% |
| benchmark | +1,056 | +0.47% |
| random_hold | +342 | +0.16% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -517 | -0.24% |
| unified | -720 | -0.32% |
| intramonth | -1,210 | -0.57% |
| snake_abs | -1,868 | -0.93% |
| snake_abs_conv | -1,890 | -0.94% |
| snake_abs_exit | -1,906 | -0.94% |
| snake_abs_exit_conv | -2,039 | -1.01% |
| snake_anaconda | -2,517 | -1.29% |
| snake_viper_tick | -5,504 | -2.83% |
| snake_viper_wild | -5,611 | -2.84% |

Average per day so far: benchmark Rs +636, unified Rs +570, oracle Rs +324, intramonth Rs +256, random_hold Rs +240, intraweek Rs +200, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -2, snake_abs Rs -44, snake_abs_conv Rs -50, snake_anaconda Rs -221, snake_viper_wild Rs -244, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -378, gold Rs -817

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.