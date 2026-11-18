# Paper trading report

Updated 2026-11-18 09:59 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,362 | +11.18% | 0 | - | 236 |
| benchmark | 220,517 | +10.26% | 0 | - | 237 |
| intraweek | 214,373 | +7.19% | 35 | 54% | 3,851 |
| snake_abs_exit | 212,534 | +6.27% | 2 | 50% | 345 |
| oracle | 212,328 | +6.16% | 0 | - | 233 |
| intramonth | 212,301 | +6.15% | 0 | - | 235 |
| snake_abs_exit_conv | 210,939 | +5.47% | 2 | 50% | 345 |
| snake_abs | 208,265 | +4.13% | 1 | 100% | 255 |
| snake_abs_conv | 208,112 | +4.06% | 1 | 100% | 255 |
| random_hold | 207,468 | +3.73% | 10 | 70% | 733 |
| snake_viper_wild | 207,266 | +3.63% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,725 | +1.86% | 15 | 47% | 2,625 |
| snake_anaconda | 203,202 | +1.60% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,999 | -0.00% | 0 | - | 237 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,485 | -11.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,390 (-4.30%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,051 | +0.49% |
| unified | +924 | +0.42% |
| intramonth | +759 | +0.36% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -158 | -0.07% |
| snake_abs | -293 | -0.14% |
| snake_abs_conv | -308 | -0.15% |
| benchmark_smallcap | -572 | -0.28% |
| snake_abs_exit | -608 | -0.28% |
| snake_abs_exit_conv | -635 | -0.30% |
| snake_anaconda | -853 | -0.42% |
| random_hold | -965 | -0.46% |
| benchmark | -1,086 | -0.49% |
| snake_viper_tick | -2,111 | -1.03% |
| snake_viper_wild | -2,149 | -1.03% |
| gold | -3,239 | -1.79% |

Average per day so far: unified Rs +621, benchmark Rs +570, intraweek Rs +399, snake_abs_exit Rs +380, oracle Rs +342, intramonth Rs +342, snake_abs_exit_conv Rs +331, snake_viper_wild Rs +260, snake_abs_conv Rs +246, snake_abs Rs +243, random_hold Rs +207, snake_viper_tick Rs +149, snake_anaconda Rs +103, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -0, snake_nonews Rs -326, snake Rs -347, gold Rs -625

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.