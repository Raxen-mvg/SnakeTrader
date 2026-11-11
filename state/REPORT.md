# Paper trading report

Updated 2026-11-11 10:25 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,991 | +10.50% | 0 | - | 237 |
| unified | 220,283 | +10.14% | 0 | - | 236 |
| snake_abs_exit_conv | 216,231 | +8.12% | 2 | 50% | 345 |
| snake_abs_exit | 214,696 | +7.35% | 2 | 50% | 345 |
| intraweek | 214,451 | +7.23% | 30 | 53% | 3,302 |
| snake_abs | 212,829 | +6.42% | 1 | 100% | 255 |
| snake_abs_conv | 212,677 | +6.34% | 1 | 100% | 255 |
| oracle | 211,393 | +5.70% | 0 | - | 233 |
| intramonth | 211,136 | +5.57% | 0 | - | 235 |
| random_hold | 206,265 | +3.13% | 9 | 67% | 709 |
| snake_anaconda | 202,602 | +1.30% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,434 | +0.72% | 0 | - | 237 |
| snake_viper_wild | 200,099 | +0.05% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 196,703 | -1.65% | 9 | 44% | 1,639 |
| gold | 189,421 | -5.29% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,140 (-4.43%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,323 | +2.04% |
| benchmark_smallcap | +3,262 | +1.65% |
| snake_abs_conv | +3,200 | +1.53% |
| snake_abs | +3,182 | +1.52% |
| snake_anaconda | +3,135 | +1.57% |
| benchmark | +2,899 | +1.33% |
| snake_abs_exit | +2,712 | +1.28% |
| snake_viper_wild | +2,669 | +1.35% |
| snake_viper_tick | +2,627 | +1.35% |
| oracle | +1,474 | +0.70% |
| random_hold | +1,304 | +0.64% |
| unified | +536 | +0.24% |
| intramonth | +527 | +0.25% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -91 | -0.04% |
| gold | -2,713 | -1.41% |

Average per day so far: benchmark Rs +677, unified Rs +654, snake_abs_exit_conv Rs +580, snake_abs_exit Rs +525, intraweek Rs +466, snake_abs_conv Rs +453, snake_abs Rs +442, oracle Rs +368, intramonth Rs +359, random_hold Rs +202, snake_anaconda Rs +100, nifty_calls Rs +59, benchmark_smallcap Rs +53, snake_viper_wild Rs +4, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -165, gold Rs -341, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.