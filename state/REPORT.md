# Paper trading report

Updated 2026-11-12 12:38 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,407 | +10.70% | 0 | - | 236 |
| benchmark | 219,920 | +9.96% | 0 | - | 237 |
| snake_abs_exit_conv | 218,643 | +9.32% | 2 | 50% | 345 |
| snake_abs_exit | 217,632 | +8.82% | 2 | 50% | 345 |
| snake_abs | 215,780 | +7.89% | 1 | 100% | 255 |
| snake_abs_conv | 215,609 | +7.80% | 1 | 100% | 255 |
| intraweek | 214,885 | +7.44% | 30 | 53% | 3,302 |
| oracle | 213,282 | +6.64% | 0 | - | 233 |
| intramonth | 211,695 | +5.85% | 0 | - | 235 |
| random_hold | 208,029 | +4.01% | 10 | 70% | 733 |
| snake_viper_wild | 207,054 | +3.53% | 10 | 50% | 1,825 |
| snake_anaconda | 206,357 | +3.18% | 3 | 33% | 374 |
| snake_viper_tick | 203,512 | +1.76% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,067 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,202 (-3.90%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,234 | +1.09% |
| benchmark_smallcap | +2,220 | +1.10% |
| snake_abs | +2,155 | +1.01% |
| snake_abs_conv | +2,151 | +1.01% |
| intraweek | +1,752 | +0.82% |
| unified | +1,593 | +0.72% |
| snake_abs_exit_conv | +1,492 | +0.69% |
| snake_abs_exit | +1,470 | +0.68% |
| oracle | +1,279 | +0.60% |
| random_hold | +918 | +0.44% |
| intramonth | +699 | +0.33% |
| benchmark | +658 | +0.30% |
| snake_viper_wild | +312 | +0.15% |
| snake_viper_tick | +303 | +0.15% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,518 | -1.86% |

Average per day so far: unified Rs +669, snake_abs_exit_conv Rs +643, benchmark Rs +623, snake_abs_exit Rs +608, snake_abs_conv Rs +538, snake_abs Rs +526, intraweek Rs +465, oracle Rs +415, intramonth Rs +365, snake_viper_wild Rs +294, random_hold Rs +251, snake_anaconda Rs +235, snake_viper_tick Rs +167, benchmark_smallcap Rs +108, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.