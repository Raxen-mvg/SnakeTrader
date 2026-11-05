# Paper trading report

Updated 2026-11-05 15:16 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,425 | +7.71% | 0 | - | 236 |
| snake_abs_exit_conv | 214,324 | +7.16% | 1 | 100% | 255 |
| snake_abs_exit | 214,172 | +7.09% | 1 | 100% | 260 |
| benchmark | 213,953 | +6.98% | 0 | - | 237 |
| snake_abs | 211,215 | +5.61% | 1 | 100% | 255 |
| snake_abs_conv | 211,070 | +5.54% | 1 | 100% | 255 |
| intraweek | 209,288 | +4.64% | 25 | 48% | 2,757 |
| intramonth | 207,382 | +3.69% | 0 | - | 235 |
| snake_viper_wild | 204,492 | +2.25% | 3 | 33% | 702 |
| random_hold | 204,208 | +2.10% | 8 | 62% | 649 |
| oracle | 203,732 | +1.87% | 0 | - | 233 |
| snake_anaconda | 202,056 | +1.03% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,977 | +0.49% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,587 | -0.71% | 0 | - | 237 |
| gold | 194,172 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,110 (-5.44%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,194 | +2.49% |
| gold | +2,778 | +1.45% |
| oracle | +1,940 | +0.96% |
| benchmark_smallcap | +1,917 | +0.97% |
| unified | +985 | +0.46% |
| random_hold | +899 | +0.44% |
| intramonth | +367 | +0.18% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -410 | -0.20% |
| snake_abs | -688 | -0.33% |
| snake_abs_conv | -688 | -0.33% |
| snake_abs_exit_conv | -691 | -0.32% |
| snake_abs_exit | -728 | -0.34% |
| snake_anaconda | -1,764 | -0.86% |
| snake_viper_tick | -4,423 | -2.15% |
| snake_viper_wild | -4,538 | -2.17% |

Average per day so far: snake_abs_exit_conv Rs +573, snake_abs_exit Rs +567, unified Rs +551, benchmark Rs +498, snake_abs_conv Rs +443, snake_abs Rs +431, intraweek Rs +332, intramonth Rs +264, snake_viper_wild Rs +225, random_hold Rs +150, oracle Rs +133, snake_anaconda Rs +89, nifty_calls Rs +66, snake_viper_tick Rs +57, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -59, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.