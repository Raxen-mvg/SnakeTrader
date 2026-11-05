# Paper trading report

Updated 2026-11-05 14:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,973 | +7.99% | 0 | - | 236 |
| snake_abs_exit_conv | 214,569 | +7.28% | 1 | 100% | 255 |
| snake_abs_exit | 214,328 | +7.16% | 1 | 100% | 260 |
| benchmark | 213,992 | +7.00% | 0 | - | 237 |
| snake_abs | 211,455 | +5.73% | 1 | 100% | 255 |
| snake_abs_conv | 211,317 | +5.66% | 1 | 100% | 255 |
| intraweek | 210,294 | +5.15% | 25 | 48% | 2,757 |
| intramonth | 207,489 | +3.75% | 0 | - | 235 |
| snake_viper_wild | 205,442 | +2.72% | 3 | 33% | 702 |
| random_hold | 204,951 | +2.48% | 8 | 62% | 649 |
| oracle | 203,660 | +1.83% | 0 | - | 233 |
| snake_anaconda | 202,743 | +1.37% | 3 | 33% | 374 |
| snake_viper_tick | 201,910 | +0.95% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| gold | 194,238 | -2.88% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,573 (-5.21%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,233 | +2.51% |
| gold | +2,844 | +1.49% |
| benchmark_smallcap | +2,511 | +1.28% |
| oracle | +1,867 | +0.93% |
| random_hold | +1,642 | +0.81% |
| unified | +1,534 | +0.71% |
| intraweek | +596 | +0.28% |
| intramonth | +473 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -441 | -0.21% |
| snake_abs_exit_conv | -446 | -0.21% |
| snake_abs | -448 | -0.21% |
| snake_abs_exit | -572 | -0.27% |
| snake_anaconda | -1,077 | -0.53% |
| snake_viper_tick | -3,490 | -1.70% |
| snake_viper_wild | -3,588 | -1.72% |

Average per day so far: snake_abs_exit_conv Rs +583, snake_abs_exit Rs +573, unified Rs +570, benchmark Rs +500, snake_abs_conv Rs +453, snake_abs Rs +441, intraweek Rs +368, snake_viper_wild Rs +272, intramonth Rs +267, random_hold Rs +177, oracle Rs +131, snake_anaconda Rs +119, snake_viper_tick Rs +112, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -34, gold Rs -206, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.