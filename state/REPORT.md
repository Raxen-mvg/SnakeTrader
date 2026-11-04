# Paper trading report

Updated 2026-11-04 09:42 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 211,205 | +5.60% | 0 | - | 236 |
| benchmark | 208,491 | +4.25% | 0 | - | 237 |
| snake_abs_exit_conv | 208,028 | +4.01% | 1 | 100% | 255 |
| snake_abs_exit | 207,792 | +3.90% | 1 | 100% | 260 |
| snake_viper_wild | 207,453 | +3.73% | 3 | 33% | 702 |
| intraweek | 206,589 | +3.29% | 25 | 48% | 2,757 |
| snake_abs | 204,953 | +2.48% | 1 | 100% | 255 |
| snake_abs_conv | 204,792 | +2.40% | 1 | 100% | 255 |
| intramonth | 204,740 | +2.37% | 0 | - | 235 |
| snake_viper_tick | 203,834 | +1.92% | 2 | 0% | 532 |
| random_hold | 203,147 | +1.57% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| oracle | 199,829 | -0.09% | 0 | - | 233 |
| snake_anaconda | 196,805 | -1.60% | 3 | 33% | 361 |
| benchmark_smallcap | 193,699 | -3.15% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 187,432 | -6.28% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,234 (-5.88%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,778 | +1.85% |
| snake_abs_exit_conv | +3,690 | +1.81% |
| snake_abs_conv | +3,651 | +1.81% |
| snake_abs | +3,644 | +1.81% |
| snake_anaconda | +2,981 | +1.54% |
| random_hold | +2,679 | +1.34% |
| gold | +2,154 | +1.16% |
| benchmark | +1,790 | +0.87% |
| intraweek | +1,504 | +0.73% |
| intramonth | +769 | +0.38% |
| benchmark_smallcap | +762 | +0.40% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -160 | -0.08% |
| unified | -796 | -0.38% |
| snake_viper_tick | -3,333 | -1.61% |
| snake_viper_wild | -3,440 | -1.63% |

Average per day so far: unified Rs +415, snake_viper_wild Rs +392, snake_abs_exit_conv Rs +335, snake_abs_exit Rs +325, benchmark Rs +314, intraweek Rs +244, snake_viper_tick Rs +240, snake_abs_conv Rs +200, snake_abs Rs +198, intramonth Rs +176, random_hold Rs +117, nifty_calls Rs +68, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, oracle Rs -6, snake_anaconda Rs -145, benchmark_smallcap Rs -274, snake_nonews Rs -444, gold Rs -465, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.