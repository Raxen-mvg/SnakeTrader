# Paper trading report

Updated 2026-11-18 13:45 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,012 | +11.51% | 0 | - | 236 |
| benchmark | 219,760 | +9.88% | 0 | - | 237 |
| intramonth | 212,847 | +6.42% | 0 | - | 235 |
| snake_abs_exit | 212,450 | +6.22% | 2 | 50% | 345 |
| oracle | 212,176 | +6.09% | 0 | - | 233 |
| intraweek | 212,157 | +6.08% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 210,701 | +5.35% | 2 | 50% | 345 |
| snake_abs | 207,960 | +3.98% | 1 | 100% | 255 |
| snake_abs_conv | 207,820 | +3.91% | 1 | 100% | 255 |
| random_hold | 207,112 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 206,790 | +3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,259 | +1.63% | 15 | 47% | 2,625 |
| snake_anaconda | 202,905 | +1.45% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,861 | -11.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,156 (-4.42%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,573 | +0.71% |
| intramonth | +1,305 | +0.62% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -310 | -0.15% |
| snake_abs | -599 | -0.29% |
| snake_abs_conv | -600 | -0.29% |
| snake_abs_exit | -692 | -0.33% |
| snake_abs_exit_conv | -873 | -0.41% |
| snake_anaconda | -1,150 | -0.56% |
| intraweek | -1,165 | -0.55% |
| random_hold | -1,320 | -0.63% |
| benchmark_smallcap | -1,412 | -0.70% |
| benchmark | -1,844 | -0.83% |
| snake_viper_tick | -2,578 | -1.25% |
| snake_viper_wild | -2,625 | -1.25% |
| gold | -3,863 | -2.14% |

Average per day so far: unified Rs +639, benchmark Rs +549, snake_abs_exit Rs +377, intramonth Rs +357, oracle Rs +338, intraweek Rs +338, snake_abs_exit_conv Rs +324, snake_viper_wild Rs +242, snake_abs_conv Rs +237, snake_abs Rs +234, random_hold Rs +198, snake_viper_tick Rs +130, snake_anaconda Rs +94, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -26, snake_nonews Rs -326, snake Rs -347, gold Rs -643

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.