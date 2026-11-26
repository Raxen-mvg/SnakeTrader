# Paper trading report

Updated 2026-11-26 12:53 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,926 | +12.96% | 0 | - | 237 |
| unified | 223,350 | +11.68% | 0 | - | 236 |
| oracle | 213,201 | +6.60% | 0 | - | 233 |
| intramonth | 210,466 | +5.23% | 0 | - | 235 |
| random_hold | 209,896 | +4.95% | 13 | 69% | 1,037 |
| intraweek | 208,327 | +4.16% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| snake_abs_exit | 200,309 | +0.15% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,856 | -0.07% | 2 | 50% | 345 |
| snake_abs | 198,247 | -0.88% | 1 | 100% | 255 |
| snake_abs_conv | 198,047 | -0.98% | 1 | 100% | 255 |
| snake_anaconda | 192,002 | -4.00% | 3 | 33% | 374 |
| snake_viper_wild | 191,994 | -4.00% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,734 | -5.63% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,520 | -16.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,794 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,923 | +1.17% |
| benchmark_smallcap | +1,760 | +0.89% |
| intraweek | +1,584 | +0.77% |
| benchmark | +903 | +0.40% |
| random_hold | +403 | +0.19% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -595 | -0.28% |
| unified | -750 | -0.34% |
| intramonth | -1,227 | -0.58% |
| snake_abs | -1,903 | -0.95% |
| snake_abs_conv | -1,926 | -0.96% |
| snake_abs_exit | -1,947 | -0.96% |
| snake_abs_exit_conv | -2,120 | -1.05% |
| snake_anaconda | -2,551 | -1.31% |
| snake_viper_tick | -5,443 | -2.80% |
| snake_viper_wild | -5,549 | -2.81% |

Average per day so far: benchmark Rs +632, unified Rs +570, oracle Rs +322, intramonth Rs +255, random_hold Rs +241, intraweek Rs +203, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +8, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -4, snake_abs Rs -45, snake_abs_conv Rs -51, snake_anaconda Rs -222, snake_viper_wild Rs -243, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -376, gold Rs -817

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.