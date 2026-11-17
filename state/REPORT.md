# Paper trading report

Updated 2026-11-17 13:02 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 222,024 | +11.01% | 0 | - | 237 |
| unified | 221,578 | +10.79% | 0 | - | 236 |
| snake_abs_exit | 214,305 | +7.15% | 2 | 50% | 345 |
| intraweek | 213,987 | +6.99% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,612 | +6.31% | 2 | 50% | 345 |
| oracle | 212,072 | +6.04% | 0 | - | 233 |
| intramonth | 211,466 | +5.73% | 0 | - | 235 |
| snake_abs | 209,450 | +4.72% | 1 | 100% | 255 |
| snake_abs_conv | 209,307 | +4.65% | 1 | 100% | 255 |
| snake_viper_wild | 208,015 | +4.01% | 14 | 50% | 2,496 |
| random_hold | 207,556 | +3.78% | 10 | 70% | 733 |
| snake_anaconda | 204,961 | +2.48% | 3 | 33% | 374 |
| snake_viper_tick | 204,460 | +2.23% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,390 | +0.69% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,398 | -9.30% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,142 (-4.43%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,721 | +1.29% |
| benchmark | +1,943 | +0.88% |
| snake_viper_wild | +1,871 | +0.91% |
| snake_viper_tick | +1,840 | +0.91% |
| benchmark_smallcap | +561 | +0.28% |
| gold | +444 | +0.24% |
| unified | +140 | +0.06% |
| oracle | +50 | +0.02% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -104 | -0.05% |
| snake_anaconda | -142 | -0.07% |
| intramonth | -153 | -0.07% |
| random_hold | -237 | -0.11% |
| snake_abs_exit_conv | -605 | -0.28% |
| snake_abs_conv | -682 | -0.33% |
| snake_abs | -684 | -0.33% |

Average per day so far: benchmark Rs +629, unified Rs +617, snake_abs_exit Rs +447, intraweek Rs +400, snake_abs_exit_conv Rs +394, oracle Rs +345, intramonth Rs +328, snake_viper_wild Rs +297, snake_abs_conv Rs +291, snake_abs Rs +286, random_hold Rs +216, snake_viper_tick Rs +186, snake_anaconda Rs +165, nifty_calls Rs +52, benchmark_smallcap Rs +45, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -531

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.