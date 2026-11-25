# Paper trading report

Updated 2026-11-25 11:38 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,017 | +13.01% | 0 | - | 237 |
| unified | 225,443 | +12.72% | 0 | - | 236 |
| intramonth | 213,189 | +6.59% | 0 | - | 235 |
| oracle | 212,031 | +6.01% | 0 | - | 233 |
| random_hold | 210,314 | +5.16% | 12 | 75% | 1,009 |
| intraweek | 208,309 | +4.16% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,593 | +1.30% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,965 | +0.98% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 201,668 | +0.83% | 1 | 100% | 255 |
| snake_abs_conv | 201,476 | +0.74% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,663 | -0.17% | 0 | - | 237 |
| snake_viper_wild | 196,578 | -1.71% | 16 | 50% | 2,827 |
| snake_anaconda | 194,007 | -3.00% | 3 | 33% | 374 |
| snake_viper_tick | 193,232 | -3.38% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,333 | -17.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,595 (-5.20%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,544 | +2.05% |
| random_hold | +1,888 | +0.91% |
| unified | +1,158 | +0.52% |
| benchmark_smallcap | +684 | +0.34% |
| intramonth | +437 | +0.20% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -311 | -0.15% |
| intraweek | -3,310 | -1.56% |
| snake_abs | -3,793 | -1.85% |
| snake_abs_conv | -3,827 | -1.86% |
| snake_viper_tick | -4,460 | -2.26% |
| snake_viper_wild | -4,546 | -2.26% |
| snake_anaconda | -4,696 | -2.36% |
| snake_abs_exit | -4,902 | -2.36% |
| snake_abs_exit_conv | -5,081 | -2.45% |
| gold | -5,096 | -3.01% |

Average per day so far: benchmark Rs +650, unified Rs +636, intramonth Rs +330, oracle Rs +301, random_hold Rs +258, intraweek Rs +208, snake_abs_exit Rs +70, snake_abs_exit_conv Rs +53, nifty_calls Rs +46, snake_abs Rs +44, snake_abs_conv Rs +40, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_viper_wild Rs -107, snake_anaconda Rs -171, snake_viper_tick Rs -233, snake_nonews Rs -292, snake Rs -311, gold Rs -892

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.