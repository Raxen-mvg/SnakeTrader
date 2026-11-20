# Paper trading report

Updated 2026-11-20 12:22 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,293 | +13.15% | 0 | - | 236 |
| benchmark | 223,707 | +11.85% | 0 | - | 237 |
| intramonth | 215,283 | +7.64% | 0 | - | 235 |
| intraweek | 214,819 | +7.41% | 35 | 54% | 3,851 |
| oracle | 212,714 | +6.36% | 0 | - | 233 |
| snake_abs_exit | 209,600 | +4.80% | 2 | 50% | 345 |
| random_hold | 208,993 | +4.50% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,627 | +3.81% | 2 | 50% | 345 |
| snake_abs | 206,764 | +3.38% | 1 | 100% | 255 |
| snake_abs_conv | 206,628 | +3.31% | 1 | 100% | 255 |
| snake_viper_wild | 206,337 | +3.17% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,814 | +1.41% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,762 | +0.38% | 0 | - | 237 |
| snake_anaconda | 200,710 | +0.35% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,717 | -16.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,081 (-3.96%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,930 | +0.91% |
| unified | +1,678 | +0.75% |
| benchmark | +1,331 | +0.60% |
| intramonth | +1,275 | +0.60% |
| oracle | +625 | +0.29% |
| random_hold | +540 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -706 | -0.35% |
| snake_viper_tick | -1,163 | -0.57% |
| snake_viper_wild | -1,186 | -0.57% |
| snake_abs | -2,215 | -1.06% |
| snake_abs_conv | -2,232 | -1.07% |
| snake_anaconda | -2,754 | -1.35% |
| snake_abs_exit_conv | -3,438 | -1.63% |
| snake_abs_exit | -3,751 | -1.76% |
| gold | -8,056 | -4.61% |

Average per day so far: unified Rs +692, benchmark Rs +624, intramonth Rs +402, intraweek Rs +390, oracle Rs +335, snake_abs_exit Rs +274, random_hold Rs +237, snake_abs_exit_conv Rs +218, snake_viper_wild Rs +211, snake_abs_conv Rs +189, snake_abs Rs +188, snake_viper_tick Rs +104, nifty_calls Rs +48, benchmark_smallcap Rs +22, snake_anaconda Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -876

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.