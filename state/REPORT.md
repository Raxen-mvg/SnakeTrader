# Paper trading report

Updated 2026-11-26 10:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,400 | +13.20% | 0 | - | 237 |
| unified | 223,642 | +11.82% | 0 | - | 236 |
| oracle | 213,101 | +6.55% | 0 | - | 233 |
| intramonth | 210,972 | +5.49% | 0 | - | 235 |
| random_hold | 209,674 | +4.84% | 13 | 69% | 1,037 |
| intraweek | 207,510 | +3.75% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,054 | +1.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,532 | +0.77% | 2 | 50% | 345 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,807 | -0.10% | 1 | 100% | 255 |
| snake_abs_conv | 199,620 | -0.19% | 1 | 100% | 255 |
| snake_anaconda | 193,438 | -3.28% | 3 | 33% | 374 |
| snake_viper_wild | 193,425 | -3.29% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,135 | -4.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,950 | -16.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,911 (-5.54%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,354 | +2.04% |
| benchmark_smallcap | +1,760 | +0.89% |
| benchmark | +1,377 | +0.61% |
| intraweek | +767 | +0.37% |
| random_hold | +181 | +0.09% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -201 | -0.10% |
| snake_abs | -343 | -0.17% |
| snake_abs_conv | -352 | -0.18% |
| snake_abs_exit_conv | -443 | -0.22% |
| unified | -458 | -0.20% |
| oracle | -694 | -0.33% |
| intramonth | -721 | -0.34% |
| snake_anaconda | -1,115 | -0.57% |
| snake_viper_tick | -4,042 | -2.08% |
| snake_viper_wild | -4,119 | -2.08% |

Average per day so far: benchmark Rs +644, unified Rs +577, oracle Rs +320, intramonth Rs +268, random_hold Rs +236, intraweek Rs +183, snake_abs_exit Rs +54, nifty_calls Rs +45, snake_abs_exit_conv Rs +40, benchmark_smallcap Rs +15, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -5, snake_abs_conv Rs -10, snake_anaconda Rs -182, snake_viper_wild Rs -199, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -329, gold Rs -782

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.