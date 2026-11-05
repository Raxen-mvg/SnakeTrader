# Paper trading report

Updated 2026-11-05 12:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,070 | +9.04% | 0 | - | 236 |
| snake_abs_exit_conv | 213,668 | +6.83% | 1 | 100% | 255 |
| snake_abs_exit | 213,365 | +6.68% | 1 | 100% | 260 |
| benchmark | 212,875 | +6.44% | 0 | - | 237 |
| intraweek | 211,369 | +5.68% | 25 | 48% | 2,757 |
| snake_abs | 210,554 | +5.28% | 1 | 100% | 255 |
| snake_abs_conv | 210,419 | +5.21% | 1 | 100% | 255 |
| intramonth | 209,758 | +4.88% | 0 | - | 235 |
| snake_viper_wild | 206,760 | +3.38% | 3 | 33% | 702 |
| random_hold | 206,560 | +3.28% | 8 | 62% | 649 |
| oracle | 204,055 | +2.03% | 0 | - | 233 |
| snake_viper_tick | 203,204 | +1.60% | 2 | 0% | 532 |
| snake_anaconda | 201,868 | +0.93% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,148 | -0.43% | 0 | - | 237 |
| gold | 194,041 | -2.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,087 (-4.96%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,116 | +1.97% |
| unified | +3,630 | +1.69% |
| random_hold | +3,251 | +1.60% |
| intramonth | +2,742 | +1.32% |
| gold | +2,647 | +1.38% |
| benchmark_smallcap | +2,477 | +1.26% |
| oracle | +2,263 | +1.12% |
| intraweek | +1,671 | +0.80% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -1,339 | -0.63% |
| snake_abs_exit_conv | -1,347 | -0.63% |
| snake_abs | -1,349 | -0.64% |
| snake_abs_exit | -1,535 | -0.71% |
| snake_anaconda | -1,953 | -0.96% |
| snake_viper_tick | -2,196 | -1.07% |
| snake_viper_wild | -2,270 | -1.09% |

Average per day so far: unified Rs +645, snake_abs_exit_conv Rs +547, snake_abs_exit Rs +535, benchmark Rs +460, snake_abs_conv Rs +417, intraweek Rs +406, snake_abs Rs +406, intramonth Rs +348, snake_viper_wild Rs +338, random_hold Rs +234, snake_viper_tick Rs +188, oracle Rs +145, snake_anaconda Rs +81, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -36, gold Rs -213, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.