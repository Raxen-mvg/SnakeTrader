# Paper trading report

Updated 2026-11-05 09:56 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,719 | +9.36% | 0 | - | 236 |
| snake_abs_exit_conv | 215,773 | +7.89% | 1 | 100% | 255 |
| snake_abs_exit | 215,521 | +7.76% | 1 | 100% | 260 |
| benchmark | 212,898 | +6.45% | 0 | - | 237 |
| snake_abs | 212,649 | +6.32% | 1 | 100% | 255 |
| snake_abs_conv | 212,500 | +6.25% | 1 | 100% | 255 |
| intraweek | 210,599 | +5.30% | 25 | 48% | 2,757 |
| intramonth | 210,489 | +5.24% | 0 | - | 235 |
| random_hold | 206,282 | +3.14% | 8 | 62% | 649 |
| snake_viper_wild | 206,063 | +3.03% | 3 | 33% | 702 |
| oracle | 204,441 | +2.22% | 0 | - | 233 |
| snake_anaconda | 203,043 | +1.52% | 3 | 33% | 374 |
| snake_viper_tick | 202,534 | +1.27% | 2 | 0% | 532 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| gold | 194,978 | -2.51% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,619 (-4.69%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,279 | +2.00% |
| benchmark | +4,139 | +1.98% |
| gold | +3,584 | +1.87% |
| intramonth | +3,473 | +1.68% |
| benchmark_smallcap | +2,982 | +1.52% |
| random_hold | +2,973 | +1.46% |
| oracle | +2,649 | +1.31% |
| intraweek | +901 | +0.43% |
| snake_abs_exit_conv | +758 | +0.35% |
| snake_abs | +746 | +0.35% |
| snake_abs_conv | +742 | +0.35% |
| snake_abs_exit | +620 | +0.29% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -777 | -0.38% |
| snake_viper_tick | -2,866 | -1.40% |
| snake_viper_wild | -2,967 | -1.42% |

Average per day so far: unified Rs +669, snake_abs_exit_conv Rs +631, snake_abs_exit Rs +621, snake_abs_conv Rs +500, snake_abs Rs +486, benchmark Rs +461, intraweek Rs +379, intramonth Rs +375, snake_viper_wild Rs +303, random_hold Rs +224, oracle Rs +159, snake_viper_tick Rs +149, snake_anaconda Rs +132, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -15, gold Rs -179, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.