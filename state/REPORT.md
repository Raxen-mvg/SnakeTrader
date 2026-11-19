# Paper trading report

Updated 2026-11-19 11:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,727 | +11.86% | 0 | - | 236 |
| benchmark | 220,961 | +10.48% | 0 | - | 237 |
| snake_abs_exit | 213,657 | +6.83% | 2 | 50% | 345 |
| intramonth | 213,314 | +6.66% | 0 | - | 235 |
| intraweek | 211,878 | +5.94% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,718 | +5.86% | 2 | 50% | 345 |
| oracle | 211,038 | +5.52% | 0 | - | 233 |
| snake_abs | 209,229 | +4.61% | 1 | 100% | 255 |
| snake_abs_conv | 209,107 | +4.55% | 1 | 100% | 255 |
| random_hold | 207,754 | +3.88% | 10 | 70% | 733 |
| snake_viper_wild | 207,417 | +3.71% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,874 | +1.94% | 15 | 47% | 2,625 |
| snake_anaconda | 203,405 | +1.70% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,470 | +0.23% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,398 | -12.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,226 (-4.39%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,143 | +0.57% |
| unified | +1,116 | +0.50% |
| intramonth | +1,040 | +0.49% |
| random_hold | +822 | +0.40% |
| benchmark | +666 | +0.30% |
| snake_viper_wild | +378 | +0.18% |
| snake_viper_tick | +370 | +0.18% |
| oracle | +242 | +0.12% |
| intraweek | +39 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -208 | -0.10% |
| snake_abs_conv | -218 | -0.10% |
| snake_abs_exit | -375 | -0.17% |
| snake_abs_exit_conv | -666 | -0.31% |
| snake_anaconda | -996 | -0.49% |
| gold | -1,923 | -1.08% |

Average per day so far: unified Rs +641, benchmark Rs +567, snake_abs_exit Rs +402, intramonth Rs +360, snake_abs_exit_conv Rs +345, intraweek Rs +321, oracle Rs +298, snake_abs_conv Rs +268, snake_abs Rs +264, snake_viper_wild Rs +256, random_hold Rs +210, snake_viper_tick Rs +149, snake_anaconda Rs +106, nifty_calls Rs +50, benchmark_smallcap Rs +14, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -665

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.