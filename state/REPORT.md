# Paper trading report

Updated 2026-11-12 12:56 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,508 | +10.75% | 0 | - | 236 |
| benchmark | 220,096 | +10.05% | 0 | - | 237 |
| snake_abs_exit_conv | 218,906 | +9.45% | 2 | 50% | 345 |
| snake_abs_exit | 217,882 | +8.94% | 2 | 50% | 345 |
| snake_abs | 215,822 | +7.91% | 1 | 100% | 255 |
| snake_abs_conv | 215,653 | +7.83% | 1 | 100% | 255 |
| intraweek | 214,593 | +7.30% | 30 | 53% | 3,302 |
| oracle | 213,296 | +6.65% | 0 | - | 233 |
| intramonth | 211,849 | +5.92% | 0 | - | 235 |
| random_hold | 208,192 | +4.10% | 10 | 70% | 733 |
| snake_viper_wild | 207,422 | +3.71% | 10 | 50% | 1,825 |
| snake_anaconda | 206,532 | +3.27% | 3 | 33% | 374 |
| snake_viper_tick | 203,873 | +1.94% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,161 | +1.58% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,067 | -6.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,232 (-3.88%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,409 | +1.18% |
| benchmark_smallcap | +2,354 | +1.17% |
| snake_abs | +2,197 | +1.03% |
| snake_abs_conv | +2,195 | +1.03% |
| snake_abs_exit_conv | +1,755 | +0.81% |
| snake_abs_exit | +1,720 | +0.80% |
| unified | +1,694 | +0.77% |
| intraweek | +1,460 | +0.69% |
| oracle | +1,293 | +0.61% |
| random_hold | +1,081 | +0.52% |
| intramonth | +853 | +0.40% |
| benchmark | +834 | +0.38% |
| snake_viper_wild | +681 | +0.33% |
| snake_viper_tick | +665 | +0.33% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,518 | -1.86% |

Average per day so far: unified Rs +672, snake_abs_exit_conv Rs +652, benchmark Rs +628, snake_abs_exit Rs +617, snake_abs_conv Rs +540, snake_abs Rs +527, intraweek Rs +456, oracle Rs +416, intramonth Rs +370, snake_viper_wild Rs +309, random_hold Rs +256, snake_anaconda Rs +242, snake_viper_tick Rs +184, benchmark_smallcap Rs +113, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -435

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.