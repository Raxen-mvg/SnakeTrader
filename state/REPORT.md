# Paper trading report

Updated 2026-11-27 10:42 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,893 | +12.45% | 0 | - | 237 |
| unified | 222,906 | +11.45% | 0 | - | 236 |
| oracle | 212,251 | +6.12% | 0 | - | 233 |
| intramonth | 210,756 | +5.38% | 0 | - | 235 |
| random_hold | 209,998 | +5.00% | 13 | 69% | 1,037 |
| intraweek | 208,055 | +4.03% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,581 | +2.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,266 | +2.13% | 2 | 50% | 345 |
| benchmark_smallcap | 202,174 | +1.09% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,362 | +0.68% | 1 | 100% | 255 |
| snake_abs_conv | 201,186 | +0.59% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,706 | -2.65% | 3 | 33% | 374 |
| snake_viper_wild | 193,561 | -3.22% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,269 | -4.87% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,690 | -15.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,749 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,504 | +2.24% |
| snake_abs_exit_conv | +3,869 | +1.93% |
| snake_abs_conv | +2,819 | +1.42% |
| snake_abs | +2,810 | +1.42% |
| gold | +2,696 | +1.62% |
| snake_anaconda | +2,410 | +1.25% |
| random_hold | +1,404 | +0.67% |
| snake_viper_wild | +1,355 | +0.70% |
| benchmark_smallcap | +1,334 | +0.66% |
| snake_viper_tick | +1,328 | +0.70% |
| intraweek | +1,006 | +0.49% |
| intramonth | +223 | +0.11% |
| oracle | +15 | +0.01% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -173 | -0.08% |
| benchmark | -1,094 | -0.48% |

Average per day so far: benchmark Rs +593, unified Rs +545, oracle Rs +292, intramonth Rs +256, random_hold Rs +238, intraweek Rs +192, snake_abs_exit Rs +143, snake_abs_exit_conv Rs +109, benchmark_smallcap Rs +57, nifty_calls Rs +44, snake_abs Rs +34, snake_abs_conv Rs +30, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -143, snake_viper_wild Rs -189, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -314, gold Rs -745

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.