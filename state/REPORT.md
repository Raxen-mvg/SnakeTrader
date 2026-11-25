# Paper trading report

Updated 2026-11-25 11:41 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,117 | +13.06% | 0 | - | 237 |
| unified | 225,542 | +12.77% | 0 | - | 236 |
| intramonth | 213,243 | +6.62% | 0 | - | 235 |
| oracle | 212,199 | +6.10% | 0 | - | 233 |
| random_hold | 210,176 | +5.09% | 12 | 75% | 1,009 |
| intraweek | 208,198 | +4.10% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,841 | +1.42% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,228 | +1.11% | 2 | 50% | 345 |
| snake_abs | 201,944 | +0.97% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_conv | 201,752 | +0.88% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,596 | -0.20% | 0 | - | 237 |
| snake_viper_wild | 196,929 | -1.54% | 16 | 50% | 2,827 |
| snake_anaconda | 194,276 | -2.86% | 3 | 33% | 374 |
| snake_viper_tick | 193,575 | -3.21% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,613 | -17.69% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,654 (-5.17%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,644 | +2.10% |
| random_hold | +1,750 | +0.84% |
| unified | +1,257 | +0.56% |
| benchmark_smallcap | +617 | +0.31% |
| intramonth | +491 | +0.23% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -143 | -0.07% |
| intraweek | -3,421 | -1.62% |
| snake_abs | -3,517 | -1.71% |
| snake_abs_conv | -3,551 | -1.73% |
| snake_viper_tick | -4,117 | -2.08% |
| snake_viper_wild | -4,195 | -2.09% |
| snake_anaconda | -4,428 | -2.23% |
| snake_abs_exit | -4,654 | -2.24% |
| gold | -4,817 | -2.84% |
| snake_abs_exit_conv | -4,817 | -2.33% |

Average per day so far: benchmark Rs +653, unified Rs +639, intramonth Rs +331, oracle Rs +305, random_hold Rs +254, intraweek Rs +205, snake_abs_exit Rs +77, snake_abs_exit_conv Rs +60, snake_abs Rs +51, snake_abs_conv Rs +47, nifty_calls Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_viper_wild Rs -96, snake_anaconda Rs -164, snake_viper_tick Rs -222, snake_nonews Rs -292, snake Rs -311, gold Rs -885

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.