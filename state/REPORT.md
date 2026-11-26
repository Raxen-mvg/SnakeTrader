# Paper trading report

Updated 2026-11-26 14:26 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,535 | +12.77% | 0 | - | 237 |
| unified | 223,269 | +11.63% | 0 | - | 236 |
| oracle | 213,145 | +6.57% | 0 | - | 233 |
| intramonth | 210,581 | +5.29% | 0 | - | 235 |
| random_hold | 209,310 | +4.66% | 13 | 69% | 1,037 |
| intraweek | 207,932 | +3.97% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,994 | -0.00% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,387 | -0.31% | 2 | 50% | 345 |
| snake_abs | 197,677 | -1.16% | 1 | 100% | 255 |
| snake_abs_conv | 197,471 | -1.26% | 1 | 100% | 255 |
| snake_viper_wild | 192,374 | -3.81% | 16 | 50% | 2,827 |
| snake_anaconda | 191,431 | -4.28% | 3 | 33% | 374 |
| snake_viper_tick | 189,106 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,487 | -16.76% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,612 (-5.69%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,891 | +1.15% |
| benchmark_smallcap | +1,749 | +0.88% |
| intraweek | +1,189 | +0.57% |
| benchmark | +513 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -182 | -0.09% |
| oracle | -650 | -0.30% |
| unified | -831 | -0.37% |
| intramonth | -1,112 | -0.53% |
| snake_abs_exit | -2,262 | -1.12% |
| snake_abs | -2,473 | -1.24% |
| snake_abs_conv | -2,502 | -1.25% |
| snake_abs_exit_conv | -2,589 | -1.28% |
| snake_anaconda | -3,122 | -1.60% |
| snake_viper_tick | -5,071 | -2.61% |
| snake_viper_wild | -5,170 | -2.62% |

Average per day so far: benchmark Rs +623, unified Rs +568, oracle Rs +321, intramonth Rs +258, random_hold Rs +227, intraweek Rs +193, nifty_calls Rs +45, benchmark_smallcap Rs +15, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -0, snake_abs_exit_conv Rs -16, snake_abs Rs -60, snake_abs_conv Rs -67, snake_viper_wild Rs -231, snake_anaconda Rs -238, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -363, gold Rs -817

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.