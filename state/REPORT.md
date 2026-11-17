# Paper trading report

Updated 2026-11-17 09:55 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,883 | +11.44% | 0 | - | 236 |
| benchmark | 221,267 | +10.63% | 0 | - | 237 |
| snake_abs_exit | 214,908 | +7.45% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,647 | +6.82% | 2 | 50% | 345 |
| intramonth | 213,094 | +6.55% | 0 | - | 235 |
| oracle | 212,949 | +6.47% | 0 | - | 233 |
| intraweek | 212,625 | +6.31% | 35 | 54% | 3,851 |
| snake_abs | 210,155 | +5.08% | 1 | 100% | 255 |
| snake_abs_conv | 210,005 | +5.00% | 1 | 100% | 255 |
| random_hold | 207,878 | +3.94% | 10 | 70% | 733 |
| snake_viper_wild | 206,627 | +3.31% | 14 | 50% | 2,496 |
| snake_anaconda | 205,501 | +2.75% | 3 | 33% | 374 |
| snake_viper_tick | 203,094 | +1.55% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,197 | +1.10% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,102 | -9.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,777 (-4.11%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,475 | +0.70% |
| unified | +1,445 | +0.65% |
| benchmark_smallcap | +1,368 | +0.68% |
| intraweek | +1,360 | +0.64% |
| benchmark | +1,186 | +0.54% |
| oracle | +926 | +0.44% |
| snake_abs_exit | +498 | +0.23% |
| snake_viper_wild | +482 | +0.23% |
| snake_viper_tick | +474 | +0.23% |
| snake_abs_exit_conv | +430 | +0.20% |
| snake_anaconda | +398 | +0.19% |
| gold | +148 | +0.08% |
| random_hold | +85 | +0.04% |
| snake_abs | +22 | +0.01% |
| snake_abs_conv | +16 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +654, benchmark Rs +608, snake_abs_exit Rs +466, snake_abs_exit_conv Rs +426, intramonth Rs +374, oracle Rs +370, intraweek Rs +361, snake_abs_conv Rs +313, snake_abs Rs +308, snake_viper_wild Rs +245, random_hold Rs +225, snake_anaconda Rs +183, snake_viper_tick Rs +129, benchmark_smallcap Rs +71, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -540

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.