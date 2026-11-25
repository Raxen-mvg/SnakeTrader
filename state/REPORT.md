# Paper trading report

Updated 2026-11-25 13:33 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,732 | +12.37% | 0 | - | 236 |
| benchmark | 224,556 | +12.28% | 0 | - | 237 |
| oracle | 212,612 | +6.31% | 0 | - | 233 |
| intramonth | 212,394 | +6.20% | 0 | - | 235 |
| random_hold | 209,814 | +4.91% | 12 | 75% | 1,009 |
| intraweek | 207,737 | +3.87% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,061 | +1.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,705 | +0.85% | 2 | 50% | 345 |
| snake_abs | 200,191 | +0.10% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_conv | 199,999 | -0.00% | 1 | 100% | 255 |
| benchmark_smallcap | 199,103 | -0.45% | 0 | - | 237 |
| snake_viper_wild | 197,390 | -1.30% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,026 | -2.99% | 15 | 47% | 2,625 |
| snake_anaconda | 193,728 | -3.14% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,580 | -17.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,186 (-5.41%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,083 | +1.39% |
| random_hold | +1,387 | +0.67% |
| unified | +446 | +0.20% |
| oracle | +270 | +0.13% |
| benchmark_smallcap | +123 | +0.06% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -357 | -0.17% |
| snake_viper_tick | -3,666 | -1.85% |
| snake_viper_wild | -3,735 | -1.86% |
| intraweek | -3,882 | -1.83% |
| gold | -4,850 | -2.86% |
| snake_anaconda | -4,975 | -2.50% |
| snake_abs | -5,270 | -2.56% |
| snake_abs_conv | -5,304 | -2.58% |
| snake_abs_exit_conv | -5,341 | -2.58% |
| snake_abs_exit | -5,434 | -2.62% |

Average per day so far: unified Rs +618, benchmark Rs +614, oracle Rs +315, intramonth Rs +310, random_hold Rs +245, intraweek Rs +193, snake_abs_exit Rs +56, snake_abs_exit_conv Rs +46, nifty_calls Rs +46, snake_abs Rs +5, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs_conv Rs -0, benchmark_smallcap Rs -25, snake_viper_wild Rs -82, snake_anaconda Rs -179, snake_viper_tick Rs -206, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.