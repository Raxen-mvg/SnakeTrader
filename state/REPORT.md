# Paper trading report

Updated 2026-11-16 15:16 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,571 | +10.79% | 0 | - | 236 |
| benchmark | 219,974 | +9.99% | 0 | - | 237 |
| snake_abs_exit | 214,769 | +7.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,446 | +6.72% | 2 | 50% | 345 |
| oracle | 212,008 | +6.00% | 0 | - | 233 |
| intramonth | 211,747 | +5.87% | 0 | - | 235 |
| intraweek | 210,817 | +5.41% | 35 | 54% | 3,851 |
| snake_abs | 210,116 | +5.06% | 1 | 100% | 255 |
| snake_abs_conv | 209,974 | +4.99% | 1 | 100% | 255 |
| random_hold | 207,851 | +3.93% | 10 | 70% | 733 |
| snake_viper_wild | 205,920 | +2.96% | 14 | 50% | 2,496 |
| snake_anaconda | 205,314 | +2.66% | 3 | 33% | 374 |
| snake_viper_tick | 202,400 | +1.20% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,076 | +0.54% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,905 | -9.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,751 (-4.62%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,551 | +1.17% |
| intramonth | +1,690 | +0.80% |
| snake_viper_wild | +1,163 | +0.57% |
| snake_viper_tick | +1,145 | +0.57% |
| benchmark | +635 | +0.29% |
| random_hold | +625 | +0.30% |
| snake_anaconda | +422 | +0.21% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -1,089 | -0.51% |
| benchmark_smallcap | -1,794 | -0.88% |
| snake_abs_exit | -2,216 | -1.02% |
| snake_abs_conv | -2,392 | -1.13% |
| snake_abs | -2,424 | -1.14% |
| snake_abs_exit_conv | -2,935 | -1.36% |
| gold | -3,091 | -1.68% |
| intraweek | -5,328 | -2.46% |

Average per day so far: unified Rs +634, benchmark Rs +587, snake_abs_exit Rs +476, snake_abs_exit_conv Rs +434, oracle Rs +353, intramonth Rs +345, snake_abs_conv Rs +322, intraweek Rs +318, snake_abs Rs +316, random_hold Rs +231, snake_viper_wild Rs +228, snake_anaconda Rs +183, snake_viper_tick Rs +104, nifty_calls Rs +54, benchmark_smallcap Rs +36, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -562

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.