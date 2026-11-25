# Paper trading report

Updated 2026-11-25 12:07 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,826 | +12.91% | 0 | - | 237 |
| unified | 225,359 | +12.68% | 0 | - | 236 |
| intramonth | 213,019 | +6.51% | 0 | - | 235 |
| oracle | 212,598 | +6.30% | 0 | - | 233 |
| random_hold | 210,047 | +5.02% | 12 | 75% | 1,009 |
| intraweek | 207,887 | +3.94% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,348 | +1.17% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,742 | +0.87% | 2 | 50% | 345 |
| snake_abs | 201,114 | +0.56% | 1 | 100% | 255 |
| snake_abs_conv | 200,926 | +0.46% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| snake_viper_wild | 196,718 | -1.64% | 16 | 50% | 2,827 |
| snake_anaconda | 193,911 | -3.04% | 3 | 33% | 374 |
| snake_viper_tick | 193,368 | -3.32% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,547 | -17.73% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,511 (-5.24%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,353 | +1.97% |
| random_hold | +1,620 | +0.78% |
| unified | +1,074 | +0.48% |
| benchmark_smallcap | +673 | +0.34% |
| intramonth | +268 | +0.13% |
| oracle | +256 | +0.12% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -3,732 | -1.76% |
| snake_viper_tick | -4,324 | -2.19% |
| snake_abs | -4,346 | -2.12% |
| snake_abs_conv | -4,377 | -2.13% |
| snake_viper_wild | -4,407 | -2.19% |
| snake_anaconda | -4,792 | -2.41% |
| gold | -4,883 | -2.88% |
| snake_abs_exit | -5,147 | -2.48% |
| snake_abs_exit_conv | -5,304 | -2.56% |

Average per day so far: benchmark Rs +646, unified Rs +634, intramonth Rs +325, oracle Rs +315, random_hold Rs +251, intraweek Rs +197, snake_abs_exit Rs +63, snake_abs_exit_conv Rs +47, nifty_calls Rs +46, snake_abs Rs +29, snake_abs_conv Rs +25, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_viper_wild Rs -103, snake_anaconda Rs -174, snake_viper_tick Rs -229, snake_nonews Rs -292, snake Rs -311, gold Rs -886

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.