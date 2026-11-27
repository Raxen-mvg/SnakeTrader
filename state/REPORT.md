# Paper trading report

Updated 2026-11-27 11:16 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,373 | +12.19% | 0 | - | 237 |
| unified | 222,427 | +11.21% | 0 | - | 236 |
| oracle | 211,990 | +6.00% | 0 | - | 233 |
| intramonth | 210,190 | +5.09% | 0 | - | 235 |
| random_hold | 210,129 | +5.06% | 13 | 69% | 1,037 |
| intraweek | 207,718 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,167 | +2.58% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,017 | +2.01% | 2 | 50% | 345 |
| benchmark_smallcap | 202,006 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,860 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,683 | +0.34% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,431 | -2.79% | 3 | 33% | 374 |
| snake_viper_wild | 193,359 | -3.32% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,071 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,150 | -15.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,506 (-5.75%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,090 | +2.03% |
| snake_abs_exit_conv | +3,620 | +1.81% |
| gold | +3,156 | +1.90% |
| snake_abs_conv | +2,317 | +1.17% |
| snake_abs | +2,308 | +1.16% |
| snake_anaconda | +2,134 | +1.11% |
| random_hold | +1,535 | +0.74% |
| benchmark_smallcap | +1,166 | +0.58% |
| snake_viper_wild | +1,154 | +0.60% |
| snake_viper_tick | +1,130 | +0.60% |
| intraweek | +669 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -246 | -0.12% |
| intramonth | -343 | -0.16% |
| unified | -652 | -0.29% |
| benchmark | -1,614 | -0.71% |

Average per day so far: benchmark Rs +580, unified Rs +534, oracle Rs +285, intramonth Rs +243, random_hold Rs +241, intraweek Rs +184, snake_abs_exit Rs +132, snake_abs_exit_conv Rs +103, benchmark_smallcap Rs +53, nifty_calls Rs +44, snake_abs Rs +21, snake_abs_conv Rs +18, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -151, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -320, gold Rs -735

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.