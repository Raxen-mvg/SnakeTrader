# Paper trading report

Updated 2026-11-12 15:28 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,879 | +10.44% | 0 | - | 236 |
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| snake_abs_exit_conv | 217,368 | +8.68% | 2 | 50% | 345 |
| snake_abs_exit | 216,150 | +8.07% | 2 | 50% | 345 |
| intraweek | 214,876 | +7.44% | 30 | 53% | 3,302 |
| snake_abs | 214,504 | +7.25% | 1 | 100% | 255 |
| snake_abs_conv | 214,316 | +7.16% | 1 | 100% | 255 |
| oracle | 213,220 | +6.61% | 0 | - | 233 |
| intramonth | 211,789 | +5.89% | 0 | - | 235 |
| random_hold | 208,231 | +4.12% | 10 | 70% | 733 |
| snake_anaconda | 204,841 | +2.42% | 3 | 33% | 374 |
| snake_viper_wild | 204,717 | +2.36% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,508 | +1.75% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,215 | +0.61% | 12 | 50% | 2,054 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,508 | -7.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,879 (-4.06%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,702 | +1.34% |
| intraweek | +1,743 | +0.82% |
| benchmark | +1,346 | +0.61% |
| oracle | +1,217 | +0.57% |
| random_hold | +1,120 | +0.54% |
| unified | +1,065 | +0.48% |
| snake_abs | +879 | +0.41% |
| snake_abs_conv | +858 | +0.40% |
| intramonth | +793 | +0.38% |
| snake_anaconda | +718 | +0.35% |
| snake_abs_exit_conv | +217 | +0.10% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_abs_exit | -12 | -0.01% |
| snake_viper_tick | -1,994 | -0.98% |
| snake_viper_wild | -2,025 | -0.98% |
| gold | -4,077 | -2.15% |

Average per day so far: unified Rs +652, benchmark Rs +644, snake_abs_exit_conv Rs +599, snake_abs_exit Rs +557, snake_abs_conv Rs +494, snake_abs Rs +483, intraweek Rs +465, oracle Rs +413, intramonth Rs +368, random_hold Rs +257, snake_viper_wild Rs +197, snake_anaconda Rs +179, benchmark_smallcap Rs +125, snake_viper_tick Rs +58, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -453

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.