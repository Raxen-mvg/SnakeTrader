# Paper trading report

Updated 2026-11-05 15:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 215,942 | +7.97% | 0 | - | 236 |
| snake_abs_exit_conv | 213,973 | +6.99% | 1 | 100% | 255 |
| snake_abs_exit | 213,852 | +6.93% | 1 | 100% | 260 |
| benchmark | 213,762 | +6.88% | 0 | - | 237 |
| snake_abs | 210,870 | +5.43% | 1 | 100% | 255 |
| snake_abs_conv | 210,719 | +5.36% | 1 | 100% | 255 |
| intraweek | 209,643 | +4.82% | 25 | 48% | 2,757 |
| intramonth | 208,020 | +4.01% | 0 | - | 235 |
| snake_viper_wild | 204,772 | +2.39% | 3 | 33% | 702 |
| random_hold | 204,483 | +2.24% | 8 | 62% | 649 |
| oracle | 204,073 | +2.04% | 0 | - | 233 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_anaconda | 201,504 | +0.75% | 3 | 33% | 374 |
| snake_viper_tick | 201,252 | +0.63% | 2 | 0% | 532 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,923 | -0.54% | 0 | - | 237 |
| gold | 194,188 | -2.91% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,214 (-5.39%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +5,003 | +2.40% |
| gold | +2,795 | +1.46% |
| oracle | +2,281 | +1.13% |
| benchmark_smallcap | +2,253 | +1.15% |
| unified | +1,503 | +0.70% |
| random_hold | +1,174 | +0.58% |
| intramonth | +1,004 | +0.48% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -55 | -0.03% |
| snake_abs | -1,033 | -0.49% |
| snake_abs_conv | -1,039 | -0.49% |
| snake_abs_exit_conv | -1,042 | -0.48% |
| snake_abs_exit | -1,048 | -0.49% |
| snake_anaconda | -2,316 | -1.14% |
| snake_viper_tick | -4,148 | -2.02% |
| snake_viper_wild | -4,258 | -2.04% |

Average per day so far: unified Rs +569, snake_abs_exit_conv Rs +559, snake_abs_exit Rs +554, benchmark Rs +492, snake_abs_conv Rs +429, snake_abs Rs +418, intraweek Rs +344, intramonth Rs +286, snake_viper_wild Rs +239, random_hold Rs +160, oracle Rs +145, snake_viper_tick Rs +74, nifty_calls Rs +66, snake_anaconda Rs +65, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -45, gold Rs -208, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.