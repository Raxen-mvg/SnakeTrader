# Paper trading report

Updated 2026-11-13 14:40 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,471 | +10.24% | 0 | - | 236 |
| benchmark | 219,362 | +9.68% | 0 | - | 237 |
| snake_abs_exit | 216,556 | +8.28% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,414 | +8.21% | 2 | 50% | 345 |
| intraweek | 215,957 | +7.98% | 30 | 53% | 3,302 |
| oracle | 213,231 | +6.62% | 0 | - | 233 |
| snake_abs | 212,310 | +6.16% | 1 | 100% | 255 |
| snake_abs_conv | 212,146 | +6.07% | 1 | 100% | 255 |
| intramonth | 211,006 | +5.50% | 0 | - | 235 |
| random_hold | 207,190 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,322 | +2.66% | 14 | 50% | 2,496 |
| snake_anaconda | 204,649 | +2.32% | 3 | 33% | 374 |
| benchmark_smallcap | 202,914 | +1.46% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,811 | +0.91% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,045 | -7.98% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,890 (-4.06%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,299 | +0.60% |
| oracle | +115 | +0.05% |
| snake_viper_wild | +29 | +0.01% |
| snake_viper_tick | +29 | +0.01% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -225 | -0.10% |
| benchmark_smallcap | -291 | -0.14% |
| intramonth | -587 | -0.28% |
| random_hold | -864 | -0.41% |
| snake_abs_exit | -887 | -0.41% |
| benchmark | -1,186 | -0.54% |
| gold | -1,266 | -0.68% |
| snake_anaconda | -1,279 | -0.62% |
| snake_abs_exit_conv | -2,260 | -1.03% |
| snake_abs_conv | -3,389 | -1.57% |
| snake_abs | -3,401 | -1.58% |

Average per day so far: unified Rs +620, benchmark Rs +587, snake_abs_exit Rs +552, snake_abs_exit_conv Rs +547, intraweek Rs +484, snake_abs_conv Rs +405, oracle Rs +401, snake_abs Rs +397, intramonth Rs +334, random_hold Rs +218, snake_viper_wild Rs +213, snake_anaconda Rs +166, benchmark_smallcap Rs +100, snake_viper_tick Rs +82, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -483

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.