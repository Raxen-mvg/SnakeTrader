# Paper trading report

Updated 2026-11-04 14:22 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,820 | +7.41% | 0 | - | 236 |
| snake_abs_exit_conv | 214,144 | +7.07% | 1 | 100% | 255 |
| snake_abs_exit | 213,992 | +7.00% | 1 | 100% | 260 |
| snake_abs | 211,028 | +5.51% | 1 | 100% | 255 |
| snake_abs_conv | 210,878 | +5.44% | 1 | 100% | 255 |
| intraweek | 209,456 | +4.73% | 25 | 48% | 2,757 |
| benchmark | 208,461 | +4.23% | 0 | - | 237 |
| snake_viper_wild | 207,571 | +3.79% | 3 | 33% | 702 |
| intramonth | 207,151 | +3.58% | 0 | - | 235 |
| snake_viper_tick | 203,951 | +1.98% | 2 | 0% | 532 |
| random_hold | 203,052 | +1.53% | 8 | 62% | 649 |
| snake_anaconda | 202,437 | +1.22% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,172 | +0.59% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,233 | -1.88% | 0 | - | 237 |
| gold | 191,377 | -4.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,761 (-5.12%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,978 | +4.89% |
| snake_abs_exit_conv | +9,806 | +4.80% |
| snake_abs_conv | +9,737 | +4.84% |
| snake_abs | +9,719 | +4.83% |
| snake_anaconda | +8,613 | +4.44% |
| gold | +6,099 | +3.29% |
| intraweek | +4,371 | +2.13% |
| benchmark_smallcap | +3,296 | +1.71% |
| intramonth | +3,180 | +1.56% |
| unified | +2,819 | +1.33% |
| random_hold | +2,584 | +1.29% |
| benchmark | +1,760 | +0.85% |
| oracle | +1,182 | +0.59% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,216 | -1.55% |
| snake_viper_wild | -3,321 | -1.57% |

Average per day so far: snake_abs_exit_conv Rs +589, snake_abs_exit Rs +583, unified Rs +549, snake_abs_conv Rs +453, snake_abs Rs +441, snake_viper_wild Rs +398, intraweek Rs +350, benchmark Rs +313, intramonth Rs +265, snake_viper_tick Rs +247, random_hold Rs +113, snake_anaconda Rs +111, nifty_calls Rs +68, oracle Rs +43, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -164, gold Rs -319, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.