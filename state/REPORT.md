# Paper trading report

Updated 2026-11-17 12:23 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,462 | +11.23% | 0 | - | 236 |
| benchmark | 222,254 | +11.13% | 0 | - | 237 |
| snake_abs_exit | 214,465 | +7.23% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,773 | +6.39% | 2 | 50% | 345 |
| intraweek | 212,764 | +6.38% | 35 | 54% | 3,851 |
| oracle | 212,355 | +6.18% | 0 | - | 233 |
| intramonth | 212,274 | +6.14% | 0 | - | 235 |
| snake_abs | 209,561 | +4.78% | 1 | 100% | 255 |
| snake_abs_conv | 209,414 | +4.71% | 1 | 100% | 255 |
| random_hold | 207,715 | +3.86% | 10 | 70% | 733 |
| snake_viper_wild | 207,649 | +3.83% | 14 | 50% | 2,496 |
| snake_anaconda | 205,064 | +2.53% | 3 | 33% | 374 |
| snake_viper_tick | 204,099 | +2.05% | 13 | 46% | 2,299 |
| benchmark_smallcap | 201,883 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,152 | -9.42% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,391 (-4.30%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,173 | +0.99% |
| snake_viper_wild | +1,505 | +0.73% |
| intraweek | +1,499 | +0.71% |
| snake_viper_tick | +1,479 | +0.73% |
| benchmark_smallcap | +1,054 | +0.53% |
| unified | +1,024 | +0.46% |
| intramonth | +655 | +0.31% |
| oracle | +332 | +0.16% |
| gold | +197 | +0.11% |
| snake_abs_exit | +55 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -38 | -0.02% |
| random_hold | -78 | -0.04% |
| snake_abs_exit_conv | -444 | -0.21% |
| snake_abs | -572 | -0.27% |
| snake_abs_conv | -576 | -0.27% |

Average per day so far: unified Rs +642, benchmark Rs +636, snake_abs_exit Rs +452, snake_abs_exit_conv Rs +399, intraweek Rs +365, oracle Rs +353, intramonth Rs +351, snake_abs_conv Rs +294, snake_abs Rs +290, snake_viper_wild Rs +283, random_hold Rs +220, snake_viper_tick Rs +171, snake_anaconda Rs +169, benchmark_smallcap Rs +61, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -539

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.