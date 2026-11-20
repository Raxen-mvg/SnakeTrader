# Paper trading report

Updated 2026-11-20 12:16 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,316 | +13.16% | 0 | - | 236 |
| benchmark | 223,676 | +11.84% | 0 | - | 237 |
| intramonth | 215,284 | +7.64% | 0 | - | 235 |
| intraweek | 214,764 | +7.38% | 35 | 54% | 3,851 |
| oracle | 212,626 | +6.31% | 0 | - | 233 |
| snake_abs_exit | 209,522 | +4.76% | 2 | 50% | 345 |
| random_hold | 208,906 | +4.45% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,561 | +3.78% | 2 | 50% | 345 |
| snake_abs | 206,582 | +3.29% | 1 | 100% | 255 |
| snake_abs_conv | 206,448 | +3.22% | 1 | 100% | 255 |
| snake_viper_wild | 206,265 | +3.13% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,743 | +1.37% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,773 | +0.39% | 0 | - | 237 |
| snake_anaconda | 200,626 | +0.31% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,356 | -16.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,036 (-3.98%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,875 | +0.88% |
| unified | +1,701 | +0.76% |
| benchmark | +1,301 | +0.58% |
| intramonth | +1,276 | +0.60% |
| oracle | +537 | +0.25% |
| random_hold | +453 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -695 | -0.34% |
| snake_viper_tick | -1,233 | -0.60% |
| snake_viper_wild | -1,258 | -0.61% |
| snake_abs | -2,398 | -1.15% |
| snake_abs_conv | -2,412 | -1.16% |
| snake_anaconda | -2,838 | -1.40% |
| snake_abs_exit_conv | -3,503 | -1.66% |
| snake_abs_exit | -3,829 | -1.79% |
| gold | -8,417 | -4.82% |

Average per day so far: unified Rs +693, benchmark Rs +623, intramonth Rs +402, intraweek Rs +389, oracle Rs +332, snake_abs_exit Rs +272, random_hold Rs +234, snake_abs_exit_conv Rs +216, snake_viper_wild Rs +209, snake_abs_conv Rs +184, snake_abs Rs +183, snake_viper_tick Rs +102, nifty_calls Rs +48, benchmark_smallcap Rs +23, snake_anaconda Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.