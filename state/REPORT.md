# Paper trading report

Updated 2026-11-25 12:16 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,887 | +12.94% | 0 | - | 237 |
| unified | 225,380 | +12.69% | 0 | - | 236 |
| intramonth | 213,073 | +6.54% | 0 | - | 235 |
| oracle | 212,622 | +6.31% | 0 | - | 233 |
| random_hold | 210,035 | +5.02% | 12 | 75% | 1,009 |
| intraweek | 207,945 | +3.97% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,316 | +1.16% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,837 | +0.92% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,800 | +0.40% | 1 | 100% | 255 |
| snake_abs_conv | 200,617 | +0.31% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_viper_wild | 196,646 | -1.68% | 16 | 50% | 2,827 |
| snake_anaconda | 193,970 | -3.02% | 3 | 33% | 374 |
| snake_viper_tick | 193,298 | -3.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,514 | -17.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,499 (-5.25%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,414 | +1.99% |
| random_hold | +1,608 | +0.77% |
| unified | +1,095 | +0.49% |
| benchmark_smallcap | +504 | +0.25% |
| intramonth | +321 | +0.15% |
| oracle | +280 | +0.13% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,674 | -1.74% |
| snake_viper_tick | -4,395 | -2.22% |
| snake_viper_wild | -4,479 | -2.23% |
| snake_abs | -4,661 | -2.27% |
| snake_abs_conv | -4,686 | -2.28% |
| snake_anaconda | -4,733 | -2.38% |
| gold | -4,916 | -2.90% |
| snake_abs_exit | -5,179 | -2.50% |
| snake_abs_exit_conv | -5,209 | -2.52% |

Average per day so far: benchmark Rs +647, unified Rs +635, intramonth Rs +327, oracle Rs +316, random_hold Rs +251, intraweek Rs +199, snake_abs_exit Rs +63, snake_abs_exit_conv Rs +50, nifty_calls Rs +46, snake_abs Rs +21, snake_abs_conv Rs +17, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -105, snake_anaconda Rs -172, snake_viper_tick Rs -231, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.