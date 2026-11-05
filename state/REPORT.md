# Paper trading report

Updated 2026-11-05 11:51 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,142 | +9.07% | 0 | - | 236 |
| snake_abs_exit_conv | 214,060 | +7.03% | 1 | 100% | 255 |
| snake_abs_exit | 213,769 | +6.88% | 1 | 100% | 260 |
| benchmark | 212,790 | +6.39% | 0 | - | 237 |
| snake_abs | 210,943 | +5.47% | 1 | 100% | 255 |
| intraweek | 210,833 | +5.42% | 25 | 48% | 2,757 |
| snake_abs_conv | 210,809 | +5.41% | 1 | 100% | 255 |
| intramonth | 209,988 | +4.99% | 0 | - | 235 |
| random_hold | 206,892 | +3.45% | 8 | 62% | 649 |
| snake_viper_wild | 206,733 | +3.37% | 3 | 33% | 702 |
| oracle | 204,306 | +2.15% | 0 | - | 233 |
| snake_viper_tick | 203,180 | +1.59% | 2 | 0% | 532 |
| snake_anaconda | 202,353 | +1.18% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,304 | -0.35% | 0 | - | 237 |
| gold | 194,599 | -2.70% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,141 (-4.93%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,032 | +1.93% |
| unified | +3,703 | +1.73% |
| random_hold | +3,583 | +1.76% |
| gold | +3,206 | +1.68% |
| intramonth | +2,972 | +1.44% |
| benchmark_smallcap | +2,634 | +1.34% |
| oracle | +2,513 | +1.25% |
| intraweek | +1,136 | +0.54% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -949 | -0.45% |
| snake_abs_exit_conv | -955 | -0.44% |
| snake_abs | -960 | -0.45% |
| snake_abs_exit | -1,132 | -0.53% |
| snake_anaconda | -1,467 | -0.72% |
| snake_viper_tick | -2,220 | -1.08% |
| snake_viper_wild | -2,297 | -1.10% |

Average per day so far: unified Rs +648, snake_abs_exit_conv Rs +562, snake_abs_exit Rs +551, benchmark Rs +457, snake_abs_conv Rs +432, snake_abs Rs +421, intraweek Rs +387, intramonth Rs +357, snake_viper_wild Rs +337, random_hold Rs +246, snake_viper_tick Rs +187, oracle Rs +154, snake_anaconda Rs +102, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, gold Rs -193, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.