# Paper trading report

Updated 2026-11-17 12:49 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,993 | +11.00% | 0 | - | 237 |
| unified | 221,819 | +10.91% | 0 | - | 236 |
| snake_abs_exit | 214,203 | +7.10% | 2 | 50% | 345 |
| intraweek | 213,972 | +6.99% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 212,480 | +6.24% | 2 | 50% | 345 |
| oracle | 212,307 | +6.15% | 0 | - | 233 |
| intramonth | 211,702 | +5.85% | 0 | - | 235 |
| snake_abs | 209,320 | +4.66% | 1 | 100% | 255 |
| snake_abs_conv | 209,171 | +4.59% | 1 | 100% | 255 |
| snake_viper_wild | 207,678 | +3.84% | 14 | 50% | 2,496 |
| random_hold | 207,621 | +3.81% | 10 | 70% | 733 |
| snake_anaconda | 204,872 | +2.44% | 3 | 33% | 374 |
| snake_viper_tick | 204,128 | +2.06% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,535 | +0.77% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,382 | -9.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,298 (-4.35%).

Profit on 2026-11-17:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,707 | +1.28% |
| benchmark | +1,913 | +0.87% |
| snake_viper_wild | +1,534 | +0.74% |
| snake_viper_tick | +1,508 | +0.74% |
| benchmark_smallcap | +706 | +0.35% |
| gold | +427 | +0.24% |
| unified | +382 | +0.17% |
| oracle | +284 | +0.13% |
| intramonth | +83 | +0.04% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| random_hold | -172 | -0.08% |
| snake_abs_exit | -207 | -0.10% |
| snake_anaconda | -230 | -0.11% |
| snake_abs_exit_conv | -738 | -0.35% |
| snake_abs | -814 | -0.39% |
| snake_abs_conv | -818 | -0.39% |

Average per day so far: benchmark Rs +628, unified Rs +623, snake_abs_exit Rs +444, intraweek Rs +399, snake_abs_exit_conv Rs +390, oracle Rs +352, intramonth Rs +334, snake_abs_conv Rs +287, snake_viper_wild Rs +284, snake_abs Rs +282, random_hold Rs +218, snake_viper_tick Rs +172, snake_anaconda Rs +162, nifty_calls Rs +52, benchmark_smallcap Rs +50, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -336, snake Rs -357, gold Rs -532

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.