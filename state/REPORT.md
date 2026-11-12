# Paper trading report

Updated 2026-11-12 14:37 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,773 | +10.39% | 0 | - | 236 |
| benchmark | 220,127 | +10.06% | 0 | - | 237 |
| snake_abs_exit_conv | 218,615 | +9.31% | 2 | 50% | 345 |
| snake_abs_exit | 217,545 | +8.77% | 2 | 50% | 345 |
| snake_abs | 215,662 | +7.83% | 1 | 100% | 255 |
| snake_abs_conv | 215,490 | +7.75% | 1 | 100% | 255 |
| intraweek | 214,356 | +7.18% | 30 | 53% | 3,302 |
| oracle | 212,770 | +6.38% | 0 | - | 233 |
| intramonth | 211,573 | +5.79% | 0 | - | 235 |
| random_hold | 207,864 | +3.93% | 10 | 70% | 733 |
| snake_anaconda | 206,337 | +3.17% | 3 | 33% | 374 |
| snake_viper_wild | 205,849 | +2.92% | 13 | 54% | 2,247 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| snake_viper_tick | 202,329 | +1.17% | 12 | 50% | 2,054 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,949 | -7.53% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,869 (-4.07%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,214 | +1.08% |
| benchmark_smallcap | +2,107 | +1.05% |
| snake_abs | +2,038 | +0.95% |
| snake_abs_conv | +2,032 | +0.95% |
| snake_abs_exit_conv | +1,463 | +0.67% |
| snake_abs_exit | +1,383 | +0.64% |
| intraweek | +1,223 | +0.57% |
| unified | +960 | +0.44% |
| benchmark | +864 | +0.39% |
| oracle | +767 | +0.36% |
| random_hold | +753 | +0.36% |
| intramonth | +577 | +0.27% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -880 | -0.43% |
| snake_viper_wild | -893 | -0.43% |
| gold | -4,636 | -2.44% |

Average per day so far: unified Rs +649, snake_abs_exit_conv Rs +642, benchmark Rs +629, snake_abs_exit Rs +605, snake_abs_conv Rs +534, snake_abs Rs +522, intraweek Rs +449, oracle Rs +399, intramonth Rs +362, random_hold Rs +246, snake_viper_wild Rs +244, snake_anaconda Rs +235, snake_viper_tick Rs +111, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -470

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.