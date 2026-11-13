# Paper trading report

Updated 2026-11-13 14:31 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,503 | +10.25% | 0 | - | 236 |
| benchmark | 219,155 | +9.58% | 0 | - | 237 |
| snake_abs_exit | 216,012 | +8.01% | 2 | 50% | 345 |
| intraweek | 215,995 | +8.00% | 30 | 53% | 3,302 |
| snake_abs_exit_conv | 215,902 | +7.95% | 2 | 50% | 345 |
| oracle | 213,119 | +6.56% | 0 | - | 233 |
| snake_abs | 212,062 | +6.03% | 1 | 100% | 255 |
| snake_abs_conv | 211,890 | +5.95% | 1 | 100% | 255 |
| intramonth | 211,034 | +5.52% | 0 | - | 235 |
| random_hold | 207,192 | +3.60% | 10 | 70% | 733 |
| snake_viper_wild | 205,116 | +2.56% | 14 | 50% | 2,496 |
| snake_anaconda | 204,182 | +2.09% | 3 | 33% | 374 |
| benchmark_smallcap | 202,342 | +1.17% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,608 | +0.80% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,930 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,847 (-4.08%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,337 | +0.62% |
| oracle | +4 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_viper_tick | -174 | -0.09% |
| snake_viper_wild | -177 | -0.09% |
| unified | -193 | -0.09% |
| intramonth | -559 | -0.26% |
| random_hold | -862 | -0.41% |
| benchmark_smallcap | -863 | -0.42% |
| gold | -1,381 | -0.74% |
| benchmark | -1,392 | -0.63% |
| snake_abs_exit | -1,431 | -0.66% |
| snake_anaconda | -1,745 | -0.85% |
| snake_abs_exit_conv | -2,772 | -1.27% |
| snake_abs_conv | -3,645 | -1.69% |
| snake_abs | -3,649 | -1.69% |

Average per day so far: unified Rs +621, benchmark Rs +580, snake_abs_exit Rs +534, snake_abs_exit_conv Rs +530, intraweek Rs +485, oracle Rs +398, snake_abs_conv Rs +396, snake_abs Rs +389, intramonth Rs +334, random_hold Rs +218, snake_viper_wild Rs +205, snake_anaconda Rs +149, benchmark_smallcap Rs +81, snake_viper_tick Rs +73, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.