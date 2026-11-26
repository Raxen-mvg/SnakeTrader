# Paper trading report

Updated 2026-11-26 15:04 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,948 | +12.97% | 0 | - | 237 |
| unified | 223,038 | +11.52% | 0 | - | 236 |
| oracle | 212,511 | +6.25% | 0 | - | 233 |
| intramonth | 210,448 | +5.22% | 0 | - | 235 |
| random_hold | 208,662 | +4.33% | 13 | 69% | 1,037 |
| intraweek | 207,446 | +3.72% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,557 | +0.78% | 2 | 50% | 345 |
| benchmark_smallcap | 200,986 | +0.49% | 0 | - | 237 |
| snake_abs_exit_conv | 200,878 | +0.44% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,124 | -0.44% | 1 | 100% | 255 |
| snake_abs_conv | 198,942 | -0.53% | 1 | 100% | 255 |
| snake_anaconda | 192,819 | -3.59% | 3 | 33% | 374 |
| snake_viper_wild | 192,287 | -3.86% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,021 | -5.49% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,448 (-5.78%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,175 | +1.09% |
| gold | +1,463 | +0.89% |
| benchmark | +926 | +0.41% |
| intraweek | +703 | +0.34% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -699 | -0.35% |
| random_hold | -830 | -0.40% |
| snake_abs | -1,026 | -0.51% |
| snake_abs_conv | -1,030 | -0.52% |
| unified | -1,062 | -0.47% |
| snake_abs_exit_conv | -1,098 | -0.54% |
| intramonth | -1,245 | -0.59% |
| oracle | -1,284 | -0.60% |
| snake_anaconda | -1,734 | -0.89% |
| snake_viper_tick | -5,156 | -2.65% |
| snake_viper_wild | -5,256 | -2.66% |

Average per day so far: benchmark Rs +633, unified Rs +562, oracle Rs +305, intramonth Rs +255, random_hold Rs +211, intraweek Rs +182, nifty_calls Rs +45, snake_abs_exit Rs +41, benchmark_smallcap Rs +27, snake_abs_exit_conv Rs +23, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -22, snake_abs_conv Rs -28, snake_anaconda Rs -199, snake_viper_wild Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -366, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.