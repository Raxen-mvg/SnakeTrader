# Paper trading report

Updated 2026-11-04 14:58 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,386 | +7.19% | 0 | - | 236 |
| snake_abs_exit_conv | 213,819 | +6.91% | 1 | 100% | 255 |
| snake_abs_exit | 213,695 | +6.85% | 1 | 100% | 260 |
| snake_abs | 210,699 | +5.35% | 1 | 100% | 255 |
| snake_abs_conv | 210,558 | +5.28% | 1 | 100% | 255 |
| intraweek | 209,624 | +4.81% | 25 | 48% | 2,757 |
| benchmark | 208,652 | +4.33% | 0 | - | 237 |
| snake_viper_wild | 208,324 | +4.16% | 3 | 33% | 702 |
| intramonth | 206,943 | +3.47% | 0 | - | 235 |
| snake_viper_tick | 204,700 | +2.35% | 2 | 0% | 532 |
| random_hold | 202,867 | +1.43% | 8 | 62% | 649 |
| snake_anaconda | 202,516 | +1.26% | 3 | 33% | 361 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,392 | +0.70% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 196,468 | -1.77% | 0 | - | 237 |
| gold | 191,607 | -4.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,885 (-5.06%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +9,681 | +4.75% |
| snake_abs_exit_conv | +9,481 | +4.64% |
| snake_abs_conv | +9,417 | +4.68% |
| snake_abs | +9,390 | +4.66% |
| snake_anaconda | +8,692 | +4.48% |
| gold | +6,329 | +3.42% |
| intraweek | +4,539 | +2.21% |
| benchmark_smallcap | +3,531 | +1.83% |
| intramonth | +2,972 | +1.46% |
| random_hold | +2,399 | +1.20% |
| unified | +2,385 | +1.12% |
| benchmark | +1,951 | +0.94% |
| oracle | +1,403 | +0.70% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -2,467 | -1.19% |
| snake_viper_wild | -2,569 | -1.22% |

Average per day so far: snake_abs_exit_conv Rs +576, snake_abs_exit Rs +571, unified Rs +533, snake_abs_conv Rs +440, snake_viper_wild Rs +438, snake_abs Rs +428, intraweek Rs +356, benchmark Rs +320, snake_viper_tick Rs +294, intramonth Rs +257, snake_anaconda Rs +114, random_hold Rs +106, nifty_calls Rs +68, oracle Rs +52, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -154, gold Rs -311, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.