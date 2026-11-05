# Paper trading report

Updated 2026-11-05 13:13 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,341 | +8.67% | 0 | - | 236 |
| snake_abs_exit_conv | 214,037 | +7.02% | 1 | 100% | 255 |
| snake_abs_exit | 213,729 | +6.87% | 1 | 100% | 260 |
| benchmark | 213,219 | +6.61% | 0 | - | 237 |
| snake_abs | 210,923 | +5.46% | 1 | 100% | 255 |
| snake_abs_conv | 210,787 | +5.39% | 1 | 100% | 255 |
| intraweek | 210,641 | +5.32% | 25 | 48% | 2,757 |
| intramonth | 209,260 | +4.63% | 0 | - | 235 |
| snake_viper_wild | 206,506 | +3.25% | 3 | 33% | 702 |
| random_hold | 205,852 | +2.93% | 8 | 62% | 649 |
| oracle | 203,889 | +1.94% | 0 | - | 233 |
| snake_viper_tick | 202,960 | +1.48% | 2 | 0% | 532 |
| snake_anaconda | 202,289 | +1.15% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,856 | -0.57% | 0 | - | 237 |
| gold | 194,123 | -2.94% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,918 (-5.04%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,460 | +2.14% |
| unified | +2,902 | +1.35% |
| gold | +2,729 | +1.43% |
| random_hold | +2,543 | +1.25% |
| intramonth | +2,244 | +1.08% |
| benchmark_smallcap | +2,186 | +1.11% |
| oracle | +2,096 | +1.04% |
| intraweek | +943 | +0.45% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -972 | -0.46% |
| snake_abs_exit_conv | -978 | -0.46% |
| snake_abs | -980 | -0.46% |
| snake_abs_exit | -1,171 | -0.55% |
| snake_anaconda | -1,531 | -0.75% |
| snake_viper_tick | -2,441 | -1.19% |
| snake_viper_wild | -2,524 | -1.21% |

Average per day so far: unified Rs +619, snake_abs_exit_conv Rs +561, snake_abs_exit Rs +549, benchmark Rs +472, snake_abs_conv Rs +431, snake_abs Rs +420, intraweek Rs +380, intramonth Rs +331, snake_viper_wild Rs +325, random_hold Rs +209, snake_viper_tick Rs +174, oracle Rs +139, snake_anaconda Rs +100, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -48, gold Rs -210, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.