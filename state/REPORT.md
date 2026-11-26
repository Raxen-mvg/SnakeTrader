# Paper trading report

Updated 2026-11-26 11:26 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,841 | +12.92% | 0 | - | 237 |
| unified | 223,172 | +11.59% | 0 | - | 236 |
| oracle | 213,011 | +6.50% | 0 | - | 233 |
| intramonth | 210,435 | +5.22% | 0 | - | 235 |
| random_hold | 209,760 | +4.88% | 13 | 69% | 1,037 |
| intraweek | 208,216 | +4.11% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,658 | +0.83% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,149 | +0.57% | 2 | 50% | 345 |
| benchmark_smallcap | 200,325 | +0.16% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,407 | -0.30% | 1 | 100% | 255 |
| snake_abs_conv | 199,219 | -0.39% | 1 | 100% | 255 |
| snake_anaconda | 193,341 | -3.33% | 3 | 33% | 374 |
| snake_viper_wild | 193,329 | -3.34% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,041 | -4.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,849 | -16.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,779 (-5.61%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,252 | +1.37% |
| benchmark_smallcap | +1,513 | +0.76% |
| intraweek | +1,473 | +0.71% |
| benchmark | +819 | +0.36% |
| random_hold | +268 | +0.13% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -597 | -0.29% |
| snake_abs | -743 | -0.37% |
| snake_abs_conv | -753 | -0.38% |
| oracle | -784 | -0.37% |
| snake_abs_exit_conv | -826 | -0.41% |
| unified | -928 | -0.41% |
| snake_anaconda | -1,212 | -0.62% |
| intramonth | -1,258 | -0.59% |
| snake_viper_tick | -4,136 | -2.13% |
| snake_viper_wild | -4,215 | -2.13% |

Average per day so far: benchmark Rs +630, unified Rs +565, oracle Rs +317, intramonth Rs +255, random_hold Rs +238, intraweek Rs +200, nifty_calls Rs +45, snake_abs_exit Rs +44, snake_abs_exit_conv Rs +30, benchmark_smallcap Rs +9, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -15, snake_abs_conv Rs -21, snake_anaconda Rs -185, snake_viper_wild Rs -202, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -332, gold Rs -809

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.