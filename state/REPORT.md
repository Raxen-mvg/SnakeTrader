# Paper trading report

Updated 2026-11-13 14:55 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,189 | +10.09% | 0 | - | 236 |
| benchmark | 219,377 | +9.69% | 0 | - | 237 |
| snake_abs_exit | 217,387 | +8.69% | 2 | 50% | 345 |
| snake_abs_exit_conv | 216,997 | +8.50% | 2 | 50% | 345 |
| intraweek | 216,262 | +8.13% | 30 | 53% | 3,302 |
| oracle | 213,281 | +6.64% | 0 | - | 233 |
| snake_abs | 213,163 | +6.58% | 1 | 100% | 255 |
| snake_abs_conv | 212,995 | +6.50% | 1 | 100% | 255 |
| intramonth | 210,747 | +5.37% | 0 | - | 235 |
| random_hold | 207,022 | +3.51% | 10 | 70% | 733 |
| snake_anaconda | 205,469 | +2.73% | 3 | 33% | 374 |
| snake_viper_wild | 205,352 | +2.68% | 14 | 50% | 2,496 |
| benchmark_smallcap | 203,026 | +1.51% | 0 | - | 237 |
| snake_viper_tick | 201,840 | +0.92% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,930 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,936 (-4.03%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,604 | +0.75% |
| oracle | +166 | +0.08% |
| snake_viper_wild | +59 | +0.03% |
| snake_viper_tick | +58 | +0.03% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -56 | -0.03% |
| benchmark_smallcap | -179 | -0.09% |
| snake_anaconda | -458 | -0.22% |
| unified | -508 | -0.23% |
| intramonth | -847 | -0.40% |
| random_hold | -1,032 | -0.50% |
| benchmark | -1,170 | -0.53% |
| gold | -1,381 | -0.74% |
| snake_abs_exit_conv | -1,677 | -0.77% |
| snake_abs_conv | -2,540 | -1.18% |
| snake_abs | -2,548 | -1.18% |

Average per day so far: unified Rs +612, benchmark Rs +587, snake_abs_exit Rs +580, snake_abs_exit_conv Rs +567, intraweek Rs +493, snake_abs_conv Rs +433, snake_abs Rs +425, oracle Rs +402, intramonth Rs +326, snake_viper_wild Rs +214, random_hold Rs +213, snake_anaconda Rs +195, benchmark_smallcap Rs +104, snake_viper_tick Rs +84, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.