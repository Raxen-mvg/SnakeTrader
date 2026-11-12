# Paper trading report

Updated 2026-11-12 13:45 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,932 | +10.47% | 0 | - | 236 |
| benchmark | 220,226 | +10.11% | 0 | - | 237 |
| snake_abs_exit_conv | 218,459 | +9.23% | 2 | 50% | 345 |
| snake_abs_exit | 217,298 | +8.65% | 2 | 50% | 345 |
| snake_abs | 215,480 | +7.74% | 1 | 100% | 255 |
| snake_abs_conv | 215,305 | +7.65% | 1 | 100% | 255 |
| intraweek | 214,461 | +7.23% | 30 | 53% | 3,302 |
| oracle | 213,001 | +6.50% | 0 | - | 233 |
| intramonth | 211,507 | +5.75% | 0 | - | 235 |
| random_hold | 207,881 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 207,043 | +3.52% | 10 | 50% | 1,825 |
| snake_anaconda | 206,261 | +3.13% | 3 | 33% | 374 |
| snake_viper_tick | 203,501 | +1.75% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,780 | +1.39% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,018 | -6.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,927 (-4.04%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,138 | +1.05% |
| benchmark_smallcap | +1,973 | +0.98% |
| snake_abs | +1,855 | +0.87% |
| snake_abs_conv | +1,847 | +0.86% |
| intraweek | +1,328 | +0.62% |
| snake_abs_exit_conv | +1,307 | +0.60% |
| snake_abs_exit | +1,136 | +0.53% |
| unified | +1,118 | +0.51% |
| oracle | +999 | +0.47% |
| benchmark | +964 | +0.44% |
| random_hold | +770 | +0.37% |
| intramonth | +511 | +0.24% |
| snake_viper_wild | +301 | +0.15% |
| snake_viper_tick | +292 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,567 | -1.88% |

Average per day so far: unified Rs +654, snake_abs_exit_conv Rs +637, benchmark Rs +632, snake_abs_exit Rs +596, snake_abs_conv Rs +528, snake_abs Rs +516, intraweek Rs +452, oracle Rs +406, intramonth Rs +360, snake_viper_wild Rs +293, random_hold Rs +246, snake_anaconda Rs +232, snake_viper_tick Rs +167, benchmark_smallcap Rs +99, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -437

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.