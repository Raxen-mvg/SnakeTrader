# Paper trading report

Updated 2026-11-23 12:46 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,145 | +12.07% | 0 | - | 236 |
| benchmark | 222,866 | +11.43% | 0 | - | 237 |
| intraweek | 212,199 | +6.10% | 40 | 55% | 4,400 |
| intramonth | 212,171 | +6.09% | 0 | - | 235 |
| oracle | 211,961 | +5.98% | 0 | - | 233 |
| random_hold | 208,884 | +4.44% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,933 | +3.47% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,763 | +2.88% | 2 | 50% | 345 |
| snake_abs | 204,362 | +2.18% | 1 | 100% | 255 |
| snake_abs_conv | 204,204 | +2.10% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,899 | +0.45% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,529 | -0.24% | 0 | - | 237 |
| snake_anaconda | 198,145 | -0.93% | 3 | 33% | 374 |
| snake_viper_tick | 197,472 | -1.26% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,581 | -14.71% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,166 (-4.92%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,532 | +1.51% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -517 | -0.24% |
| snake_abs_exit_conv | -853 | -0.41% |
| benchmark_smallcap | -1,379 | -0.69% |
| snake_abs | -1,558 | -0.76% |
| snake_abs_conv | -1,579 | -0.77% |
| snake_abs_exit | -1,629 | -0.78% |
| snake_anaconda | -1,761 | -0.88% |
| random_hold | -1,875 | -0.89% |
| snake_viper_tick | -1,900 | -0.95% |
| snake_viper_wild | -1,931 | -0.95% |
| unified | -2,037 | -0.90% |
| benchmark | -2,272 | -1.01% |
| intramonth | -2,833 | -1.32% |
| intraweek | -3,513 | -1.63% |

Average per day so far: unified Rs +619, benchmark Rs +586, intraweek Rs +313, intramonth Rs +312, oracle Rs +307, random_hold Rs +228, snake_abs_exit Rs +193, snake_abs_exit_conv Rs +160, snake_abs Rs +118, snake_abs_conv Rs +117, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_anaconda Rs -55, snake_viper_tick Rs -90, snake_nonews Rs -300, snake Rs -320, gold Rs -754

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.