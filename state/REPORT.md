# Paper trading report

Updated 2026-11-05 09:17 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,163 | +9.08% | 0 | - | 236 |
| snake_abs_exit_conv | 216,716 | +8.36% | 1 | 100% | 255 |
| snake_abs_exit | 216,647 | +8.32% | 1 | 100% | 260 |
| snake_abs | 213,561 | +6.78% | 1 | 100% | 255 |
| snake_abs_conv | 213,436 | +6.72% | 1 | 100% | 255 |
| intraweek | 212,407 | +6.20% | 25 | 48% | 2,757 |
| benchmark | 212,286 | +6.14% | 0 | - | 237 |
| intramonth | 210,935 | +5.47% | 0 | - | 235 |
| snake_viper_wild | 207,142 | +3.57% | 3 | 33% | 702 |
| random_hold | 206,824 | +3.41% | 8 | 62% | 649 |
| oracle | 205,746 | +2.87% | 0 | - | 233 |
| snake_anaconda | 204,638 | +2.32% | 3 | 33% | 361 |
| snake_viper_tick | 203,613 | +1.81% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,887 | -0.06% | 0 | - | 237 |
| gold | 194,961 | -2.52% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,369 (-4.32%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +3,953 | +1.96% |
| intramonth | +3,919 | +1.89% |
| unified | +3,724 | +1.74% |
| gold | +3,567 | +1.86% |
| benchmark | +3,527 | +1.69% |
| random_hold | +3,515 | +1.73% |
| benchmark_smallcap | +3,217 | +1.64% |
| intraweek | +2,709 | +1.29% |
| snake_abs_exit | +1,746 | +0.81% |
| snake_abs_exit_conv | +1,701 | +0.79% |
| snake_abs_conv | +1,677 | +0.79% |
| snake_abs | +1,658 | +0.78% |
| snake_anaconda | +818 | +0.40% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,787 | -0.87% |
| snake_viper_wild | -1,888 | -0.90% |

Average per day so far: snake_abs_exit_conv Rs +669, snake_abs_exit Rs +666, unified Rs +649, snake_abs_conv Rs +537, snake_abs Rs +522, intraweek Rs +443, benchmark Rs +439, intramonth Rs +391, snake_viper_wild Rs +357, random_hold Rs +244, snake_viper_tick Rs +213, oracle Rs +205, snake_anaconda Rs +202, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -5, gold Rs -180, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.