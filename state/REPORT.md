# Paper trading report

Updated 2026-11-18 10:19 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,340 | +11.17% | 0 | - | 236 |
| benchmark | 220,387 | +10.19% | 0 | - | 237 |
| intraweek | 214,789 | +7.39% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,575 | +6.29% | 2 | 50% | 345 |
| oracle | 212,385 | +6.19% | 0 | - | 233 |
| intramonth | 212,209 | +6.11% | 0 | - | 235 |
| snake_abs_exit_conv | 210,855 | +5.43% | 2 | 50% | 345 |
| snake_abs | 208,063 | +4.03% | 1 | 100% | 255 |
| snake_abs_conv | 207,912 | +3.96% | 1 | 100% | 255 |
| random_hold | 207,398 | +3.70% | 10 | 70% | 733 |
| snake_viper_wild | 207,135 | +3.57% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,597 | +1.80% | 15 | 47% | 2,625 |
| snake_anaconda | 202,712 | +1.36% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,112 | +0.06% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,337 | -11.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,427 (-4.29%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,466 | +0.69% |
| unified | +901 | +0.41% |
| intramonth | +667 | +0.32% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -101 | -0.05% |
| benchmark_smallcap | -460 | -0.23% |
| snake_abs | -496 | -0.24% |
| snake_abs_conv | -507 | -0.24% |
| snake_abs_exit | -566 | -0.27% |
| snake_abs_exit_conv | -719 | -0.34% |
| random_hold | -1,034 | -0.50% |
| benchmark | -1,216 | -0.55% |
| snake_anaconda | -1,343 | -0.66% |
| snake_viper_tick | -2,239 | -1.09% |
| snake_viper_wild | -2,280 | -1.09% |
| gold | -3,387 | -1.87% |

Average per day so far: unified Rs +621, benchmark Rs +566, intraweek Rs +411, snake_abs_exit Rs +381, oracle Rs +344, intramonth Rs +339, snake_abs_exit_conv Rs +329, snake_viper_wild Rs +255, snake_abs_conv Rs +240, snake_abs Rs +237, random_hold Rs +206, snake_viper_tick Rs +144, snake_anaconda Rs +87, nifty_calls Rs +51, benchmark_smallcap Rs +3, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -630

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.