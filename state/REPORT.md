# Paper trading report

Updated 2026-11-19 12:36 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,779 | +11.89% | 0 | - | 236 |
| benchmark | 221,603 | +10.80% | 0 | - | 237 |
| intramonth | 213,428 | +6.71% | 0 | - | 235 |
| snake_abs_exit | 212,938 | +6.47% | 2 | 50% | 345 |
| intraweek | 211,598 | +5.80% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,069 | +5.54% | 2 | 50% | 345 |
| oracle | 210,986 | +5.49% | 0 | - | 233 |
| snake_abs | 208,780 | +4.39% | 1 | 100% | 255 |
| snake_abs_conv | 208,651 | +4.33% | 1 | 100% | 255 |
| snake_viper_wild | 207,806 | +3.90% | 16 | 50% | 2,827 |
| random_hold | 207,671 | +3.84% | 10 | 70% | 733 |
| snake_viper_tick | 204,254 | +2.13% | 15 | 47% | 2,625 |
| snake_anaconda | 203,061 | +1.53% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,627 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,003 | -12.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,190 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,308 | +0.59% |
| benchmark_smallcap | +1,300 | +0.65% |
| unified | +1,168 | +0.53% |
| intramonth | +1,154 | +0.54% |
| snake_viper_wild | +767 | +0.37% |
| snake_viper_tick | +751 | +0.37% |
| random_hold | +739 | +0.36% |
| oracle | +190 | +0.09% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -242 | -0.11% |
| snake_abs | -657 | -0.31% |
| snake_abs_conv | -674 | -0.32% |
| snake_abs_exit | -1,093 | -0.51% |
| snake_abs_exit_conv | -1,314 | -0.62% |
| snake_anaconda | -1,340 | -0.66% |
| gold | -2,318 | -1.31% |

Average per day so far: unified Rs +643, benchmark Rs +584, snake_abs_exit Rs +381, intramonth Rs +363, snake_abs_exit_conv Rs +326, intraweek Rs +313, oracle Rs +297, snake_viper_wild Rs +269, snake_abs_conv Rs +254, snake_abs Rs +251, random_hold Rs +207, snake_viper_tick Rs +164, snake_anaconda Rs +96, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -676

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.