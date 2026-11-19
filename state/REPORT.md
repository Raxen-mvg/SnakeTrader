# Paper trading report

Updated 2026-11-19 12:18 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,911 | +11.96% | 0 | - | 236 |
| benchmark | 221,389 | +10.70% | 0 | - | 237 |
| intramonth | 213,438 | +6.72% | 0 | - | 235 |
| snake_abs_exit | 212,982 | +6.49% | 2 | 50% | 345 |
| intraweek | 211,497 | +5.75% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,120 | +5.56% | 2 | 50% | 345 |
| oracle | 210,889 | +5.44% | 0 | - | 233 |
| snake_abs | 208,719 | +4.36% | 1 | 100% | 255 |
| snake_abs_conv | 208,589 | +4.29% | 1 | 100% | 255 |
| random_hold | 207,617 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 207,600 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,052 | +2.03% | 15 | 47% | 2,625 |
| snake_anaconda | 202,982 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,549 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,118 | -12.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,177 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,300 | +0.58% |
| benchmark_smallcap | +1,222 | +0.61% |
| intramonth | +1,164 | +0.55% |
| benchmark | +1,094 | +0.50% |
| random_hold | +685 | +0.33% |
| snake_viper_wild | +560 | +0.27% |
| snake_viper_tick | +549 | +0.27% |
| oracle | +93 | +0.04% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -342 | -0.16% |
| snake_abs | -717 | -0.34% |
| snake_abs_conv | -736 | -0.35% |
| snake_abs_exit | -1,050 | -0.49% |
| snake_abs_exit_conv | -1,264 | -0.59% |
| snake_anaconda | -1,419 | -0.69% |
| gold | -2,203 | -1.24% |

Average per day so far: unified Rs +646, benchmark Rs +578, snake_abs_exit Rs +382, intramonth Rs +363, snake_abs_exit_conv Rs +327, intraweek Rs +311, oracle Rs +294, snake_viper_wild Rs +262, snake_abs_conv Rs +253, snake_abs Rs +249, random_hold Rs +206, snake_viper_tick Rs +156, snake_anaconda Rs +93, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.