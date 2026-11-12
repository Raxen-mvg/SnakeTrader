# Paper trading report

Updated 2026-11-12 13:24 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,436 | +10.72% | 0 | - | 236 |
| benchmark | 220,089 | +10.04% | 0 | - | 237 |
| snake_abs_exit_conv | 218,322 | +9.16% | 2 | 50% | 345 |
| snake_abs_exit | 217,371 | +8.69% | 2 | 50% | 345 |
| snake_abs | 215,555 | +7.78% | 1 | 100% | 255 |
| snake_abs_conv | 215,379 | +7.69% | 1 | 100% | 255 |
| intraweek | 214,384 | +7.19% | 30 | 53% | 3,302 |
| oracle | 213,298 | +6.65% | 0 | - | 233 |
| intramonth | 212,039 | +6.02% | 0 | - | 235 |
| random_hold | 208,045 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,203 | +3.60% | 10 | 50% | 1,825 |
| snake_anaconda | 206,167 | +3.08% | 3 | 33% | 374 |
| snake_viper_tick | 203,658 | +1.83% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,093 | +1.55% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,116 | -6.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,127 (-3.94%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,287 | +1.14% |
| snake_anaconda | +2,044 | +1.00% |
| snake_abs | +1,930 | +0.90% |
| snake_abs_conv | +1,921 | +0.90% |
| unified | +1,622 | +0.74% |
| oracle | +1,295 | +0.61% |
| intraweek | +1,251 | +0.59% |
| snake_abs_exit | +1,209 | +0.56% |
| snake_abs_exit_conv | +1,170 | +0.54% |
| intramonth | +1,043 | +0.49% |
| random_hold | +935 | +0.45% |
| benchmark | +826 | +0.38% |
| snake_viper_wild | +461 | +0.22% |
| snake_viper_tick | +449 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,469 | -1.83% |

Average per day so far: unified Rs +670, snake_abs_exit_conv Rs +632, benchmark Rs +628, snake_abs_exit Rs +599, snake_abs_conv Rs +530, snake_abs Rs +518, intraweek Rs +450, oracle Rs +416, intramonth Rs +376, snake_viper_wild Rs +300, random_hold Rs +251, snake_anaconda Rs +228, snake_viper_tick Rs +174, benchmark_smallcap Rs +110, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.