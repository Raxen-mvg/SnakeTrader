# Paper trading report

Updated 2026-11-23 09:38 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,388 | +12.69% | 0 | - | 236 |
| benchmark | 224,151 | +12.07% | 0 | - | 237 |
| intraweek | 213,581 | +6.79% | 40 | 55% | 4,400 |
| intramonth | 213,111 | +6.56% | 0 | - | 235 |
| oracle | 211,739 | +5.87% | 0 | - | 233 |
| random_hold | 211,071 | +5.54% | 12 | 75% | 1,009 |
| snake_abs_exit | 208,711 | +4.36% | 2 | 50% | 345 |
| snake_abs_exit_conv | 207,224 | +3.61% | 2 | 50% | 345 |
| snake_abs | 205,780 | +2.89% | 1 | 100% | 255 |
| snake_abs_conv | 205,639 | +2.82% | 1 | 100% | 255 |
| snake_viper_wild | 203,799 | +1.90% | 16 | 50% | 2,827 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,321 | +0.16% | 15 | 47% | 2,625 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,999 | -0.00% | 0 | - | 237 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,983 | -0.01% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,970 | -15.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,228 (-4.39%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +970 | +0.48% |
| snake_viper_tick | +949 | +0.48% |
| gold | +921 | +0.55% |
| snake_abs_exit_conv | +608 | +0.29% |
| random_hold | +312 | +0.15% |
| snake_abs_exit | +149 | +0.07% |
| snake_anaconda | +78 | +0.04% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_abs | -140 | -0.07% |
| snake_abs_conv | -144 | -0.07% |
| oracle | -740 | -0.35% |
| unified | -794 | -0.35% |
| benchmark_smallcap | -908 | -0.45% |
| benchmark | -987 | -0.44% |
| intramonth | -1,893 | -0.88% |
| intraweek | -2,131 | -0.99% |

Average per day so far: unified Rs +651, benchmark Rs +619, intraweek Rs +348, intramonth Rs +336, oracle Rs +301, random_hold Rs +284, snake_abs_exit Rs +242, snake_abs_exit_conv Rs +201, snake_abs_conv Rs +157, snake_abs Rs +156, snake_viper_wild Rs +123, nifty_calls Rs +47, snake_viper_tick Rs +11, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, benchmark_smallcap Rs -0, snake_anaconda Rs -0, snake_nonews Rs -300, snake Rs -320, gold Rs -796

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.