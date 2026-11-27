# Paper trading report

Updated 2026-11-27 11:00 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,373 | +12.19% | 0 | - | 237 |
| unified | 222,539 | +11.27% | 0 | - | 236 |
| oracle | 212,089 | +6.04% | 0 | - | 233 |
| intramonth | 210,383 | +5.19% | 0 | - | 235 |
| random_hold | 209,851 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 207,713 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,339 | +2.67% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,145 | +2.07% | 2 | 50% | 345 |
| benchmark_smallcap | 202,006 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,233 | +0.62% | 1 | 100% | 255 |
| snake_abs_conv | 201,054 | +0.53% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,716 | -2.64% | 3 | 33% | 374 |
| snake_viper_wild | 193,705 | -3.15% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,410 | -4.79% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,479 | -15.26% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,523 (-5.74%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,261 | +2.12% |
| snake_abs_exit_conv | +3,748 | +1.87% |
| gold | +3,485 | +2.10% |
| snake_abs_conv | +2,687 | +1.35% |
| snake_abs | +2,681 | +1.35% |
| snake_anaconda | +2,419 | +1.26% |
| snake_viper_wild | +1,499 | +0.78% |
| snake_viper_tick | +1,469 | +0.78% |
| random_hold | +1,257 | +0.60% |
| benchmark_smallcap | +1,166 | +0.58% |
| intraweek | +664 | +0.32% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -146 | -0.07% |
| intramonth | -150 | -0.07% |
| unified | -539 | -0.24% |
| benchmark | -1,614 | -0.71% |

Average per day so far: benchmark Rs +580, unified Rs +537, oracle Rs +288, intramonth Rs +247, random_hold Rs +235, intraweek Rs +184, snake_abs_exit Rs +137, snake_abs_exit_conv Rs +106, benchmark_smallcap Rs +53, nifty_calls Rs +44, snake_abs Rs +31, snake_abs_conv Rs +27, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -143, snake_viper_wild Rs -185, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -309, gold Rs -727

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.