# Paper trading report

Updated 2026-11-27 10:24 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,260 | +12.63% | 0 | - | 237 |
| unified | 222,610 | +11.30% | 0 | - | 236 |
| oracle | 212,235 | +6.12% | 0 | - | 233 |
| intramonth | 210,546 | +5.27% | 0 | - | 235 |
| random_hold | 210,133 | +5.07% | 13 | 69% | 1,037 |
| intraweek | 208,361 | +4.18% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,210 | +2.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,956 | +1.98% | 2 | 50% | 345 |
| benchmark_smallcap | 202,096 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,151 | +0.57% | 1 | 100% | 255 |
| snake_abs_conv | 200,968 | +0.48% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,494 | -2.75% | 3 | 33% | 374 |
| snake_viper_wild | 193,767 | -3.12% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,471 | -4.76% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,361 | -15.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,707 (-5.65%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,133 | +2.06% |
| snake_abs_exit_conv | +3,559 | +1.78% |
| snake_abs_conv | +2,601 | +1.31% |
| snake_abs | +2,598 | +1.31% |
| gold | +2,367 | +1.43% |
| snake_anaconda | +2,197 | +1.14% |
| snake_viper_wild | +1,562 | +0.81% |
| random_hold | +1,539 | +0.74% |
| snake_viper_tick | +1,530 | +0.81% |
| intraweek | +1,313 | +0.63% |
| benchmark_smallcap | +1,256 | +0.62% |
| intramonth | +12 | +0.01% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -1 | -0.00% |
| unified | -469 | -0.21% |
| benchmark | -727 | -0.32% |

Average per day so far: benchmark Rs +601, unified Rs +538, oracle Rs +291, intramonth Rs +251, random_hold Rs +241, intraweek Rs +199, snake_abs_exit Rs +134, snake_abs_exit_conv Rs +101, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +29, snake_abs_conv Rs +25, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -149, snake_viper_wild Rs -183, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -307, gold Rs -753

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.