# Paper trading report

Updated 2026-11-17 14:44 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,871 | +10.94% | 0 | - | 237 |
| unified | 221,388 | +10.69% | 0 | - | 236 |
| intraweek | 214,175 | +7.09% | 35 | 54% | 3,851 |
| snake_abs_exit | 213,258 | +6.63% | 2 | 50% | 345 |
| oracle | 212,658 | +6.33% | 0 | - | 233 |
| snake_abs_exit_conv | 211,706 | +5.85% | 2 | 50% | 345 |
| intramonth | 211,326 | +5.66% | 0 | - | 235 |
| snake_viper_wild | 209,577 | +4.79% | 14 | 50% | 2,496 |
| snake_abs | 208,494 | +4.25% | 1 | 100% | 255 |
| snake_abs_conv | 208,356 | +4.18% | 1 | 100% | 255 |
| random_hold | 207,989 | +3.99% | 10 | 70% | 733 |
| snake_viper_tick | 205,995 | +3.00% | 13 | 46% | 2,299 |
| snake_anaconda | 204,029 | +2.01% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,199 | +0.60% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,658 | -9.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,260 (-4.37%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,432 | +1.67% |
| snake_viper_tick | +3,376 | +1.67% |
| intraweek | +2,909 | +1.38% |
| benchmark | +1,790 | +0.81% |
| oracle | +635 | +0.30% |
| benchmark_smallcap | +370 | +0.18% |
| random_hold | +195 | +0.09% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -50 | -0.02% |
| intramonth | -293 | -0.14% |
| gold | -296 | -0.16% |
| snake_anaconda | -1,074 | -0.52% |
| snake_abs_exit | -1,151 | -0.54% |
| snake_abs_exit_conv | -1,511 | -0.71% |
| snake_abs_conv | -1,634 | -0.78% |
| snake_abs | -1,640 | -0.78% |

Average per day so far: benchmark Rs +625, unified Rs +611, snake_abs_exit Rs +414, intraweek Rs +405, snake_abs_exit_conv Rs +366, oracle Rs +362, snake_viper_wild Rs +355, intramonth Rs +324, snake_abs_conv Rs +261, snake_abs Rs +257, snake_viper_tick Rs +250, random_hold Rs +228, snake_anaconda Rs +134, nifty_calls Rs +52, benchmark_smallcap Rs +39, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -553

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.