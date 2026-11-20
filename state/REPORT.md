# Paper trading report

Updated 2026-11-20 15:30 IST. Model picks as of 2026-11-18. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 226,182 | +13.09% | 0 | - | 236 |
| benchmark | 225,138 | +12.57% | 0 | - | 237 |
| intraweek | 215,712 | +7.86% | 35 | 54% | 3,851 |
| intramonth | 215,004 | +7.50% | 0 | - | 235 |
| oracle | 212,478 | +6.24% | 0 | - | 233 |
| random_hold | 210,759 | +5.38% | 11 | 73% | 979 |
| snake_abs_exit | 208,562 | +4.28% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,616 | +3.31% | 2 | 50% | 345 |
| snake_abs | 205,920 | +2.96% | 1 | 100% | 255 |
| snake_abs_conv | 205,783 | +2.89% | 1 | 100% | 255 |
| snake_viper_wild | 202,829 | +1.42% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,907 | +0.45% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,906 | -0.05% | 3 | 33% | 374 |
| snake_viper_tick | 199,372 | -0.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,049 | -15.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,986 (-4.01%).

Profit on 2026-11-20:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,823 | +1.33% |
| benchmark | +2,762 | +1.24% |
| random_hold | +2,306 | +1.11% |
| unified | +1,567 | +0.70% |
| intramonth | +996 | +0.47% |
| oracle | +390 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -560 | -0.28% |
| snake_abs | -3,060 | -1.46% |
| snake_abs_conv | -3,077 | -1.47% |
| snake_anaconda | -3,558 | -1.75% |
| snake_abs_exit_conv | -4,448 | -2.11% |
| snake_viper_tick | -4,605 | -2.26% |
| snake_viper_wild | -4,694 | -2.26% |
| snake_abs_exit | -4,789 | -2.25% |
| gold | -6,724 | -3.85% |

Average per day so far: unified Rs +689, benchmark Rs +662, intraweek Rs +413, intramonth Rs +395, oracle Rs +328, random_hold Rs +283, snake_abs_exit Rs +245, snake_abs_exit_conv Rs +189, snake_abs_conv Rs +165, snake_abs Rs +164, snake_viper_wild Rs +94, nifty_calls Rs +48, benchmark_smallcap Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -3, snake_viper_tick Rs -23, snake_nonews Rs -308, snake Rs -328, gold Rs -841

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.