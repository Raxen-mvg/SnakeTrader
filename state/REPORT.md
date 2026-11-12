# Paper trading report

Updated 2026-11-12 13:03 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,634 | +10.82% | 0 | - | 236 |
| benchmark | 220,265 | +10.13% | 0 | - | 237 |
| snake_abs_exit_conv | 219,064 | +9.53% | 2 | 50% | 345 |
| snake_abs_exit | 217,985 | +8.99% | 2 | 50% | 345 |
| snake_abs | 215,934 | +7.97% | 1 | 100% | 255 |
| snake_abs_conv | 215,764 | +7.88% | 1 | 100% | 255 |
| intraweek | 214,691 | +7.34% | 30 | 53% | 3,302 |
| oracle | 213,423 | +6.71% | 0 | - | 233 |
| intramonth | 211,982 | +5.99% | 0 | - | 235 |
| random_hold | 208,147 | +4.07% | 10 | 70% | 733 |
| snake_viper_wild | 207,498 | +3.75% | 10 | 50% | 1,825 |
| snake_anaconda | 206,643 | +3.32% | 3 | 33% | 374 |
| snake_viper_tick | 203,948 | +1.97% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,217 | +1.61% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,919 | -7.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,326 (-3.84%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,520 | +1.23% |
| benchmark_smallcap | +2,410 | +1.20% |
| snake_abs | +2,309 | +1.08% |
| snake_abs_conv | +2,306 | +1.08% |
| snake_abs_exit_conv | +1,913 | +0.88% |
| snake_abs_exit | +1,822 | +0.84% |
| unified | +1,820 | +0.83% |
| intraweek | +1,558 | +0.73% |
| oracle | +1,420 | +0.67% |
| random_hold | +1,037 | +0.50% |
| benchmark | +1,002 | +0.46% |
| intramonth | +986 | +0.47% |
| snake_viper_wild | +757 | +0.37% |
| snake_viper_tick | +739 | +0.36% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,666 | -1.93% |

Average per day so far: unified Rs +676, snake_abs_exit_conv Rs +657, benchmark Rs +633, snake_abs_exit Rs +620, snake_abs_conv Rs +544, snake_abs Rs +531, intraweek Rs +459, oracle Rs +419, intramonth Rs +374, snake_viper_wild Rs +312, random_hold Rs +255, snake_anaconda Rs +246, snake_viper_tick Rs +188, benchmark_smallcap Rs +115, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -440

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.