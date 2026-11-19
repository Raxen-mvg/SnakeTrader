# Paper trading report

Updated 2026-11-19 09:35 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,662 | +11.83% | 0 | - | 236 |
| benchmark | 219,362 | +9.68% | 0 | - | 237 |
| intramonth | 213,675 | +6.84% | 0 | - | 235 |
| snake_abs_exit | 213,267 | +6.63% | 2 | 50% | 345 |
| intraweek | 211,826 | +5.91% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,631 | +5.82% | 2 | 50% | 345 |
| oracle | 211,199 | +5.60% | 0 | - | 233 |
| snake_abs | 209,026 | +4.51% | 1 | 100% | 255 |
| snake_abs_conv | 208,903 | +4.45% | 1 | 100% | 255 |
| snake_viper_wild | 207,855 | +3.93% | 16 | 50% | 2,827 |
| random_hold | 207,541 | +3.77% | 10 | 70% | 733 |
| snake_viper_tick | 204,302 | +2.15% | 15 | 47% | 2,625 |
| snake_anaconda | 203,818 | +1.91% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,607 | -0.20% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,855 | -12.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,268 (-4.37%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| intramonth | +1,401 | +0.66% |
| unified | +1,050 | +0.47% |
| snake_viper_wild | +816 | +0.39% |
| snake_viper_tick | +799 | +0.39% |
| random_hold | +609 | +0.29% |
| oracle | +403 | +0.19% |
| benchmark_smallcap | +280 | +0.14% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraweek | -13 | -0.01% |
| snake_abs | -410 | -0.20% |
| snake_abs_conv | -422 | -0.20% |
| snake_anaconda | -583 | -0.28% |
| snake_abs_exit_conv | -752 | -0.35% |
| snake_abs_exit | -765 | -0.36% |
| benchmark | -933 | -0.42% |
| gold | -2,466 | -1.39% |

Average per day so far: unified Rs +640, benchmark Rs +523, snake_abs_exit Rs +390, intramonth Rs +370, snake_abs_exit_conv Rs +342, intraweek Rs +320, oracle Rs +303, snake_viper_wild Rs +271, snake_abs_conv Rs +262, snake_abs Rs +258, random_hold Rs +204, snake_viper_tick Rs +165, snake_anaconda Rs +119, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -12, snake_nonews Rs -317, snake Rs -337, gold Rs -680

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.