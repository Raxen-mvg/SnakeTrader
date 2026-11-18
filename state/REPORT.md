# Paper trading report

Updated 2026-11-18 10:10 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,573 | +11.29% | 0 | - | 236 |
| benchmark | 220,670 | +10.34% | 0 | - | 237 |
| intraweek | 214,398 | +7.20% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,558 | +6.28% | 2 | 50% | 345 |
| intramonth | 212,442 | +6.22% | 0 | - | 235 |
| oracle | 212,153 | +6.08% | 0 | - | 233 |
| snake_abs_exit_conv | 210,941 | +5.47% | 2 | 50% | 345 |
| snake_abs | 208,245 | +4.12% | 1 | 100% | 255 |
| snake_abs_conv | 208,094 | +4.05% | 1 | 100% | 255 |
| random_hold | 207,545 | +3.77% | 10 | 70% | 733 |
| snake_viper_wild | 207,166 | +3.58% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,627 | +1.81% | 15 | 47% | 2,625 |
| snake_anaconda | 203,149 | +1.57% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,156 | +0.08% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,272 | -11.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,433 (-4.28%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,134 | +0.51% |
| intraweek | +1,075 | +0.50% |
| intramonth | +900 | +0.42% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -314 | -0.15% |
| snake_abs_conv | -326 | -0.16% |
| oracle | -333 | -0.16% |
| benchmark_smallcap | -415 | -0.21% |
| snake_abs_exit | -584 | -0.27% |
| snake_abs_exit_conv | -633 | -0.30% |
| random_hold | -888 | -0.43% |
| snake_anaconda | -906 | -0.44% |
| benchmark | -933 | -0.42% |
| snake_viper_tick | -2,210 | -1.07% |
| snake_viper_wild | -2,249 | -1.07% |
| gold | -3,452 | -1.91% |

Average per day so far: unified Rs +627, benchmark Rs +574, intraweek Rs +400, snake_abs_exit Rs +381, intramonth Rs +346, oracle Rs +338, snake_abs_exit_conv Rs +332, snake_viper_wild Rs +256, snake_abs_conv Rs +245, snake_abs Rs +242, random_hold Rs +210, snake_viper_tick Rs +145, snake_anaconda Rs +102, nifty_calls Rs +51, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -631

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.