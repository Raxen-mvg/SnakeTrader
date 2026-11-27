# Paper trading report

Updated 2026-11-27 10:03 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,528 | +12.76% | 0 | - | 237 |
| unified | 223,273 | +11.64% | 0 | - | 236 |
| oracle | 212,613 | +6.31% | 0 | - | 233 |
| intramonth | 210,882 | +5.44% | 0 | - | 235 |
| random_hold | 209,970 | +4.99% | 13 | 69% | 1,037 |
| intraweek | 208,355 | +4.18% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,710 | +2.85% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,572 | +2.29% | 2 | 50% | 345 |
| benchmark_smallcap | 202,073 | +1.04% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,630 | +0.81% | 1 | 100% | 255 |
| snake_abs_conv | 201,454 | +0.73% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,300 | -2.35% | 3 | 33% | 374 |
| snake_viper_wild | 193,377 | -3.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,088 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,493 | -15.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,923 (-5.54%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,633 | +2.30% |
| snake_abs_exit_conv | +4,175 | +2.08% |
| snake_abs_conv | +3,087 | +1.56% |
| snake_abs | +3,078 | +1.55% |
| snake_anaconda | +3,004 | +1.56% |
| gold | +2,499 | +1.50% |
| random_hold | +1,376 | +0.66% |
| intraweek | +1,307 | +0.63% |
| benchmark_smallcap | +1,233 | +0.61% |
| snake_viper_wild | +1,171 | +0.61% |
| snake_viper_tick | +1,147 | +0.61% |
| oracle | +378 | +0.18% |
| intramonth | +349 | +0.17% |
| unified | +195 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -459 | -0.20% |

Average per day so far: benchmark Rs +608, unified Rs +554, oracle Rs +300, intramonth Rs +259, random_hold Rs +237, intraweek Rs +199, snake_abs_exit Rs +146, snake_abs_exit_conv Rs +117, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +41, snake_abs_conv Rs +37, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -127, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -320, gold Rs -750

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.