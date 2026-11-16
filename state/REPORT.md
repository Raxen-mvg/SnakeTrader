# Paper trading report

Updated 2026-11-16 15:28 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,832 | +10.92% | 0 | - | 236 |
| benchmark | 220,525 | +10.26% | 0 | - | 237 |
| snake_abs_exit | 214,529 | +7.26% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,287 | +6.64% | 2 | 50% | 345 |
| oracle | 212,138 | +6.07% | 0 | - | 233 |
| intramonth | 211,874 | +5.94% | 0 | - | 235 |
| intraweek | 211,640 | +5.82% | 35 | 54% | 3,851 |
| snake_abs | 210,347 | +5.17% | 1 | 100% | 255 |
| snake_abs_conv | 210,201 | +5.10% | 1 | 100% | 255 |
| random_hold | 207,823 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 206,763 | +3.38% | 14 | 50% | 2,496 |
| snake_anaconda | 205,053 | +2.53% | 3 | 33% | 374 |
| snake_viper_tick | 203,229 | +1.61% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,493 | +0.25% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,889 | -9.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,972 (-4.51%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,812 | +1.28% |
| snake_viper_wild | +2,006 | +0.98% |
| snake_viper_tick | +1,974 | +0.98% |
| intramonth | +1,817 | +0.86% |
| benchmark | +1,186 | +0.54% |
| random_hold | +597 | +0.29% |
| snake_anaconda | +161 | +0.08% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -960 | -0.45% |
| snake_abs_conv | -2,165 | -1.02% |
| snake_abs | -2,193 | -1.03% |
| benchmark_smallcap | -2,377 | -1.17% |
| snake_abs_exit | -2,456 | -1.13% |
| snake_abs_exit_conv | -3,094 | -1.43% |
| gold | -3,107 | -1.69% |
| intraweek | -4,505 | -2.08% |

Average per day so far: unified Rs +642, benchmark Rs +604, snake_abs_exit Rs +469, snake_abs_exit_conv Rs +429, oracle Rs +357, intramonth Rs +349, intraweek Rs +342, snake_abs_conv Rs +329, snake_abs Rs +323, snake_viper_wild Rs +260, random_hold Rs +230, snake_anaconda Rs +174, snake_viper_tick Rs +140, nifty_calls Rs +54, benchmark_smallcap Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -562

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.