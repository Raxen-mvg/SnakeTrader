# Paper trading report

Updated 2026-11-25 14:26 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,656 | +12.33% | 0 | - | 237 |
| unified | 224,481 | +12.24% | 0 | - | 236 |
| oracle | 212,629 | +6.31% | 0 | - | 233 |
| intramonth | 211,993 | +6.00% | 0 | - | 235 |
| random_hold | 209,559 | +4.78% | 12 | 75% | 1,009 |
| intraweek | 207,118 | +3.56% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,203 | +0.60% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,897 | +0.45% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,628 | -0.19% | 1 | 100% | 255 |
| snake_abs_conv | 199,425 | -0.29% | 1 | 100% | 255 |
| benchmark_smallcap | 198,677 | -0.66% | 0 | - | 237 |
| snake_viper_wild | 197,169 | -1.42% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,810 | -3.10% | 15 | 47% | 2,625 |
| snake_anaconda | 193,008 | -3.50% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,123 | -17.44% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,853 (-5.57%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,182 | +1.44% |
| random_hold | +1,133 | +0.54% |
| oracle | +287 | +0.14% |
| unified | +196 | +0.09% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -303 | -0.15% |
| intramonth | -759 | -0.36% |
| snake_viper_tick | -3,882 | -1.96% |
| snake_viper_wild | -3,955 | -1.97% |
| gold | -4,307 | -2.54% |
| intraweek | -4,501 | -2.13% |
| snake_anaconda | -5,695 | -2.87% |
| snake_abs | -5,833 | -2.84% |
| snake_abs_conv | -5,878 | -2.86% |
| snake_abs_exit_conv | -6,149 | -2.97% |
| snake_abs_exit | -6,292 | -3.03% |

Average per day so far: benchmark Rs +616, unified Rs +612, oracle Rs +316, intramonth Rs +300, random_hold Rs +239, intraweek Rs +178, nifty_calls Rs +46, snake_abs_exit Rs +33, snake_abs_exit_conv Rs +24, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -10, snake_abs_conv Rs -16, benchmark_smallcap Rs -37, snake_viper_wild Rs -88, snake_anaconda Rs -200, snake_viper_tick Rs -213, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.