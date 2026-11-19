# Paper trading report

Updated 2026-11-19 10:10 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,034 | +12.02% | 0 | - | 236 |
| benchmark | 220,563 | +10.28% | 0 | - | 237 |
| intramonth | 213,803 | +6.90% | 0 | - | 235 |
| snake_abs_exit | 213,200 | +6.60% | 2 | 50% | 345 |
| intraweek | 213,121 | +6.56% | 35 | 54% | 3,851 |
| oracle | 212,272 | +6.14% | 0 | - | 233 |
| snake_abs_exit_conv | 211,364 | +5.68% | 2 | 50% | 345 |
| snake_abs | 208,684 | +4.34% | 1 | 100% | 255 |
| snake_abs_conv | 208,550 | +4.28% | 1 | 100% | 255 |
| random_hold | 207,943 | +3.97% | 10 | 70% | 733 |
| snake_viper_wild | 207,678 | +3.84% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,128 | +2.06% | 15 | 47% | 2,625 |
| snake_anaconda | 203,884 | +1.94% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,559 | -12.72% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,827 (-4.09%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,530 | +0.72% |
| oracle | +1,476 | +0.70% |
| unified | +1,422 | +0.64% |
| intraweek | +1,282 | +0.60% |
| benchmark_smallcap | +1,233 | +0.62% |
| random_hold | +1,010 | +0.49% |
| snake_viper_wild | +638 | +0.31% |
| snake_viper_tick | +625 | +0.31% |
| benchmark | +268 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -517 | -0.25% |
| snake_abs | -753 | -0.36% |
| snake_abs_conv | -775 | -0.37% |
| snake_abs_exit | -831 | -0.39% |
| snake_abs_exit_conv | -1,020 | -0.48% |
| gold | -2,762 | -1.56% |

Average per day so far: unified Rs +650, benchmark Rs +556, snake_abs_exit Rs +388, intramonth Rs +373, intraweek Rs +355, snake_abs_exit_conv Rs +334, oracle Rs +332, snake_viper_wild Rs +265, snake_abs_conv Rs +251, snake_abs Rs +248, random_hold Rs +215, snake_viper_tick Rs +159, snake_anaconda Rs +121, nifty_calls Rs +50, benchmark_smallcap Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -688

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.