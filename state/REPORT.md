# Paper trading report

Updated 2026-11-18 13:56 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,742 | +11.37% | 0 | - | 236 |
| benchmark | 220,318 | +10.16% | 0 | - | 237 |
| snake_abs_exit | 212,775 | +6.39% | 2 | 50% | 345 |
| intraweek | 212,662 | +6.33% | 35 | 54% | 3,851 |
| intramonth | 212,418 | +6.21% | 0 | - | 235 |
| oracle | 212,375 | +6.19% | 0 | - | 233 |
| snake_abs_exit_conv | 210,958 | +5.48% | 2 | 50% | 345 |
| snake_abs | 208,100 | +4.05% | 1 | 100% | 255 |
| snake_abs_conv | 207,960 | +3.98% | 1 | 100% | 255 |
| random_hold | 207,288 | +3.64% | 10 | 70% | 733 |
| snake_viper_wild | 206,679 | +3.34% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,151 | +1.57% | 15 | 47% | 2,625 |
| snake_anaconda | 203,040 | +1.52% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,042 | -11.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,191 (-4.40%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,304 | +0.59% |
| intramonth | +876 | +0.41% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -111 | -0.05% |
| snake_abs_exit | -366 | -0.17% |
| snake_abs | -459 | -0.22% |
| snake_abs_conv | -459 | -0.22% |
| snake_abs_exit_conv | -615 | -0.29% |
| intraweek | -661 | -0.31% |
| benchmark_smallcap | -919 | -0.46% |
| snake_anaconda | -1,015 | -0.50% |
| random_hold | -1,145 | -0.55% |
| benchmark | -1,285 | -0.58% |
| snake_viper_tick | -2,686 | -1.30% |
| snake_viper_wild | -2,736 | -1.31% |
| gold | -3,683 | -2.04% |

Average per day so far: unified Rs +632, benchmark Rs +564, snake_abs_exit Rs +387, intraweek Rs +352, intramonth Rs +345, oracle Rs +344, snake_abs_exit_conv Rs +332, snake_abs_conv Rs +241, snake_viper_wild Rs +239, snake_abs Rs +238, random_hold Rs +202, snake_viper_tick Rs +126, snake_anaconda Rs +98, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -638

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.