# Paper trading report

Updated 2026-11-23 12:55 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,931 | +11.97% | 0 | - | 236 |
| benchmark | 222,506 | +11.25% | 0 | - | 237 |
| intraweek | 212,335 | +6.17% | 40 | 55% | 4,400 |
| intramonth | 212,025 | +6.01% | 0 | - | 235 |
| oracle | 211,740 | +5.87% | 0 | - | 233 |
| random_hold | 208,548 | +4.27% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,774 | +3.39% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,478 | +2.74% | 2 | 50% | 345 |
| snake_abs | 204,332 | +2.17% | 1 | 100% | 255 |
| snake_abs_conv | 204,170 | +2.08% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,884 | +0.44% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,405 | -0.30% | 0 | - | 237 |
| snake_anaconda | 197,964 | -1.02% | 3 | 33% | 374 |
| snake_viper_tick | 197,458 | -1.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,466 | -14.77% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,030 (-4.99%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,417 | +1.44% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -739 | -0.35% |
| snake_abs_exit_conv | -1,139 | -0.55% |
| benchmark_smallcap | -1,502 | -0.75% |
| snake_abs | -1,588 | -0.77% |
| snake_abs_conv | -1,613 | -0.78% |
| snake_abs_exit | -1,789 | -0.86% |
| snake_viper_tick | -1,914 | -0.96% |
| snake_anaconda | -1,942 | -0.97% |
| snake_viper_wild | -1,945 | -0.96% |
| random_hold | -2,211 | -1.05% |
| unified | -2,251 | -0.99% |
| benchmark | -2,632 | -1.17% |
| intramonth | -2,979 | -1.39% |
| intraweek | -3,377 | -1.57% |

Average per day so far: unified Rs +614, benchmark Rs +577, intraweek Rs +316, intramonth Rs +308, oracle Rs +301, random_hold Rs +219, snake_abs_exit Rs +188, snake_abs_exit_conv Rs +152, snake_abs Rs +117, snake_abs_conv Rs +116, nifty_calls Rs +47, snake_viper_wild Rs +29, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -17, snake_anaconda Rs -60, snake_viper_tick Rs -91, snake_nonews Rs -300, snake Rs -320, gold Rs -757

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.