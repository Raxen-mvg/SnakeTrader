# Paper trading report

Updated 2026-11-26 13:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,551 | +12.78% | 0 | - | 237 |
| unified | 223,349 | +11.68% | 0 | - | 236 |
| oracle | 213,142 | +6.57% | 0 | - | 233 |
| intramonth | 210,489 | +5.24% | 0 | - | 235 |
| random_hold | 209,931 | +4.96% | 13 | 69% | 1,037 |
| intraweek | 208,522 | +4.26% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,538 | +0.27% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,889 | -0.06% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,372 | -0.31% | 2 | 50% | 345 |
| snake_abs | 197,689 | -1.16% | 1 | 100% | 255 |
| snake_abs_conv | 197,486 | -1.26% | 1 | 100% | 255 |
| snake_viper_wild | 191,793 | -4.10% | 16 | 50% | 2,827 |
| snake_anaconda | 191,380 | -4.31% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,537 | -5.73% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,339 | -16.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,762 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,779 | +0.86% |
| gold | +1,743 | +1.06% |
| benchmark_smallcap | +1,726 | +0.87% |
| benchmark | +528 | +0.23% |
| random_hold | +438 | +0.21% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -653 | -0.30% |
| unified | -751 | -0.34% |
| intramonth | -1,204 | -0.57% |
| snake_abs_exit | -2,367 | -1.17% |
| snake_abs | -2,461 | -1.23% |
| snake_abs_conv | -2,486 | -1.24% |
| snake_abs_exit_conv | -2,604 | -1.29% |
| snake_anaconda | -3,173 | -1.63% |
| snake_viper_tick | -5,640 | -2.90% |
| snake_viper_wild | -5,751 | -2.91% |

Average per day so far: benchmark Rs +623, unified Rs +569, oracle Rs +321, intramonth Rs +256, random_hold Rs +242, intraweek Rs +208, nifty_calls Rs +45, benchmark_smallcap Rs +15, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -3, snake_abs_exit_conv Rs -17, snake_abs Rs -59, snake_abs_conv Rs -66, snake_anaconda Rs -239, snake_viper_wild Rs -249, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -382, gold Rs -821

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.