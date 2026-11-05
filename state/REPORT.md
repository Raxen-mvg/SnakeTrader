# Paper trading report

Updated 2026-11-05 13:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,740 | +8.87% | 0 | - | 236 |
| snake_abs_exit_conv | 214,662 | +7.33% | 1 | 100% | 255 |
| snake_abs_exit | 214,369 | +7.18% | 1 | 100% | 260 |
| benchmark | 213,418 | +6.71% | 0 | - | 237 |
| snake_abs | 211,536 | +5.77% | 1 | 100% | 255 |
| snake_abs_conv | 211,401 | +5.70% | 1 | 100% | 255 |
| intraweek | 210,837 | +5.42% | 25 | 48% | 2,757 |
| intramonth | 209,665 | +4.83% | 0 | - | 235 |
| snake_viper_wild | 206,610 | +3.31% | 3 | 33% | 702 |
| random_hold | 206,219 | +3.11% | 8 | 62% | 649 |
| oracle | 204,037 | +2.02% | 0 | - | 233 |
| snake_viper_tick | 203,061 | +1.53% | 2 | 0% | 532 |
| snake_anaconda | 202,666 | +1.33% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,013 | -0.49% | 0 | - | 237 |
| gold | 194,090 | -2.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,234 (-4.88%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,659 | +2.23% |
| unified | +3,301 | +1.54% |
| random_hold | +2,910 | +1.43% |
| gold | +2,696 | +1.41% |
| intramonth | +2,650 | +1.28% |
| benchmark_smallcap | +2,343 | +1.19% |
| oracle | +2,245 | +1.11% |
| intraweek | +1,140 | +0.54% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -353 | -0.16% |
| snake_abs_conv | -357 | -0.17% |
| snake_abs | -367 | -0.17% |
| snake_abs_exit | -531 | -0.25% |
| snake_anaconda | -1,155 | -0.57% |
| snake_viper_tick | -2,339 | -1.14% |
| snake_viper_wild | -2,420 | -1.16% |

Average per day so far: unified Rs +634, snake_abs_exit_conv Rs +586, snake_abs_exit Rs +575, benchmark Rs +479, snake_abs_conv Rs +456, snake_abs Rs +444, intraweek Rs +387, intramonth Rs +345, snake_viper_wild Rs +331, random_hold Rs +222, snake_viper_tick Rs +180, oracle Rs +144, snake_anaconda Rs +116, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -41, gold Rs -211, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.