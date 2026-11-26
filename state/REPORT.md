# Paper trading report

Updated 2026-11-26 10:44 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,155 | +13.08% | 0 | - | 237 |
| unified | 223,529 | +11.77% | 0 | - | 236 |
| oracle | 212,894 | +6.45% | 0 | - | 233 |
| intramonth | 210,871 | +5.43% | 0 | - | 235 |
| random_hold | 209,927 | +4.96% | 13 | 69% | 1,037 |
| intraweek | 208,031 | +4.01% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,228 | +1.11% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,771 | +0.89% | 2 | 50% | 345 |
| benchmark_smallcap | 200,672 | +0.34% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,972 | -0.01% | 1 | 100% | 255 |
| snake_abs_conv | 199,786 | -0.11% | 1 | 100% | 255 |
| snake_anaconda | 193,661 | -3.17% | 3 | 33% | 374 |
| snake_viper_wild | 193,550 | -3.23% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,257 | -4.87% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,654 | -16.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,953 (-5.52%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +3,058 | +1.86% |
| benchmark_smallcap | +1,861 | +0.94% |
| intraweek | +1,288 | +0.62% |
| benchmark | +1,132 | +0.50% |
| random_hold | +434 | +0.21% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -28 | -0.01% |
| snake_abs | -178 | -0.09% |
| snake_abs_conv | -187 | -0.09% |
| snake_abs_exit_conv | -205 | -0.10% |
| unified | -571 | -0.26% |
| intramonth | -822 | -0.39% |
| snake_anaconda | -892 | -0.46% |
| oracle | -901 | -0.42% |
| snake_viper_tick | -3,920 | -2.02% |
| snake_viper_wild | -3,994 | -2.02% |

Average per day so far: benchmark Rs +638, unified Rs +574, oracle Rs +314, intramonth Rs +265, random_hold Rs +242, intraweek Rs +196, snake_abs_exit Rs +59, snake_abs_exit_conv Rs +47, nifty_calls Rs +45, benchmark_smallcap Rs +18, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -1, snake_abs_conv Rs -6, snake_anaconda Rs -176, snake_viper_wild Rs -195, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -325, gold Rs -789

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.