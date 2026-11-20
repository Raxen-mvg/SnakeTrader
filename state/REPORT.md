# Paper trading report

Updated 2026-11-20 11:02 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,216 | +12.61% | 0 | - | 236 |
| benchmark | 222,965 | +11.48% | 0 | - | 237 |
| intramonth | 214,124 | +7.06% | 0 | - | 235 |
| intraweek | 213,725 | +6.86% | 35 | 54% | 3,851 |
| oracle | 212,852 | +6.43% | 0 | - | 233 |
| snake_abs_exit | 210,670 | +5.33% | 2 | 50% | 345 |
| random_hold | 209,063 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,294 | +4.15% | 2 | 50% | 345 |
| snake_abs | 207,464 | +3.73% | 1 | 100% | 255 |
| snake_abs_conv | 207,324 | +3.66% | 1 | 100% | 255 |
| snake_viper_wild | 206,834 | +3.42% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,303 | +1.65% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,519 | +0.76% | 3 | 33% | 374 |
| benchmark_smallcap | 200,302 | +0.15% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,909 | -17.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,798 (-4.10%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +836 | +0.39% |
| oracle | +763 | +0.36% |
| random_hold | +610 | +0.29% |
| unified | +601 | +0.27% |
| benchmark | +589 | +0.27% |
| intramonth | +116 | +0.05% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -674 | -0.33% |
| snake_viper_wild | -689 | -0.33% |
| benchmark_smallcap | -1,166 | -0.58% |
| snake_abs | -1,515 | -0.72% |
| snake_abs_conv | -1,536 | -0.73% |
| snake_anaconda | -1,944 | -0.96% |
| snake_abs_exit | -2,682 | -1.26% |
| snake_abs_exit_conv | -2,770 | -1.31% |
| gold | -9,864 | -5.64% |

Average per day so far: unified Rs +664, benchmark Rs +604, intramonth Rs +372, intraweek Rs +361, oracle Rs +338, snake_abs_exit Rs +305, random_hold Rs +239, snake_abs_exit_conv Rs +237, snake_viper_wild Rs +228, snake_abs_conv Rs +209, snake_abs Rs +207, snake_viper_tick Rs +122, nifty_calls Rs +48, snake_anaconda Rs +46, benchmark_smallcap Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -923

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.