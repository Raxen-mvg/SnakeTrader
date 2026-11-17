# Paper trading report

Updated 2026-11-17 12:52 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,047 | +11.02% | 0 | - | 237 |
| unified | 221,748 | +10.87% | 0 | - | 236 |
| snake_abs_exit | 214,142 | +7.07% | 2 | 50% | 345 |
| intraweek | 213,936 | +6.97% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,431 | +6.21% | 2 | 50% | 345 |
| oracle | 212,326 | +6.16% | 0 | - | 233 |
| intramonth | 211,685 | +5.84% | 0 | - | 235 |
| snake_abs | 209,301 | +4.65% | 1 | 100% | 255 |
| snake_abs_conv | 209,153 | +4.58% | 1 | 100% | 255 |
| random_hold | 207,678 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 207,678 | +3.84% | 14 | 50% | 2,496 |
| snake_anaconda | 204,848 | +2.42% | 3 | 33% | 374 |
| snake_viper_tick | 204,128 | +2.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,535 | +0.77% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,398 | -9.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,283 (-4.36%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,670 | +1.26% |
| benchmark | +1,966 | +0.89% |
| snake_viper_wild | +1,534 | +0.74% |
| snake_viper_tick | +1,508 | +0.74% |
| benchmark_smallcap | +706 | +0.35% |
| gold | +444 | +0.24% |
| unified | +311 | +0.14% |
| oracle | +304 | +0.14% |
| intramonth | +66 | +0.03% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -115 | -0.06% |
| snake_anaconda | -255 | -0.12% |
| snake_abs_exit | -268 | -0.12% |
| snake_abs_exit_conv | -786 | -0.37% |
| snake_abs | -833 | -0.40% |
| snake_abs_conv | -837 | -0.40% |

Average per day so far: benchmark Rs +630, unified Rs +621, snake_abs_exit Rs +442, intraweek Rs +398, snake_abs_exit_conv Rs +388, oracle Rs +352, intramonth Rs +334, snake_abs_conv Rs +286, snake_viper_wild Rs +284, snake_abs Rs +282, random_hold Rs +219, snake_viper_tick Rs +172, snake_anaconda Rs +162, nifty_calls Rs +52, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.