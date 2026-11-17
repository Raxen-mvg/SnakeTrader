# Paper trading report

Updated 2026-11-17 13:29 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,517 | +10.76% | 0 | - | 236 |
| benchmark | 221,358 | +10.68% | 0 | - | 237 |
| snake_abs_exit | 214,142 | +7.07% | 2 | 50% | 345 |
| intraweek | 214,015 | +7.01% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,596 | +6.30% | 2 | 50% | 345 |
| oracle | 212,170 | +6.08% | 0 | - | 233 |
| intramonth | 211,497 | +5.75% | 0 | - | 235 |
| snake_abs | 209,428 | +4.71% | 1 | 100% | 255 |
| snake_abs_conv | 209,290 | +4.64% | 1 | 100% | 255 |
| snake_viper_wild | 209,142 | +4.57% | 14 | 50% | 2,496 |
| random_hold | 207,400 | +3.70% | 10 | 70% | 733 |
| snake_viper_tick | 205,568 | +2.78% | 13 | 46% | 2,299 |
| snake_anaconda | 205,085 | +2.54% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,952 | +0.48% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,283 | -9.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,140 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +2,998 | +1.45% |
| snake_viper_tick | +2,948 | +1.46% |
| intraweek | +2,749 | +1.30% |
| benchmark | +1,278 | +0.58% |
| gold | +329 | +0.18% |
| oracle | +147 | +0.07% |
| benchmark_smallcap | +123 | +0.06% |
| unified | +79 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -17 | -0.01% |
| intramonth | -122 | -0.06% |
| snake_abs_exit | -267 | -0.12% |
| random_hold | -394 | -0.19% |
| snake_abs_exit_conv | -621 | -0.29% |
| snake_abs_conv | -699 | -0.33% |
| snake_abs | -706 | -0.34% |

Average per day so far: unified Rs +615, benchmark Rs +610, snake_abs_exit Rs +442, intraweek Rs +400, snake_abs_exit_conv Rs +394, oracle Rs +348, snake_viper_wild Rs +339, intramonth Rs +328, snake_abs_conv Rs +290, snake_abs Rs +286, snake_viper_tick Rs +232, random_hold Rs +211, snake_anaconda Rs +170, nifty_calls Rs +52, benchmark_smallcap Rs +31, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -535

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.