# Paper trading report

Updated 2026-11-25 10:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,427 | +12.71% | 0 | - | 236 |
| benchmark | 224,893 | +12.45% | 0 | - | 237 |
| oracle | 213,070 | +6.54% | 0 | - | 233 |
| intramonth | 213,036 | +6.52% | 0 | - | 235 |
| random_hold | 209,328 | +4.66% | 12 | 75% | 1,009 |
| intraweek | 207,117 | +3.56% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,004 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,432 | +0.72% | 2 | 50% | 345 |
| snake_abs | 201,081 | +0.54% | 1 | 100% | 255 |
| snake_abs_conv | 200,889 | +0.45% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,226 | -0.39% | 0 | - | 237 |
| snake_viper_wild | 195,537 | -2.23% | 16 | 50% | 2,827 |
| snake_anaconda | 193,616 | -3.19% | 3 | 33% | 374 |
| snake_viper_tick | 192,212 | -3.89% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,682 | -17.16% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,339 (-5.33%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,420 | +1.54% |
| unified | +1,142 | +0.51% |
| random_hold | +902 | +0.43% |
| oracle | +728 | +0.34% |
| intramonth | +285 | +0.13% |
| benchmark_smallcap | +247 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,748 | -2.21% |
| snake_abs | -4,380 | -2.13% |
| snake_abs_conv | -4,413 | -2.15% |
| intraweek | -4,502 | -2.13% |
| snake_anaconda | -5,088 | -2.56% |
| snake_viper_tick | -5,480 | -2.77% |
| snake_abs_exit | -5,491 | -2.65% |
| snake_viper_wild | -5,587 | -2.78% |
| snake_abs_exit_conv | -5,614 | -2.71% |

Average per day so far: unified Rs +636, benchmark Rs +622, oracle Rs +327, intramonth Rs +326, random_hold Rs +233, intraweek Rs +178, snake_abs_exit Rs +54, nifty_calls Rs +46, snake_abs_exit_conv Rs +39, snake_abs Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_viper_wild Rs -139, snake_anaconda Rs -182, snake_viper_tick Rs -269, snake_nonews Rs -292, snake Rs -311, gold Rs -858

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.