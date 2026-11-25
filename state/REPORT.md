# Paper trading report

Updated 2026-11-25 13:12 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,359 | +12.18% | 0 | - | 236 |
| benchmark | 223,875 | +11.94% | 0 | - | 237 |
| oracle | 212,456 | +6.23% | 0 | - | 233 |
| intramonth | 212,263 | +6.13% | 0 | - | 235 |
| random_hold | 209,680 | +4.84% | 12 | 75% | 1,009 |
| intraweek | 208,348 | +4.17% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,530 | +0.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,176 | +0.59% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,713 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,524 | -0.24% | 1 | 100% | 255 |
| benchmark_smallcap | 198,878 | -0.56% | 0 | - | 237 |
| snake_viper_wild | 196,766 | -1.62% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,415 | -3.29% | 15 | 47% | 2,625 |
| snake_anaconda | 193,243 | -3.38% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,531 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,036 (-5.48%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,402 | +1.08% |
| random_hold | +1,254 | +0.60% |
| oracle | +114 | +0.05% |
| unified | +74 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -101 | -0.05% |
| intramonth | -488 | -0.23% |
| intraweek | -3,271 | -1.54% |
| snake_viper_tick | -4,277 | -2.16% |
| snake_viper_wild | -4,359 | -2.17% |
| gold | -4,899 | -2.89% |
| snake_anaconda | -5,460 | -2.75% |
| snake_abs | -5,748 | -2.80% |
| snake_abs_conv | -5,779 | -2.81% |
| snake_abs_exit_conv | -5,870 | -2.83% |
| snake_abs_exit | -5,964 | -2.88% |

Average per day so far: unified Rs +609, benchmark Rs +597, oracle Rs +311, intramonth Rs +307, random_hold Rs +242, intraweek Rs +209, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +32, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, benchmark_smallcap Rs -31, snake_viper_wild Rs -101, snake_anaconda Rs -193, snake_viper_tick Rs -227, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.