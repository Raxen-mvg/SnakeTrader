# Paper trading report

Updated 2026-11-27 14:01 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,975 | +11.99% | 0 | - | 237 |
| unified | 223,265 | +11.63% | 0 | - | 236 |
| oracle | 211,776 | +5.89% | 0 | - | 233 |
| random_hold | 210,937 | +5.47% | 13 | 69% | 1,037 |
| intramonth | 210,780 | +5.39% | 0 | - | 235 |
| intraweek | 208,350 | +4.17% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,637 | +2.82% | 2 | 50% | 345 |
| snake_abs_exit | 204,562 | +2.28% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| snake_abs | 200,446 | +0.22% | 1 | 100% | 255 |
| snake_abs_conv | 200,264 | +0.13% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,723 | -3.14% | 3 | 33% | 374 |
| snake_viper_wild | 192,366 | -3.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,098 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,400 | -14.80% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,864 (-5.57%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,240 | +2.62% |
| gold | +4,406 | +2.65% |
| snake_abs_exit | +3,485 | +1.73% |
| random_hold | +2,343 | +1.12% |
| snake_abs_conv | +1,898 | +0.96% |
| snake_abs | +1,893 | +0.95% |
| snake_anaconda | +1,426 | +0.74% |
| intraweek | +1,301 | +0.63% |
| benchmark_smallcap | +706 | +0.35% |
| intramonth | +246 | +0.12% |
| unified | +187 | +0.08% |
| snake_viper_wild | +160 | +0.08% |
| snake_viper_tick | +157 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -459 | -0.22% |
| benchmark | -2,012 | -0.89% |

Average per day so far: benchmark Rs +571, unified Rs +554, oracle Rs +280, random_hold Rs +260, intramonth Rs +257, intraweek Rs +199, snake_abs_exit_conv Rs +145, snake_abs_exit Rs +117, nifty_calls Rs +44, benchmark_smallcap Rs +41, snake_abs Rs +11, snake_abs_conv Rs +7, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -352, gold Rs -705

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.