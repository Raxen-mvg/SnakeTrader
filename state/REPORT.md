# Paper trading report

Updated 2026-11-06 09:21 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,028 | +7.51% | 0 | - | 236 |
| benchmark | 213,678 | +6.84% | 0 | - | 237 |
| snake_abs_exit_conv | 211,338 | +5.67% | 1 | 100% | 255 |
| snake_abs_exit | 211,083 | +5.54% | 1 | 100% | 260 |
| intraweek | 208,931 | +4.47% | 25 | 48% | 2,757 |
| snake_abs | 208,258 | +4.13% | 1 | 100% | 255 |
| snake_abs_conv | 208,105 | +4.05% | 1 | 100% | 255 |
| intramonth | 206,675 | +3.34% | 0 | - | 235 |
| oracle | 203,782 | +1.89% | 0 | - | 233 |
| random_hold | 203,603 | +1.80% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 199,197 | -0.40% | 3 | 33% | 702 |
| snake_anaconda | 198,616 | -0.69% | 3 | 33% | 374 |
| snake_viper_tick | 195,818 | -2.09% | 2 | 0% | 532 |
| benchmark_smallcap | 195,302 | -2.35% | 0 | - | 237 |
| gold | 190,489 | -4.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,688 (-6.16%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -92 | -0.04% |
| oracle | -290 | -0.14% |
| intraweek | -487 | -0.23% |
| random_hold | -720 | -0.35% |
| unified | -956 | -0.44% |
| intramonth | -1,274 | -0.61% |
| benchmark_smallcap | -3,385 | -1.70% |
| snake_abs | -3,431 | -1.62% |
| snake_abs_conv | -3,439 | -1.63% |
| snake_abs_exit_conv | -3,466 | -1.61% |
| snake_abs_exit | -3,575 | -1.67% |
| gold | -3,732 | -1.92% |
| snake_anaconda | -3,863 | -1.91% |
| snake_viper_tick | -5,320 | -2.65% |
| snake_viper_wild | -5,459 | -2.67% |

Average per day so far: unified Rs +518, benchmark Rs +472, snake_abs_exit_conv Rs +436, snake_abs_exit Rs +426, snake_abs_conv Rs +312, intraweek Rs +308, snake_abs Rs +306, intramonth Rs +230, oracle Rs +130, random_hold Rs +124, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -38, snake_anaconda Rs -58, benchmark_smallcap Rs -188, snake_viper_tick Rs -232, gold Rs -328, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.