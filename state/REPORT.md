# Paper trading report

Updated 2026-11-26 09:24 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,679 | +12.34% | 0 | - | 237 |
| unified | 224,081 | +12.04% | 0 | - | 236 |
| oracle | 213,677 | +6.84% | 0 | - | 233 |
| intramonth | 211,748 | +5.87% | 0 | - | 235 |
| random_hold | 210,099 | +5.05% | 12 | 75% | 1,009 |
| intraweek | 207,499 | +3.75% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,410 | +1.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,733 | +1.37% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,447 | +0.22% | 1 | 100% | 255 |
| snake_abs_conv | 200,281 | +0.14% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,899 | -0.05% | 0 | - | 237 |
| snake_viper_wild | 196,545 | -1.73% | 16 | 50% | 2,827 |
| snake_anaconda | 195,213 | -2.39% | 3 | 33% | 374 |
| snake_viper_tick | 193,199 | -3.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,030 | -16.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,298 (-5.35%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,433 | +1.48% |
| snake_abs_exit | +1,154 | +0.57% |
| benchmark_smallcap | +1,087 | +0.55% |
| snake_abs_exit_conv | +757 | +0.38% |
| intraweek | +756 | +0.37% |
| snake_anaconda | +660 | +0.34% |
| random_hold | +607 | +0.29% |
| snake_abs_conv | +309 | +0.15% |
| snake_abs | +297 | +0.15% |
| intramonth | +55 | +0.03% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| unified | -18 | -0.01% |
| oracle | -118 | -0.06% |
| benchmark | -344 | -0.15% |
| snake_viper_tick | -978 | -0.50% |
| snake_viper_wild | -998 | -0.51% |

Average per day so far: benchmark Rs +602, unified Rs +587, oracle Rs +334, intramonth Rs +287, random_hold Rs +246, intraweek Rs +183, snake_abs_exit Rs +90, snake_abs_exit_conv Rs +72, nifty_calls Rs +45, snake_abs Rs +11, snake_abs_conv Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -3, snake_viper_wild Rs -105, snake_anaconda Rs -133, snake_viper_tick Rs -227, snake_nonews Rs -284, snake Rs -304, gold Rs -804

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.