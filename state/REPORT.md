# Paper trading report

Updated 2026-11-27 14:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,013 | +12.01% | 0 | - | 237 |
| unified | 223,459 | +11.73% | 0 | - | 236 |
| oracle | 212,097 | +6.05% | 0 | - | 233 |
| random_hold | 211,150 | +5.58% | 13 | 69% | 1,037 |
| intramonth | 210,746 | +5.37% | 0 | - | 235 |
| intraweek | 208,425 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,250 | +3.12% | 2 | 50% | 345 |
| snake_abs_exit | 203,876 | +1.94% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,546 | -0.23% | 1 | 100% | 255 |
| snake_abs_conv | 199,357 | -0.32% | 1 | 100% | 255 |
| snake_anaconda | 192,984 | -3.51% | 3 | 33% | 374 |
| snake_viper_wild | 192,337 | -3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,070 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,318 | -14.84% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,996 (-5.50%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,853 | +2.92% |
| gold | +4,324 | +2.60% |
| snake_abs_exit | +2,798 | +1.39% |
| random_hold | +2,556 | +1.23% |
| intraweek | +1,377 | +0.67% |
| snake_abs | +994 | +0.50% |
| snake_abs_conv | +990 | +0.50% |
| snake_anaconda | +688 | +0.36% |
| benchmark_smallcap | +617 | +0.31% |
| unified | +380 | +0.17% |
| intramonth | +213 | +0.10% |
| snake_viper_wild | +131 | +0.07% |
| snake_viper_tick | +129 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -138 | -0.07% |
| benchmark | -1,974 | -0.87% |

Average per day so far: benchmark Rs +572, unified Rs +559, oracle Rs +288, random_hold Rs +265, intramonth Rs +256, intraweek Rs +201, snake_abs_exit_conv Rs +160, snake_abs_exit Rs +99, nifty_calls Rs +44, benchmark_smallcap Rs +38, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -11, snake_abs_conv Rs -16, snake_anaconda Rs -190, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -353, gold Rs -707

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.