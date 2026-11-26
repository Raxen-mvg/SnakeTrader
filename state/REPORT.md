# Paper trading report

Updated 2026-11-26 11:02 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,308 | +13.15% | 0 | - | 237 |
| unified | 223,486 | +11.74% | 0 | - | 236 |
| oracle | 212,840 | +6.42% | 0 | - | 233 |
| intramonth | 210,774 | +5.39% | 0 | - | 235 |
| random_hold | 210,038 | +5.02% | 13 | 69% | 1,037 |
| intraweek | 207,907 | +3.95% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,822 | +0.91% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,208 | +0.60% | 2 | 50% | 345 |
| benchmark_smallcap | 200,661 | +0.33% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,507 | -0.25% | 1 | 100% | 255 |
| snake_abs_conv | 199,316 | -0.34% | 1 | 100% | 255 |
| snake_viper_wild | 193,185 | -3.41% | 16 | 50% | 2,827 |
| snake_anaconda | 193,129 | -3.44% | 3 | 33% | 374 |
| snake_viper_tick | 189,900 | -5.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,901 | -16.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,888 (-5.56%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,304 | +2.01% |
| benchmark_smallcap | +1,850 | +0.93% |
| benchmark | +1,285 | +0.57% |
| intraweek | +1,163 | +0.56% |
| random_hold | +545 | +0.26% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -433 | -0.21% |
| unified | -614 | -0.27% |
| snake_abs | -643 | -0.32% |
| snake_abs_conv | -656 | -0.33% |
| snake_abs_exit_conv | -768 | -0.38% |
| intramonth | -919 | -0.43% |
| oracle | -956 | -0.45% |
| snake_anaconda | -1,424 | -0.73% |
| snake_viper_tick | -4,277 | -2.20% |
| snake_viper_wild | -4,359 | -2.21% |

Average per day so far: benchmark Rs +642, unified Rs +573, oracle Rs +313, intramonth Rs +263, random_hold Rs +245, intraweek Rs +193, snake_abs_exit Rs +48, nifty_calls Rs +45, snake_abs_exit_conv Rs +32, benchmark_smallcap Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -13, snake_abs_conv Rs -18, snake_anaconda Rs -191, snake_viper_wild Rs -207, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -337, gold Rs -783

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.