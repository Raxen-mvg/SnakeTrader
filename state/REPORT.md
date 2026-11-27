# Paper trading report

Updated 2026-11-27 11:13 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,564 | +12.28% | 0 | - | 237 |
| unified | 222,475 | +11.24% | 0 | - | 236 |
| oracle | 212,123 | +6.06% | 0 | - | 233 |
| intramonth | 210,292 | +5.15% | 0 | - | 235 |
| random_hold | 210,099 | +5.05% | 13 | 69% | 1,037 |
| intraweek | 207,711 | +3.85% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,265 | +2.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,110 | +2.06% | 2 | 50% | 345 |
| benchmark_smallcap | 202,096 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,972 | +0.49% | 1 | 100% | 255 |
| snake_abs_conv | 200,795 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,541 | -2.73% | 3 | 33% | 374 |
| snake_viper_wild | 193,359 | -3.32% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,071 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,315 | -15.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,557 (-5.72%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,188 | +2.08% |
| snake_abs_exit_conv | +3,713 | +1.85% |
| gold | +3,321 | +2.00% |
| snake_abs_conv | +2,429 | +1.22% |
| snake_abs | +2,419 | +1.22% |
| snake_anaconda | +2,244 | +1.17% |
| random_hold | +1,505 | +0.72% |
| benchmark_smallcap | +1,256 | +0.62% |
| snake_viper_wild | +1,154 | +0.60% |
| snake_viper_tick | +1,130 | +0.60% |
| intraweek | +662 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -113 | -0.05% |
| intramonth | -242 | -0.12% |
| unified | -603 | -0.27% |
| benchmark | -1,423 | -0.63% |

Average per day so far: benchmark Rs +585, unified Rs +535, oracle Rs +289, intramonth Rs +245, random_hold Rs +240, intraweek Rs +184, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +105, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +24, snake_abs_conv Rs +20, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -148, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -320, gold Rs -731

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.