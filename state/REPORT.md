# Paper trading report

Updated 2026-11-04 13:25 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,237 | +7.12% | 0 | - | 236 |
| snake_abs_exit_conv | 212,739 | +6.37% | 1 | 100% | 255 |
| snake_abs_exit | 212,587 | +6.29% | 1 | 100% | 260 |
| snake_abs | 209,636 | +4.82% | 1 | 100% | 255 |
| snake_abs_conv | 209,482 | +4.74% | 1 | 100% | 255 |
| intraweek | 209,150 | +4.58% | 25 | 48% | 2,757 |
| benchmark | 208,178 | +4.09% | 0 | - | 237 |
| snake_viper_wild | 206,906 | +3.45% | 3 | 33% | 702 |
| intramonth | 206,525 | +3.26% | 0 | - | 235 |
| snake_viper_tick | 203,298 | +1.65% | 2 | 0% | 532 |
| random_hold | 202,712 | +1.36% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,304 | +0.65% | 0 | - | 233 |
| snake_anaconda | 201,120 | +0.56% | 3 | 33% | 361 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 195,628 | -2.19% | 0 | - | 237 |
| gold | 190,703 | -4.65% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,312 (-5.34%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +8,573 | +4.20% |
| snake_abs_exit_conv | +8,400 | +4.11% |
| snake_abs_conv | +8,341 | +4.15% |
| snake_abs | +8,327 | +4.14% |
| snake_anaconda | +7,295 | +3.76% |
| gold | +5,425 | +2.93% |
| intraweek | +4,065 | +1.98% |
| benchmark_smallcap | +2,690 | +1.39% |
| intramonth | +2,554 | +1.25% |
| random_hold | +2,244 | +1.12% |
| unified | +2,236 | +1.05% |
| benchmark | +1,476 | +0.71% |
| oracle | +1,314 | +0.66% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,869 | -1.87% |
| snake_viper_wild | -3,987 | -1.89% |

Average per day so far: snake_abs_exit_conv Rs +531, unified Rs +527, snake_abs_exit Rs +524, snake_abs_conv Rs +395, snake_abs Rs +385, snake_viper_wild Rs +363, intraweek Rs +339, benchmark Rs +303, intramonth Rs +242, snake_viper_tick Rs +206, random_hold Rs +100, nifty_calls Rs +68, snake_anaconda Rs +51, oracle Rs +48, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -190, gold Rs -344, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.