# Paper trading report

Updated 2026-11-25 10:20 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,314 | +12.66% | 0 | - | 236 |
| benchmark | 225,038 | +12.52% | 0 | - | 237 |
| intramonth | 212,924 | +6.46% | 0 | - | 235 |
| oracle | 212,707 | +6.35% | 0 | - | 233 |
| random_hold | 209,327 | +4.66% | 12 | 75% | 1,009 |
| intraweek | 207,544 | +3.77% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,885 | +0.94% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,263 | +0.63% | 2 | 50% | 345 |
| snake_abs | 200,917 | +0.46% | 1 | 100% | 255 |
| snake_abs_conv | 200,728 | +0.36% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,495 | -0.25% | 0 | - | 237 |
| snake_viper_wild | 194,774 | -2.61% | 16 | 50% | 2,827 |
| snake_anaconda | 193,294 | -3.35% | 3 | 33% | 374 |
| snake_viper_tick | 191,465 | -4.27% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,599 | -17.20% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,283 (-5.36%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,565 | +1.61% |
| unified | +1,029 | +0.46% |
| random_hold | +901 | +0.43% |
| benchmark_smallcap | +516 | +0.26% |
| oracle | +365 | +0.17% |
| intramonth | +173 | +0.08% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,831 | -2.26% |
| intraweek | -4,075 | -1.93% |
| snake_abs | -4,544 | -2.21% |
| snake_abs_conv | -4,575 | -2.23% |
| snake_anaconda | -5,410 | -2.72% |
| snake_abs_exit | -5,610 | -2.70% |
| snake_abs_exit_conv | -5,782 | -2.79% |
| snake_viper_tick | -6,228 | -3.15% |
| snake_viper_wild | -6,351 | -3.16% |

Average per day so far: unified Rs +633, benchmark Rs +626, intramonth Rs +323, oracle Rs +318, random_hold Rs +233, intraweek Rs +189, snake_abs_exit Rs +51, nifty_calls Rs +46, snake_abs_exit_conv Rs +34, snake_abs Rs +24, snake_abs_conv Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -14, snake_viper_wild Rs -163, snake_anaconda Rs -192, snake_nonews Rs -292, snake_viper_tick Rs -294, snake Rs -311, gold Rs -860

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.