# Paper trading report

Updated 2026-11-16 15:22 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,741 | +10.87% | 0 | - | 236 |
| benchmark | 220,196 | +10.10% | 0 | - | 237 |
| snake_abs_exit | 215,030 | +7.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,734 | +6.87% | 2 | 50% | 345 |
| oracle | 212,384 | +6.19% | 0 | - | 233 |
| intraweek | 212,073 | +6.04% | 35 | 54% | 3,851 |
| intramonth | 211,836 | +5.92% | 0 | - | 235 |
| snake_abs | 210,894 | +5.45% | 1 | 100% | 255 |
| snake_abs_conv | 210,747 | +5.37% | 1 | 100% | 255 |
| random_hold | 207,812 | +3.91% | 10 | 70% | 733 |
| snake_viper_wild | 206,375 | +3.19% | 14 | 50% | 2,496 |
| snake_anaconda | 205,569 | +2.78% | 3 | 33% | 374 |
| snake_viper_tick | 202,847 | +1.42% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,896 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,905 | -9.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,125 (-4.44%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +2,720 | +1.24% |
| intramonth | +1,779 | +0.85% |
| snake_viper_wild | +1,618 | +0.79% |
| snake_viper_tick | +1,592 | +0.79% |
| benchmark | +857 | +0.39% |
| snake_anaconda | +677 | +0.33% |
| random_hold | +586 | +0.28% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -714 | -0.34% |
| snake_abs_conv | -1,619 | -0.76% |
| snake_abs | -1,647 | -0.78% |
| snake_abs_exit | -1,955 | -0.90% |
| benchmark_smallcap | -1,973 | -0.97% |
| snake_abs_exit_conv | -2,647 | -1.22% |
| gold | -3,091 | -1.68% |
| intraweek | -4,072 | -1.88% |

Average per day so far: unified Rs +639, benchmark Rs +594, snake_abs_exit Rs +485, snake_abs_exit_conv Rs +443, oracle Rs +364, intraweek Rs +355, intramonth Rs +348, snake_abs_conv Rs +347, snake_abs Rs +340, snake_viper_wild Rs +245, random_hold Rs +230, snake_anaconda Rs +192, snake_viper_tick Rs +124, nifty_calls Rs +54, benchmark_smallcap Rs +30, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -562

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.