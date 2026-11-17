# Paper trading report

Updated 2026-11-17 09:42 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,300 | +11.65% | 0 | - | 236 |
| benchmark | 221,022 | +10.51% | 0 | - | 237 |
| snake_abs_exit | 214,731 | +7.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,709 | +6.85% | 2 | 50% | 345 |
| intramonth | 213,574 | +6.79% | 0 | - | 235 |
| oracle | 213,018 | +6.51% | 0 | - | 233 |
| intraweek | 212,913 | +6.46% | 35 | 54% | 3,851 |
| snake_abs | 210,462 | +5.23% | 1 | 100% | 255 |
| snake_abs_conv | 210,312 | +5.16% | 1 | 100% | 255 |
| random_hold | 208,062 | +4.03% | 10 | 70% | 733 |
| snake_viper_wild | 206,587 | +3.29% | 14 | 50% | 2,496 |
| snake_anaconda | 205,748 | +2.87% | 3 | 33% | 374 |
| snake_viper_tick | 203,055 | +1.53% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,298 | +1.15% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,234 | -9.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,032 (-3.98%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,955 | +0.92% |
| unified | +1,862 | +0.84% |
| intraweek | +1,647 | +0.78% |
| benchmark_smallcap | +1,469 | +0.73% |
| oracle | +995 | +0.47% |
| benchmark | +941 | +0.43% |
| snake_anaconda | +645 | +0.32% |
| snake_abs_exit_conv | +491 | +0.23% |
| snake_viper_wild | +442 | +0.21% |
| snake_viper_tick | +435 | +0.21% |
| snake_abs | +328 | +0.16% |
| snake_abs_conv | +323 | +0.15% |
| snake_abs_exit | +321 | +0.15% |
| gold | +279 | +0.15% |
| random_hold | +269 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +666, benchmark Rs +601, snake_abs_exit Rs +460, snake_abs_exit_conv Rs +428, intramonth Rs +388, oracle Rs +372, intraweek Rs +369, snake_abs_conv Rs +322, snake_abs Rs +317, snake_viper_wild Rs +244, random_hold Rs +230, snake_anaconda Rs +192, snake_viper_tick Rs +127, benchmark_smallcap Rs +74, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -536

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.