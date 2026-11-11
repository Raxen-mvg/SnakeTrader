# Paper trading report

Updated 2026-11-11 09:37 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,328 | +10.66% | 0 | - | 237 |
| unified | 220,793 | +10.40% | 0 | - | 236 |
| snake_abs_exit_conv | 215,788 | +7.89% | 2 | 50% | 345 |
| intraweek | 214,876 | +7.44% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,597 | +7.30% | 2 | 50% | 345 |
| snake_abs | 212,974 | +6.49% | 1 | 100% | 255 |
| snake_abs_conv | 212,812 | +6.41% | 1 | 100% | 255 |
| oracle | 211,410 | +5.71% | 0 | - | 233 |
| intramonth | 211,274 | +5.64% | 0 | - | 235 |
| random_hold | 206,014 | +3.01% | 9 | 67% | 709 |
| snake_anaconda | 202,642 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,109 | +0.56% | 0 | - | 237 |
| snake_viper_wild | 200,726 | +0.36% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,317 | -1.34% | 9 | 44% | 1,639 |
| gold | 189,437 | -5.28% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,314 (-4.34%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,879 | +1.83% |
| snake_abs_conv | +3,334 | +1.59% |
| snake_abs | +3,328 | +1.59% |
| snake_viper_wild | +3,296 | +1.67% |
| snake_viper_tick | +3,240 | +1.67% |
| benchmark | +3,236 | +1.48% |
| snake_anaconda | +3,175 | +1.59% |
| benchmark_smallcap | +2,937 | +1.48% |
| snake_abs_exit | +2,613 | +1.23% |
| oracle | +1,492 | +0.71% |
| random_hold | +1,053 | +0.51% |
| unified | +1,046 | +0.48% |
| intramonth | +665 | +0.32% |
| intraweek | +334 | +0.16% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,696 | -1.40% |

Average per day so far: benchmark Rs +688, unified Rs +671, snake_abs_exit_conv Rs +564, snake_abs_exit Rs +521, intraweek Rs +480, snake_abs_conv Rs +458, snake_abs Rs +447, oracle Rs +368, intramonth Rs +364, random_hold Rs +194, snake_anaconda Rs +102, nifty_calls Rs +59, benchmark_smallcap Rs +41, snake_viper_wild Rs +32, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -134, gold Rs -341, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.