# Paper trading report

Updated 2026-11-20 09:31 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,529 | +12.77% | 0 | - | 236 |
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| intramonth | 214,694 | +7.35% | 0 | - | 235 |
| oracle | 213,211 | +6.61% | 0 | - | 233 |
| intraweek | 213,099 | +6.55% | 35 | 54% | 3,851 |
| snake_abs_exit | 211,110 | +5.55% | 2 | 50% | 345 |
| snake_abs_exit_conv | 208,982 | +4.49% | 2 | 50% | 345 |
| random_hold | 208,090 | +4.04% | 11 | 73% | 979 |
| snake_abs | 207,346 | +3.67% | 1 | 100% | 255 |
| snake_abs_conv | 207,214 | +3.61% | 1 | 100% | 255 |
| snake_viper_wild | 206,611 | +3.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,084 | +1.54% | 15 | 47% | 2,625 |
| snake_anaconda | 201,958 | +0.98% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,999 | -0.00% | 0 | - | 237 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,388 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,832 (-4.08%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,122 | +0.53% |
| unified | +914 | +0.41% |
| intramonth | +686 | +0.32% |
| intraweek | +210 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -363 | -0.17% |
| benchmark | -467 | -0.21% |
| snake_viper_tick | -893 | -0.44% |
| snake_viper_wild | -912 | -0.44% |
| benchmark_smallcap | -1,469 | -0.73% |
| snake_anaconda | -1,505 | -0.74% |
| snake_abs | -1,634 | -0.78% |
| snake_abs_conv | -1,646 | -0.79% |
| snake_abs_exit_conv | -2,083 | -0.99% |
| snake_abs_exit | -2,241 | -1.05% |
| gold | -8,384 | -4.80% |

Average per day so far: unified Rs +672, benchmark Rs +577, intramonth Rs +387, oracle Rs +348, intraweek Rs +345, snake_abs_exit Rs +317, snake_abs_exit_conv Rs +257, snake_viper_wild Rs +220, random_hold Rs +213, snake_abs_conv Rs +206, snake_abs Rs +204, snake_viper_tick Rs +114, snake_anaconda Rs +59, nifty_calls Rs +48, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.