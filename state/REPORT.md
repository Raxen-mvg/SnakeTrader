# Paper trading report

Updated 2026-11-05 11:15 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,487 | +9.24% | 0 | - | 236 |
| snake_abs_exit_conv | 215,160 | +7.58% | 1 | 100% | 255 |
| snake_abs_exit | 214,869 | +7.43% | 1 | 100% | 260 |
| benchmark | 212,393 | +6.20% | 0 | - | 237 |
| snake_abs | 212,034 | +6.02% | 1 | 100% | 255 |
| snake_abs_conv | 211,901 | +5.95% | 1 | 100% | 255 |
| intraweek | 211,165 | +5.58% | 25 | 48% | 2,757 |
| intramonth | 210,324 | +5.16% | 0 | - | 235 |
| random_hold | 206,894 | +3.45% | 8 | 62% | 649 |
| snake_viper_wild | 206,551 | +3.27% | 3 | 33% | 702 |
| oracle | 204,187 | +2.09% | 0 | - | 233 |
| snake_anaconda | 203,343 | +1.67% | 3 | 33% | 374 |
| snake_viper_tick | 203,001 | +1.50% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,304 | -0.35% | 0 | - | 237 |
| gold | 194,057 | -2.97% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,566 (-4.72%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,048 | +1.89% |
| benchmark | +3,634 | +1.74% |
| random_hold | +3,585 | +1.76% |
| intramonth | +3,309 | +1.60% |
| gold | +2,663 | +1.39% |
| benchmark_smallcap | +2,634 | +1.34% |
| oracle | +2,395 | +1.19% |
| intraweek | +1,467 | +0.70% |
| snake_abs_exit_conv | +145 | +0.07% |
| snake_abs_conv | +143 | +0.07% |
| snake_abs | +131 | +0.06% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -32 | -0.01% |
| snake_anaconda | -477 | -0.23% |
| snake_viper_tick | -2,399 | -1.17% |
| snake_viper_wild | -2,479 | -1.19% |

Average per day so far: unified Rs +660, snake_abs_exit_conv Rs +606, snake_abs_exit Rs +595, snake_abs_conv Rs +476, snake_abs Rs +463, benchmark Rs +443, intraweek Rs +399, intramonth Rs +369, snake_viper_wild Rs +328, random_hold Rs +246, snake_viper_tick Rs +177, oracle Rs +150, snake_anaconda Rs +145, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -29, gold Rs -212, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.