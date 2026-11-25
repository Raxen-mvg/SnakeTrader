# Paper trading report

Updated 2026-11-25 13:09 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,454 | +12.23% | 0 | - | 236 |
| benchmark | 223,822 | +11.91% | 0 | - | 237 |
| oracle | 212,445 | +6.22% | 0 | - | 233 |
| intramonth | 212,342 | +6.17% | 0 | - | 235 |
| random_hold | 209,738 | +4.87% | 12 | 75% | 1,009 |
| intraweek | 208,275 | +4.14% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,345 | +0.67% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,984 | +0.49% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,684 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,488 | -0.26% | 1 | 100% | 255 |
| benchmark_smallcap | 198,979 | -0.51% | 0 | - | 237 |
| snake_viper_wild | 196,814 | -1.59% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,462 | -3.27% | 15 | 47% | 2,625 |
| snake_anaconda | 193,091 | -3.46% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,712 | -17.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,046 (-5.48%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,349 | +1.06% |
| random_hold | +1,311 | +0.63% |
| unified | +169 | +0.07% |
| oracle | +102 | +0.05% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| benchmark_smallcap | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -410 | -0.19% |
| intraweek | -3,344 | -1.58% |
| snake_viper_tick | -4,230 | -2.14% |
| snake_viper_wild | -4,311 | -2.14% |
| gold | -4,718 | -2.79% |
| snake_anaconda | -5,613 | -2.83% |
| snake_abs | -5,777 | -2.81% |
| snake_abs_conv | -5,815 | -2.83% |
| snake_abs_exit_conv | -6,061 | -2.93% |
| snake_abs_exit | -6,150 | -2.96% |

Average per day so far: unified Rs +611, benchmark Rs +596, oracle Rs +311, intramonth Rs +309, random_hold Rs +243, intraweek Rs +207, nifty_calls Rs +46, snake_abs_exit Rs +36, snake_abs_exit_conv Rs +27, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -8, snake_abs_conv Rs -14, benchmark_smallcap Rs -28, snake_viper_wild Rs -100, snake_anaconda Rs -197, snake_viper_tick Rs -225, snake_nonews Rs -292, snake Rs -311, gold Rs -882

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.