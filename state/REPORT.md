# Paper trading report

Updated 2026-11-18 13:52 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,859 | +11.43% | 0 | - | 236 |
| benchmark | 220,020 | +10.01% | 0 | - | 237 |
| intramonth | 212,611 | +6.31% | 0 | - | 235 |
| snake_abs_exit | 212,547 | +6.27% | 2 | 50% | 345 |
| intraweek | 212,544 | +6.27% | 35 | 54% | 3,851 |
| oracle | 212,351 | +6.18% | 0 | - | 233 |
| snake_abs_exit_conv | 210,762 | +5.38% | 2 | 50% | 345 |
| snake_abs | 207,943 | +3.97% | 1 | 100% | 255 |
| snake_abs_conv | 207,804 | +3.90% | 1 | 100% | 255 |
| random_hold | 207,202 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 206,478 | +3.24% | 16 | 50% | 2,827 |
| snake_viper_tick | 202,953 | +1.48% | 15 | 47% | 2,625 |
| snake_anaconda | 202,879 | +1.44% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,383 | -0.31% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 176,992 | -11.50% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,196 (-4.40%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,421 | +0.64% |
| intramonth | +1,069 | +0.51% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -135 | -0.06% |
| snake_abs_exit | -594 | -0.28% |
| snake_abs | -615 | -0.29% |
| snake_abs_conv | -615 | -0.29% |
| intraweek | -778 | -0.36% |
| snake_abs_exit_conv | -812 | -0.38% |
| snake_anaconda | -1,176 | -0.58% |
| benchmark_smallcap | -1,188 | -0.59% |
| random_hold | -1,230 | -0.59% |
| benchmark | -1,584 | -0.71% |
| snake_viper_tick | -2,883 | -1.40% |
| snake_viper_wild | -2,937 | -1.40% |
| gold | -3,732 | -2.06% |

Average per day so far: unified Rs +635, benchmark Rs +556, snake_abs_exit Rs +380, intramonth Rs +350, intraweek Rs +348, oracle Rs +343, snake_abs_exit_conv Rs +326, snake_abs_conv Rs +236, snake_abs Rs +234, snake_viper_wild Rs +231, random_hold Rs +200, snake_viper_tick Rs +118, snake_anaconda Rs +93, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -19, snake_nonews Rs -326, snake Rs -347, gold Rs -639

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.