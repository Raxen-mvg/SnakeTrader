# Paper trading report

Updated 2026-11-27 14:04 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,013 | +12.01% | 0 | - | 237 |
| unified | 223,375 | +11.69% | 0 | - | 236 |
| oracle | 211,862 | +5.93% | 0 | - | 233 |
| random_hold | 210,947 | +5.47% | 13 | 69% | 1,037 |
| intramonth | 210,805 | +5.40% | 0 | - | 235 |
| intraweek | 208,404 | +4.20% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 204,869 | +2.43% | 2 | 50% | 345 |
| snake_abs_exit | 203,834 | +1.92% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,546 | +0.77% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,749 | -0.13% | 1 | 100% | 255 |
| snake_abs_conv | 199,561 | -0.22% | 1 | 100% | 255 |
| snake_anaconda | 193,041 | -3.48% | 3 | 33% | 374 |
| snake_viper_wild | 192,366 | -3.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,098 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,318 | -14.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,912 (-5.54%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,472 | +2.23% |
| gold | +4,324 | +2.60% |
| snake_abs_exit | +2,756 | +1.37% |
| random_hold | +2,353 | +1.13% |
| intraweek | +1,356 | +0.66% |
| snake_abs | +1,196 | +0.60% |
| snake_abs_conv | +1,194 | +0.60% |
| snake_anaconda | +745 | +0.39% |
| benchmark_smallcap | +706 | +0.35% |
| unified | +296 | +0.13% |
| intramonth | +272 | +0.13% |
| snake_viper_wild | +160 | +0.08% |
| snake_viper_tick | +157 | +0.08% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -373 | -0.18% |
| benchmark | -1,974 | -0.87% |

Average per day so far: benchmark Rs +572, unified Rs +557, oracle Rs +282, random_hold Rs +261, intramonth Rs +257, intraweek Rs +200, snake_abs_exit_conv Rs +125, snake_abs_exit Rs +98, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -6, snake_abs_conv Rs -11, snake_anaconda Rs -188, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -352, gold Rs -707

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.