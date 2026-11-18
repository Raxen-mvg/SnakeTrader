# Paper trading report

Updated 2026-11-18 12:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,125 | +11.56% | 0 | - | 236 |
| benchmark | 220,226 | +10.11% | 0 | - | 237 |
| intraweek | 214,071 | +7.04% | 35 | 54% | 3,851 |
| intramonth | 212,937 | +6.47% | 0 | - | 235 |
| snake_abs_exit | 212,492 | +6.25% | 2 | 50% | 345 |
| oracle | 212,468 | +6.23% | 0 | - | 233 |
| snake_abs_exit_conv | 210,821 | +5.41% | 2 | 50% | 345 |
| snake_abs | 207,791 | +3.90% | 1 | 100% | 255 |
| snake_abs_conv | 207,656 | +3.83% | 1 | 100% | 255 |
| random_hold | 207,341 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 206,718 | +3.36% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,188 | +1.59% | 15 | 47% | 2,625 |
| snake_anaconda | 202,899 | +1.45% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,383 | -0.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,074 | -11.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,567 (-4.22%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,686 | +0.76% |
| intramonth | +1,395 | +0.66% |
| intraweek | +748 | +0.35% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -19 | -0.01% |
| snake_abs_exit | -650 | -0.30% |
| snake_abs_exit_conv | -753 | -0.36% |
| snake_abs_conv | -764 | -0.37% |
| snake_abs | -767 | -0.37% |
| random_hold | -1,092 | -0.52% |
| snake_anaconda | -1,156 | -0.57% |
| benchmark_smallcap | -1,188 | -0.59% |
| benchmark | -1,377 | -0.62% |
| snake_viper_tick | -2,648 | -1.29% |
| snake_viper_wild | -2,697 | -1.29% |
| gold | -3,650 | -2.02% |

Average per day so far: unified Rs +642, benchmark Rs +562, intraweek Rs +391, snake_abs_exit Rs +379, intramonth Rs +359, oracle Rs +346, snake_abs_exit_conv Rs +328, snake_viper_wild Rs +240, snake_abs_conv Rs +232, snake_abs Rs +229, random_hold Rs +204, snake_viper_tick Rs +128, snake_anaconda Rs +94, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, snake_nonews Rs -326, snake Rs -347, gold Rs -637

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.