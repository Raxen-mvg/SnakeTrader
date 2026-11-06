# Paper trading report

Updated 2026-11-06 11:49 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,898 | +7.45% | 0 | - | 236 |
| benchmark | 214,642 | +7.32% | 0 | - | 237 |
| intraweek | 210,842 | +5.42% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,173 | +4.59% | 1 | 100% | 255 |
| snake_abs_exit | 208,961 | +4.48% | 1 | 100% | 260 |
| intramonth | 206,945 | +3.47% | 0 | - | 235 |
| snake_abs | 206,132 | +3.07% | 1 | 100% | 255 |
| snake_abs_conv | 205,963 | +2.98% | 1 | 100% | 255 |
| oracle | 204,611 | +2.31% | 0 | - | 233 |
| random_hold | 203,346 | +1.67% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,552 | -1.72% | 3 | 33% | 374 |
| snake_viper_wild | 195,508 | -2.25% | 3 | 33% | 702 |
| benchmark_smallcap | 194,921 | -2.54% | 0 | - | 237 |
| snake_viper_tick | 192,196 | -3.90% | 2 | 0% | 532 |
| gold | 190,078 | -4.96% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,267 (-6.37%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,424 | +0.68% |
| benchmark | +872 | +0.41% |
| oracle | +539 | +0.26% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -978 | -0.48% |
| intramonth | -1,004 | -0.48% |
| unified | -1,086 | -0.50% |
| benchmark_smallcap | -3,767 | -1.90% |
| gold | -4,143 | -2.13% |
| snake_abs | -5,557 | -2.62% |
| snake_abs_conv | -5,582 | -2.64% |
| snake_abs_exit_conv | -5,630 | -2.62% |
| snake_abs_exit | -5,698 | -2.65% |
| snake_anaconda | -5,927 | -2.93% |
| snake_viper_tick | -8,942 | -4.45% |
| snake_viper_wild | -9,148 | -4.47% |

Average per day so far: unified Rs +514, benchmark Rs +505, intraweek Rs +374, snake_abs_exit_conv Rs +353, snake_abs_exit Rs +345, intramonth Rs +239, snake_abs_conv Rs +229, snake_abs Rs +227, oracle Rs +159, random_hold Rs +115, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -144, benchmark_smallcap Rs -203, snake_viper_wild Rs -214, gold Rs -342, snake_nonews Rs -411, snake_viper_tick Rs -434, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.