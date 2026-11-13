# Paper trading report

Updated 2026-11-13 13:22 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,095 | +10.05% | 0 | - | 236 |
| benchmark | 219,431 | +9.71% | 0 | - | 237 |
| snake_abs_exit | 216,748 | +8.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,389 | +8.20% | 2 | 50% | 345 |
| intraweek | 215,697 | +7.85% | 30 | 53% | 3,302 |
| oracle | 213,020 | +6.51% | 0 | - | 233 |
| snake_abs | 212,179 | +6.09% | 1 | 100% | 255 |
| snake_abs_conv | 212,010 | +6.00% | 1 | 100% | 255 |
| intramonth | 210,774 | +5.39% | 0 | - | 235 |
| random_hold | 207,129 | +3.56% | 10 | 70% | 733 |
| snake_viper_wild | 205,580 | +2.79% | 14 | 50% | 2,496 |
| snake_anaconda | 204,426 | +2.21% | 3 | 33% | 374 |
| benchmark_smallcap | 202,690 | +1.34% | 0 | - | 237 |
| snake_viper_tick | 202,063 | +1.03% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,831 | -8.08% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,681 (-4.16%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,039 | +0.48% |
| snake_viper_wild | +287 | +0.14% |
| snake_viper_tick | +282 | +0.14% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -95 | -0.04% |
| benchmark_smallcap | -516 | -0.25% |
| unified | -602 | -0.27% |
| snake_abs_exit | -694 | -0.32% |
| intramonth | -819 | -0.39% |
| random_hold | -925 | -0.45% |
| benchmark | -1,117 | -0.51% |
| gold | -1,480 | -0.80% |
| snake_anaconda | -1,501 | -0.73% |
| snake_abs_exit_conv | -2,285 | -1.04% |
| snake_abs_conv | -3,525 | -1.64% |
| snake_abs | -3,533 | -1.64% |

Average per day so far: unified Rs +609, benchmark Rs +589, snake_abs_exit Rs +558, snake_abs_exit_conv Rs +546, intraweek Rs +476, snake_abs_conv Rs +400, oracle Rs +395, snake_abs Rs +393, intramonth Rs +326, snake_viper_wild Rs +223, random_hold Rs +216, snake_anaconda Rs +158, snake_viper_tick Rs +94, benchmark_smallcap Rs +93, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -490

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.