# Paper trading report

Updated 2026-11-04 10:33 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,047 | +6.52% | 0 | - | 236 |
| snake_abs_exit_conv | 208,760 | +4.38% | 1 | 100% | 255 |
| snake_abs_exit | 208,587 | +4.29% | 1 | 100% | 260 |
| intraweek | 208,335 | +4.17% | 25 | 48% | 2,757 |
| benchmark | 207,879 | +3.94% | 0 | - | 237 |
| snake_viper_wild | 206,746 | +3.37% | 3 | 33% | 702 |
| snake_abs | 205,669 | +2.83% | 1 | 100% | 255 |
| snake_abs_conv | 205,516 | +2.76% | 1 | 100% | 255 |
| intramonth | 205,413 | +2.71% | 0 | - | 235 |
| snake_viper_tick | 203,137 | +1.57% | 2 | 0% | 532 |
| random_hold | 202,321 | +1.16% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 200,231 | +0.12% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 197,499 | -1.25% | 3 | 33% | 361 |
| benchmark_smallcap | 194,439 | -2.78% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,415 | -6.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,749 (-5.63%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,573 | +2.24% |
| snake_abs_exit_conv | +4,422 | +2.16% |
| snake_abs_conv | +4,375 | +2.17% |
| snake_abs | +4,360 | +2.17% |
| snake_anaconda | +3,674 | +1.90% |
| intraweek | +3,249 | +1.58% |
| gold | +2,137 | +1.15% |
| random_hold | +1,853 | +0.92% |
| benchmark_smallcap | +1,502 | +0.78% |
| intramonth | +1,442 | +0.71% |
| benchmark | +1,178 | +0.57% |
| unified | +1,046 | +0.49% |
| oracle | +242 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -4,030 | -1.95% |
| snake_viper_wild | -4,146 | -1.97% |

Average per day so far: unified Rs +483, snake_abs_exit_conv Rs +365, snake_abs_exit Rs +358, snake_viper_wild Rs +355, intraweek Rs +309, benchmark Rs +292, snake_abs_conv Rs +230, snake_abs Rs +227, intramonth Rs +200, snake_viper_tick Rs +196, random_hold Rs +86, nifty_calls Rs +68, oracle Rs +9, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -114, benchmark_smallcap Rs -242, snake_nonews Rs -444, gold Rs -466, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.