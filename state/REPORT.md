# Paper trading report

Updated 2026-11-12 14:16 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,872 | +10.44% | 0 | - | 236 |
| benchmark | 220,502 | +10.25% | 0 | - | 237 |
| snake_abs_exit_conv | 218,306 | +9.15% | 2 | 50% | 345 |
| snake_abs_exit | 217,190 | +8.60% | 2 | 50% | 345 |
| snake_abs | 215,414 | +7.71% | 1 | 100% | 255 |
| snake_abs_conv | 215,237 | +7.62% | 1 | 100% | 255 |
| intraweek | 214,431 | +7.21% | 30 | 53% | 3,302 |
| oracle | 212,831 | +6.42% | 0 | - | 233 |
| intramonth | 211,465 | +5.73% | 0 | - | 235 |
| random_hold | 207,978 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 206,624 | +3.31% | 10 | 50% | 1,825 |
| snake_anaconda | 206,029 | +3.01% | 3 | 33% | 374 |
| snake_viper_tick | 203,090 | +1.54% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,278 | -7.36% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,863 (-4.07%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,107 | +1.05% |
| snake_anaconda | +1,906 | +0.93% |
| snake_abs | +1,790 | +0.84% |
| snake_abs_conv | +1,779 | +0.83% |
| intraweek | +1,298 | +0.61% |
| benchmark | +1,239 | +0.56% |
| snake_abs_exit_conv | +1,154 | +0.53% |
| unified | +1,058 | +0.48% |
| snake_abs_exit | +1,028 | +0.48% |
| random_hold | +868 | +0.42% |
| oracle | +828 | +0.39% |
| intramonth | +469 | +0.22% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_wild | -118 | -0.06% |
| snake_viper_tick | -119 | -0.06% |
| gold | -4,307 | -2.27% |

Average per day so far: unified Rs +652, benchmark Rs +641, snake_abs_exit_conv Rs +631, snake_abs_exit Rs +593, snake_abs_conv Rs +525, snake_abs Rs +514, intraweek Rs +451, oracle Rs +401, intramonth Rs +358, snake_viper_wild Rs +276, random_hold Rs +249, snake_anaconda Rs +223, snake_viper_tick Rs +147, benchmark_smallcap Rs +104, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -460

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.