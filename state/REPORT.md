# Paper trading report

Updated 2026-11-16 09:56 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,922 | +10.46% | 0 | - | 237 |
| unified | 220,873 | +10.44% | 0 | - | 236 |
| intraweek | 215,122 | +7.56% | 35 | 54% | 3,851 |
| snake_abs_exit | 214,643 | +7.32% | 2 | 50% | 345 |
| oracle | 213,880 | +6.94% | 0 | - | 233 |
| snake_abs_exit_conv | 213,474 | +6.74% | 2 | 50% | 345 |
| intramonth | 211,259 | +5.63% | 0 | - | 235 |
| snake_abs | 210,754 | +5.38% | 1 | 100% | 255 |
| snake_abs_conv | 210,579 | +5.29% | 1 | 100% | 255 |
| random_hold | 208,220 | +4.11% | 10 | 70% | 733 |
| snake_anaconda | 204,698 | +2.35% | 3 | 33% | 374 |
| snake_viper_wild | 203,530 | +1.76% | 14 | 50% | 2,496 |
| benchmark_smallcap | 202,320 | +1.16% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,048 | +0.02% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,368 | -8.82% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,984 (-4.01%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,852 | +0.85% |
| benchmark | +1,584 | +0.72% |
| intramonth | +1,202 | +0.57% |
| random_hold | +994 | +0.48% |
| oracle | +782 | +0.37% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -194 | -0.10% |
| benchmark_smallcap | -549 | -0.27% |
| intraweek | -1,023 | -0.47% |
| snake_viper_tick | -1,207 | -0.60% |
| snake_viper_wild | -1,228 | -0.60% |
| gold | -1,628 | -0.89% |
| snake_abs | -1,786 | -0.84% |
| snake_abs_conv | -1,788 | -0.84% |
| snake_abs_exit | -2,342 | -1.08% |
| snake_abs_exit_conv | -2,907 | -1.34% |

Average per day so far: benchmark Rs +615, unified Rs +614, snake_abs_exit Rs +472, intraweek Rs +445, snake_abs_exit_conv Rs +435, oracle Rs +408, snake_abs_conv Rs +341, snake_abs Rs +336, intramonth Rs +331, random_hold Rs +242, snake_anaconda Rs +162, snake_viper_wild Rs +136, benchmark_smallcap Rs +77, nifty_calls Rs +54, snake_viper_tick Rs +2, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -519

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.