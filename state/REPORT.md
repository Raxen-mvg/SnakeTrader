# Paper trading report

Updated 2026-11-13 13:34 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,394 | +10.20% | 0 | - | 236 |
| benchmark | 219,347 | +9.67% | 0 | - | 237 |
| snake_abs_exit | 216,864 | +8.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,588 | +8.29% | 2 | 50% | 345 |
| intraweek | 216,044 | +8.02% | 30 | 53% | 3,302 |
| oracle | 213,183 | +6.59% | 0 | - | 233 |
| snake_abs | 212,522 | +6.26% | 1 | 100% | 255 |
| snake_abs_conv | 212,355 | +6.18% | 1 | 100% | 255 |
| intramonth | 211,043 | +5.52% | 0 | - | 235 |
| random_hold | 207,343 | +3.67% | 10 | 70% | 733 |
| snake_viper_wild | 205,679 | +2.84% | 14 | 50% | 2,496 |
| snake_anaconda | 204,785 | +2.39% | 3 | 33% | 374 |
| benchmark_smallcap | 202,724 | +1.36% | 0 | - | 237 |
| snake_viper_tick | 202,161 | +1.08% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,996 | -8.00% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,916 (-4.04%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,386 | +0.65% |
| snake_viper_wild | +386 | +0.19% |
| snake_viper_tick | +379 | +0.19% |
| oracle | +67 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -303 | -0.14% |
| benchmark_smallcap | -482 | -0.24% |
| intramonth | -550 | -0.26% |
| snake_abs_exit | -579 | -0.27% |
| random_hold | -711 | -0.34% |
| snake_anaconda | -1,142 | -0.55% |
| benchmark | -1,201 | -0.55% |
| gold | -1,315 | -0.71% |
| snake_abs_exit_conv | -2,086 | -0.95% |
| snake_abs_conv | -3,180 | -1.48% |
| snake_abs | -3,189 | -1.48% |

Average per day so far: unified Rs +618, benchmark Rs +586, snake_abs_exit Rs +562, snake_abs_exit_conv Rs +553, intraweek Rs +486, snake_abs_conv Rs +412, snake_abs Rs +404, oracle Rs +399, intramonth Rs +335, snake_viper_wild Rs +227, random_hold Rs +223, snake_anaconda Rs +171, snake_viper_tick Rs +98, benchmark_smallcap Rs +94, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -485

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.