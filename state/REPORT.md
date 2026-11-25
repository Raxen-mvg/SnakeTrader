# Paper trading report

Updated 2026-11-25 11:10 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,079 | +13.04% | 0 | - | 237 |
| unified | 224,889 | +12.45% | 0 | - | 236 |
| intramonth | 212,680 | +6.34% | 0 | - | 235 |
| oracle | 211,934 | +5.97% | 0 | - | 233 |
| random_hold | 210,151 | +5.08% | 12 | 75% | 1,009 |
| intraweek | 208,502 | +4.25% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,580 | +0.79% | 2 | 50% | 345 |
| snake_abs | 201,067 | +0.53% | 1 | 100% | 255 |
| snake_abs_exit_conv | 201,036 | +0.52% | 2 | 50% | 345 |
| snake_abs_conv | 200,871 | +0.44% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,439 | -0.28% | 0 | - | 237 |
| snake_viper_wild | 195,364 | -2.32% | 16 | 50% | 2,827 |
| snake_anaconda | 193,181 | -3.41% | 3 | 33% | 374 |
| snake_viper_tick | 192,043 | -3.98% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,843 | -17.58% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,280 (-5.36%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,605 | +2.08% |
| random_hold | +1,725 | +0.83% |
| unified | +604 | +0.27% |
| benchmark_smallcap | +460 | +0.23% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -71 | -0.03% |
| oracle | -408 | -0.19% |
| intraweek | -3,117 | -1.47% |
| snake_abs | -4,393 | -2.14% |
| snake_abs_conv | -4,431 | -2.16% |
| gold | -4,587 | -2.71% |
| snake_anaconda | -5,523 | -2.78% |
| snake_viper_tick | -5,650 | -2.86% |
| snake_viper_wild | -5,760 | -2.86% |
| snake_abs_exit | -5,915 | -2.85% |
| snake_abs_exit_conv | -6,010 | -2.90% |

Average per day so far: benchmark Rs +652, unified Rs +622, intramonth Rs +317, oracle Rs +298, random_hold Rs +254, intraweek Rs +213, nifty_calls Rs +46, snake_abs_exit Rs +43, snake_abs Rs +28, snake_abs_exit_conv Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -16, snake_viper_wild Rs -145, snake_anaconda Rs -195, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -879

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.