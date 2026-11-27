# Paper trading report

Updated 2026-11-27 09:49 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,658 | +12.83% | 0 | - | 237 |
| unified | 223,473 | +11.74% | 0 | - | 236 |
| oracle | 212,511 | +6.25% | 0 | - | 233 |
| intramonth | 211,104 | +5.55% | 0 | - | 235 |
| random_hold | 209,744 | +4.87% | 13 | 69% | 1,037 |
| intraweek | 208,038 | +4.02% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,181 | +2.59% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,090 | +2.04% | 2 | 50% | 345 |
| benchmark_smallcap | 202,511 | +1.25% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,104 | +0.55% | 1 | 100% | 255 |
| snake_abs_conv | 200,926 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,745 | -2.63% | 3 | 33% | 374 |
| snake_viper_wild | 192,940 | -3.53% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,660 | -5.17% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,411 | -15.79% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,942 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,103 | +2.04% |
| snake_abs_exit_conv | +3,693 | +1.84% |
| snake_abs_conv | +2,559 | +1.29% |
| snake_abs | +2,552 | +1.28% |
| snake_anaconda | +2,449 | +1.27% |
| gold | +2,417 | +1.46% |
| benchmark_smallcap | +1,670 | +0.83% |
| random_hold | +1,150 | +0.55% |
| intraweek | +989 | +0.48% |
| snake_viper_wild | +734 | +0.38% |
| snake_viper_tick | +719 | +0.38% |
| intramonth | +570 | +0.27% |
| unified | +395 | +0.18% |
| oracle | +275 | +0.13% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -329 | -0.15% |

Average per day so far: benchmark Rs +611, unified Rs +559, oracle Rs +298, intramonth Rs +264, random_hold Rs +232, intraweek Rs +191, snake_abs_exit Rs +133, snake_abs_exit_conv Rs +105, benchmark_smallcap Rs +66, nifty_calls Rs +44, snake_abs Rs +28, snake_abs_conv Rs +24, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -142, snake_viper_wild Rs -208, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -334, gold Rs -752

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.