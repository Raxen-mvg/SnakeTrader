# Paper trading report

Updated 2026-11-25 14:01 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,770 | +12.38% | 0 | - | 237 |
| unified | 224,674 | +12.34% | 0 | - | 236 |
| oracle | 212,584 | +6.29% | 0 | - | 233 |
| intramonth | 212,210 | +6.11% | 0 | - | 235 |
| random_hold | 209,527 | +4.76% | 12 | 75% | 1,009 |
| intraweek | 207,227 | +3.61% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,515 | +0.76% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,228 | +0.61% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,776 | -0.11% | 1 | 100% | 255 |
| snake_abs_conv | 199,582 | -0.21% | 1 | 100% | 255 |
| benchmark_smallcap | 198,665 | -0.67% | 0 | - | 237 |
| snake_viper_wild | 197,183 | -1.41% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,824 | -3.09% | 15 | 47% | 2,625 |
| snake_anaconda | 193,314 | -3.34% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,925 | -17.54% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,949 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,297 | +1.49% |
| random_hold | +1,101 | +0.53% |
| unified | +389 | +0.17% |
| oracle | +242 | +0.11% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -314 | -0.16% |
| intramonth | -542 | -0.26% |
| snake_viper_tick | -3,868 | -1.96% |
| snake_viper_wild | -3,941 | -1.96% |
| intraweek | -4,392 | -2.08% |
| gold | -4,505 | -2.66% |
| snake_anaconda | -5,389 | -2.71% |
| snake_abs | -5,685 | -2.77% |
| snake_abs_conv | -5,720 | -2.79% |
| snake_abs_exit_conv | -5,818 | -2.81% |
| snake_abs_exit | -5,980 | -2.88% |

Average per day so far: benchmark Rs +619, unified Rs +617, oracle Rs +315, intramonth Rs +305, random_hold Rs +238, intraweek Rs +181, nifty_calls Rs +46, snake_abs_exit Rs +41, snake_abs_exit_conv Rs +33, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, benchmark_smallcap Rs -37, snake_viper_wild Rs -88, snake_anaconda Rs -191, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -877

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.