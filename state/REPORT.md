# Paper trading report

Updated 2026-11-19 15:25 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,595 | +12.30% | 0 | - | 236 |
| benchmark | 222,384 | +11.19% | 0 | - | 237 |
| intramonth | 214,022 | +7.01% | 0 | - | 235 |
| snake_abs_exit | 213,256 | +6.63% | 2 | 50% | 345 |
| intraweek | 212,997 | +6.50% | 35 | 54% | 3,851 |
| oracle | 212,306 | +6.15% | 0 | - | 233 |
| snake_abs_exit_conv | 210,926 | +5.46% | 2 | 50% | 345 |
| snake_abs | 209,320 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,191 | +4.59% | 1 | 100% | 255 |
| random_hold | 208,500 | +4.25% | 10 | 70% | 733 |
| snake_viper_wild | 207,528 | +3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,982 | +1.99% | 15 | 47% | 2,625 |
| snake_anaconda | 203,352 | +1.68% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,457 | +0.73% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,855 | -12.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,034 (-3.98%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,130 | +1.07% |
| benchmark | +2,088 | +0.95% |
| unified | +1,983 | +0.89% |
| intramonth | +1,749 | +0.82% |
| random_hold | +1,567 | +0.76% |
| oracle | +1,510 | +0.72% |
| intraweek | +1,157 | +0.55% |
| snake_viper_wild | +488 | +0.24% |
| snake_viper_tick | +478 | +0.23% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -116 | -0.06% |
| snake_abs_conv | -134 | -0.06% |
| snake_abs_exit | -776 | -0.36% |
| snake_anaconda | -1,049 | -0.51% |
| snake_abs_exit_conv | -1,457 | -0.69% |
| gold | -2,466 | -1.39% |

Average per day so far: unified Rs +665, benchmark Rs +605, snake_abs_exit Rs +390, intramonth Rs +379, intraweek Rs +351, oracle Rs +333, snake_abs_exit_conv Rs +321, snake_abs_conv Rs +270, snake_abs Rs +266, snake_viper_wild Rs +260, random_hold Rs +230, snake_viper_tick Rs +153, snake_anaconda Rs +105, nifty_calls Rs +50, benchmark_smallcap Rs +44, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.