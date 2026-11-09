# Paper trading report

Updated 2026-11-09 14:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,957 | +9.98% | 0 | - | 236 |
| benchmark | 217,763 | +8.88% | 0 | - | 237 |
| intraweek | 214,948 | +7.47% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 213,222 | +6.61% | 2 | 50% | 330 |
| snake_abs_exit | 212,584 | +6.29% | 2 | 50% | 308 |
| intramonth | 210,030 | +5.01% | 0 | - | 235 |
| snake_abs | 209,843 | +4.92% | 1 | 100% | 255 |
| snake_abs_conv | 209,677 | +4.84% | 1 | 100% | 255 |
| oracle | 209,450 | +4.72% | 0 | - | 233 |
| random_hold | 204,439 | +2.22% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,044 | +0.02% | 7 | 57% | 1,332 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,988 | -0.01% | 3 | 33% | 374 |
| benchmark_smallcap | 198,038 | -0.98% | 0 | - | 237 |
| snake_viper_tick | 196,645 | -1.68% | 6 | 50% | 1,154 |
| gold | 192,101 | -3.95% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,375 (-4.81%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,800 | +2.30% |
| intraweek | +4,585 | +2.18% |
| snake_abs_conv | +4,450 | +2.17% |
| snake_abs | +4,424 | +2.15% |
| unified | +4,348 | +2.02% |
| snake_abs_exit | +4,272 | +2.05% |
| snake_anaconda | +4,161 | +2.12% |
| snake_viper_wild | +4,006 | +2.04% |
| snake_viper_tick | +3,935 | +2.04% |
| oracle | +3,623 | +1.76% |
| intramonth | +2,427 | +1.17% |
| benchmark_smallcap | +1,244 | +0.63% |
| gold | +1,052 | +0.55% |
| random_hold | +532 | +0.26% |
| benchmark | +275 | +0.13% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +665, benchmark Rs +592, intraweek Rs +498, snake_abs_exit_conv Rs +490, snake_abs_exit Rs +466, snake_abs_conv Rs +358, snake_abs Rs +352, intramonth Rs +334, oracle Rs +315, random_hold Rs +148, nifty_calls Rs +61, snake_viper_wild Rs +2, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, snake_anaconda Rs -0, benchmark_smallcap Rs -75, snake_viper_tick Rs -177, gold Rs -263, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.