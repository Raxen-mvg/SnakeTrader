# Paper trading report

Updated 2026-11-19 11:50 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,753 | +11.88% | 0 | - | 236 |
| benchmark | 221,412 | +10.71% | 0 | - | 237 |
| intramonth | 213,297 | +6.65% | 0 | - | 235 |
| snake_abs_exit | 213,190 | +6.59% | 2 | 50% | 345 |
| intraweek | 211,873 | +5.94% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 211,339 | +5.67% | 2 | 50% | 345 |
| oracle | 211,021 | +5.51% | 0 | - | 233 |
| snake_abs | 208,737 | +4.37% | 1 | 100% | 255 |
| snake_abs_conv | 208,607 | +4.30% | 1 | 100% | 255 |
| random_hold | 207,684 | +3.84% | 10 | 70% | 733 |
| snake_viper_wild | 207,220 | +3.61% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,681 | +1.84% | 15 | 47% | 2,625 |
| snake_anaconda | 202,986 | +1.49% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,616 | +0.31% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 175,315 | -12.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,206 (-4.40%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,289 | +0.65% |
| unified | +1,142 | +0.51% |
| benchmark | +1,117 | +0.51% |
| intramonth | +1,024 | +0.48% |
| random_hold | +752 | +0.36% |
| oracle | +225 | +0.11% |
| snake_viper_wild | +181 | +0.09% |
| snake_viper_tick | +178 | +0.09% |
| intraweek | +34 | +0.02% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_abs | -699 | -0.33% |
| snake_abs_conv | -718 | -0.34% |
| snake_abs_exit | -842 | -0.39% |
| snake_abs_exit_conv | -1,044 | -0.49% |
| snake_anaconda | -1,415 | -0.69% |
| gold | -2,006 | -1.13% |

Average per day so far: unified Rs +642, benchmark Rs +579, snake_abs_exit Rs +388, intramonth Rs +359, snake_abs_exit_conv Rs +334, intraweek Rs +321, oracle Rs +298, snake_abs_conv Rs +253, snake_abs Rs +250, snake_viper_wild Rs +249, random_hold Rs +208, snake_viper_tick Rs +142, snake_anaconda Rs +93, nifty_calls Rs +50, benchmark_smallcap Rs +19, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -317, snake Rs -337, gold Rs -667

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.