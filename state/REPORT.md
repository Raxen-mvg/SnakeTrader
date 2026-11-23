# Paper trading report

Updated 2026-11-23 15:11 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,062 | +12.03% | 0 | - | 236 |
| benchmark | 221,450 | +10.72% | 0 | - | 237 |
| oracle | 212,290 | +6.14% | 0 | - | 233 |
| intramonth | 212,028 | +6.01% | 0 | - | 235 |
| intraweek | 211,436 | +5.72% | 40 | 55% | 4,400 |
| random_hold | 208,467 | +4.23% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,680 | +3.84% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,192 | +3.60% | 2 | 50% | 345 |
| snake_abs | 205,572 | +2.79% | 1 | 100% | 255 |
| snake_abs_conv | 205,415 | +2.71% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,172 | +0.59% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,551 | -0.22% | 0 | - | 237 |
| snake_anaconda | 198,901 | -0.55% | 3 | 33% | 374 |
| snake_viper_tick | 197,740 | -1.13% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,298 | -15.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,183 (-4.91%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,249 | +0.74% |
| snake_abs_exit_conv | +576 | +0.28% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -188 | -0.09% |
| snake_abs | -348 | -0.17% |
| snake_abs_conv | -368 | -0.18% |
| snake_abs_exit | -882 | -0.42% |
| snake_anaconda | -1,004 | -0.50% |
| benchmark_smallcap | -1,356 | -0.68% |
| snake_viper_tick | -1,632 | -0.82% |
| snake_viper_wild | -1,657 | -0.82% |
| unified | -2,120 | -0.94% |
| random_hold | -2,292 | -1.09% |
| intramonth | -2,976 | -1.38% |
| benchmark | -3,687 | -1.64% |
| intraweek | -4,276 | -1.98% |

Average per day so far: unified Rs +617, benchmark Rs +550, oracle Rs +315, intramonth Rs +308, intraweek Rs +293, random_hold Rs +217, snake_abs_exit Rs +213, snake_abs_exit_conv Rs +200, snake_abs Rs +151, snake_abs_conv Rs +150, nifty_calls Rs +47, snake_viper_wild Rs +38, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -32, snake_viper_tick Rs -81, snake_nonews Rs -300, snake Rs -320, gold Rs -787

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.