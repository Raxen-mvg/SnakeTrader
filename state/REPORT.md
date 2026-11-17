# Paper trading report

Updated 2026-11-17 13:45 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,741 | +10.87% | 0 | - | 237 |
| unified | 221,577 | +10.79% | 0 | - | 236 |
| snake_abs_exit | 214,869 | +7.43% | 2 | 50% | 345 |
| intraweek | 213,490 | +6.75% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,254 | +6.63% | 2 | 50% | 345 |
| oracle | 212,240 | +6.12% | 0 | - | 233 |
| intramonth | 211,562 | +5.78% | 0 | - | 235 |
| snake_abs | 210,135 | +5.07% | 1 | 100% | 255 |
| snake_abs_conv | 209,997 | +5.00% | 1 | 100% | 255 |
| snake_viper_wild | 209,229 | +4.62% | 14 | 50% | 2,496 |
| random_hold | 207,510 | +3.75% | 10 | 70% | 733 |
| snake_anaconda | 205,682 | +2.84% | 3 | 33% | 374 |
| snake_viper_tick | 205,653 | +2.83% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,031 | +0.52% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 180,823 | -9.59% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,120 (-4.44%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,085 | +1.50% |
| snake_viper_tick | +3,033 | +1.50% |
| intraweek | +2,224 | +1.05% |
| benchmark | +1,660 | +0.75% |
| snake_anaconda | +580 | +0.28% |
| snake_abs_exit | +460 | +0.21% |
| oracle | +217 | +0.10% |
| benchmark_smallcap | +202 | +0.10% |
| unified | +140 | +0.06% |
| snake_abs_exit_conv | +36 | +0.02% |
| snake_abs_conv | +7 | +0.00% |
| snake_abs | +1 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -57 | -0.03% |
| gold | -132 | -0.07% |
| random_hold | -284 | -0.14% |

Average per day so far: benchmark Rs +621, unified Rs +616, snake_abs_exit Rs +465, snake_abs_exit_conv Rs +414, intraweek Rs +385, oracle Rs +350, snake_viper_wild Rs +342, intramonth Rs +330, snake_abs_conv Rs +312, snake_abs Rs +307, snake_viper_tick Rs +236, random_hold Rs +215, snake_anaconda Rs +189, nifty_calls Rs +52, benchmark_smallcap Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -548

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.