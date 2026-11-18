# Paper trading report

Updated 2026-11-18 12:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,088 | +11.54% | 0 | - | 236 |
| benchmark | 220,188 | +10.09% | 0 | - | 237 |
| intraweek | 213,914 | +6.96% | 35 | 54% | 3,851 |
| intramonth | 213,033 | +6.52% | 0 | - | 235 |
| snake_abs_exit | 213,008 | +6.50% | 2 | 50% | 345 |
| oracle | 212,316 | +6.16% | 0 | - | 233 |
| snake_abs_exit_conv | 211,165 | +5.58% | 2 | 50% | 345 |
| snake_abs | 208,136 | +4.07% | 1 | 100% | 255 |
| snake_abs_conv | 208,004 | +4.00% | 1 | 100% | 255 |
| random_hold | 207,453 | +3.73% | 10 | 70% | 733 |
| snake_viper_wild | 207,395 | +3.70% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,851 | +1.93% | 15 | 47% | 2,625 |
| snake_anaconda | 203,250 | +1.62% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,529 | -0.24% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,074 | -11.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,560 (-4.22%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,649 | +0.74% |
| intramonth | +1,490 | +0.70% |
| intraweek | +591 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs_exit | -134 | -0.06% |
| oracle | -170 | -0.08% |
| snake_abs_exit_conv | -409 | -0.19% |
| snake_abs_conv | -416 | -0.20% |
| snake_abs | -422 | -0.20% |
| snake_anaconda | -805 | -0.40% |
| random_hold | -980 | -0.47% |
| benchmark_smallcap | -1,043 | -0.52% |
| benchmark | -1,415 | -0.64% |
| snake_viper_tick | -1,986 | -0.96% |
| snake_viper_wild | -2,020 | -0.96% |
| gold | -3,650 | -2.02% |

Average per day so far: unified Rs +641, benchmark Rs +561, snake_abs_exit Rs +394, intraweek Rs +386, intramonth Rs +362, oracle Rs +342, snake_abs_exit_conv Rs +338, snake_viper_wild Rs +264, snake_abs_conv Rs +243, snake_abs Rs +239, random_hold Rs +207, snake_viper_tick Rs +154, snake_anaconda Rs +105, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -15, snake_nonews Rs -326, snake Rs -347, gold Rs -637

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.