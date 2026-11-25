# Paper trading report

Updated 2026-11-25 11:17 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,094 | +13.05% | 0 | - | 237 |
| unified | 224,876 | +12.44% | 0 | - | 236 |
| intramonth | 212,713 | +6.36% | 0 | - | 235 |
| oracle | 211,854 | +5.93% | 0 | - | 233 |
| random_hold | 210,211 | +5.11% | 12 | 75% | 1,009 |
| intraweek | 208,329 | +4.16% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,770 | +0.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,200 | +0.60% | 2 | 50% | 345 |
| snake_abs | 201,195 | +0.60% | 1 | 100% | 255 |
| snake_abs_conv | 201,000 | +0.50% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_viper_wild | 195,378 | -2.31% | 16 | 50% | 2,827 |
| snake_anaconda | 193,319 | -3.34% | 3 | 33% | 374 |
| snake_viper_tick | 192,057 | -3.97% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,744 | -17.63% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,289 (-5.36%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,621 | +2.09% |
| random_hold | +1,784 | +0.86% |
| unified | +591 | +0.26% |
| benchmark_smallcap | +527 | +0.27% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -39 | -0.02% |
| oracle | -488 | -0.23% |
| intraweek | -3,290 | -1.55% |
| snake_abs | -4,266 | -2.08% |
| snake_abs_conv | -4,303 | -2.10% |
| gold | -4,685 | -2.77% |
| snake_anaconda | -5,384 | -2.71% |
| snake_viper_tick | -5,635 | -2.85% |
| snake_abs_exit | -5,725 | -2.76% |
| snake_viper_wild | -5,746 | -2.86% |
| snake_abs_exit_conv | -5,846 | -2.82% |

Average per day so far: benchmark Rs +652, unified Rs +622, intramonth Rs +318, oracle Rs +296, random_hold Rs +255, intraweek Rs +208, snake_abs_exit Rs +48, nifty_calls Rs +46, snake_abs_exit_conv Rs +32, snake_abs Rs +31, snake_abs_conv Rs +27, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -144, snake_anaconda Rs -191, snake_viper_tick Rs -274, snake_nonews Rs -292, snake Rs -311, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.