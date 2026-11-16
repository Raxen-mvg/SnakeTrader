# Paper trading report

Updated 2026-11-16 09:52 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,953 | +10.48% | 0 | - | 237 |
| unified | 220,281 | +10.14% | 0 | - | 236 |
| intraweek | 214,687 | +7.34% | 35 | 54% | 3,851 |
| snake_abs_exit | 214,362 | +7.18% | 2 | 50% | 345 |
| oracle | 213,720 | +6.86% | 0 | - | 233 |
| snake_abs_exit_conv | 213,294 | +6.65% | 2 | 50% | 345 |
| intramonth | 210,843 | +5.42% | 0 | - | 235 |
| snake_abs | 210,640 | +5.32% | 1 | 100% | 255 |
| snake_abs_conv | 210,461 | +5.23% | 1 | 100% | 255 |
| random_hold | 208,089 | +4.04% | 10 | 70% | 733 |
| snake_anaconda | 204,517 | +2.26% | 3 | 33% | 374 |
| snake_viper_wild | 203,357 | +1.68% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,197 | +1.10% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 199,878 | -0.06% | 13 | 46% | 2,299 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,204 | -8.90% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,678 (-4.16%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,614 | +0.74% |
| unified | +1,261 | +0.58% |
| random_hold | +863 | +0.42% |
| intramonth | +786 | +0.37% |
| oracle | +622 | +0.29% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -375 | -0.18% |
| benchmark_smallcap | -673 | -0.33% |
| snake_viper_tick | -1,377 | -0.68% |
| snake_viper_wild | -1,400 | -0.68% |
| intraweek | -1,458 | -0.68% |
| gold | -1,792 | -0.97% |
| snake_abs | -1,900 | -0.89% |
| snake_abs_conv | -1,905 | -0.90% |
| snake_abs_exit | -2,623 | -1.21% |
| snake_abs_exit_conv | -3,087 | -1.43% |

Average per day so far: benchmark Rs +616, unified Rs +597, snake_abs_exit Rs +463, intraweek Rs +432, snake_abs_exit_conv Rs +429, oracle Rs +404, snake_abs_conv Rs +337, snake_abs Rs +332, intramonth Rs +319, random_hold Rs +238, snake_anaconda Rs +156, snake_viper_wild Rs +129, benchmark_smallcap Rs +73, nifty_calls Rs +54, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -5, snake_nonews Rs -347, snake Rs -368, gold Rs -523

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.