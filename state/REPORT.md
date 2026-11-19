# Paper trading report

Updated 2026-11-19 14:22 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,457 | +11.73% | 0 | - | 236 |
| benchmark | 222,254 | +11.13% | 0 | - | 237 |
| snake_abs_exit | 213,223 | +6.61% | 2 | 50% | 345 |
| intramonth | 213,099 | +6.55% | 0 | - | 235 |
| intraweek | 211,801 | +5.90% | 35 | 54% | 3,851 |
| oracle | 211,263 | +5.63% | 0 | - | 233 |
| snake_abs_exit_conv | 210,968 | +5.48% | 2 | 50% | 345 |
| snake_abs | 208,839 | +4.42% | 1 | 100% | 255 |
| snake_abs_conv | 208,715 | +4.36% | 1 | 100% | 255 |
| random_hold | 207,949 | +3.97% | 10 | 70% | 733 |
| snake_viper_wild | 207,595 | +3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,047 | +2.02% | 15 | 47% | 2,625 |
| snake_anaconda | 203,341 | +1.67% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,795 | +0.40% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,888 | -12.56% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,181 (-4.41%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,958 | +0.89% |
| benchmark_smallcap | +1,469 | +0.74% |
| random_hold | +1,016 | +0.49% |
| unified | +845 | +0.38% |
| intramonth | +825 | +0.39% |
| snake_viper_wild | +555 | +0.27% |
| snake_viper_tick | +544 | +0.27% |
| oracle | +467 | +0.22% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -39 | -0.02% |
| snake_abs | -598 | -0.28% |
| snake_abs_conv | -610 | -0.29% |
| snake_abs_exit | -809 | -0.38% |
| snake_anaconda | -1,060 | -0.52% |
| snake_abs_exit_conv | -1,416 | -0.67% |
| gold | -2,433 | -1.37% |

Average per day so far: unified Rs +634, benchmark Rs +601, snake_abs_exit Rs +389, intramonth Rs +354, snake_abs_exit_conv Rs +323, intraweek Rs +319, oracle Rs +304, snake_viper_wild Rs +262, snake_abs_conv Rs +256, snake_abs Rs +253, random_hold Rs +215, snake_viper_tick Rs +156, snake_anaconda Rs +104, nifty_calls Rs +50, benchmark_smallcap Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -679

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.