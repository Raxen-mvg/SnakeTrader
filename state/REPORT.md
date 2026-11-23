# Paper trading report

Updated 2026-11-23 14:19 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,014 | +12.01% | 0 | - | 236 |
| benchmark | 222,192 | +11.10% | 0 | - | 237 |
| intraweek | 212,273 | +6.14% | 40 | 55% | 4,400 |
| intramonth | 212,228 | +6.11% | 0 | - | 235 |
| oracle | 211,862 | +5.93% | 0 | - | 233 |
| random_hold | 208,994 | +4.50% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,769 | +3.38% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,038 | +3.02% | 2 | 50% | 345 |
| snake_abs | 204,373 | +2.19% | 1 | 100% | 255 |
| snake_abs_conv | 204,199 | +2.10% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,769 | +0.39% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,484 | -0.26% | 0 | - | 237 |
| snake_anaconda | 197,790 | -1.10% | 3 | 33% | 374 |
| snake_viper_tick | 197,345 | -1.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,150 (-4.93%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,381 | +0.82% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -578 | -0.28% |
| oracle | -616 | -0.29% |
| benchmark_smallcap | -1,424 | -0.71% |
| snake_abs | -1,547 | -0.75% |
| snake_abs_conv | -1,584 | -0.77% |
| random_hold | -1,765 | -0.84% |
| snake_abs_exit | -1,793 | -0.86% |
| snake_viper_tick | -2,027 | -1.02% |
| snake_viper_wild | -2,060 | -1.02% |
| snake_anaconda | -2,116 | -1.06% |
| unified | -2,167 | -0.96% |
| intramonth | -2,776 | -1.29% |
| benchmark | -2,945 | -1.31% |
| intraweek | -3,439 | -1.59% |

Average per day so far: unified Rs +616, benchmark Rs +569, intraweek Rs +315, intramonth Rs +314, oracle Rs +304, random_hold Rs +231, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +168, snake_abs Rs +118, snake_abs_conv Rs +117, nifty_calls Rs +47, snake_viper_wild Rs +25, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -15, snake_anaconda Rs -65, snake_viper_tick Rs -95, snake_nonews Rs -300, snake Rs -320, gold Rs -784

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.