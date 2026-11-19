# Paper trading report

Updated 2026-11-19 09:21 IST. Model picks as of 2026-10-22. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,039 | +11.52% | 0 | - | 236 |
| benchmark | 219,607 | +9.80% | 0 | - | 237 |
| snake_abs_exit | 213,247 | +6.62% | 2 | 50% | 345 |
| intramonth | 212,852 | +6.43% | 0 | - | 235 |
| snake_abs_exit_conv | 211,499 | +5.75% | 2 | 50% | 345 |
| intraweek | 211,311 | +5.66% | 35 | 54% | 3,851 |
| oracle | 210,688 | +5.34% | 0 | - | 233 |
| snake_abs | 208,706 | +4.35% | 1 | 100% | 255 |
| snake_abs_conv | 208,581 | +4.29% | 1 | 100% | 255 |
| snake_viper_wild | 207,788 | +3.89% | 16 | 50% | 2,827 |
| random_hold | 206,923 | +3.46% | 10 | 70% | 733 |
| snake_viper_tick | 204,236 | +2.12% | 15 | 47% | 2,625 |
| snake_anaconda | 203,690 | +1.84% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,047 | -0.48% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 174,444 | -12.78% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,732 (-4.63%).

Profit on 2026-11-19:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +749 | +0.36% |
| snake_viper_tick | +733 | +0.36% |
| intramonth | +579 | +0.27% |
| unified | +427 | +0.19% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| random_hold | -9 | -0.00% |
| oracle | -108 | -0.05% |
| benchmark_smallcap | -280 | -0.14% |
| intraweek | -528 | -0.25% |
| benchmark | -689 | -0.31% |
| snake_anaconda | -711 | -0.35% |
| snake_abs | -731 | -0.35% |
| snake_abs_conv | -743 | -0.35% |
| snake_abs_exit | -785 | -0.37% |
| snake_abs_exit_conv | -885 | -0.42% |
| gold | -2,877 | -1.62% |

Average per day so far: unified Rs +623, benchmark Rs +530, snake_abs_exit Rs +390, intramonth Rs +347, snake_abs_exit_conv Rs +338, intraweek Rs +306, oracle Rs +289, snake_viper_wild Rs +269, snake_abs_conv Rs +252, snake_abs Rs +249, random_hold Rs +187, snake_viper_tick Rs +163, snake_anaconda Rs +115, nifty_calls Rs +50, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, snake_nonews Rs -317, snake Rs -337, gold Rs -691

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.