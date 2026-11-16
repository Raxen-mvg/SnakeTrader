# Paper trading report

Updated 2026-11-16 09:42 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,609 | +10.30% | 0 | - | 237 |
| unified | 219,241 | +9.62% | 0 | - | 236 |
| snake_abs_exit | 214,990 | +7.50% | 2 | 50% | 345 |
| intraweek | 214,703 | +7.35% | 35 | 54% | 3,851 |
| snake_abs_exit_conv | 213,809 | +6.91% | 2 | 50% | 345 |
| oracle | 213,405 | +6.70% | 0 | - | 233 |
| snake_abs | 210,844 | +5.42% | 1 | 100% | 255 |
| snake_abs_conv | 210,674 | +5.34% | 1 | 100% | 255 |
| intramonth | 210,223 | +5.11% | 0 | - | 235 |
| random_hold | 207,612 | +3.81% | 10 | 70% | 733 |
| snake_anaconda | 204,891 | +2.44% | 3 | 33% | 374 |
| snake_viper_wild | 203,483 | +1.74% | 14 | 50% | 2,496 |
| benchmark_smallcap | 201,995 | +1.00% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 200,002 | +0.00% | 13 | 46% | 2,299 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 182,253 | -8.87% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,307 (-4.35%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +1,270 | +0.58% |
| random_hold | +386 | +0.19% |
| oracle | +307 | +0.14% |
| unified | +220 | +0.10% |
| intramonth | +166 | +0.08% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_anaconda | -1 | -0.00% |
| benchmark_smallcap | -874 | -0.43% |
| snake_viper_tick | -1,253 | -0.62% |
| snake_viper_wild | -1,275 | -0.62% |
| intraweek | -1,442 | -0.67% |
| snake_abs_conv | -1,693 | -0.80% |
| snake_abs | -1,696 | -0.80% |
| gold | -1,743 | -0.95% |
| snake_abs_exit | -1,995 | -0.92% |
| snake_abs_exit_conv | -2,572 | -1.19% |

Average per day so far: benchmark Rs +606, unified Rs +566, snake_abs_exit Rs +484, snake_abs_exit_conv Rs +445, intraweek Rs +432, oracle Rs +394, snake_abs_conv Rs +344, snake_abs Rs +339, intramonth Rs +301, random_hold Rs +224, snake_anaconda Rs +169, snake_viper_wild Rs +134, benchmark_smallcap Rs +66, nifty_calls Rs +54, snake_viper_tick Rs +0, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -522

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.