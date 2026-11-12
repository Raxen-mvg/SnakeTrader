# Paper trading report

Updated 2026-11-12 15:30 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,697 | +10.35% | 0 | - | 236 |
| benchmark | 220,548 | +10.27% | 0 | - | 237 |
| snake_abs_exit_conv | 218,674 | +9.34% | 2 | 50% | 345 |
| snake_abs_exit | 217,443 | +8.72% | 2 | 50% | 345 |
| snake_abs | 215,711 | +7.86% | 1 | 100% | 255 |
| snake_abs_conv | 215,535 | +7.77% | 1 | 100% | 255 |
| intraweek | 214,658 | +7.33% | 30 | 53% | 3,302 |
| oracle | 213,115 | +6.56% | 0 | - | 233 |
| intramonth | 211,593 | +5.80% | 0 | - | 235 |
| random_hold | 208,054 | +4.03% | 10 | 70% | 733 |
| snake_anaconda | 205,927 | +2.96% | 3 | 33% | 374 |
| snake_viper_wild | 205,293 | +2.65% | 13 | 54% | 2,247 |
| benchmark_smallcap | 203,206 | +1.60% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,782 | +0.89% | 12 | 50% | 2,054 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,311 | -7.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,980 (-4.01%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,399 | +1.20% |
| snake_abs | +2,087 | +0.98% |
| snake_abs_conv | +2,077 | +0.97% |
| snake_anaconda | +1,804 | +0.88% |
| intraweek | +1,525 | +0.71% |
| snake_abs_exit_conv | +1,523 | +0.70% |
| benchmark | +1,285 | +0.59% |
| snake_abs_exit | +1,280 | +0.59% |
| oracle | +1,112 | +0.53% |
| random_hold | +943 | +0.46% |
| unified | +883 | +0.40% |
| intramonth | +597 | +0.28% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,427 | -0.70% |
| snake_viper_wild | -1,449 | -0.70% |
| gold | -4,274 | -2.25% |

Average per day so far: unified Rs +647, snake_abs_exit_conv Rs +644, benchmark Rs +642, snake_abs_exit Rs +601, snake_abs_conv Rs +536, snake_abs Rs +524, intraweek Rs +458, oracle Rs +410, intramonth Rs +362, random_hold Rs +252, snake_viper_wild Rs +221, snake_anaconda Rs +220, benchmark_smallcap Rs +114, snake_viper_tick Rs +85, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -459

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.