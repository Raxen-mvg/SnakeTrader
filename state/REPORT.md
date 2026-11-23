# Paper trading report

Updated 2026-11-23 11:06 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,167 | +12.08% | 0 | - | 236 |
| benchmark | 223,057 | +11.53% | 0 | - | 237 |
| intraweek | 212,385 | +6.19% | 40 | 55% | 4,400 |
| intramonth | 212,303 | +6.15% | 0 | - | 235 |
| oracle | 211,035 | +5.52% | 0 | - | 233 |
| random_hold | 209,782 | +4.89% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,905 | +3.45% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,957 | +2.98% | 2 | 50% | 345 |
| snake_abs | 204,239 | +2.12% | 1 | 100% | 255 |
| snake_abs_conv | 204,084 | +2.04% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,548 | +0.27% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,192 | -0.40% | 0 | - | 237 |
| snake_anaconda | 197,894 | -1.05% | 3 | 33% | 374 |
| snake_viper_tick | 197,129 | -1.44% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,005 | -15.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,174 (-4.91%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,956 | +1.16% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit_conv | -660 | -0.32% |
| random_hold | -977 | -0.46% |
| oracle | -1,444 | -0.68% |
| snake_abs_exit | -1,657 | -0.79% |
| snake_abs | -1,681 | -0.82% |
| snake_abs_conv | -1,699 | -0.83% |
| benchmark_smallcap | -1,715 | -0.85% |
| snake_anaconda | -2,012 | -1.01% |
| unified | -2,014 | -0.89% |
| benchmark | -2,081 | -0.92% |
| snake_viper_tick | -2,243 | -1.12% |
| snake_viper_wild | -2,281 | -1.12% |
| intramonth | -2,701 | -1.26% |
| intraweek | -3,327 | -1.54% |

Average per day so far: unified Rs +620, benchmark Rs +591, intraweek Rs +318, intramonth Rs +315, oracle Rs +283, random_hold Rs +251, snake_abs_exit Rs +192, snake_abs_exit_conv Rs +165, snake_abs Rs +115, snake_abs_conv Rs +113, nifty_calls Rs +47, snake_viper_wild Rs +18, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -23, snake_anaconda Rs -62, snake_viper_tick Rs -103, snake_nonews Rs -300, snake Rs -320, gold Rs -769

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.