# Paper trading report

Updated 2026-11-06 11:10 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 214,672 | +7.34% | 0 | - | 237 |
| unified | 214,655 | +7.33% | 0 | - | 236 |
| intraweek | 211,507 | +5.75% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,606 | +4.80% | 1 | 100% | 255 |
| snake_abs_exit | 209,397 | +4.70% | 1 | 100% | 260 |
| intramonth | 206,767 | +3.38% | 0 | - | 235 |
| snake_abs | 206,560 | +3.28% | 1 | 100% | 255 |
| snake_abs_conv | 206,393 | +3.20% | 1 | 100% | 255 |
| oracle | 204,872 | +2.44% | 0 | - | 233 |
| random_hold | 203,520 | +1.76% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,942 | -1.53% | 3 | 33% | 374 |
| snake_viper_wild | 196,058 | -1.97% | 3 | 33% | 702 |
| benchmark_smallcap | 194,776 | -2.61% | 0 | - | 237 |
| snake_viper_tick | 192,737 | -3.63% | 2 | 0% | 532 |
| gold | 189,898 | -5.05% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,465 (-6.27%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,088 | +1.00% |
| benchmark | +903 | +0.42% |
| oracle | +800 | +0.39% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -803 | -0.39% |
| intramonth | -1,182 | -0.57% |
| unified | -1,329 | -0.61% |
| benchmark_smallcap | -3,912 | -1.97% |
| gold | -4,324 | -2.23% |
| snake_abs | -5,129 | -2.42% |
| snake_abs_conv | -5,152 | -2.44% |
| snake_abs_exit_conv | -5,197 | -2.42% |
| snake_abs_exit | -5,261 | -2.45% |
| snake_anaconda | -5,537 | -2.73% |
| snake_viper_tick | -8,401 | -4.18% |
| snake_viper_wild | -8,598 | -4.20% |

Average per day so far: benchmark Rs +506, unified Rs +505, intraweek Rs +397, snake_abs_exit_conv Rs +369, snake_abs_exit Rs +361, snake_abs_conv Rs +246, snake_abs Rs +243, intramonth Rs +233, oracle Rs +168, random_hold Rs +121, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -127, snake_viper_wild Rs -188, benchmark_smallcap Rs -209, gold Rs -348, snake_viper_tick Rs -404, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.