# Paper trading report

Updated 2026-11-05 11:08 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,786 | +9.39% | 0 | - | 236 |
| snake_abs_exit_conv | 215,450 | +7.72% | 1 | 100% | 255 |
| snake_abs_exit | 215,159 | +7.58% | 1 | 100% | 260 |
| benchmark | 212,492 | +6.25% | 0 | - | 237 |
| snake_abs | 212,323 | +6.16% | 1 | 100% | 255 |
| snake_abs_conv | 212,188 | +6.09% | 1 | 100% | 255 |
| intraweek | 210,853 | +5.43% | 25 | 48% | 2,757 |
| intramonth | 210,557 | +5.28% | 0 | - | 235 |
| random_hold | 206,971 | +3.48% | 8 | 62% | 649 |
| snake_viper_wild | 206,735 | +3.37% | 3 | 33% | 702 |
| oracle | 204,336 | +2.17% | 0 | - | 233 |
| snake_anaconda | 203,441 | +1.72% | 3 | 33% | 374 |
| snake_viper_tick | 203,185 | +1.59% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,304 | -0.35% | 0 | - | 237 |
| gold | 193,860 | -3.07% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,683 (-4.66%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,346 | +2.03% |
| benchmark | +3,733 | +1.79% |
| random_hold | +3,662 | +1.80% |
| intramonth | +3,541 | +1.71% |
| benchmark_smallcap | +2,634 | +1.34% |
| oracle | +2,544 | +1.26% |
| gold | +2,466 | +1.29% |
| intraweek | +1,155 | +0.55% |
| snake_abs_exit_conv | +435 | +0.20% |
| snake_abs_conv | +429 | +0.20% |
| snake_abs | +420 | +0.20% |
| snake_abs_exit | +258 | +0.12% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -380 | -0.19% |
| snake_viper_tick | -2,215 | -1.08% |
| snake_viper_wild | -2,295 | -1.10% |

Average per day so far: unified Rs +671, snake_abs_exit_conv Rs +618, snake_abs_exit Rs +606, snake_abs_conv Rs +488, snake_abs Rs +474, benchmark Rs +446, intraweek Rs +388, intramonth Rs +377, snake_viper_wild Rs +337, random_hold Rs +249, snake_viper_tick Rs +187, oracle Rs +155, snake_anaconda Rs +150, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, gold Rs -219, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.