# Paper trading report

Updated 2026-11-25 12:19 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,841 | +12.92% | 0 | - | 237 |
| unified | 225,393 | +12.70% | 0 | - | 236 |
| intramonth | 212,996 | +6.50% | 0 | - | 235 |
| oracle | 212,779 | +6.39% | 0 | - | 233 |
| random_hold | 210,137 | +5.07% | 12 | 75% | 1,009 |
| intraweek | 208,406 | +4.20% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,368 | +1.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,944 | +0.97% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,789 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,607 | +0.30% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,506 | -0.25% | 0 | - | 237 |
| snake_viper_wild | 196,646 | -1.68% | 16 | 50% | 2,827 |
| snake_anaconda | 194,032 | -2.98% | 3 | 33% | 374 |
| snake_viper_tick | 193,298 | -3.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,580 | -17.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,585 (-5.21%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,368 | +1.97% |
| random_hold | +1,710 | +0.82% |
| unified | +1,108 | +0.49% |
| benchmark_smallcap | +527 | +0.27% |
| oracle | +437 | +0.21% |
| intramonth | +245 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,213 | -1.52% |
| snake_viper_tick | -4,395 | -2.22% |
| snake_viper_wild | -4,479 | -2.23% |
| snake_abs | -4,671 | -2.27% |
| snake_anaconda | -4,672 | -2.35% |
| snake_abs_conv | -4,696 | -2.29% |
| gold | -4,850 | -2.86% |
| snake_abs_exit_conv | -5,102 | -2.46% |
| snake_abs_exit | -5,127 | -2.47% |

Average per day so far: benchmark Rs +646, unified Rs +635, intramonth Rs +325, oracle Rs +319, random_hold Rs +253, intraweek Rs +210, snake_abs_exit Rs +64, snake_abs_exit_conv Rs +53, nifty_calls Rs +46, snake_abs Rs +21, snake_abs_conv Rs +16, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -105, snake_anaconda Rs -171, snake_viper_tick Rs -231, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.