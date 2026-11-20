# Paper trading report

Updated 2026-11-20 11:27 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,848 | +12.92% | 0 | - | 236 |
| benchmark | 222,827 | +11.41% | 0 | - | 237 |
| intramonth | 214,827 | +7.41% | 0 | - | 235 |
| intraweek | 214,398 | +7.20% | 35 | 54% | 3,851 |
| oracle | 212,662 | +6.33% | 0 | - | 233 |
| snake_abs_exit | 210,531 | +5.27% | 2 | 50% | 345 |
| random_hold | 209,220 | +4.61% | 11 | 73% | 979 |
| snake_abs_exit_conv | 208,158 | +4.08% | 2 | 50% | 345 |
| snake_abs | 207,665 | +3.83% | 1 | 100% | 255 |
| snake_abs_conv | 207,521 | +3.76% | 1 | 100% | 255 |
| snake_viper_wild | 206,055 | +3.03% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,538 | +1.27% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,259 | +0.63% | 3 | 33% | 374 |
| benchmark_smallcap | 200,358 | +0.18% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,764 | -17.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,022 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,509 | +0.71% |
| unified | +1,233 | +0.55% |
| intramonth | +820 | +0.38% |
| random_hold | +767 | +0.37% |
| oracle | +574 | +0.27% |
| benchmark | +451 | +0.20% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -1,110 | -0.55% |
| snake_abs | -1,315 | -0.63% |
| snake_abs_conv | -1,339 | -0.64% |
| snake_viper_tick | -1,439 | -0.71% |
| snake_viper_wild | -1,468 | -0.71% |
| snake_anaconda | -2,205 | -1.08% |
| snake_abs_exit | -2,820 | -1.32% |
| snake_abs_exit_conv | -2,907 | -1.38% |
| gold | -9,009 | -5.16% |

Average per day so far: unified Rs +680, benchmark Rs +601, intramonth Rs +390, intraweek Rs +379, oracle Rs +333, snake_abs_exit Rs +301, random_hold Rs +243, snake_abs_exit_conv Rs +233, snake_abs_conv Rs +215, snake_abs Rs +213, snake_viper_wild Rs +202, snake_viper_tick Rs +94, nifty_calls Rs +48, snake_anaconda Rs +38, benchmark_smallcap Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -901

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.