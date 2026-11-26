# Paper trading report

Updated 2026-11-26 11:12 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,140 | +13.07% | 0 | - | 237 |
| unified | 223,216 | +11.61% | 0 | - | 236 |
| oracle | 212,822 | +6.41% | 0 | - | 233 |
| intramonth | 210,555 | +5.28% | 0 | - | 235 |
| random_hold | 209,948 | +4.97% | 13 | 69% | 1,037 |
| intraweek | 207,973 | +3.99% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,826 | +0.91% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,301 | +0.65% | 2 | 50% | 345 |
| benchmark_smallcap | 200,482 | +0.24% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,479 | -0.26% | 1 | 100% | 255 |
| snake_abs_conv | 199,290 | -0.35% | 1 | 100% | 255 |
| snake_viper_wild | 193,358 | -3.32% | 16 | 50% | 2,827 |
| snake_anaconda | 193,263 | -3.37% | 3 | 33% | 374 |
| snake_viper_tick | 190,069 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,868 | -16.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,792 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,272 | +1.99% |
| benchmark_smallcap | +1,670 | +0.84% |
| intraweek | +1,229 | +0.59% |
| benchmark | +1,117 | +0.50% |
| random_hold | +455 | +0.22% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -430 | -0.21% |
| snake_abs | -671 | -0.34% |
| snake_abs_exit_conv | -675 | -0.33% |
| snake_abs_conv | -682 | -0.34% |
| unified | -883 | -0.39% |
| oracle | -974 | -0.46% |
| intramonth | -1,139 | -0.54% |
| snake_anaconda | -1,290 | -0.66% |
| snake_viper_tick | -4,108 | -2.12% |
| snake_viper_wild | -4,186 | -2.12% |

Average per day so far: benchmark Rs +638, unified Rs +566, oracle Rs +313, intramonth Rs +257, random_hold Rs +243, intraweek Rs +194, snake_abs_exit Rs +48, nifty_calls Rs +45, snake_abs_exit_conv Rs +34, benchmark_smallcap Rs +13, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -13, snake_abs_conv Rs -19, snake_anaconda Rs -187, snake_viper_wild Rs -201, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -331, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.