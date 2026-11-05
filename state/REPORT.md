# Paper trading report

Updated 2026-11-05 14:19 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 216,062 | +8.03% | 0 | - | 236 |
| snake_abs_exit_conv | 214,492 | +7.25% | 1 | 100% | 255 |
| snake_abs_exit | 214,247 | +7.12% | 1 | 100% | 260 |
| benchmark | 213,831 | +6.92% | 0 | - | 237 |
| snake_abs | 211,381 | +5.69% | 1 | 100% | 255 |
| snake_abs_conv | 211,241 | +5.62% | 1 | 100% | 255 |
| intraweek | 210,730 | +5.37% | 25 | 48% | 2,757 |
| intramonth | 207,653 | +3.83% | 0 | - | 235 |
| snake_viper_wild | 205,472 | +2.74% | 3 | 33% | 702 |
| random_hold | 204,970 | +2.48% | 8 | 62% | 649 |
| oracle | 203,860 | +1.93% | 0 | - | 233 |
| snake_anaconda | 202,606 | +1.30% | 3 | 33% | 374 |
| snake_viper_tick | 201,939 | +0.97% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,035 | -0.48% | 0 | - | 237 |
| gold | 194,287 | -2.86% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,648 (-5.18%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,072 | +2.43% |
| gold | +2,893 | +1.51% |
| benchmark_smallcap | +2,365 | +1.20% |
| oracle | +2,067 | +1.02% |
| random_hold | +1,661 | +0.82% |
| unified | +1,623 | +0.76% |
| intraweek | +1,032 | +0.49% |
| intramonth | +637 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -518 | -0.24% |
| snake_abs | -522 | -0.25% |
| snake_abs_exit_conv | -523 | -0.24% |
| snake_abs_exit | -653 | -0.30% |
| snake_anaconda | -1,215 | -0.60% |
| snake_viper_tick | -3,461 | -1.69% |
| snake_viper_wild | -3,558 | -1.70% |

Average per day so far: snake_abs_exit_conv Rs +580, unified Rs +574, snake_abs_exit Rs +570, benchmark Rs +494, snake_abs_conv Rs +450, snake_abs Rs +438, intraweek Rs +383, snake_viper_wild Rs +274, intramonth Rs +273, random_hold Rs +178, oracle Rs +138, snake_viper_tick Rs +114, snake_anaconda Rs +113, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -40, gold Rs -204, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.