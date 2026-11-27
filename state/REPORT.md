# Paper trading report

Updated 2026-11-27 13:43 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,059 | +12.03% | 0 | - | 237 |
| unified | 223,049 | +11.53% | 0 | - | 236 |
| oracle | 211,584 | +5.79% | 0 | - | 233 |
| random_hold | 210,860 | +5.43% | 13 | 69% | 1,037 |
| intramonth | 210,453 | +5.23% | 0 | - | 235 |
| intraweek | 208,477 | +4.24% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,400 | +2.70% | 2 | 50% | 345 |
| snake_abs_exit | 204,464 | +2.23% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| snake_abs | 200,285 | +0.14% | 1 | 100% | 255 |
| snake_abs_conv | 200,103 | +0.05% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,584 | -3.21% | 3 | 33% | 374 |
| snake_viper_wild | 191,996 | -4.00% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,736 | -5.63% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,087 | -14.96% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,733 (-5.63%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,003 | +2.50% |
| gold | +4,094 | +2.47% |
| snake_abs_exit | +3,387 | +1.68% |
| random_hold | +2,266 | +1.09% |
| snake_abs_conv | +1,737 | +0.88% |
| snake_abs | +1,733 | +0.87% |
| intraweek | +1,428 | +0.69% |
| snake_anaconda | +1,288 | +0.67% |
| benchmark_smallcap | +617 | +0.31% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -29 | -0.01% |
| intramonth | -80 | -0.04% |
| snake_viper_tick | -205 | -0.11% |
| snake_viper_wild | -210 | -0.11% |
| oracle | -651 | -0.31% |
| benchmark | -1,928 | -0.85% |

Average per day so far: benchmark Rs +573, unified Rs +549, oracle Rs +276, random_hold Rs +259, intramonth Rs +249, intraweek Rs +202, snake_abs_exit_conv Rs +138, snake_abs_exit Rs +114, nifty_calls Rs +44, benchmark_smallcap Rs +38, snake_abs Rs +7, snake_abs_conv Rs +3, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -173, snake_viper_wild Rs -235, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -363, gold Rs -712

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.