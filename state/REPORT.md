# Paper trading report

Updated 2026-11-17 11:14 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,174 | +11.09% | 0 | - | 236 |
| benchmark | 221,718 | +10.86% | 0 | - | 237 |
| snake_abs_exit | 215,866 | +7.93% | 2 | 50% | 345 |
| intraweek | 213,998 | +7.00% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,841 | +6.92% | 2 | 50% | 345 |
| oracle | 212,798 | +6.40% | 0 | - | 233 |
| intramonth | 212,200 | +6.10% | 0 | - | 235 |
| snake_abs | 210,275 | +5.14% | 1 | 100% | 255 |
| snake_abs_conv | 210,127 | +5.06% | 1 | 100% | 255 |
| random_hold | 208,047 | +4.02% | 10 | 70% | 733 |
| snake_viper_wild | 207,356 | +3.68% | 14 | 50% | 2,496 |
| snake_anaconda | 205,697 | +2.85% | 3 | 33% | 374 |
| snake_viper_tick | 203,811 | +1.91% | 13 | 46% | 2,299 |
| benchmark_smallcap | 202,320 | +1.16% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,612 | -9.19% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,648 (-4.18%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,732 | +1.29% |
| benchmark | +1,637 | +0.74% |
| benchmark_smallcap | +1,491 | +0.74% |
| snake_abs_exit | +1,457 | +0.68% |
| snake_viper_wild | +1,212 | +0.59% |
| snake_viper_tick | +1,191 | +0.59% |
| oracle | +775 | +0.36% |
| unified | +736 | +0.33% |
| gold | +658 | +0.36% |
| snake_abs_exit_conv | +624 | +0.29% |
| snake_anaconda | +594 | +0.29% |
| intramonth | +581 | +0.28% |
| random_hold | +254 | +0.12% |
| snake_abs | +142 | +0.07% |
| snake_abs_conv | +137 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +634, benchmark Rs +621, snake_abs_exit Rs +496, snake_abs_exit_conv Rs +433, intraweek Rs +400, oracle Rs +366, intramonth Rs +349, snake_abs_conv Rs +316, snake_abs Rs +311, snake_viper_wild Rs +272, random_hold Rs +230, snake_anaconda Rs +190, snake_viper_tick Rs +159, benchmark_smallcap Rs +75, nifty_calls Rs +52, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -525

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.