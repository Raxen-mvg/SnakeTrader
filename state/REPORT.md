# Paper trading report

Updated 2026-11-18 14:13 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,436 | +11.22% | 0 | - | 236 |
| benchmark | 220,379 | +10.19% | 0 | - | 237 |
| snake_abs_exit | 213,977 | +6.99% | 2 | 50% | 345 |
| intraweek | 212,393 | +6.20% | 35 | 54% | 3,851 |
| oracle | 212,255 | +6.13% | 0 | - | 233 |
| snake_abs_exit_conv | 212,195 | +6.10% | 2 | 50% | 345 |
| intramonth | 212,136 | +6.07% | 0 | - | 235 |
| snake_abs | 209,132 | +4.57% | 1 | 100% | 255 |
| snake_abs_conv | 209,018 | +4.51% | 1 | 100% | 255 |
| random_hold | 207,063 | +3.53% | 10 | 70% | 733 |
| snake_viper_wild | 206,943 | +3.47% | 16 | 50% | 2,827 |
| snake_anaconda | 204,274 | +2.14% | 3 | 33% | 374 |
| snake_viper_tick | 203,409 | +1.71% | 15 | 47% | 2,625 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,157 | -11.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,045 (-4.48%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +998 | +0.45% |
| snake_abs_exit | +835 | +0.39% |
| snake_abs_exit_conv | +621 | +0.29% |
| snake_abs_conv | +599 | +0.29% |
| intramonth | +594 | +0.28% |
| snake_abs | +573 | +0.28% |
| snake_anaconda | +219 | +0.11% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -231 | -0.11% |
| benchmark_smallcap | -908 | -0.45% |
| intraweek | -930 | -0.44% |
| benchmark | -1,224 | -0.55% |
| random_hold | -1,370 | -0.66% |
| snake_viper_tick | -2,427 | -1.18% |
| snake_viper_wild | -2,472 | -1.18% |
| gold | -3,567 | -1.97% |

Average per day so far: unified Rs +623, benchmark Rs +566, snake_abs_exit Rs +424, snake_abs_exit_conv Rs +370, intraweek Rs +344, oracle Rs +340, intramonth Rs +337, snake_abs_conv Rs +273, snake_abs Rs +269, snake_viper_wild Rs +248, random_hold Rs +196, snake_anaconda Rs +138, snake_viper_tick Rs +136, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -11, snake_nonews Rs -326, snake Rs -347, gold Rs -635

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.