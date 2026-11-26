# Paper trading report

Updated 2026-11-26 15:25 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,933 | +12.97% | 0 | - | 237 |
| unified | 223,046 | +11.52% | 0 | - | 236 |
| oracle | 212,049 | +6.02% | 0 | - | 233 |
| intramonth | 210,561 | +5.28% | 0 | - | 235 |
| random_hold | 208,565 | +4.28% | 13 | 69% | 1,037 |
| intraweek | 207,178 | +3.59% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,480 | +0.74% | 2 | 50% | 345 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| snake_abs_exit_conv | 200,766 | +0.38% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,935 | -0.53% | 1 | 100% | 255 |
| snake_abs_conv | 198,752 | -0.62% | 1 | 100% | 255 |
| snake_anaconda | 192,723 | -3.64% | 3 | 33% | 374 |
| snake_viper_wild | 192,705 | -3.65% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,430 | -5.29% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,977 | -17.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,312 (-5.84%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,973 | +0.99% |
| gold | +1,381 | +0.84% |
| benchmark | +910 | +0.41% |
| intraweek | +435 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -775 | -0.38% |
| random_hold | -927 | -0.44% |
| unified | -1,054 | -0.47% |
| intramonth | -1,132 | -0.54% |
| snake_abs_exit_conv | -1,210 | -0.60% |
| snake_abs | -1,215 | -0.61% |
| snake_abs_conv | -1,220 | -0.61% |
| oracle | -1,747 | -0.82% |
| snake_anaconda | -1,830 | -0.94% |
| snake_viper_tick | -4,747 | -2.44% |
| snake_viper_wild | -4,839 | -2.45% |

Average per day so far: benchmark Rs +633, unified Rs +562, oracle Rs +294, intramonth Rs +258, random_hold Rs +209, intraweek Rs +175, nifty_calls Rs +45, snake_abs_exit Rs +39, benchmark_smallcap Rs +21, snake_abs_exit_conv Rs +20, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -27, snake_abs_conv Rs -33, snake_anaconda Rs -202, snake_viper_wild Rs -221, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -352, gold Rs -830

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.