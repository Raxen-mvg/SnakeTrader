# Paper trading report

Updated 2026-11-04 12:52 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,752 | +6.88% | 0 | - | 236 |
| snake_abs_exit_conv | 212,368 | +6.18% | 1 | 100% | 255 |
| snake_abs_exit | 212,237 | +6.12% | 1 | 100% | 260 |
| snake_abs | 209,266 | +4.63% | 1 | 100% | 255 |
| snake_abs_conv | 209,113 | +4.56% | 1 | 100% | 255 |
| intraweek | 208,930 | +4.46% | 25 | 48% | 2,757 |
| benchmark | 207,902 | +3.95% | 0 | - | 237 |
| snake_viper_wild | 207,063 | +3.53% | 3 | 33% | 702 |
| intramonth | 206,138 | +3.07% | 0 | - | 235 |
| snake_viper_tick | 203,454 | +1.73% | 2 | 0% | 532 |
| random_hold | 202,855 | +1.43% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,069 | +0.54% | 0 | - | 233 |
| snake_anaconda | 200,770 | +0.39% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 194,955 | -2.52% | 0 | - | 237 |
| gold | 190,588 | -4.71% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,176 (-5.41%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,222 | +4.03% |
| snake_abs_exit_conv | +8,030 | +3.93% |
| snake_abs_conv | +7,972 | +3.96% |
| snake_abs | +7,956 | +3.95% |
| snake_anaconda | +6,946 | +3.58% |
| gold | +5,310 | +2.87% |
| intraweek | +3,844 | +1.87% |
| random_hold | +2,386 | +1.19% |
| intramonth | +2,167 | +1.06% |
| benchmark_smallcap | +2,018 | +1.05% |
| unified | +1,751 | +0.83% |
| benchmark | +1,201 | +0.58% |
| oracle | +1,080 | +0.54% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,713 | -1.79% |
| snake_viper_wild | -3,830 | -1.82% |

Average per day so far: snake_abs_exit_conv Rs +515, snake_abs_exit Rs +510, unified Rs +509, snake_abs_conv Rs +380, snake_viper_wild Rs +372, snake_abs Rs +371, intraweek Rs +331, benchmark Rs +293, intramonth Rs +227, snake_viper_tick Rs +216, random_hold Rs +106, nifty_calls Rs +68, oracle Rs +40, snake_anaconda Rs +35, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -219, gold Rs -349, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.