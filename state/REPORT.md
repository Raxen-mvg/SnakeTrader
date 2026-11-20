# Paper trading report

Updated 2026-11-20 13:27 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,386 | +13.19% | 0 | - | 236 |
| benchmark | 224,235 | +12.12% | 0 | - | 237 |
| intramonth | 215,356 | +7.68% | 0 | - | 235 |
| intraweek | 215,273 | +7.64% | 35 | 54% | 3,851 |
| oracle | 212,600 | +6.30% | 0 | - | 233 |
| random_hold | 209,523 | +4.76% | 11 | 73% | 979 |
| snake_abs_exit | 209,360 | +4.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,310 | +3.65% | 2 | 50% | 345 |
| snake_abs | 206,489 | +3.24% | 1 | 100% | 255 |
| snake_abs_conv | 206,358 | +3.18% | 1 | 100% | 255 |
| snake_viper_wild | 204,079 | +2.04% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,907 | +0.45% | 0 | - | 237 |
| snake_anaconda | 200,632 | +0.32% | 3 | 33% | 374 |
| snake_viper_tick | 200,597 | +0.30% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,997 | -16.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,076 (-3.96%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,384 | +1.12% |
| benchmark | +1,859 | +0.84% |
| unified | +1,771 | +0.79% |
| intramonth | +1,348 | +0.63% |
| random_hold | +1,069 | +0.51% |
| oracle | +511 | +0.24% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -560 | -0.28% |
| snake_abs | -2,491 | -1.19% |
| snake_abs_conv | -2,502 | -1.20% |
| snake_anaconda | -2,831 | -1.39% |
| snake_viper_tick | -3,380 | -1.66% |
| snake_viper_wild | -3,444 | -1.66% |
| snake_abs_exit_conv | -3,755 | -1.78% |
| snake_abs_exit | -3,991 | -1.87% |
| gold | -7,776 | -4.45% |

Average per day so far: unified Rs +694, benchmark Rs +638, intramonth Rs +404, intraweek Rs +402, oracle Rs +332, snake_abs_exit Rs +267, random_hold Rs +251, snake_abs_exit_conv Rs +209, snake_abs_conv Rs +182, snake_abs Rs +180, snake_viper_wild Rs +136, nifty_calls Rs +48, benchmark_smallcap Rs +27, snake_viper_tick Rs +22, snake_anaconda Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -869

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.