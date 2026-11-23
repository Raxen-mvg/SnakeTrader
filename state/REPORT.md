# Paper trading report

Updated 2026-11-23 13:31 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,882 | +11.94% | 0 | - | 236 |
| benchmark | 222,368 | +11.18% | 0 | - | 237 |
| intramonth | 212,060 | +6.03% | 0 | - | 235 |
| intraweek | 211,916 | +5.96% | 40 | 55% | 4,400 |
| oracle | 211,603 | +5.80% | 0 | - | 233 |
| random_hold | 208,826 | +4.41% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,504 | +3.25% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,156 | +2.58% | 2 | 50% | 345 |
| snake_abs | 204,032 | +2.02% | 1 | 100% | 255 |
| snake_abs_conv | 203,863 | +1.93% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,553 | +0.28% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,595 | -1.20% | 3 | 33% | 374 |
| snake_viper_tick | 197,133 | -1.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,824 | -15.09% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,934 (-5.03%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,776 | +1.06% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -876 | -0.41% |
| snake_abs_exit_conv | -1,460 | -0.71% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_abs | -1,888 | -0.92% |
| snake_abs_conv | -1,920 | -0.93% |
| random_hold | -1,934 | -0.92% |
| snake_abs_exit | -2,058 | -0.99% |
| snake_viper_tick | -2,238 | -1.12% |
| snake_viper_wild | -2,276 | -1.12% |
| unified | -2,299 | -1.02% |
| snake_anaconda | -2,310 | -1.16% |
| benchmark | -2,769 | -1.23% |
| intramonth | -2,944 | -1.37% |
| intraweek | -3,796 | -1.76% |

Average per day so far: unified Rs +612, benchmark Rs +574, intramonth Rs +309, intraweek Rs +306, oracle Rs +298, random_hold Rs +226, snake_abs_exit Rs +181, snake_abs_exit_conv Rs +143, snake_abs Rs +109, snake_abs_conv Rs +107, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -71, snake_viper_tick Rs -102, snake_nonews Rs -300, snake Rs -320, gold Rs -774

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.