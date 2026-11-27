# Paper trading report

Updated 2026-11-27 09:59 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,474 | +12.74% | 0 | - | 237 |
| unified | 223,172 | +11.59% | 0 | - | 236 |
| oracle | 212,421 | +6.21% | 0 | - | 233 |
| intramonth | 210,810 | +5.41% | 0 | - | 235 |
| random_hold | 209,682 | +4.84% | 13 | 69% | 1,037 |
| intraweek | 207,839 | +3.92% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,589 | +2.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,439 | +2.22% | 2 | 50% | 345 |
| benchmark_smallcap | 202,096 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,586 | +0.79% | 1 | 100% | 255 |
| snake_abs_conv | 201,407 | +0.70% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 195,198 | -2.40% | 3 | 33% | 374 |
| snake_viper_wild | 193,386 | -3.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,097 | -4.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,460 | -15.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,757 (-5.62%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,512 | +2.24% |
| snake_abs_exit_conv | +4,042 | +2.02% |
| snake_abs_conv | +3,041 | +1.53% |
| snake_abs | +3,034 | +1.53% |
| snake_anaconda | +2,902 | +1.51% |
| gold | +2,466 | +1.49% |
| benchmark_smallcap | +1,256 | +0.62% |
| snake_viper_wild | +1,181 | +0.61% |
| snake_viper_tick | +1,156 | +0.61% |
| random_hold | +1,088 | +0.52% |
| intraweek | +790 | +0.38% |
| intramonth | +277 | +0.13% |
| oracle | +185 | +0.09% |
| unified | +93 | +0.04% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -513 | -0.23% |

Average per day so far: benchmark Rs +607, unified Rs +552, oracle Rs +296, intramonth Rs +257, random_hold Rs +231, intraweek Rs +187, snake_abs_exit Rs +143, snake_abs_exit_conv Rs +114, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +40, snake_abs_conv Rs +36, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -130, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -319, gold Rs -751

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.