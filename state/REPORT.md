# Paper trading report

Updated 2026-11-09 10:36 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,141 | +10.07% | 0 | - | 236 |
| benchmark | 217,296 | +8.65% | 0 | - | 237 |
| intraweek | 216,871 | +8.44% | 30 | 53% | 3,302 |
| snake_abs_exit | 212,039 | +6.02% | 2 | 50% | 308 |
| snake_abs_exit_conv | 212,017 | +6.01% | 2 | 50% | 330 |
| intramonth | 210,120 | +5.06% | 0 | - | 235 |
| snake_abs | 209,974 | +4.99% | 1 | 100% | 255 |
| snake_abs_conv | 209,799 | +4.90% | 1 | 100% | 255 |
| oracle | 209,581 | +4.79% | 0 | - | 233 |
| random_hold | 204,020 | +2.01% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,506 | -0.25% | 3 | 33% | 374 |
| benchmark_smallcap | 198,609 | -0.69% | 0 | - | 237 |
| snake_viper_wild | 197,184 | -1.41% | 7 | 57% | 1,332 |
| snake_viper_tick | 193,834 | -3.08% | 6 | 50% | 1,154 |
| gold | 193,038 | -3.48% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,733 (-4.63%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +6,508 | +3.09% |
| snake_abs_conv | +4,572 | +2.23% |
| snake_abs | +4,554 | +2.22% |
| unified | +4,532 | +2.10% |
| oracle | +3,754 | +1.82% |
| snake_abs_exit | +3,727 | +1.79% |
| snake_anaconda | +3,679 | +1.88% |
| snake_abs_exit_conv | +3,595 | +1.73% |
| intramonth | +2,517 | +1.21% |
| gold | +1,989 | +1.04% |
| benchmark_smallcap | +1,816 | +0.92% |
| snake_viper_wild | +1,147 | +0.58% |
| snake_viper_tick | +1,124 | +0.58% |
| random_hold | +114 | +0.06% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -191 | -0.09% |

Average per day so far: unified Rs +671, benchmark Rs +577, intraweek Rs +562, snake_abs_exit Rs +446, snake_abs_exit_conv Rs +445, snake_abs_conv Rs +363, snake_abs Rs +356, intramonth Rs +337, oracle Rs +319, random_hold Rs +134, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -20, benchmark_smallcap Rs -53, snake_viper_wild Rs -128, gold Rs -232, snake_viper_tick Rs -325, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.