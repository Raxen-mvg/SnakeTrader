# Paper trading report

Updated 2026-11-17 11:47 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,403 | +11.20% | 0 | - | 236 |
| benchmark | 221,986 | +10.99% | 0 | - | 237 |
| snake_abs_exit | 214,983 | +7.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 213,147 | +6.57% | 2 | 50% | 345 |
| intraweek | 212,725 | +6.36% | 35 | 54% | 3,851 |
| oracle | 212,643 | +6.32% | 0 | - | 233 |
| intramonth | 212,329 | +6.17% | 0 | - | 235 |
| snake_abs | 209,813 | +4.91% | 1 | 100% | 255 |
| snake_abs_conv | 209,664 | +4.83% | 1 | 100% | 255 |
| random_hold | 208,086 | +4.04% | 10 | 70% | 733 |
| snake_viper_wild | 207,343 | +3.67% | 14 | 50% | 2,496 |
| snake_anaconda | 205,418 | +2.71% | 3 | 33% | 374 |
| snake_viper_tick | 203,798 | +1.90% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,264 | +1.13% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,332 | -9.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,493 (-4.25%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,905 | +0.87% |
| intraweek | +1,459 | +0.69% |
| benchmark_smallcap | +1,435 | +0.71% |
| snake_viper_wild | +1,199 | +0.58% |
| snake_viper_tick | +1,178 | +0.58% |
| unified | +965 | +0.44% |
| intramonth | +710 | +0.34% |
| oracle | +620 | +0.29% |
| snake_abs_exit | +574 | +0.27% |
| gold | +378 | +0.21% |
| snake_anaconda | +315 | +0.15% |
| random_hold | +293 | +0.14% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -70 | -0.03% |
| snake_abs | -320 | -0.15% |
| snake_abs_conv | -326 | -0.15% |

Average per day so far: unified Rs +640, benchmark Rs +628, snake_abs_exit Rs +468, snake_abs_exit_conv Rs +411, intraweek Rs +364, oracle Rs +361, intramonth Rs +352, snake_abs_conv Rs +302, snake_abs Rs +297, snake_viper_wild Rs +272, random_hold Rs +231, snake_anaconda Rs +181, snake_viper_tick Rs +158, benchmark_smallcap Rs +73, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -533

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.