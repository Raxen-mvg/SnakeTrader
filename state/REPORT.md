# Paper trading report

Updated 2026-11-19 13:01 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,723 | +11.86% | 0 | - | 236 |
| benchmark | 221,710 | +10.86% | 0 | - | 237 |
| intramonth | 213,299 | +6.65% | 0 | - | 235 |
| snake_abs_exit | 212,573 | +6.29% | 2 | 50% | 345 |
| intraweek | 211,756 | +5.88% | 35 | 54% | 3,851 |
| oracle | 211,611 | +5.80% | 0 | - | 233 |
| snake_abs_exit_conv | 210,724 | +5.36% | 2 | 50% | 345 |
| snake_abs | 208,235 | +4.12% | 1 | 100% | 255 |
| snake_abs_conv | 208,097 | +4.05% | 1 | 100% | 255 |
| random_hold | 207,708 | +3.85% | 10 | 70% | 733 |
| snake_viper_wild | 207,633 | +3.82% | 16 | 50% | 2,827 |
| snake_viper_tick | 204,085 | +2.04% | 15 | 47% | 2,625 |
| snake_anaconda | 203,027 | +1.51% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,706 | +0.35% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,135 | -12.43% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,295 (-4.35%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,415 | +0.64% |
| benchmark_smallcap | +1,379 | +0.69% |
| unified | +1,112 | +0.50% |
| intramonth | +1,026 | +0.48% |
| oracle | +815 | +0.39% |
| random_hold | +775 | +0.38% |
| snake_viper_wild | +594 | +0.29% |
| snake_viper_tick | +582 | +0.29% |
| intraday | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -83 | -0.04% |
| snake_abs | -1,201 | -0.57% |
| snake_abs_conv | -1,228 | -0.59% |
| snake_anaconda | -1,374 | -0.67% |
| snake_abs_exit | -1,459 | -0.68% |
| snake_abs_exit_conv | -1,660 | -0.78% |
| gold | -2,187 | -1.23% |

Average per day so far: unified Rs +641, benchmark Rs +587, snake_abs_exit Rs +370, intramonth Rs +359, intraweek Rs +318, snake_abs_exit_conv Rs +315, oracle Rs +314, snake_viper_wild Rs +263, snake_abs_conv Rs +238, snake_abs Rs +235, random_hold Rs +208, snake_viper_tick Rs +157, snake_anaconda Rs +95, nifty_calls Rs +50, benchmark_smallcap Rs +21, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -672

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.