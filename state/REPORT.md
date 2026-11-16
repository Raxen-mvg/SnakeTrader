# Paper trading report

Updated 2026-11-16 13:32 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,000 | +10.50% | 0 | - | 236 |
| benchmark | 220,165 | +10.08% | 0 | - | 237 |
| snake_abs_exit | 213,420 | +6.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,252 | +6.13% | 2 | 50% | 345 |
| oracle | 212,146 | +6.07% | 0 | - | 233 |
| intraweek | 211,850 | +5.92% | 35 | 54% | 3,851 |
| intramonth | 211,643 | +5.82% | 0 | - | 235 |
| snake_abs | 209,487 | +4.74% | 1 | 100% | 255 |
| snake_abs_conv | 209,329 | +4.66% | 1 | 100% | 255 |
| random_hold | 207,920 | +3.96% | 10 | 70% | 733 |
| snake_viper_wild | 205,583 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 203,906 | +1.95% | 3 | 33% | 374 |
| snake_viper_tick | 202,068 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,863 | +0.43% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,036 | -9.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,868 (-4.57%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,979 | +0.90% |
| intramonth | +1,586 | +0.76% |
| benchmark | +826 | +0.38% |
| snake_viper_wild | +826 | +0.40% |
| snake_viper_tick | +813 | +0.40% |
| random_hold | +694 | +0.34% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -952 | -0.45% |
| snake_anaconda | -986 | -0.48% |
| benchmark_smallcap | -2,007 | -0.99% |
| gold | -2,959 | -1.61% |
| snake_abs_conv | -3,038 | -1.43% |
| snake_abs | -3,053 | -1.44% |
| snake_abs_exit | -3,565 | -1.64% |
| snake_abs_exit_conv | -4,129 | -1.91% |
| intraweek | -4,295 | -1.99% |

Average per day so far: unified Rs +618, benchmark Rs +593, snake_abs_exit Rs +433, snake_abs_exit_conv Rs +395, oracle Rs +357, intraweek Rs +349, intramonth Rs +342, snake_abs_conv Rs +301, snake_abs Rs +296, random_hold Rs +233, snake_viper_wild Rs +215, snake_anaconda Rs +135, snake_viper_tick Rs +90, nifty_calls Rs +54, benchmark_smallcap Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -558

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.