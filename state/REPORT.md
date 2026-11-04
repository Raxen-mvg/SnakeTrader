# Paper trading report

Updated 2026-11-04 13:46 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,123 | +7.06% | 0 | - | 236 |
| snake_abs_exit_conv | 213,090 | +6.54% | 1 | 100% | 255 |
| snake_abs_exit | 212,932 | +6.47% | 1 | 100% | 260 |
| snake_abs | 209,991 | +5.00% | 1 | 100% | 255 |
| snake_abs_conv | 209,836 | +4.92% | 1 | 100% | 255 |
| intraweek | 209,378 | +4.69% | 25 | 48% | 2,757 |
| benchmark | 208,575 | +4.29% | 0 | - | 237 |
| snake_viper_wild | 207,047 | +3.52% | 3 | 33% | 702 |
| intramonth | 206,334 | +3.17% | 0 | - | 235 |
| snake_viper_tick | 203,437 | +1.72% | 2 | 0% | 532 |
| random_hold | 202,767 | +1.38% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,648 | +0.82% | 3 | 33% | 361 |
| oracle | 201,227 | +0.61% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,009 | -2.00% | 0 | - | 237 |
| gold | 191,213 | -4.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,339 (-5.33%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,918 | +4.37% |
| snake_abs_exit_conv | +8,751 | +4.28% |
| snake_abs_conv | +8,695 | +4.32% |
| snake_abs | +8,681 | +4.31% |
| snake_anaconda | +7,823 | +4.04% |
| gold | +5,935 | +3.20% |
| intraweek | +4,292 | +2.09% |
| benchmark_smallcap | +3,072 | +1.59% |
| intramonth | +2,363 | +1.16% |
| random_hold | +2,298 | +1.15% |
| unified | +2,122 | +1.00% |
| benchmark | +1,874 | +0.91% |
| oracle | +1,238 | +0.62% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,729 | -1.80% |
| snake_viper_wild | -3,845 | -1.82% |

Average per day so far: snake_abs_exit_conv Rs +545, snake_abs_exit Rs +539, unified Rs +523, snake_abs_conv Rs +410, snake_abs Rs +400, snake_viper_wild Rs +371, intraweek Rs +347, benchmark Rs +318, intramonth Rs +235, snake_viper_tick Rs +215, random_hold Rs +102, snake_anaconda Rs +75, nifty_calls Rs +68, oracle Rs +45, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -174, gold Rs -325, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.