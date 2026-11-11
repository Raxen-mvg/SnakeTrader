# Paper trading report

Updated 2026-11-11 13:27 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,488 | +10.24% | 0 | - | 236 |
| benchmark | 220,463 | +10.23% | 0 | - | 237 |
| snake_abs_exit_conv | 217,912 | +8.96% | 2 | 50% | 345 |
| snake_abs_exit | 216,843 | +8.42% | 2 | 50% | 345 |
| snake_abs | 214,302 | +7.15% | 1 | 100% | 255 |
| snake_abs_conv | 214,146 | +7.07% | 1 | 100% | 255 |
| intraweek | 213,594 | +6.80% | 30 | 53% | 3,302 |
| oracle | 211,950 | +5.97% | 0 | - | 233 |
| intramonth | 211,455 | +5.73% | 0 | - | 235 |
| random_hold | 207,193 | +3.60% | 9 | 67% | 709 |
| snake_viper_wild | 205,506 | +2.75% | 10 | 50% | 1,825 |
| snake_anaconda | 204,796 | +2.40% | 3 | 33% | 374 |
| snake_viper_tick | 201,999 | +1.00% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,233 | +0.62% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,367 (-4.32%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,076 | +4.09% |
| snake_viper_tick | +7,922 | +4.08% |
| snake_abs_exit_conv | +6,003 | +2.83% |
| snake_anaconda | +5,329 | +2.67% |
| snake_abs_exit | +4,859 | +2.29% |
| snake_abs_conv | +4,668 | +2.23% |
| snake_abs | +4,655 | +2.22% |
| benchmark_smallcap | +3,060 | +1.54% |
| benchmark | +2,371 | +1.09% |
| random_hold | +2,233 | +1.09% |
| oracle | +2,032 | +0.97% |
| intramonth | +846 | +0.40% |
| unified | +741 | +0.34% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -948 | -0.44% |
| gold | -2,236 | -1.16% |

Average per day so far: unified Rs +661, benchmark Rs +660, snake_abs_exit_conv Rs +640, snake_abs_exit Rs +602, snake_abs_conv Rs +505, snake_abs Rs +493, intraweek Rs +439, oracle Rs +385, intramonth Rs +370, snake_viper_wild Rs +239, random_hold Rs +232, snake_anaconda Rs +184, snake_viper_tick Rs +100, nifty_calls Rs +59, benchmark_smallcap Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -326, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.