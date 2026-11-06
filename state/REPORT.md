# Paper trading report

Updated 2026-11-06 12:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,891 | +7.45% | 0 | - | 236 |
| benchmark | 214,496 | +7.25% | 0 | - | 237 |
| intraweek | 209,870 | +4.93% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,653 | +4.33% | 1 | 100% | 255 |
| snake_abs_exit | 208,480 | +4.24% | 1 | 100% | 260 |
| intramonth | 207,052 | +3.53% | 0 | - | 235 |
| snake_abs | 205,622 | +2.81% | 1 | 100% | 255 |
| snake_abs_conv | 205,447 | +2.72% | 1 | 100% | 255 |
| oracle | 204,887 | +2.44% | 0 | - | 233 |
| random_hold | 203,226 | +1.61% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,898 | -2.05% | 3 | 33% | 374 |
| snake_viper_wild | 195,600 | -2.20% | 3 | 33% | 702 |
| benchmark_smallcap | 194,417 | -2.79% | 0 | - | 237 |
| snake_viper_tick | 192,287 | -3.86% | 2 | 0% | 532 |
| gold | 190,325 | -4.84% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,038 (-6.48%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +815 | +0.40% |
| benchmark | +727 | +0.34% |
| intraweek | +452 | +0.22% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intramonth | -897 | -0.43% |
| unified | -1,092 | -0.51% |
| random_hold | -1,098 | -0.54% |
| gold | -3,896 | -2.01% |
| benchmark_smallcap | -4,271 | -2.15% |
| snake_abs | -6,067 | -2.87% |
| snake_abs_conv | -6,098 | -2.88% |
| snake_abs_exit_conv | -6,150 | -2.86% |
| snake_abs_exit | -6,179 | -2.88% |
| snake_anaconda | -6,581 | -3.25% |
| snake_viper_tick | -8,851 | -4.40% |
| snake_viper_wild | -9,056 | -4.42% |

Average per day so far: unified Rs +513, benchmark Rs +500, intraweek Rs +340, snake_abs_exit_conv Rs +333, snake_abs_exit Rs +326, intramonth Rs +243, snake_abs_conv Rs +210, snake_abs Rs +208, oracle Rs +169, random_hold Rs +111, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -171, snake_viper_wild Rs -210, benchmark_smallcap Rs -223, gold Rs -334, snake_nonews Rs -411, snake_viper_tick Rs -429, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.