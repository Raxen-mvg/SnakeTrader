# Paper trading report

Updated 2026-11-11 10:55 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,144 | +10.57% | 0 | - | 237 |
| unified | 220,841 | +10.42% | 0 | - | 236 |
| snake_abs_exit_conv | 216,079 | +8.04% | 2 | 50% | 345 |
| intraweek | 214,747 | +7.37% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,648 | +7.32% | 2 | 50% | 345 |
| snake_abs | 212,600 | +6.30% | 1 | 100% | 255 |
| snake_abs_conv | 212,445 | +6.22% | 1 | 100% | 255 |
| oracle | 212,230 | +6.12% | 0 | - | 233 |
| intramonth | 211,592 | +5.80% | 0 | - | 235 |
| random_hold | 206,940 | +3.47% | 9 | 67% | 709 |
| snake_anaconda | 202,559 | +1.28% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,771 | +0.89% | 0 | - | 237 |
| snake_viper_wild | 200,840 | +0.42% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,429 | -1.29% | 9 | 44% | 1,639 |
| gold | 189,865 | -5.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,507 (-4.25%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,170 | +1.97% |
| benchmark_smallcap | +3,598 | +1.82% |
| snake_viper_wild | +3,410 | +1.73% |
| snake_viper_tick | +3,352 | +1.73% |
| snake_anaconda | +3,093 | +1.55% |
| benchmark | +3,052 | +1.40% |
| snake_abs_conv | +2,968 | +1.42% |
| snake_abs | +2,953 | +1.41% |
| snake_abs_exit | +2,664 | +1.26% |
| oracle | +2,311 | +1.10% |
| random_hold | +1,979 | +0.97% |
| unified | +1,094 | +0.50% |
| intramonth | +983 | +0.47% |
| intraweek | +205 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,269 | -1.18% |

Average per day so far: benchmark Rs +682, unified Rs +672, snake_abs_exit_conv Rs +574, snake_abs_exit Rs +523, intraweek Rs +476, snake_abs_conv Rs +444, snake_abs Rs +434, oracle Rs +395, intramonth Rs +374, random_hold Rs +224, snake_anaconda Rs +98, benchmark_smallcap Rs +66, nifty_calls Rs +59, snake_viper_wild Rs +37, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -129, gold Rs -327, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.