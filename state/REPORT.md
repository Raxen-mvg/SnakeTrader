# Paper trading report

Updated 2026-11-12 14:09 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,913 | +10.46% | 0 | - | 236 |
| benchmark | 220,372 | +10.19% | 0 | - | 237 |
| snake_abs_exit_conv | 218,332 | +9.17% | 2 | 50% | 345 |
| snake_abs_exit | 217,247 | +8.62% | 2 | 50% | 345 |
| snake_abs | 215,475 | +7.74% | 1 | 100% | 255 |
| snake_abs_conv | 215,298 | +7.65% | 1 | 100% | 255 |
| intraweek | 214,392 | +7.20% | 30 | 53% | 3,302 |
| oracle | 212,839 | +6.42% | 0 | - | 233 |
| intramonth | 211,523 | +5.76% | 0 | - | 235 |
| random_hold | 208,010 | +4.00% | 10 | 70% | 733 |
| snake_viper_wild | 206,769 | +3.38% | 10 | 50% | 1,825 |
| snake_anaconda | 206,098 | +3.05% | 3 | 33% | 374 |
| snake_viper_tick | 203,233 | +1.62% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,903 | +1.45% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,590 | -7.21% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,885 (-4.06%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,096 | +1.04% |
| snake_anaconda | +1,975 | +0.97% |
| snake_abs | +1,850 | +0.87% |
| snake_abs_conv | +1,840 | +0.86% |
| intraweek | +1,259 | +0.59% |
| snake_abs_exit_conv | +1,180 | +0.54% |
| benchmark | +1,109 | +0.51% |
| unified | +1,099 | +0.50% |
| snake_abs_exit | +1,085 | +0.50% |
| random_hold | +900 | +0.43% |
| oracle | +836 | +0.39% |
| intramonth | +527 | +0.25% |
| snake_viper_wild | +27 | +0.01% |
| snake_viper_tick | +24 | +0.01% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,995 | -2.11% |

Average per day so far: unified Rs +654, benchmark Rs +637, snake_abs_exit_conv Rs +632, snake_abs_exit Rs +595, snake_abs_conv Rs +528, snake_abs Rs +516, intraweek Rs +450, oracle Rs +401, intramonth Rs +360, snake_viper_wild Rs +282, random_hold Rs +250, snake_anaconda Rs +226, snake_viper_tick Rs +154, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.