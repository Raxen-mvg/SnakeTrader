# Paper trading report

Updated 2026-11-27 13:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,860 | +11.93% | 0 | - | 237 |
| unified | 223,295 | +11.65% | 0 | - | 236 |
| oracle | 211,742 | +5.87% | 0 | - | 233 |
| intramonth | 210,893 | +5.45% | 0 | - | 235 |
| random_hold | 210,789 | +5.39% | 13 | 69% | 1,037 |
| intraweek | 208,431 | +4.21% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 205,505 | +2.75% | 2 | 50% | 345 |
| snake_abs_exit | 204,490 | +2.25% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,322 | +0.66% | 0 | - | 237 |
| snake_abs | 200,214 | +0.11% | 1 | 100% | 255 |
| snake_abs_conv | 200,032 | +0.02% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,511 | -3.25% | 3 | 33% | 374 |
| snake_viper_wild | 191,986 | -4.01% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,727 | -5.64% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,808 | -15.10% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,838 (-5.58%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,108 | +2.55% |
| gold | +3,814 | +2.30% |
| snake_abs_exit | +3,413 | +1.70% |
| random_hold | +2,195 | +1.05% |
| snake_abs_conv | +1,665 | +0.84% |
| snake_abs | +1,662 | +0.84% |
| intraweek | +1,382 | +0.67% |
| snake_anaconda | +1,215 | +0.63% |
| benchmark_smallcap | +482 | +0.24% |
| intramonth | +360 | +0.17% |
| unified | +216 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -214 | -0.11% |
| snake_viper_wild | -219 | -0.11% |
| oracle | -493 | -0.23% |
| benchmark | -2,127 | -0.94% |

Average per day so far: benchmark Rs +568, unified Rs +555, oracle Rs +280, intramonth Rs +259, random_hold Rs +257, intraweek Rs +201, snake_abs_exit_conv Rs +141, snake_abs_exit Rs +115, nifty_calls Rs +44, benchmark_smallcap Rs +35, snake_abs Rs +5, snake_abs_conv Rs +1, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -175, snake_viper_wild Rs -236, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -364, gold Rs -719

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.