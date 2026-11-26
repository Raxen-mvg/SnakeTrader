# Paper trading report

Updated 2026-11-26 13:48 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,604 | +12.80% | 0 | - | 237 |
| unified | 223,185 | +11.59% | 0 | - | 236 |
| oracle | 213,159 | +6.58% | 0 | - | 233 |
| intramonth | 210,348 | +5.17% | 0 | - | 235 |
| random_hold | 209,207 | +4.60% | 13 | 69% | 1,037 |
| intraweek | 207,703 | +3.85% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,448 | +0.22% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,961 | -0.02% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,361 | -0.32% | 2 | 50% | 345 |
| snake_abs | 197,720 | -1.14% | 1 | 100% | 255 |
| snake_abs_conv | 197,513 | -1.24% | 1 | 100% | 255 |
| snake_viper_wild | 192,158 | -3.92% | 16 | 50% | 2,827 |
| snake_anaconda | 191,420 | -4.29% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,894 | -5.55% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,524 (-5.74%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,637 | +0.82% |
| gold | +1,463 | +0.89% |
| intraweek | +960 | +0.46% |
| benchmark | +581 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -286 | -0.14% |
| oracle | -636 | -0.30% |
| unified | -914 | -0.41% |
| intramonth | -1,345 | -0.64% |
| snake_abs_exit | -2,295 | -1.14% |
| snake_abs | -2,430 | -1.21% |
| snake_abs_conv | -2,459 | -1.23% |
| snake_abs_exit_conv | -2,615 | -1.29% |
| snake_anaconda | -3,133 | -1.61% |
| snake_viper_tick | -5,283 | -2.72% |
| snake_viper_wild | -5,386 | -2.73% |

Average per day so far: benchmark Rs +624, unified Rs +565, oracle Rs +321, intramonth Rs +252, random_hold Rs +225, intraweek Rs +188, nifty_calls Rs +45, benchmark_smallcap Rs +12, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -1, snake_abs_exit_conv Rs -17, snake_abs Rs -58, snake_abs_conv Rs -65, snake_viper_wild Rs -238, snake_anaconda Rs -238, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -370, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.