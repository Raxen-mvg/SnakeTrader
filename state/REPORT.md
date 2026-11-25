# Paper trading report

Updated 2026-11-25 09:38 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,809 | +12.90% | 0 | - | 236 |
| benchmark | 224,549 | +12.27% | 0 | - | 237 |
| intramonth | 213,457 | +6.73% | 0 | - | 235 |
| oracle | 212,932 | +6.47% | 0 | - | 233 |
| intraweek | 211,802 | +5.90% | 40 | 55% | 4,400 |
| random_hold | 209,904 | +4.95% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,585 | +1.79% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,025 | +1.51% | 2 | 50% | 345 |
| snake_abs | 202,263 | +1.13% | 1 | 100% | 255 |
| snake_abs_conv | 202,085 | +1.04% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,719 | -0.14% | 0 | - | 237 |
| snake_viper_wild | 199,209 | -0.40% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,817 | -2.09% | 15 | 47% | 2,625 |
| snake_anaconda | 195,264 | -2.37% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,353 | -17.32% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,317 (-4.84%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,075 | +1.39% |
| unified | +1,524 | +0.68% |
| random_hold | +1,478 | +0.71% |
| benchmark_smallcap | +740 | +0.37% |
| intramonth | +705 | +0.33% |
| oracle | +589 | +0.28% |
| intraweek | +183 | +0.09% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -1,875 | -0.95% |
| snake_viper_wild | -1,915 | -0.95% |
| snake_abs | -3,198 | -1.56% |
| snake_abs_conv | -3,218 | -1.57% |
| snake_anaconda | -3,439 | -1.73% |
| snake_abs_exit | -3,910 | -1.88% |
| snake_abs_exit_conv | -4,021 | -1.94% |
| gold | -4,077 | -2.41% |

Average per day so far: unified Rs +645, benchmark Rs +614, intramonth Rs +336, oracle Rs +323, intraweek Rs +295, random_hold Rs +248, snake_abs_exit Rs +97, snake_abs_exit_conv Rs +82, snake_abs Rs +60, snake_abs_conv Rs +56, nifty_calls Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -8, snake_viper_wild Rs -25, snake_anaconda Rs -135, snake_viper_tick Rs -144, snake_nonews Rs -292, snake Rs -311, gold Rs -866

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.