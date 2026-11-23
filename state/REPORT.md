# Paper trading report

Updated 2026-11-23 14:10 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,847 | +11.92% | 0 | - | 236 |
| benchmark | 221,986 | +10.99% | 0 | - | 237 |
| intraweek | 212,182 | +6.09% | 40 | 55% | 4,400 |
| intramonth | 212,016 | +6.01% | 0 | - | 235 |
| oracle | 211,631 | +5.82% | 0 | - | 233 |
| random_hold | 208,877 | +4.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,640 | +3.32% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,756 | +2.88% | 2 | 50% | 345 |
| snake_abs | 204,270 | +2.13% | 1 | 100% | 255 |
| snake_abs_conv | 204,094 | +2.05% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,827 | +0.41% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,271 | -0.36% | 0 | - | 237 |
| snake_anaconda | 197,689 | -1.16% | 3 | 33% | 374 |
| snake_viper_tick | 197,401 | -1.30% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,216 | -15.39% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,006 (-5.00%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,167 | +0.69% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -848 | -0.40% |
| snake_abs_exit_conv | -861 | -0.42% |
| benchmark_smallcap | -1,637 | -0.81% |
| snake_abs | -1,650 | -0.80% |
| snake_abs_conv | -1,689 | -0.82% |
| random_hold | -1,883 | -0.89% |
| snake_abs_exit | -1,922 | -0.92% |
| snake_viper_tick | -1,970 | -0.99% |
| snake_viper_wild | -2,003 | -0.99% |
| snake_anaconda | -2,217 | -1.11% |
| unified | -2,335 | -1.03% |
| intramonth | -2,988 | -1.39% |
| benchmark | -3,152 | -1.40% |
| intraweek | -3,530 | -1.64% |

Average per day so far: unified Rs +611, benchmark Rs +564, intraweek Rs +312, intramonth Rs +308, oracle Rs +298, random_hold Rs +228, snake_abs_exit Rs +184, snake_abs_exit_conv Rs +160, snake_abs Rs +115, snake_abs_conv Rs +114, nifty_calls Rs +47, snake_viper_wild Rs +27, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -21, snake_anaconda Rs -68, snake_viper_tick Rs -93, snake_nonews Rs -300, snake Rs -320, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.