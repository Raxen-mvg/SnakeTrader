# Paper trading report

Updated 2026-11-13 13:52 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,178 | +10.09% | 0 | - | 236 |
| benchmark | 219,186 | +9.59% | 0 | - | 237 |
| snake_abs_exit | 216,350 | +8.18% | 2 | 50% | 345 |
| snake_abs_exit_conv | 215,963 | +7.98% | 2 | 50% | 345 |
| intraweek | 215,732 | +7.87% | 30 | 53% | 3,302 |
| oracle | 212,822 | +6.41% | 0 | - | 233 |
| snake_abs | 212,074 | +6.04% | 1 | 100% | 255 |
| snake_abs_conv | 211,905 | +5.95% | 1 | 100% | 255 |
| intramonth | 210,884 | +5.44% | 0 | - | 235 |
| random_hold | 207,155 | +3.58% | 10 | 70% | 733 |
| snake_viper_wild | 205,476 | +2.74% | 14 | 50% | 2,496 |
| snake_anaconda | 204,221 | +2.11% | 3 | 33% | 374 |
| benchmark_smallcap | 202,421 | +1.21% | 0 | - | 237 |
| snake_viper_tick | 201,962 | +0.98% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,749 | -8.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,660 (-4.17%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,074 | +0.50% |
| snake_viper_wild | +183 | +0.09% |
| snake_viper_tick | +180 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| oracle | -293 | -0.14% |
| unified | -518 | -0.23% |
| intramonth | -709 | -0.34% |
| benchmark_smallcap | -785 | -0.39% |
| random_hold | -899 | -0.43% |
| snake_abs_exit | -1,092 | -0.50% |
| benchmark | -1,362 | -0.62% |
| gold | -1,562 | -0.84% |
| snake_anaconda | -1,706 | -0.83% |
| snake_abs_exit_conv | -2,711 | -1.24% |
| snake_abs_conv | -3,630 | -1.68% |
| snake_abs | -3,637 | -1.69% |

Average per day so far: unified Rs +611, benchmark Rs +581, snake_abs_exit Rs +545, snake_abs_exit_conv Rs +532, intraweek Rs +477, snake_abs_conv Rs +397, snake_abs Rs +389, oracle Rs +389, intramonth Rs +330, snake_viper_wild Rs +219, random_hold Rs +217, snake_anaconda Rs +151, snake_viper_tick Rs +89, benchmark_smallcap Rs +83, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -492

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.