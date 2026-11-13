# Paper trading report

Updated 2026-11-13 15:16 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 219,316 | +9.66% | 0 | - | 237 |
| unified | 219,071 | +9.54% | 0 | - | 236 |
| snake_abs_exit | 217,011 | +8.51% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,427 | +8.21% | 2 | 50% | 345 |
| intraweek | 215,947 | +7.97% | 30 | 53% | 3,302 |
| oracle | 213,125 | +6.56% | 0 | - | 233 |
| snake_abs | 212,492 | +6.25% | 1 | 100% | 255 |
| snake_abs_conv | 212,318 | +6.16% | 1 | 100% | 255 |
| intramonth | 210,145 | +5.07% | 0 | - | 235 |
| random_hold | 207,252 | +3.63% | 10 | 70% | 733 |
| snake_anaconda | 204,871 | +2.44% | 3 | 33% | 374 |
| snake_viper_wild | 204,733 | +2.37% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,231 | +0.61% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,979 | -8.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,547 (-4.23%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,289 | +0.60% |
| oracle | +10 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| benchmark_smallcap | -291 | -0.14% |
| snake_abs_exit | -431 | -0.20% |
| snake_viper_tick | -551 | -0.27% |
| snake_viper_wild | -560 | -0.27% |
| random_hold | -802 | -0.39% |
| snake_anaconda | -1,056 | -0.51% |
| benchmark | -1,232 | -0.56% |
| gold | -1,332 | -0.72% |
| intramonth | -1,448 | -0.68% |
| unified | -1,626 | -0.74% |
| snake_abs_exit_conv | -2,247 | -1.03% |
| snake_abs_conv | -3,217 | -1.49% |
| snake_abs | -3,220 | -1.49% |

Average per day so far: benchmark Rs +585, unified Rs +578, snake_abs_exit Rs +567, snake_abs_exit_conv Rs +548, intraweek Rs +483, snake_abs_conv Rs +411, snake_abs Rs +403, oracle Rs +398, intramonth Rs +307, random_hold Rs +220, snake_viper_wild Rs +189, snake_anaconda Rs +174, benchmark_smallcap Rs +100, snake_viper_tick Rs +56, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.