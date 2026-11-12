# Paper trading report

Updated 2026-11-12 13:52 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,086 | +10.54% | 0 | - | 236 |
| benchmark | 220,456 | +10.23% | 0 | - | 237 |
| snake_abs_exit_conv | 218,422 | +9.21% | 2 | 50% | 345 |
| snake_abs_exit | 217,238 | +8.62% | 2 | 50% | 345 |
| snake_abs | 215,408 | +7.70% | 1 | 100% | 255 |
| snake_abs_conv | 215,236 | +7.62% | 1 | 100% | 255 |
| intraweek | 214,464 | +7.23% | 30 | 53% | 3,302 |
| oracle | 212,988 | +6.49% | 0 | - | 233 |
| intramonth | 211,642 | +5.82% | 0 | - | 235 |
| random_hold | 207,974 | +3.99% | 10 | 70% | 733 |
| snake_viper_wild | 206,549 | +3.27% | 10 | 50% | 1,825 |
| snake_anaconda | 206,152 | +3.08% | 3 | 33% | 374 |
| snake_viper_tick | 203,017 | +1.51% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,746 | +1.37% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,886 | -7.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,955 (-4.02%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,029 | +0.99% |
| benchmark_smallcap | +1,939 | +0.97% |
| snake_abs | +1,784 | +0.83% |
| snake_abs_conv | +1,778 | +0.83% |
| intraweek | +1,331 | +0.62% |
| unified | +1,272 | +0.58% |
| snake_abs_exit_conv | +1,270 | +0.58% |
| benchmark | +1,193 | +0.54% |
| snake_abs_exit | +1,076 | +0.50% |
| oracle | +985 | +0.47% |
| random_hold | +864 | +0.42% |
| intramonth | +645 | +0.31% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -192 | -0.09% |
| snake_viper_wild | -193 | -0.09% |
| gold | -3,699 | -1.95% |

Average per day so far: unified Rs +659, benchmark Rs +639, snake_abs_exit_conv Rs +635, snake_abs_exit Rs +594, snake_abs_conv Rs +525, snake_abs Rs +514, intraweek Rs +452, oracle Rs +406, intramonth Rs +364, snake_viper_wild Rs +273, random_hold Rs +249, snake_anaconda Rs +228, snake_viper_tick Rs +144, benchmark_smallcap Rs +98, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -441

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.