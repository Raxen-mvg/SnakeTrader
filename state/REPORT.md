# Paper trading report

Updated 2026-11-17 12:30 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,254 | +11.13% | 0 | - | 237 |
| unified | 222,090 | +11.04% | 0 | - | 236 |
| snake_abs_exit | 214,339 | +7.17% | 2 | 50% | 345 |
| intraweek | 212,784 | +6.39% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,564 | +6.28% | 2 | 50% | 345 |
| oracle | 212,377 | +6.19% | 0 | - | 233 |
| intramonth | 211,971 | +5.99% | 0 | - | 235 |
| snake_abs | 209,386 | +4.69% | 1 | 100% | 255 |
| snake_abs_conv | 209,238 | +4.62% | 1 | 100% | 255 |
| random_hold | 207,648 | +3.82% | 10 | 70% | 733 |
| snake_viper_wild | 207,603 | +3.80% | 14 | 50% | 2,496 |
| snake_anaconda | 204,999 | +2.50% | 3 | 33% | 374 |
| snake_viper_tick | 204,054 | +2.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,715 | +0.86% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,184 | -9.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,254 (-4.37%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,173 | +0.99% |
| intraweek | +1,518 | +0.72% |
| snake_viper_wild | +1,459 | +0.71% |
| snake_viper_tick | +1,434 | +0.71% |
| benchmark_smallcap | +886 | +0.44% |
| unified | +653 | +0.29% |
| oracle | +354 | +0.17% |
| intramonth | +352 | +0.17% |
| gold | +230 | +0.13% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -70 | -0.03% |
| snake_anaconda | -104 | -0.05% |
| random_hold | -145 | -0.07% |
| snake_abs_exit_conv | -653 | -0.31% |
| snake_abs | -748 | -0.36% |
| snake_abs_conv | -752 | -0.36% |

Average per day so far: benchmark Rs +636, unified Rs +631, snake_abs_exit Rs +448, snake_abs_exit_conv Rs +393, intraweek Rs +365, oracle Rs +354, intramonth Rs +342, snake_abs_conv Rs +289, snake_abs Rs +284, snake_viper_wild Rs +282, random_hold Rs +219, snake_viper_tick Rs +169, snake_anaconda Rs +167, benchmark_smallcap Rs +55, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -538

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.