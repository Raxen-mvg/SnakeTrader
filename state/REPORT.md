# Paper trading report

Updated 2026-11-25 09:52 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,637 | +12.82% | 0 | - | 236 |
| benchmark | 224,702 | +12.35% | 0 | - | 237 |
| intramonth | 213,154 | +6.58% | 0 | - | 235 |
| oracle | 213,113 | +6.56% | 0 | - | 233 |
| intraweek | 210,879 | +5.44% | 40 | 55% | 4,400 |
| random_hold | 209,819 | +4.91% | 12 | 75% | 1,009 |
| snake_abs_exit | 202,693 | +1.35% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,059 | +1.03% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,418 | +0.71% | 1 | 100% | 255 |
| snake_abs_conv | 201,227 | +0.61% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_viper_wild | 199,051 | -0.47% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,662 | -2.17% | 15 | 47% | 2,625 |
| snake_anaconda | 194,314 | -2.84% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,862 | -17.07% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,024 (-4.99%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,228 | +1.46% |
| random_hold | +1,393 | +0.67% |
| unified | +1,352 | +0.60% |
| benchmark_smallcap | +796 | +0.40% |
| oracle | +771 | +0.36% |
| intramonth | +402 | +0.19% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -740 | -0.35% |
| snake_viper_tick | -2,030 | -1.03% |
| snake_viper_wild | -2,074 | -1.03% |
| gold | -3,567 | -2.11% |
| snake_abs | -4,043 | -1.97% |
| snake_abs_conv | -4,075 | -1.99% |
| snake_anaconda | -4,390 | -2.21% |
| snake_abs_exit | -4,802 | -2.31% |
| snake_abs_exit_conv | -4,987 | -2.41% |

Average per day so far: unified Rs +641, benchmark Rs +618, intramonth Rs +329, oracle Rs +328, intraweek Rs +272, random_hold Rs +245, snake_abs_exit Rs +73, snake_abs_exit_conv Rs +56, nifty_calls Rs +46, snake_abs Rs +37, snake_abs_conv Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_viper_wild Rs -30, snake_viper_tick Rs -150, snake_anaconda Rs -162, snake_nonews Rs -292, snake Rs -311, gold Rs -853

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.