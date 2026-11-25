# Paper trading report

Updated 2026-11-25 12:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,773 | +12.89% | 0 | - | 237 |
| unified | 225,408 | +12.70% | 0 | - | 236 |
| intramonth | 213,060 | +6.53% | 0 | - | 235 |
| oracle | 212,638 | +6.32% | 0 | - | 233 |
| random_hold | 210,083 | +5.04% | 12 | 75% | 1,009 |
| intraweek | 208,086 | +4.04% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,393 | +1.20% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,834 | +0.92% | 2 | 50% | 345 |
| snake_abs | 200,819 | +0.41% | 1 | 100% | 255 |
| snake_abs_conv | 200,636 | +0.32% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,596 | -0.20% | 0 | - | 237 |
| snake_viper_wild | 196,646 | -1.68% | 16 | 50% | 2,827 |
| snake_anaconda | 193,979 | -3.01% | 3 | 33% | 374 |
| snake_viper_tick | 193,298 | -3.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,481 | -17.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,537 (-5.23%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,299 | +1.94% |
| random_hold | +1,656 | +0.80% |
| unified | +1,123 | +0.50% |
| benchmark_smallcap | +617 | +0.31% |
| intramonth | +309 | +0.14% |
| oracle | +295 | +0.14% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,533 | -1.67% |
| snake_viper_tick | -4,395 | -2.22% |
| snake_viper_wild | -4,479 | -2.23% |
| snake_abs | -4,642 | -2.26% |
| snake_abs_conv | -4,667 | -2.27% |
| snake_anaconda | -4,724 | -2.38% |
| gold | -4,948 | -2.92% |
| snake_abs_exit | -5,102 | -2.46% |
| snake_abs_exit_conv | -5,212 | -2.52% |

Average per day so far: benchmark Rs +644, unified Rs +635, intramonth Rs +327, oracle Rs +316, random_hold Rs +252, intraweek Rs +202, snake_abs_exit Rs +65, snake_abs_exit_conv Rs +50, nifty_calls Rs +46, snake_abs Rs +22, snake_abs_conv Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_viper_wild Rs -105, snake_anaconda Rs -172, snake_viper_tick Rs -231, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.