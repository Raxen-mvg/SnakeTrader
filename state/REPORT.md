# Paper trading report

Updated 2026-11-06 12:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 215,108 | +7.55% | 0 | - | 237 |
| unified | 214,770 | +7.38% | 0 | - | 236 |
| intraweek | 208,953 | +4.48% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 208,666 | +4.33% | 1 | 100% | 255 |
| snake_abs_exit | 208,492 | +4.25% | 1 | 100% | 260 |
| intramonth | 207,054 | +3.53% | 0 | - | 235 |
| snake_abs | 205,636 | +2.82% | 1 | 100% | 255 |
| snake_abs_conv | 205,460 | +2.73% | 1 | 100% | 255 |
| oracle | 204,954 | +2.48% | 0 | - | 233 |
| random_hold | 203,189 | +1.59% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,925 | -2.04% | 3 | 33% | 374 |
| snake_viper_wild | 195,608 | -2.20% | 3 | 33% | 702 |
| benchmark_smallcap | 194,686 | -2.66% | 0 | - | 237 |
| snake_viper_tick | 192,296 | -3.85% | 2 | 0% | 532 |
| gold | 190,309 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 186,921 (-6.54%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,339 | +0.63% |
| oracle | +882 | +0.43% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -465 | -0.22% |
| intramonth | -895 | -0.43% |
| random_hold | -1,134 | -0.56% |
| unified | -1,214 | -0.56% |
| gold | -3,913 | -2.02% |
| benchmark_smallcap | -4,002 | -2.01% |
| snake_abs | -6,052 | -2.86% |
| snake_abs_conv | -6,084 | -2.88% |
| snake_abs_exit_conv | -6,137 | -2.86% |
| snake_abs_exit | -6,167 | -2.87% |
| snake_anaconda | -6,554 | -3.24% |
| snake_viper_tick | -8,842 | -4.40% |
| snake_viper_wild | -9,048 | -4.42% |

Average per day so far: benchmark Rs +521, unified Rs +509, snake_abs_exit_conv Rs +333, snake_abs_exit Rs +327, intraweek Rs +309, intramonth Rs +243, snake_abs_conv Rs +210, snake_abs Rs +209, oracle Rs +171, random_hold Rs +110, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -209, benchmark_smallcap Rs -213, gold Rs -334, snake_nonews Rs -411, snake_viper_tick Rs -428, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.