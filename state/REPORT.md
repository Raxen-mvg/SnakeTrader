# Paper trading report

Updated 2026-11-25 14:23 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,579 | +12.29% | 0 | - | 237 |
| unified | 224,560 | +12.28% | 0 | - | 236 |
| oracle | 212,636 | +6.32% | 0 | - | 233 |
| intramonth | 212,129 | +6.06% | 0 | - | 235 |
| random_hold | 209,499 | +4.75% | 12 | 75% | 1,009 |
| intraweek | 207,062 | +3.53% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,398 | +0.70% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,148 | +0.57% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,832 | -0.08% | 1 | 100% | 255 |
| snake_abs_conv | 199,629 | -0.18% | 1 | 100% | 255 |
| benchmark_smallcap | 198,654 | -0.67% | 0 | - | 237 |
| snake_viper_wild | 197,414 | -1.29% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,050 | -2.98% | 15 | 47% | 2,625 |
| snake_anaconda | 193,216 | -3.39% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,073 | -17.46% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,903 (-5.55%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,106 | +1.40% |
| random_hold | +1,073 | +0.52% |
| oracle | +294 | +0.14% |
| unified | +275 | +0.12% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -325 | -0.16% |
| intramonth | -623 | -0.29% |
| snake_viper_tick | -3,643 | -1.84% |
| snake_viper_wild | -3,711 | -1.84% |
| gold | -4,357 | -2.57% |
| intraweek | -4,557 | -2.15% |
| snake_anaconda | -5,487 | -2.76% |
| snake_abs | -5,629 | -2.74% |
| snake_abs_conv | -5,673 | -2.76% |
| snake_abs_exit_conv | -5,898 | -2.85% |
| snake_abs_exit | -6,097 | -2.94% |

Average per day so far: benchmark Rs +614, unified Rs +614, oracle Rs +316, intramonth Rs +303, random_hold Rs +237, intraweek Rs +177, nifty_calls Rs +46, snake_abs_exit Rs +38, snake_abs_exit_conv Rs +31, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -4, snake_abs_conv Rs -10, benchmark_smallcap Rs -37, snake_viper_wild Rs -81, snake_anaconda Rs -194, snake_viper_tick Rs -205, snake_nonews Rs -292, snake Rs -311, gold Rs -873

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.