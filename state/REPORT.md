# Paper trading report

Updated 2026-11-27 14:22 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,112 | +12.06% | 0 | - | 237 |
| unified | 223,573 | +11.79% | 0 | - | 236 |
| oracle | 212,137 | +6.07% | 0 | - | 233 |
| random_hold | 211,166 | +5.58% | 13 | 69% | 1,037 |
| intramonth | 210,913 | +5.46% | 0 | - | 235 |
| intraweek | 208,284 | +4.14% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,526 | +3.26% | 2 | 50% | 345 |
| snake_abs_exit | 204,265 | +2.13% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,603 | +0.80% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,720 | -0.14% | 1 | 100% | 255 |
| snake_abs_conv | 199,536 | -0.23% | 1 | 100% | 255 |
| snake_anaconda | 193,157 | -3.42% | 3 | 33% | 374 |
| snake_viper_wild | 192,174 | -3.91% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,910 | -5.54% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,729 | -14.64% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,051 (-5.47%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,129 | +3.06% |
| gold | +4,735 | +2.85% |
| snake_abs_exit | +3,187 | +1.58% |
| random_hold | +2,572 | +1.23% |
| intraweek | +1,235 | +0.60% |
| snake_abs_conv | +1,170 | +0.59% |
| snake_abs | +1,167 | +0.59% |
| snake_anaconda | +861 | +0.45% |
| benchmark_smallcap | +762 | +0.38% |
| unified | +495 | +0.22% |
| intramonth | +380 | +0.18% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -31 | -0.02% |
| snake_viper_wild | -32 | -0.02% |
| oracle | -98 | -0.05% |
| benchmark | -1,874 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +561, oracle Rs +289, random_hold Rs +266, intramonth Rs +260, intraweek Rs +197, snake_abs_exit_conv Rs +167, snake_abs_exit Rs +109, nifty_calls Rs +44, benchmark_smallcap Rs +42, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -7, snake_abs_conv Rs -12, snake_anaconda Rs -185, snake_viper_wild Rs -230, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -358, gold Rs -697

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.