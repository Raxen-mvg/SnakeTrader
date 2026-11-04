# Paper trading report

Updated 2026-11-04 13:49 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,420 | +7.21% | 0 | - | 236 |
| snake_abs_exit_conv | 213,013 | +6.51% | 1 | 100% | 255 |
| snake_abs_exit | 212,857 | +6.43% | 1 | 100% | 260 |
| snake_abs | 209,919 | +4.96% | 1 | 100% | 255 |
| snake_abs_conv | 209,762 | +4.88% | 1 | 100% | 255 |
| intraweek | 209,402 | +4.70% | 25 | 48% | 2,757 |
| benchmark | 208,407 | +4.20% | 0 | - | 237 |
| snake_viper_wild | 207,042 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,636 | +3.32% | 0 | - | 235 |
| snake_viper_tick | 203,432 | +1.72% | 2 | 0% | 532 |
| random_hold | 202,881 | +1.44% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,577 | +0.79% | 3 | 33% | 361 |
| oracle | 201,283 | +0.64% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,076 | -1.96% | 0 | - | 237 |
| gold | 191,131 | -4.43% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,444 (-5.28%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,843 | +4.33% |
| snake_abs_exit_conv | +8,675 | +4.25% |
| snake_abs_conv | +8,621 | +4.29% |
| snake_abs | +8,610 | +4.28% |
| snake_anaconda | +7,753 | +4.00% |
| gold | +5,853 | +3.16% |
| intraweek | +4,317 | +2.10% |
| benchmark_smallcap | +3,139 | +1.63% |
| intramonth | +2,665 | +1.31% |
| unified | +2,420 | +1.14% |
| random_hold | +2,413 | +1.20% |
| benchmark | +1,706 | +0.82% |
| oracle | +1,293 | +0.65% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,734 | -1.80% |
| snake_viper_wild | -3,851 | -1.83% |

Average per day so far: snake_abs_exit_conv Rs +542, snake_abs_exit Rs +536, unified Rs +534, snake_abs_conv Rs +407, snake_abs Rs +397, snake_viper_wild Rs +371, intraweek Rs +348, benchmark Rs +311, intramonth Rs +246, snake_viper_tick Rs +215, random_hold Rs +107, snake_anaconda Rs +72, nifty_calls Rs +68, oracle Rs +48, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -171, gold Rs -328, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.