# Paper trading report

Updated 2026-11-26 12:35 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,247 | +13.12% | 0 | - | 237 |
| unified | 223,412 | +11.71% | 0 | - | 236 |
| oracle | 213,334 | +6.67% | 0 | - | 233 |
| intramonth | 210,517 | +5.26% | 0 | - | 235 |
| random_hold | 209,912 | +4.96% | 13 | 69% | 1,037 |
| intraweek | 208,401 | +4.20% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,403 | +0.20% | 0 | - | 237 |
| snake_abs_exit | 200,215 | +0.11% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,718 | -0.14% | 2 | 50% | 345 |
| snake_abs | 198,148 | -0.93% | 1 | 100% | 255 |
| snake_abs_conv | 197,948 | -1.03% | 1 | 100% | 255 |
| snake_anaconda | 191,938 | -4.03% | 3 | 33% | 374 |
| snake_viper_wild | 191,841 | -4.08% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,584 | -5.71% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,454 | -16.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,823 (-5.59%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,858 | +1.13% |
| intraweek | +1,658 | +0.80% |
| benchmark_smallcap | +1,592 | +0.80% |
| benchmark | +1,224 | +0.54% |
| random_hold | +419 | +0.20% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -461 | -0.22% |
| unified | -687 | -0.31% |
| intramonth | -1,177 | -0.56% |
| snake_abs | -2,002 | -1.00% |
| snake_abs_conv | -2,024 | -1.01% |
| snake_abs_exit | -2,041 | -1.01% |
| snake_abs_exit_conv | -2,258 | -1.12% |
| snake_anaconda | -2,615 | -1.34% |
| snake_viper_tick | -5,593 | -2.88% |
| snake_viper_wild | -5,703 | -2.89% |

Average per day so far: benchmark Rs +640, unified Rs +571, oracle Rs +325, intramonth Rs +257, random_hold Rs +242, intraweek Rs +205, nifty_calls Rs +45, benchmark_smallcap Rs +11, snake_abs_exit Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -7, snake_abs Rs -47, snake_abs_conv Rs -54, snake_anaconda Rs -224, snake_viper_wild Rs -247, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -381, gold Rs -818

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.