# Paper trading report

Updated 2026-11-25 10:06 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,984 | +12.49% | 0 | - | 236 |
| benchmark | 224,564 | +12.28% | 0 | - | 237 |
| oracle | 212,738 | +6.37% | 0 | - | 233 |
| intramonth | 212,649 | +6.33% | 0 | - | 235 |
| random_hold | 209,309 | +4.66% | 12 | 75% | 1,009 |
| intraweek | 208,431 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,435 | +1.22% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,829 | +0.91% | 2 | 50% | 345 |
| snake_abs | 201,442 | +0.72% | 1 | 100% | 255 |
| snake_abs_conv | 201,257 | +0.63% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,125 | -0.44% | 0 | - | 237 |
| snake_viper_wild | 198,201 | -0.90% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,830 | -2.58% | 15 | 47% | 2,625 |
| snake_anaconda | 194,217 | -2.89% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,566 | -17.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,409 (-5.30%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,091 | +1.40% |
| random_hold | +883 | +0.42% |
| unified | +699 | +0.31% |
| oracle | +396 | +0.19% |
| benchmark_smallcap | +146 | +0.07% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -102 | -0.05% |
| snake_viper_tick | -2,862 | -1.45% |
| snake_viper_wild | -2,923 | -1.45% |
| intraweek | -3,188 | -1.51% |
| gold | -3,863 | -2.28% |
| snake_abs | -4,019 | -1.96% |
| snake_abs_conv | -4,045 | -1.97% |
| snake_anaconda | -4,486 | -2.26% |
| snake_abs_exit | -5,060 | -2.44% |
| snake_abs_exit_conv | -5,217 | -2.52% |

Average per day so far: unified Rs +625, benchmark Rs +614, oracle Rs +318, intramonth Rs +316, random_hold Rs +233, intraweek Rs +211, snake_abs_exit Rs +66, snake_abs_exit_conv Rs +49, nifty_calls Rs +46, snake_abs Rs +38, snake_abs_conv Rs +34, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -24, snake_viper_wild Rs -56, snake_anaconda Rs -165, snake_viper_tick Rs -178, snake_nonews Rs -292, snake Rs -311, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.