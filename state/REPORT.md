# Paper trading report

Updated 2026-11-26 10:58 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,369 | +13.19% | 0 | - | 237 |
| unified | 223,559 | +11.78% | 0 | - | 236 |
| oracle | 212,947 | +6.47% | 0 | - | 233 |
| intramonth | 210,869 | +5.43% | 0 | - | 235 |
| random_hold | 209,614 | +4.81% | 13 | 69% | 1,037 |
| intraweek | 207,518 | +3.76% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,945 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,352 | +0.68% | 2 | 50% | 345 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,616 | -0.19% | 1 | 100% | 255 |
| snake_abs_conv | 199,428 | -0.29% | 1 | 100% | 255 |
| snake_anaconda | 193,243 | -3.38% | 3 | 33% | 374 |
| snake_viper_wild | 193,190 | -3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,905 | -5.05% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,000 | -16.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,832 (-5.58%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,403 | +2.07% |
| benchmark_smallcap | +1,760 | +0.89% |
| benchmark | +1,346 | +0.60% |
| intraweek | +775 | +0.38% |
| random_hold | +122 | +0.06% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -310 | -0.15% |
| snake_abs | -534 | -0.27% |
| unified | -541 | -0.24% |
| snake_abs_conv | -544 | -0.27% |
| snake_abs_exit_conv | -624 | -0.31% |
| intramonth | -825 | -0.39% |
| oracle | -849 | -0.40% |
| snake_anaconda | -1,310 | -0.67% |
| snake_viper_tick | -4,272 | -2.20% |
| snake_viper_wild | -4,354 | -2.20% |

Average per day so far: benchmark Rs +643, unified Rs +575, oracle Rs +316, intramonth Rs +265, random_hold Rs +234, intraweek Rs +183, snake_abs_exit Rs +51, nifty_calls Rs +45, snake_abs_exit_conv Rs +36, benchmark_smallcap Rs +15, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, snake_anaconda Rs -188, snake_viper_wild Rs -206, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -337, gold Rs -780

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.