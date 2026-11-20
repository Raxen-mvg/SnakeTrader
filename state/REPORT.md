# Paper trading report

Updated 2026-11-20 12:28 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,060 | +13.03% | 0 | - | 236 |
| benchmark | 224,097 | +12.05% | 0 | - | 237 |
| intramonth | 214,997 | +7.50% | 0 | - | 235 |
| intraweek | 214,481 | +7.24% | 35 | 54% | 3,851 |
| oracle | 212,661 | +6.33% | 0 | - | 233 |
| snake_abs_exit | 209,359 | +4.68% | 2 | 50% | 345 |
| random_hold | 208,937 | +4.47% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,335 | +3.67% | 2 | 50% | 345 |
| snake_abs | 206,517 | +3.26% | 1 | 100% | 255 |
| snake_abs_conv | 206,381 | +3.19% | 1 | 100% | 255 |
| snake_viper_wild | 205,895 | +2.95% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,382 | +1.19% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,941 | +0.47% | 0 | - | 237 |
| snake_anaconda | 200,482 | +0.24% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,717 | -16.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,905 (-4.05%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,721 | +0.77% |
| intraweek | +1,592 | +0.75% |
| unified | +1,445 | +0.64% |
| intramonth | +989 | +0.46% |
| oracle | +573 | +0.27% |
| random_hold | +484 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -527 | -0.26% |
| snake_viper_tick | -1,595 | -0.78% |
| snake_viper_wild | -1,627 | -0.78% |
| snake_abs | -2,463 | -1.18% |
| snake_abs_conv | -2,479 | -1.19% |
| snake_anaconda | -2,981 | -1.47% |
| snake_abs_exit_conv | -3,729 | -1.77% |
| snake_abs_exit | -3,992 | -1.87% |
| gold | -8,056 | -4.61% |

Average per day so far: unified Rs +686, benchmark Rs +634, intramonth Rs +395, intraweek Rs +381, oracle Rs +333, snake_abs_exit Rs +267, random_hold Rs +235, snake_abs_exit_conv Rs +210, snake_viper_wild Rs +197, snake_abs_conv Rs +182, snake_abs Rs +181, snake_viper_tick Rs +88, nifty_calls Rs +48, benchmark_smallcap Rs +28, snake_anaconda Rs +15, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -876

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.