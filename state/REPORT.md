# Paper trading report

Updated 2026-11-05 10:29 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,421 | +9.21% | 0 | - | 236 |
| snake_abs_exit_conv | 214,739 | +7.37% | 1 | 100% | 255 |
| snake_abs_exit | 214,444 | +7.22% | 1 | 100% | 260 |
| benchmark | 212,515 | +6.26% | 0 | - | 237 |
| snake_abs | 211,613 | +5.81% | 1 | 100% | 255 |
| snake_abs_conv | 211,475 | +5.74% | 1 | 100% | 255 |
| intraweek | 210,724 | +5.36% | 25 | 48% | 2,757 |
| intramonth | 210,236 | +5.12% | 0 | - | 235 |
| snake_viper_wild | 206,649 | +3.32% | 3 | 33% | 702 |
| random_hold | 206,631 | +3.31% | 8 | 62% | 649 |
| oracle | 204,431 | +2.22% | 0 | - | 233 |
| snake_viper_tick | 203,112 | +1.56% | 2 | 0% | 532 |
| snake_anaconda | 202,690 | +1.34% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,495 | -0.25% | 0 | - | 237 |
| gold | 195,126 | -2.44% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,365 (-4.82%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +3,981 | +1.86% |
| benchmark | +3,756 | +1.80% |
| gold | +3,732 | +1.95% |
| random_hold | +3,322 | +1.63% |
| intramonth | +3,220 | +1.55% |
| benchmark_smallcap | +2,825 | +1.44% |
| oracle | +2,639 | +1.31% |
| intraweek | +1,026 | +0.49% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -276 | -0.13% |
| snake_abs_conv | -283 | -0.13% |
| snake_abs | -291 | -0.14% |
| snake_abs_exit | -456 | -0.21% |
| snake_anaconda | -1,130 | -0.55% |
| snake_viper_tick | -2,288 | -1.11% |
| snake_viper_wild | -2,381 | -1.14% |

Average per day so far: unified Rs +658, snake_abs_exit_conv Rs +590, snake_abs_exit Rs +578, snake_abs_conv Rs +459, benchmark Rs +447, snake_abs Rs +447, intraweek Rs +383, intramonth Rs +366, snake_viper_wild Rs +332, random_hold Rs +237, snake_viper_tick Rs +183, oracle Rs +158, snake_anaconda Rs +117, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -21, gold Rs -174, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.