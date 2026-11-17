# Paper trading report

Updated 2026-11-17 14:24 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| unified | 221,715 | +10.86% | 0 | - | 236 |
| snake_abs_exit | 213,799 | +6.90% | 2 | 50% | 345 |
| intraweek | 213,550 | +6.78% | 35 | 54% | 3,851 |
| oracle | 212,416 | +6.21% | 0 | - | 233 |
| snake_abs_exit_conv | 212,256 | +6.13% | 2 | 50% | 345 |
| intramonth | 211,718 | +5.86% | 0 | - | 235 |
| snake_viper_wild | 210,006 | +5.00% | 14 | 50% | 2,496 |
| snake_abs | 209,000 | +4.50% | 1 | 100% | 255 |
| snake_abs_conv | 208,867 | +4.43% | 1 | 100% | 255 |
| random_hold | 207,750 | +3.88% | 10 | 70% | 733 |
| snake_viper_tick | 206,418 | +3.21% | 13 | 46% | 2,299 |
| snake_anaconda | 204,465 | +2.23% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,221 | +0.61% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,905 | -9.55% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,239 (-4.38%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,862 | +1.87% |
| snake_viper_tick | +3,798 | +1.87% |
| intraweek | +2,285 | +1.08% |
| benchmark | +1,943 | +0.88% |
| oracle | +393 | +0.18% |
| benchmark_smallcap | +392 | +0.20% |
| unified | +278 | +0.12% |
| intramonth | +99 | +0.05% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| random_hold | -43 | -0.02% |
| gold | -49 | -0.03% |
| snake_abs_exit | -611 | -0.28% |
| snake_anaconda | -638 | -0.31% |
| snake_abs_exit_conv | -961 | -0.45% |
| snake_abs_conv | -1,122 | -0.53% |
| snake_abs | -1,134 | -0.54% |

Average per day so far: benchmark Rs +629, unified Rs +620, snake_abs_exit Rs +431, intraweek Rs +387, snake_abs_exit_conv Rs +383, snake_viper_wild Rs +371, oracle Rs +355, intramonth Rs +335, snake_abs_conv Rs +277, snake_abs Rs +273, snake_viper_tick Rs +267, random_hold Rs +221, snake_anaconda Rs +149, nifty_calls Rs +52, benchmark_smallcap Rs +39, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -546

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.