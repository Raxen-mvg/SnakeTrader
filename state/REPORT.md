# Paper trading report

Updated 2026-11-18 10:23 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,444 | +11.22% | 0 | - | 236 |
| benchmark | 220,364 | +10.18% | 0 | - | 237 |
| intraweek | 214,903 | +7.45% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,565 | +6.28% | 2 | 50% | 345 |
| intramonth | 212,333 | +6.17% | 0 | - | 235 |
| oracle | 212,291 | +6.14% | 0 | - | 233 |
| snake_abs_exit_conv | 210,860 | +5.43% | 2 | 50% | 345 |
| snake_abs | 207,991 | +4.00% | 1 | 100% | 255 |
| snake_abs_conv | 207,840 | +3.92% | 1 | 100% | 255 |
| random_hold | 207,403 | +3.70% | 10 | 70% | 733 |
| snake_viper_wild | 207,121 | +3.56% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,583 | +1.79% | 15 | 47% | 2,625 |
| snake_anaconda | 202,656 | +1.33% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,156 | +0.08% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,370 | -11.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,466 (-4.27%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,580 | +0.74% |
| unified | +1,005 | +0.45% |
| intramonth | +791 | +0.37% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -196 | -0.09% |
| benchmark_smallcap | -415 | -0.21% |
| snake_abs | -567 | -0.27% |
| snake_abs_exit | -577 | -0.27% |
| snake_abs_conv | -580 | -0.28% |
| snake_abs_exit_conv | -714 | -0.34% |
| random_hold | -1,030 | -0.49% |
| benchmark | -1,239 | -0.56% |
| snake_anaconda | -1,399 | -0.69% |
| snake_viper_tick | -2,253 | -1.09% |
| snake_viper_wild | -2,294 | -1.09% |
| gold | -3,354 | -1.86% |

Average per day so far: unified Rs +623, benchmark Rs +566, intraweek Rs +414, snake_abs_exit Rs +381, intramonth Rs +343, oracle Rs +341, snake_abs_exit_conv Rs +329, snake_viper_wild Rs +254, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +206, snake_viper_tick Rs +143, snake_anaconda Rs +86, nifty_calls Rs +51, benchmark_smallcap Rs +5, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -326, snake Rs -347, gold Rs -629

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.