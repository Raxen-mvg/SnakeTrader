# Paper trading report

Updated 2026-11-26 10:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,581 | +12.79% | 0 | - | 237 |
| unified | 223,637 | +11.82% | 0 | - | 236 |
| oracle | 213,146 | +6.57% | 0 | - | 233 |
| intramonth | 210,940 | +5.47% | 0 | - | 235 |
| random_hold | 209,905 | +4.95% | 13 | 69% | 1,037 |
| intraweek | 207,787 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,156 | +1.58% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,517 | +1.26% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,605 | +0.30% | 0 | - | 237 |
| snake_abs | 200,431 | +0.21% | 1 | 100% | 255 |
| snake_abs_conv | 200,258 | +0.13% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,424 | -2.79% | 3 | 33% | 374 |
| snake_viper_wild | 193,550 | -3.23% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,257 | -4.87% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,835 | -16.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,051 (-5.47%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,239 | +1.97% |
| benchmark_smallcap | +1,794 | +0.90% |
| intraweek | +1,044 | +0.51% |
| snake_abs_exit | +900 | +0.45% |
| benchmark | +558 | +0.25% |
| snake_abs_exit_conv | +542 | +0.27% |
| random_hold | +413 | +0.20% |
| snake_abs_conv | +286 | +0.14% |
| snake_abs | +281 | +0.14% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_anaconda | -129 | -0.07% |
| unified | -463 | -0.21% |
| oracle | -649 | -0.30% |
| intramonth | -753 | -0.36% |
| snake_viper_tick | -3,920 | -2.02% |
| snake_viper_wild | -3,994 | -2.02% |

Average per day so far: benchmark Rs +624, unified Rs +577, oracle Rs +321, intramonth Rs +267, random_hold Rs +242, intraweek Rs +190, snake_abs_exit Rs +83, snake_abs_exit_conv Rs +66, nifty_calls Rs +45, benchmark_smallcap Rs +16, snake_abs Rs +11, snake_abs_conv Rs +7, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -155, snake_viper_wild Rs -195, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -325, gold Rs -785

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.