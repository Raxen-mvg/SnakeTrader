# Paper trading report

Updated 2026-11-17 11:27 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,020 | +11.01% | 0 | - | 236 |
| benchmark | 221,871 | +10.94% | 0 | - | 237 |
| snake_abs_exit | 215,571 | +7.79% | 2 | 50% | 345 |
| intraweek | 213,844 | +6.92% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,527 | +6.76% | 2 | 50% | 345 |
| oracle | 212,459 | +6.23% | 0 | - | 233 |
| intramonth | 212,039 | +6.02% | 0 | - | 235 |
| snake_abs | 209,863 | +4.93% | 1 | 100% | 255 |
| snake_abs_conv | 209,715 | +4.86% | 1 | 100% | 255 |
| random_hold | 207,979 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 207,771 | +3.88% | 14 | 50% | 2,496 |
| snake_anaconda | 205,466 | +2.73% | 3 | 33% | 374 |
| snake_viper_tick | 204,219 | +2.11% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,129 | +1.06% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,546 | -9.23% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,470 (-4.27%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,578 | +1.22% |
| benchmark | +1,790 | +0.81% |
| snake_viper_wild | +1,627 | +0.79% |
| snake_viper_tick | +1,599 | +0.79% |
| benchmark_smallcap | +1,300 | +0.65% |
| snake_abs_exit | +1,162 | +0.54% |
| gold | +592 | +0.33% |
| unified | +583 | +0.26% |
| oracle | +436 | +0.21% |
| intramonth | +420 | +0.20% |
| snake_anaconda | +363 | +0.18% |
| snake_abs_exit_conv | +309 | +0.14% |
| random_hold | +186 | +0.09% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -271 | -0.13% |
| snake_abs_conv | -274 | -0.13% |

Average per day so far: unified Rs +629, benchmark Rs +625, snake_abs_exit Rs +487, snake_abs_exit_conv Rs +423, intraweek Rs +396, oracle Rs +356, intramonth Rs +344, snake_abs_conv Rs +304, snake_abs Rs +299, snake_viper_wild Rs +288, random_hold Rs +228, snake_anaconda Rs +182, snake_viper_tick Rs +176, benchmark_smallcap Rs +69, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -527

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.