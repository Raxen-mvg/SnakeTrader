# Paper trading report

Updated 2026-11-13 11:34 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,536 | +10.27% | 0 | - | 236 |
| benchmark | 219,538 | +9.77% | 0 | - | 237 |
| snake_abs_exit_conv | 216,401 | +8.20% | 2 | 50% | 345 |
| snake_abs_exit | 216,303 | +8.15% | 2 | 50% | 345 |
| intraweek | 216,166 | +8.08% | 30 | 53% | 3,302 |
| oracle | 213,499 | +6.75% | 0 | - | 233 |
| snake_abs | 212,668 | +6.33% | 1 | 100% | 255 |
| snake_abs_conv | 212,496 | +6.25% | 1 | 100% | 255 |
| intramonth | 211,283 | +5.64% | 0 | - | 235 |
| random_hold | 207,187 | +3.59% | 10 | 70% | 733 |
| snake_viper_wild | 206,005 | +3.00% | 14 | 50% | 2,496 |
| snake_anaconda | 204,732 | +2.37% | 3 | 33% | 374 |
| benchmark_smallcap | 203,273 | +1.64% | 0 | - | 237 |
| snake_viper_tick | 202,481 | +1.24% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,930 | -8.04% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,064 (-3.97%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,508 | +0.70% |
| snake_viper_wild | +712 | +0.35% |
| snake_viper_tick | +700 | +0.35% |
| oracle | +384 | +0.18% |
| benchmark_smallcap | +67 | +0.03% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -161 | -0.07% |
| intramonth | -310 | -0.15% |
| random_hold | -867 | -0.42% |
| benchmark | -1,010 | -0.46% |
| snake_abs_exit | -1,140 | -0.52% |
| snake_anaconda | -1,195 | -0.58% |
| gold | -1,381 | -0.74% |
| snake_abs_exit_conv | -2,273 | -1.04% |
| snake_abs_conv | -3,039 | -1.41% |
| snake_abs | -3,043 | -1.41% |

Average per day so far: unified Rs +622, benchmark Rs +592, snake_abs_exit_conv Rs +547, snake_abs_exit Rs +543, intraweek Rs +490, snake_abs_conv Rs +417, oracle Rs +409, snake_abs Rs +409, intramonth Rs +342, snake_viper_wild Rs +240, random_hold Rs +218, snake_anaconda Rs +169, benchmark_smallcap Rs +113, snake_viper_tick Rs +113, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -487

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.