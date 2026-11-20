# Paper trading report

Updated 2026-11-20 13:16 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,331 | +13.17% | 0 | - | 236 |
| benchmark | 224,311 | +12.16% | 0 | - | 237 |
| intraweek | 215,272 | +7.64% | 35 | 54% | 3,851 |
| intramonth | 215,273 | +7.64% | 0 | - | 235 |
| oracle | 212,651 | +6.33% | 0 | - | 233 |
| random_hold | 209,615 | +4.81% | 11 | 73% | 979 |
| snake_abs_exit | 209,004 | +4.50% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,053 | +3.53% | 2 | 50% | 345 |
| snake_abs | 206,190 | +3.10% | 1 | 100% | 255 |
| snake_abs_conv | 206,050 | +3.02% | 1 | 100% | 255 |
| snake_viper_wild | 204,016 | +2.01% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,008 | +0.50% | 0 | - | 237 |
| snake_viper_tick | 200,536 | +0.27% | 15 | 47% | 2,625 |
| snake_anaconda | 200,310 | +0.15% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,388 | -16.81% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,020 (-3.99%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,383 | +1.12% |
| benchmark | +1,935 | +0.87% |
| unified | +1,716 | +0.76% |
| intramonth | +1,265 | +0.59% |
| random_hold | +1,162 | +0.56% |
| oracle | +563 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -460 | -0.23% |
| snake_abs | -2,790 | -1.33% |
| snake_abs_conv | -2,810 | -1.34% |
| snake_anaconda | -3,154 | -1.55% |
| snake_viper_tick | -3,441 | -1.69% |
| snake_viper_wild | -3,506 | -1.69% |
| snake_abs_exit_conv | -4,012 | -1.90% |
| snake_abs_exit | -4,347 | -2.04% |
| gold | -8,384 | -4.80% |

Average per day so far: unified Rs +693, benchmark Rs +640, intramonth Rs +402, intraweek Rs +402, oracle Rs +333, snake_abs_exit Rs +257, random_hold Rs +253, snake_abs_exit_conv Rs +202, snake_abs_conv Rs +173, snake_abs Rs +172, snake_viper_wild Rs +134, nifty_calls Rs +48, benchmark_smallcap Rs +30, snake_viper_tick Rs +20, snake_anaconda Rs +9, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.