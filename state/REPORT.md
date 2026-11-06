# Paper trading report

Updated 2026-11-06 09:59 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,702 | +7.35% | 0 | - | 236 |
| benchmark | 214,657 | +7.33% | 0 | - | 237 |
| intraweek | 211,476 | +5.74% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 210,501 | +5.25% | 1 | 100% | 255 |
| snake_abs_exit | 210,264 | +5.13% | 1 | 100% | 260 |
| snake_abs | 207,439 | +3.72% | 1 | 100% | 255 |
| snake_abs_conv | 207,272 | +3.64% | 1 | 100% | 255 |
| intramonth | 206,421 | +3.21% | 0 | - | 235 |
| oracle | 204,621 | +2.31% | 0 | - | 233 |
| random_hold | 204,059 | +2.03% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 198,223 | -0.89% | 3 | 33% | 702 |
| snake_anaconda | 197,441 | -1.28% | 3 | 33% | 374 |
| benchmark_smallcap | 195,123 | -2.44% | 0 | - | 237 |
| snake_viper_tick | 194,862 | -2.57% | 2 | 0% | 532 |
| gold | 190,309 | -4.85% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,762 (-6.12%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +2,057 | +0.98% |
| benchmark | +887 | +0.41% |
| oracle | +549 | +0.27% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -264 | -0.13% |
| unified | -1,281 | -0.59% |
| intramonth | -1,527 | -0.73% |
| benchmark_smallcap | -3,565 | -1.79% |
| gold | -3,913 | -2.02% |
| snake_abs | -4,250 | -2.01% |
| snake_abs_conv | -4,273 | -2.02% |
| snake_abs_exit_conv | -4,303 | -2.00% |
| snake_abs_exit | -4,395 | -2.05% |
| snake_anaconda | -5,038 | -2.49% |
| snake_viper_tick | -6,276 | -3.12% |
| snake_viper_wild | -6,433 | -3.14% |

Average per day so far: unified Rs +507, benchmark Rs +505, snake_abs_exit_conv Rs +404, intraweek Rs +396, snake_abs_exit Rs +395, snake_abs_conv Rs +280, snake_abs Rs +276, intramonth Rs +221, oracle Rs +159, random_hold Rs +140, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_viper_wild Rs -85, snake_anaconda Rs -107, benchmark_smallcap Rs -195, snake_viper_tick Rs -285, gold Rs -334, snake_nonews Rs -411, snake Rs -434

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.