# Paper trading report

Updated 2026-11-12 09:24 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,264 | +10.63% | 0 | - | 236 |
| benchmark | 220,593 | +10.30% | 0 | - | 237 |
| snake_abs_exit_conv | 220,222 | +10.11% | 2 | 50% | 345 |
| snake_abs_exit | 219,370 | +9.69% | 2 | 50% | 345 |
| snake_abs | 216,811 | +8.41% | 1 | 100% | 255 |
| snake_abs_conv | 216,651 | +8.32% | 1 | 100% | 255 |
| intraweek | 214,873 | +7.44% | 30 | 53% | 3,302 |
| oracle | 212,631 | +6.32% | 0 | - | 233 |
| intramonth | 212,282 | +6.14% | 0 | - | 235 |
| snake_viper_wild | 210,651 | +5.33% | 10 | 50% | 1,825 |
| random_hold | 207,888 | +3.94% | 9 | 67% | 709 |
| snake_anaconda | 207,677 | +3.84% | 3 | 33% | 374 |
| snake_viper_tick | 207,037 | +3.52% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,194 | +1.60% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,708 | -6.65% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,440 (-3.78%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +3,910 | +1.89% |
| snake_viper_tick | +3,828 | +1.88% |
| snake_anaconda | +3,554 | +1.74% |
| snake_abs_exit | +3,207 | +1.48% |
| snake_abs_conv | +3,193 | +1.50% |
| snake_abs | +3,187 | +1.49% |
| snake_abs_exit_conv | +3,070 | +1.41% |
| benchmark_smallcap | +2,388 | +1.19% |
| intraweek | +1,740 | +0.82% |
| unified | +1,450 | +0.66% |
| benchmark | +1,331 | +0.61% |
| intramonth | +1,285 | +0.61% |
| random_hold | +777 | +0.38% |
| oracle | +629 | +0.30% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,877 | -1.52% |

Average per day so far: snake_abs_exit_conv Rs +697, snake_abs_exit Rs +668, unified Rs +664, benchmark Rs +644, snake_abs_conv Rs +574, snake_abs Rs +560, intraweek Rs +465, snake_viper_wild Rs +444, oracle Rs +395, intramonth Rs +384, snake_viper_tick Rs +335, snake_anaconda Rs +284, random_hold Rs +246, benchmark_smallcap Rs +114, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -415

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.