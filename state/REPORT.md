# Paper trading report

Updated 2026-11-20 13:34 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,452 | +13.23% | 0 | - | 236 |
| benchmark | 224,151 | +12.07% | 0 | - | 237 |
| intraweek | 215,416 | +7.71% | 35 | 54% | 3,851 |
| intramonth | 215,347 | +7.67% | 0 | - | 235 |
| oracle | 212,652 | +6.33% | 0 | - | 233 |
| random_hold | 209,643 | +4.82% | 11 | 73% | 979 |
| snake_abs_exit | 209,395 | +4.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,380 | +3.69% | 2 | 50% | 345 |
| snake_abs | 206,542 | +3.27% | 1 | 100% | 255 |
| snake_abs_conv | 206,413 | +3.21% | 1 | 100% | 255 |
| snake_viper_wild | 204,079 | +2.04% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,143 | +0.57% | 0 | - | 237 |
| snake_anaconda | 200,688 | +0.34% | 3 | 33% | 374 |
| snake_viper_tick | 200,597 | +0.30% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,506 | -16.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,141 (-3.93%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,527 | +1.19% |
| unified | +1,837 | +0.82% |
| benchmark | +1,775 | +0.80% |
| intramonth | +1,339 | +0.62% |
| random_hold | +1,190 | +0.57% |
| oracle | +563 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -325 | -0.16% |
| snake_abs | -2,438 | -1.17% |
| snake_abs_conv | -2,447 | -1.17% |
| snake_anaconda | -2,776 | -1.36% |
| snake_viper_tick | -3,380 | -1.66% |
| snake_viper_wild | -3,444 | -1.66% |
| snake_abs_exit_conv | -3,685 | -1.75% |
| snake_abs_exit | -3,956 | -1.85% |
| gold | -7,266 | -4.16% |

Average per day so far: unified Rs +696, benchmark Rs +636, intraweek Rs +406, intramonth Rs +404, oracle Rs +333, snake_abs_exit Rs +268, random_hold Rs +254, snake_abs_exit_conv Rs +211, snake_abs_conv Rs +183, snake_abs Rs +182, snake_viper_wild Rs +136, nifty_calls Rs +48, benchmark_smallcap Rs +34, snake_viper_tick Rs +22, snake_anaconda Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -855

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.