# Paper trading report

Updated 2026-11-20 12:43 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,139 | +13.07% | 0 | - | 236 |
| benchmark | 224,365 | +12.18% | 0 | - | 237 |
| intramonth | 215,010 | +7.50% | 0 | - | 235 |
| intraweek | 214,666 | +7.33% | 35 | 54% | 3,851 |
| oracle | 212,624 | +6.31% | 0 | - | 233 |
| snake_abs_exit | 209,153 | +4.58% | 2 | 50% | 345 |
| random_hold | 209,058 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,223 | +3.61% | 2 | 50% | 345 |
| snake_abs | 206,374 | +3.19% | 1 | 100% | 255 |
| snake_abs_conv | 206,238 | +3.12% | 1 | 100% | 255 |
| snake_viper_wild | 205,387 | +2.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 201,883 | +0.94% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,975 | +0.49% | 0 | - | 237 |
| snake_anaconda | 200,313 | +0.16% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,339 | -16.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,901 (-4.05%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,989 | +0.89% |
| intraweek | +1,777 | +0.83% |
| unified | +1,524 | +0.68% |
| intramonth | +1,002 | +0.47% |
| random_hold | +605 | +0.29% |
| oracle | +535 | +0.25% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -493 | -0.24% |
| snake_viper_tick | -2,094 | -1.03% |
| snake_viper_wild | -2,136 | -1.03% |
| snake_abs | -2,605 | -1.25% |
| snake_abs_conv | -2,622 | -1.25% |
| snake_anaconda | -3,151 | -1.55% |
| snake_abs_exit_conv | -3,841 | -1.82% |
| snake_abs_exit | -4,198 | -1.97% |
| gold | -8,434 | -4.83% |

Average per day so far: unified Rs +688, benchmark Rs +641, intramonth Rs +395, intraweek Rs +386, oracle Rs +332, snake_abs_exit Rs +262, random_hold Rs +238, snake_abs_exit_conv Rs +206, snake_viper_wild Rs +180, snake_abs_conv Rs +178, snake_abs Rs +177, snake_viper_tick Rs +70, nifty_calls Rs +48, benchmark_smallcap Rs +29, snake_anaconda Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.