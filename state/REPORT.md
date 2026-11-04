# Paper trading report

Updated 2026-11-04 12:25 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,978 | +6.99% | 0 | - | 236 |
| snake_abs_exit_conv | 211,183 | +5.59% | 1 | 100% | 255 |
| snake_abs_exit | 211,020 | +5.51% | 1 | 100% | 260 |
| intraweek | 208,922 | +4.46% | 25 | 48% | 2,757 |
| snake_abs | 208,093 | +4.05% | 1 | 100% | 255 |
| snake_abs_conv | 207,933 | +3.97% | 1 | 100% | 255 |
| benchmark | 207,451 | +3.73% | 0 | - | 237 |
| snake_viper_wild | 207,184 | +3.59% | 3 | 33% | 702 |
| intramonth | 206,202 | +3.10% | 0 | - | 235 |
| snake_viper_tick | 203,576 | +1.79% | 2 | 0% | 532 |
| random_hold | 202,844 | +1.42% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,184 | +0.59% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,528 | -0.24% | 3 | 33% | 361 |
| benchmark_smallcap | 194,518 | -2.74% | 0 | - | 237 |
| gold | 190,835 | -4.58% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,270 (-5.36%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +7,005 | +3.43% |
| snake_abs_exit_conv | +6,845 | +3.35% |
| snake_abs_conv | +6,792 | +3.38% |
| snake_abs | +6,784 | +3.37% |
| snake_anaconda | +5,704 | +2.94% |
| gold | +5,557 | +3.00% |
| intraweek | +3,837 | +1.87% |
| random_hold | +2,375 | +1.19% |
| intramonth | +2,231 | +1.09% |
| unified | +1,977 | +0.93% |
| benchmark_smallcap | +1,581 | +0.82% |
| oracle | +1,195 | +0.60% |
| benchmark | +750 | +0.36% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,590 | -1.73% |
| snake_viper_wild | -3,708 | -1.76% |

Average per day so far: unified Rs +518, snake_abs_exit_conv Rs +466, snake_abs_exit Rs +459, snake_viper_wild Rs +378, snake_abs_conv Rs +331, intraweek Rs +330, snake_abs Rs +324, benchmark Rs +276, intramonth Rs +230, snake_viper_tick Rs +224, random_hold Rs +105, nifty_calls Rs +68, oracle Rs +44, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -21, benchmark_smallcap Rs -238, gold Rs -339, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.