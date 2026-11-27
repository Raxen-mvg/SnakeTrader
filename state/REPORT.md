# Paper trading report

Updated 2026-11-27 14:46 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 223,784 | +11.89% | 0 | - | 237 |
| unified | 223,583 | +11.79% | 0 | - | 236 |
| oracle | 211,745 | +5.87% | 0 | - | 233 |
| random_hold | 211,352 | +5.68% | 13 | 69% | 1,037 |
| intramonth | 210,846 | +5.42% | 0 | - | 235 |
| intraweek | 207,743 | +3.87% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,453 | +3.23% | 2 | 50% | 345 |
| snake_abs_exit | 204,131 | +2.07% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,423 | +0.71% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,690 | -0.15% | 1 | 100% | 255 |
| snake_abs_conv | 199,506 | -0.25% | 1 | 100% | 255 |
| snake_anaconda | 192,992 | -3.50% | 3 | 33% | 374 |
| snake_viper_wild | 192,255 | -3.87% | 16 | 50% | 2,827 |
| snake_viper_tick | 188,990 | -5.50% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,860 | -14.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,930 (-5.54%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,056 | +3.02% |
| gold | +4,866 | +2.93% |
| snake_abs_exit | +3,054 | +1.52% |
| random_hold | +2,758 | +1.32% |
| snake_abs_conv | +1,140 | +0.57% |
| snake_abs | +1,138 | +0.57% |
| snake_anaconda | +696 | +0.36% |
| intraweek | +694 | +0.34% |
| benchmark_smallcap | +583 | +0.29% |
| unified | +504 | +0.23% |
| intramonth | +313 | +0.15% |
| snake_viper_wild | +50 | +0.03% |
| snake_viper_tick | +49 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -491 | -0.23% |
| benchmark | -2,203 | -0.97% |

Average per day so far: benchmark Rs +566, unified Rs +561, oracle Rs +280, random_hold Rs +270, intramonth Rs +258, intraweek Rs +184, snake_abs_exit_conv Rs +165, snake_abs_exit Rs +106, nifty_calls Rs +44, benchmark_smallcap Rs +37, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, snake_anaconda Rs -189, snake_viper_wild Rs -228, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -355, gold Rs -694

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.