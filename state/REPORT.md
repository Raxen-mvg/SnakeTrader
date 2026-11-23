# Paper trading report

Updated 2026-11-23 13:22 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,947 | +11.97% | 0 | - | 236 |
| benchmark | 222,445 | +11.22% | 0 | - | 237 |
| intraweek | 212,201 | +6.10% | 40 | 55% | 4,400 |
| intramonth | 212,118 | +6.06% | 0 | - | 235 |
| oracle | 211,605 | +5.80% | 0 | - | 233 |
| random_hold | 208,774 | +4.39% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,833 | +3.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,424 | +2.71% | 2 | 50% | 345 |
| snake_abs | 204,293 | +2.15% | 1 | 100% | 255 |
| snake_abs_conv | 204,126 | +2.06% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,692 | +0.35% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,237 | -0.38% | 0 | - | 237 |
| snake_anaconda | 197,908 | -1.05% | 3 | 33% | 374 |
| snake_viper_tick | 197,270 | -1.36% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,055 | -14.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,025 (-4.99%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,006 | +1.19% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -873 | -0.41% |
| snake_abs_exit_conv | -1,193 | -0.58% |
| snake_abs | -1,627 | -0.79% |
| snake_abs_conv | -1,657 | -0.81% |
| benchmark_smallcap | -1,670 | -0.83% |
| snake_abs_exit | -1,729 | -0.83% |
| random_hold | -1,985 | -0.94% |
| snake_anaconda | -1,998 | -1.00% |
| snake_viper_tick | -2,102 | -1.05% |
| snake_viper_wild | -2,137 | -1.05% |
| unified | -2,235 | -0.99% |
| benchmark | -2,693 | -1.20% |
| intramonth | -2,886 | -1.34% |
| intraweek | -3,511 | -1.63% |

Average per day so far: unified Rs +614, benchmark Rs +576, intraweek Rs +313, intramonth Rs +311, oracle Rs +298, random_hold Rs +225, snake_abs_exit Rs +190, snake_abs_exit_conv Rs +151, snake_abs Rs +116, snake_abs_conv Rs +115, nifty_calls Rs +47, snake_viper_wild Rs +22, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -22, snake_anaconda Rs -62, snake_viper_tick Rs -98, snake_nonews Rs -300, snake Rs -320, gold Rs -768

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.