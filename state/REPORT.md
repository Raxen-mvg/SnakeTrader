# Paper trading report

Updated 2026-11-26 11:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,872 | +12.94% | 0 | - | 237 |
| unified | 223,340 | +11.67% | 0 | - | 236 |
| oracle | 212,979 | +6.49% | 0 | - | 233 |
| intramonth | 210,609 | +5.30% | 0 | - | 235 |
| random_hold | 209,975 | +4.99% | 13 | 69% | 1,037 |
| intraweek | 208,042 | +4.02% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,736 | +0.87% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,173 | +0.59% | 2 | 50% | 345 |
| benchmark_smallcap | 200,482 | +0.24% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,351 | -0.32% | 1 | 100% | 255 |
| snake_abs_conv | 199,164 | -0.42% | 1 | 100% | 255 |
| snake_anaconda | 193,232 | -3.38% | 3 | 33% | 374 |
| snake_viper_wild | 193,190 | -3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,905 | -5.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,062 | -16.47% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,851 (-5.57%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,466 | +1.50% |
| benchmark_smallcap | +1,670 | +0.84% |
| intraweek | +1,298 | +0.63% |
| benchmark | +849 | +0.38% |
| random_hold | +482 | +0.23% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -520 | -0.26% |
| unified | -760 | -0.34% |
| snake_abs | -799 | -0.40% |
| snake_abs_exit_conv | -803 | -0.40% |
| snake_abs_conv | -809 | -0.40% |
| oracle | -816 | -0.38% |
| intramonth | -1,084 | -0.51% |
| snake_anaconda | -1,321 | -0.68% |
| snake_viper_tick | -4,272 | -2.20% |
| snake_viper_wild | -4,354 | -2.20% |

Average per day so far: benchmark Rs +631, unified Rs +569, oracle Rs +317, intramonth Rs +259, random_hold Rs +243, intraweek Rs +196, snake_abs_exit Rs +46, nifty_calls Rs +45, snake_abs_exit_conv Rs +31, benchmark_smallcap Rs +13, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -17, snake_abs_conv Rs -22, snake_anaconda Rs -188, snake_viper_wild Rs -206, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -337, gold Rs -803

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.