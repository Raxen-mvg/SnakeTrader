# Paper trading report

Updated 2026-11-06 13:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,131 | +7.57% | 0 | - | 237 |
| unified | 214,722 | +7.36% | 0 | - | 236 |
| intraweek | 208,381 | +4.19% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,339 | +4.17% | 1 | 100% | 255 |
| snake_abs_exit | 208,232 | +4.12% | 1 | 100% | 260 |
| intramonth | 207,053 | +3.53% | 0 | - | 235 |
| snake_abs | 205,329 | +2.67% | 1 | 100% | 255 |
| snake_abs_conv | 205,144 | +2.57% | 1 | 100% | 255 |
| oracle | 205,112 | +2.56% | 0 | - | 233 |
| random_hold | 203,236 | +1.62% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,737 | -1.63% | 3 | 33% | 702 |
| snake_anaconda | 195,777 | -2.11% | 3 | 33% | 374 |
| benchmark_smallcap | 194,753 | -2.62% | 0 | - | 237 |
| snake_viper_tick | 193,406 | -3.30% | 2 | 0% | 532 |
| gold | 189,980 | -5.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,828 (-6.59%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,362 | +0.64% |
| oracle | +1,040 | +0.51% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -895 | -0.43% |
| intraweek | -1,038 | -0.49% |
| random_hold | -1,087 | -0.53% |
| unified | -1,261 | -0.58% |
| benchmark_smallcap | -3,935 | -1.98% |
| gold | -4,242 | -2.18% |
| snake_abs | -6,359 | -3.00% |
| snake_abs_conv | -6,401 | -3.03% |
| snake_abs_exit | -6,427 | -2.99% |
| snake_abs_exit_conv | -6,465 | -3.01% |
| snake_anaconda | -6,702 | -3.31% |
| snake_viper_tick | -7,732 | -3.84% |
| snake_viper_wild | -7,919 | -3.87% |

Average per day so far: benchmark Rs +522, unified Rs +508, snake_abs_exit_conv Rs +321, snake_abs_exit Rs +317, intraweek Rs +289, intramonth Rs +243, snake_abs_conv Rs +198, snake_abs Rs +197, oracle Rs +176, random_hold Rs +112, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -155, snake_anaconda Rs -176, benchmark_smallcap Rs -210, gold Rs -346, snake_viper_tick Rs -366, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.