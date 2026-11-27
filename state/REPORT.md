# Paper trading report

Updated 2026-11-27 14:07 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,975 | +11.99% | 0 | - | 237 |
| unified | 223,469 | +11.73% | 0 | - | 236 |
| oracle | 212,164 | +6.08% | 0 | - | 233 |
| random_hold | 211,155 | +5.58% | 13 | 69% | 1,037 |
| intramonth | 210,928 | +5.46% | 0 | - | 235 |
| intraweek | 208,527 | +4.26% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,226 | +2.61% | 2 | 50% | 345 |
| snake_abs_exit | 203,759 | +1.88% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,524 | +0.76% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,515 | -0.24% | 1 | 100% | 255 |
| snake_abs_conv | 199,324 | -0.34% | 1 | 100% | 255 |
| snake_anaconda | 192,962 | -3.52% | 3 | 33% | 374 |
| snake_viper_wild | 192,558 | -3.72% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,286 | -5.36% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,285 | -14.86% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,052 (-5.47%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,829 | +2.41% |
| gold | +4,291 | +2.58% |
| snake_abs_exit | +2,682 | +1.33% |
| random_hold | +2,561 | +1.23% |
| intraweek | +1,478 | +0.71% |
| snake_abs | +963 | +0.48% |
| snake_abs_conv | +958 | +0.48% |
| benchmark_smallcap | +684 | +0.34% |
| snake_anaconda | +666 | +0.35% |
| intramonth | +395 | +0.19% |
| unified | +391 | +0.17% |
| snake_viper_wild | +352 | +0.18% |
| snake_viper_tick | +345 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -71 | -0.03% |
| benchmark | -2,012 | -0.89% |

Average per day so far: benchmark Rs +571, unified Rs +559, oracle Rs +290, random_hold Rs +266, intramonth Rs +260, intraweek Rs +203, snake_abs_exit_conv Rs +134, snake_abs_exit Rs +96, nifty_calls Rs +44, benchmark_smallcap Rs +40, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -12, snake_abs_conv Rs -17, snake_anaconda Rs -190, snake_viper_wild Rs -219, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -346, gold Rs -708

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.