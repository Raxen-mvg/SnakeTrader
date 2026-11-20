# Paper trading report

Updated 2026-11-20 12:40 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,286 | +13.14% | 0 | - | 236 |
| benchmark | 224,319 | +12.16% | 0 | - | 237 |
| intramonth | 215,163 | +7.58% | 0 | - | 235 |
| intraweek | 214,751 | +7.38% | 35 | 54% | 3,851 |
| oracle | 212,724 | +6.36% | 0 | - | 233 |
| snake_abs_exit | 209,273 | +4.64% | 2 | 50% | 345 |
| random_hold | 209,053 | +4.53% | 11 | 73% | 979 |
| snake_abs_exit_conv | 207,335 | +3.67% | 2 | 50% | 345 |
| snake_abs | 206,439 | +3.22% | 1 | 100% | 255 |
| snake_abs_conv | 206,304 | +3.15% | 1 | 100% | 255 |
| snake_viper_wild | 205,550 | +2.77% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,043 | +1.02% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,885 | +0.44% | 0 | - | 237 |
| snake_anaconda | 200,416 | +0.21% | 3 | 33% | 374 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,504 | -16.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,985 (-4.01%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,943 | +0.87% |
| intraweek | +1,862 | +0.88% |
| unified | +1,671 | +0.74% |
| intramonth | +1,155 | +0.54% |
| oracle | +635 | +0.30% |
| random_hold | +600 | +0.29% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -583 | -0.29% |
| snake_viper_tick | -1,934 | -0.95% |
| snake_viper_wild | -1,973 | -0.95% |
| snake_abs | -2,541 | -1.22% |
| snake_abs_conv | -2,556 | -1.22% |
| snake_anaconda | -3,048 | -1.50% |
| snake_abs_exit_conv | -3,729 | -1.77% |
| snake_abs_exit | -4,078 | -1.91% |
| gold | -8,269 | -4.73% |

Average per day so far: unified Rs +692, benchmark Rs +640, intramonth Rs +399, intraweek Rs +388, oracle Rs +335, snake_abs_exit Rs +265, random_hold Rs +238, snake_abs_exit_conv Rs +210, snake_viper_wild Rs +185, snake_abs_conv Rs +180, snake_abs Rs +179, snake_viper_tick Rs +76, nifty_calls Rs +48, benchmark_smallcap Rs +26, snake_anaconda Rs +13, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -308, snake Rs -328, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.