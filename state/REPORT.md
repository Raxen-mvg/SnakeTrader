# Paper trading report

Updated 2026-11-12 12:45 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,545 | +10.77% | 0 | - | 236 |
| benchmark | 220,043 | +10.02% | 0 | - | 237 |
| snake_abs_exit_conv | 218,706 | +9.35% | 2 | 50% | 345 |
| snake_abs_exit | 217,689 | +8.84% | 2 | 50% | 345 |
| snake_abs | 215,755 | +7.88% | 1 | 100% | 255 |
| snake_abs_conv | 215,584 | +7.79% | 1 | 100% | 255 |
| intraweek | 214,811 | +7.41% | 30 | 53% | 3,302 |
| oracle | 213,364 | +6.68% | 0 | - | 233 |
| intramonth | 211,872 | +5.94% | 0 | - | 235 |
| random_hold | 208,110 | +4.05% | 10 | 70% | 733 |
| snake_viper_wild | 206,979 | +3.49% | 10 | 50% | 1,825 |
| snake_anaconda | 206,361 | +3.18% | 3 | 33% | 374 |
| snake_viper_tick | 203,439 | +1.72% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,116 | +1.56% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,968 | -7.02% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,255 (-3.87%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,309 | +1.15% |
| snake_anaconda | +2,238 | +1.10% |
| snake_abs | +2,130 | +1.00% |
| snake_abs_conv | +2,126 | +1.00% |
| unified | +1,731 | +0.79% |
| intraweek | +1,678 | +0.79% |
| snake_abs_exit_conv | +1,554 | +0.72% |
| snake_abs_exit | +1,526 | +0.71% |
| oracle | +1,361 | +0.64% |
| random_hold | +999 | +0.48% |
| intramonth | +876 | +0.41% |
| benchmark | +780 | +0.36% |
| snake_viper_wild | +237 | +0.12% |
| snake_viper_tick | +230 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,617 | -1.91% |

Average per day so far: unified Rs +673, snake_abs_exit_conv Rs +645, benchmark Rs +626, snake_abs_exit Rs +610, snake_abs_conv Rs +537, snake_abs Rs +525, intraweek Rs +463, oracle Rs +418, intramonth Rs +371, snake_viper_wild Rs +291, random_hold Rs +253, snake_anaconda Rs +236, snake_viper_tick Rs +164, benchmark_smallcap Rs +111, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -438

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.