# Paper trading report

Updated 2026-11-05 11:29 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,435 | +9.22% | 0 | - | 236 |
| snake_abs_exit_conv | 214,681 | +7.34% | 1 | 100% | 255 |
| snake_abs_exit | 214,379 | +7.19% | 1 | 100% | 260 |
| benchmark | 212,615 | +6.31% | 0 | - | 237 |
| snake_abs | 211,559 | +5.78% | 1 | 100% | 255 |
| snake_abs_conv | 211,425 | +5.71% | 1 | 100% | 255 |
| intraweek | 211,021 | +5.51% | 25 | 48% | 2,757 |
| intramonth | 210,219 | +5.11% | 0 | - | 235 |
| random_hold | 206,993 | +3.50% | 8 | 62% | 649 |
| snake_viper_wild | 206,697 | +3.35% | 3 | 33% | 702 |
| oracle | 204,286 | +2.14% | 0 | - | 233 |
| snake_viper_tick | 203,148 | +1.57% | 2 | 0% | 532 |
| snake_anaconda | 202,871 | +1.44% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,125 | -0.44% | 0 | - | 237 |
| gold | 193,909 | -3.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,406 (-4.80%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +3,996 | +1.86% |
| benchmark | +3,856 | +1.85% |
| random_hold | +3,684 | +1.81% |
| intramonth | +3,204 | +1.55% |
| gold | +2,515 | +1.31% |
| oracle | +2,493 | +1.24% |
| benchmark_smallcap | +2,455 | +1.25% |
| intraweek | +1,323 | +0.63% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -333 | -0.16% |
| snake_abs_exit_conv | -334 | -0.15% |
| snake_abs | -344 | -0.16% |
| snake_abs_exit | -521 | -0.24% |
| snake_anaconda | -949 | -0.47% |
| snake_viper_tick | -2,253 | -1.10% |
| snake_viper_wild | -2,333 | -1.12% |

Average per day so far: unified Rs +658, snake_abs_exit_conv Rs +587, snake_abs_exit Rs +575, snake_abs_conv Rs +457, benchmark Rs +451, snake_abs Rs +445, intraweek Rs +394, intramonth Rs +365, snake_viper_wild Rs +335, random_hold Rs +250, snake_viper_tick Rs +185, oracle Rs +153, snake_anaconda Rs +125, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -218, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.