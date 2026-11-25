# Paper trading report

Updated 2026-11-25 14:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,549 | +12.27% | 0 | - | 237 |
| unified | 224,409 | +12.20% | 0 | - | 236 |
| oracle | 213,064 | +6.53% | 0 | - | 233 |
| intramonth | 211,844 | +5.92% | 0 | - | 235 |
| random_hold | 209,939 | +4.97% | 12 | 75% | 1,009 |
| intraweek | 207,062 | +3.53% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,787 | +0.89% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,450 | +0.72% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,622 | -0.19% | 1 | 100% | 255 |
| snake_abs_conv | 199,430 | -0.28% | 1 | 100% | 255 |
| benchmark_smallcap | 198,822 | -0.59% | 0 | - | 237 |
| snake_viper_wild | 197,682 | -1.16% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,313 | -2.84% | 15 | 47% | 2,625 |
| snake_anaconda | 193,699 | -3.15% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,303 | -17.35% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,008 (-5.50%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,075 | +1.39% |
| random_hold | +1,513 | +0.73% |
| oracle | +722 | +0.34% |
| unified | +123 | +0.06% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -157 | -0.08% |
| intramonth | -908 | -0.43% |
| snake_viper_tick | -3,379 | -1.71% |
| snake_viper_wild | -3,442 | -1.71% |
| gold | -4,126 | -2.44% |
| intraweek | -4,557 | -2.15% |
| snake_anaconda | -5,005 | -2.52% |
| snake_abs_exit_conv | -5,595 | -2.70% |
| snake_abs_exit | -5,707 | -2.75% |
| snake_abs | -5,839 | -2.84% |
| snake_abs_conv | -5,873 | -2.86% |

Average per day so far: benchmark Rs +614, unified Rs +610, oracle Rs +327, intramonth Rs +296, random_hold Rs +248, intraweek Rs +177, snake_abs_exit Rs +48, nifty_calls Rs +46, snake_abs_exit_conv Rs +39, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -10, snake_abs_conv Rs -15, benchmark_smallcap Rs -33, snake_viper_wild Rs -72, snake_anaconda Rs -180, snake_viper_tick Rs -196, snake_nonews Rs -292, snake Rs -311, gold Rs -867

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.