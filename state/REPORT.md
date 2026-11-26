# Paper trading report

Updated 2026-11-26 11:09 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,163 | +13.08% | 0 | - | 237 |
| unified | 223,436 | +11.72% | 0 | - | 236 |
| oracle | 212,955 | +6.48% | 0 | - | 233 |
| intramonth | 210,766 | +5.38% | 0 | - | 235 |
| random_hold | 210,012 | +5.01% | 13 | 69% | 1,037 |
| intraweek | 208,100 | +4.05% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,993 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,421 | +0.71% | 2 | 50% | 345 |
| benchmark_smallcap | 200,784 | +0.39% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,583 | -0.21% | 1 | 100% | 255 |
| snake_abs_conv | 199,395 | -0.30% | 1 | 100% | 255 |
| snake_viper_wild | 193,391 | -3.30% | 16 | 50% | 2,827 |
| snake_anaconda | 193,366 | -3.32% | 3 | 33% | 374 |
| snake_viper_tick | 190,102 | -4.95% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,000 | -16.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,936 (-5.53%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,403 | +2.07% |
| benchmark_smallcap | +1,973 | +0.99% |
| intraweek | +1,357 | +0.66% |
| benchmark | +1,140 | +0.51% |
| random_hold | +519 | +0.25% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -262 | -0.13% |
| snake_abs_exit_conv | -555 | -0.28% |
| snake_abs | -567 | -0.28% |
| snake_abs_conv | -577 | -0.29% |
| unified | -664 | -0.30% |
| oracle | -840 | -0.39% |
| intramonth | -927 | -0.44% |
| snake_anaconda | -1,187 | -0.61% |
| snake_viper_tick | -4,075 | -2.10% |
| snake_viper_wild | -4,152 | -2.10% |

Average per day so far: benchmark Rs +638, unified Rs +572, oracle Rs +316, intramonth Rs +263, random_hold Rs +244, intraweek Rs +198, snake_abs_exit Rs +52, nifty_calls Rs +45, snake_abs_exit_conv Rs +37, benchmark_smallcap Rs +21, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -11, snake_abs_conv Rs -16, snake_anaconda Rs -184, snake_viper_wild Rs -200, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -330, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.