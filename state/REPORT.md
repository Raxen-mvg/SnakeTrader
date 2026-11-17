# Paper trading report

Updated 2026-11-17 11:40 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,405 | +11.20% | 0 | - | 236 |
| benchmark | 221,909 | +10.96% | 0 | - | 237 |
| snake_abs_exit | 215,156 | +7.58% | 2 | 50% | 345 |
| intraweek | 214,211 | +7.11% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,342 | +6.67% | 2 | 50% | 345 |
| oracle | 212,693 | +6.35% | 0 | - | 233 |
| intramonth | 212,354 | +6.18% | 0 | - | 235 |
| snake_abs | 209,995 | +5.00% | 1 | 100% | 255 |
| snake_abs_conv | 209,846 | +4.92% | 1 | 100% | 255 |
| random_hold | 208,097 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 207,602 | +3.80% | 14 | 50% | 2,496 |
| snake_anaconda | 205,550 | +2.77% | 3 | 33% | 374 |
| snake_viper_tick | 204,053 | +2.03% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,286 | +1.14% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,415 | -9.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,733 (-4.13%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,945 | +1.39% |
| benchmark | +1,828 | +0.83% |
| snake_viper_wild | +1,458 | +0.71% |
| benchmark_smallcap | +1,457 | +0.73% |
| snake_viper_tick | +1,433 | +0.71% |
| unified | +967 | +0.44% |
| snake_abs_exit | +747 | +0.35% |
| intramonth | +735 | +0.35% |
| oracle | +670 | +0.32% |
| gold | +460 | +0.25% |
| snake_anaconda | +447 | +0.22% |
| random_hold | +303 | +0.15% |
| snake_abs_exit_conv | +125 | +0.06% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -139 | -0.07% |
| snake_abs_conv | -144 | -0.07% |

Average per day so far: unified Rs +640, benchmark Rs +626, snake_abs_exit Rs +474, snake_abs_exit_conv Rs +417, intraweek Rs +406, oracle Rs +363, intramonth Rs +353, snake_abs_conv Rs +308, snake_abs Rs +303, snake_viper_wild Rs +282, random_hold Rs +231, snake_anaconda Rs +185, snake_viper_tick Rs +169, benchmark_smallcap Rs +74, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.