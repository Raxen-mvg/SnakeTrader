# Paper trading report

Updated 2026-11-04 14:07 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,423 | +7.21% | 0 | - | 236 |
| snake_abs_exit_conv | 213,444 | +6.72% | 1 | 100% | 255 |
| snake_abs_exit | 213,302 | +6.65% | 1 | 100% | 260 |
| snake_abs | 210,337 | +5.17% | 1 | 100% | 255 |
| snake_abs_conv | 210,187 | +5.09% | 1 | 100% | 255 |
| intraweek | 209,966 | +4.98% | 25 | 48% | 2,757 |
| benchmark | 208,178 | +4.09% | 0 | - | 237 |
| snake_viper_wild | 207,575 | +3.79% | 3 | 33% | 702 |
| intramonth | 206,523 | +3.26% | 0 | - | 235 |
| snake_viper_tick | 203,953 | +1.98% | 2 | 0% | 532 |
| random_hold | 202,992 | +1.50% | 8 | 62% | 649 |
| snake_anaconda | 202,010 | +1.00% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,083 | +0.54% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,042 | -1.98% | 0 | - | 237 |
| gold | 191,213 | -4.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,670 (-5.17%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,288 | +4.55% |
| snake_abs_exit_conv | +9,106 | +4.46% |
| snake_abs_conv | +9,046 | +4.50% |
| snake_abs | +9,028 | +4.49% |
| snake_anaconda | +8,186 | +4.22% |
| gold | +5,935 | +3.20% |
| intraweek | +4,881 | +2.38% |
| benchmark_smallcap | +3,105 | +1.61% |
| intramonth | +2,552 | +1.25% |
| random_hold | +2,524 | +1.26% |
| unified | +2,422 | +1.14% |
| benchmark | +1,476 | +0.71% |
| oracle | +1,094 | +0.55% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,214 | -1.55% |
| snake_viper_wild | -3,317 | -1.57% |

Average per day so far: snake_abs_exit_conv Rs +560, snake_abs_exit Rs +554, unified Rs +534, snake_abs_conv Rs +424, snake_abs Rs +413, snake_viper_wild Rs +399, intraweek Rs +369, benchmark Rs +303, snake_viper_tick Rs +247, intramonth Rs +242, random_hold Rs +111, snake_anaconda Rs +91, nifty_calls Rs +68, oracle Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -172, gold Rs -325, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.