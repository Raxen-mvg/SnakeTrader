# Paper trading report

Updated 2026-11-18 13:59 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,779 | +11.39% | 0 | - | 236 |
| benchmark | 220,448 | +10.22% | 0 | - | 237 |
| snake_abs_exit | 212,962 | +6.48% | 2 | 50% | 345 |
| intraweek | 212,705 | +6.35% | 35 | 54% | 3,851 |
| oracle | 212,492 | +6.25% | 0 | - | 233 |
| intramonth | 212,431 | +6.22% | 0 | - | 235 |
| snake_abs_exit_conv | 211,220 | +5.61% | 2 | 50% | 345 |
| snake_abs | 208,285 | +4.14% | 1 | 100% | 255 |
| snake_abs_conv | 208,147 | +4.07% | 1 | 100% | 255 |
| random_hold | 207,325 | +3.66% | 10 | 70% | 733 |
| snake_viper_wild | 206,799 | +3.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 203,268 | +1.63% | 15 | 47% | 2,625 |
| snake_anaconda | 203,226 | +1.61% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,775 | -0.11% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 177,042 | -11.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,248 (-4.38%).

Profit on 2026-11-18:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,341 | +0.60% |
| intramonth | +889 | +0.42% |
| oracle | +6 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_abs_exit | -180 | -0.08% |
| snake_abs_conv | -273 | -0.13% |
| snake_abs | -273 | -0.13% |
| snake_abs_exit_conv | -354 | -0.17% |
| intraweek | -618 | -0.29% |
| benchmark_smallcap | -796 | -0.40% |
| snake_anaconda | -829 | -0.41% |
| random_hold | -1,108 | -0.53% |
| benchmark | -1,155 | -0.52% |
| snake_viper_tick | -2,568 | -1.25% |
| snake_viper_wild | -2,616 | -1.25% |
| gold | -3,683 | -2.04% |

Average per day so far: unified Rs +633, benchmark Rs +568, snake_abs_exit Rs +393, intraweek Rs +353, oracle Rs +347, intramonth Rs +345, snake_abs_exit_conv Rs +340, snake_abs_conv Rs +247, snake_abs Rs +244, snake_viper_wild Rs +243, random_hold Rs +203, snake_viper_tick Rs +131, snake_anaconda Rs +104, nifty_calls Rs +51, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -7, snake_nonews Rs -326, snake Rs -347, gold Rs -638

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.