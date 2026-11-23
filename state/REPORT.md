# Paper trading report

Updated 2026-11-23 09:28 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,802 | +12.40% | 0 | - | 236 |
| benchmark | 224,120 | +12.06% | 0 | - | 237 |
| intraweek | 215,109 | +7.55% | 35 | 54% | 3,851 |
| intramonth | 212,283 | +6.14% | 0 | - | 235 |
| random_hold | 211,362 | +5.68% | 11 | 73% | 979 |
| oracle | 211,131 | +5.57% | 0 | - | 233 |
| snake_abs_exit | 208,158 | +4.08% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,696 | +3.35% | 2 | 50% | 345 |
| snake_abs | 206,131 | +3.06% | 1 | 100% | 255 |
| snake_abs_conv | 205,977 | +2.99% | 1 | 100% | 255 |
| snake_viper_wild | 203,429 | +1.72% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,959 | -0.02% | 15 | 47% | 2,625 |
| benchmark_smallcap | 199,955 | -0.02% | 0 | - | 237 |
| snake_anaconda | 199,374 | -0.31% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,134 (-4.43%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,184 | +0.70% |
| random_hold | +603 | +0.29% |
| snake_viper_wild | +600 | +0.30% |
| snake_viper_tick | +588 | +0.29% |
| snake_abs | +211 | +0.10% |
| snake_abs_conv | +194 | +0.09% |
| snake_abs_exit_conv | +80 | +0.04% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_abs_exit | -405 | -0.19% |
| snake_anaconda | -532 | -0.27% |
| intraweek | -603 | -0.28% |
| benchmark_smallcap | -953 | -0.47% |
| benchmark | -1,017 | -0.45% |
| oracle | -1,348 | -0.63% |
| unified | -1,380 | -0.61% |
| intramonth | -2,721 | -1.27% |

Average per day so far: unified Rs +636, benchmark Rs +618, intraweek Rs +387, intramonth Rs +315, random_hold Rs +291, oracle Rs +285, snake_abs_exit Rs +227, snake_abs_exit_conv Rs +186, snake_abs_conv Rs +166, snake_abs Rs +166, snake_viper_wild Rs +111, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -1, snake_viper_tick Rs -1, snake_anaconda Rs -18, snake_nonews Rs -300, snake Rs -320, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.