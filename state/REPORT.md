# Paper trading report

Updated 2026-11-05 13:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 217,414 | +8.71% | 0 | - | 236 |
| snake_abs_exit_conv | 214,581 | +7.29% | 1 | 100% | 255 |
| snake_abs_exit | 214,299 | +7.15% | 1 | 100% | 260 |
| benchmark | 213,533 | +6.77% | 0 | - | 237 |
| snake_abs | 211,459 | +5.73% | 1 | 100% | 255 |
| snake_abs_conv | 211,325 | +5.66% | 1 | 100% | 255 |
| intraweek | 211,158 | +5.58% | 25 | 48% | 2,757 |
| intramonth | 209,340 | +4.67% | 0 | - | 235 |
| snake_viper_wild | 207,034 | +3.52% | 3 | 33% | 702 |
| random_hold | 206,008 | +3.00% | 8 | 62% | 649 |
| oracle | 203,916 | +1.96% | 0 | - | 233 |
| snake_viper_tick | 203,475 | +1.74% | 2 | 0% | 532 |
| snake_anaconda | 202,714 | +1.36% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 198,968 | -0.52% | 0 | - | 237 |
| gold | 193,975 | -3.01% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,272 (-4.86%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,774 | +2.29% |
| unified | +2,975 | +1.39% |
| random_hold | +2,699 | +1.33% |
| gold | +2,581 | +1.35% |
| intramonth | +2,324 | +1.12% |
| benchmark_smallcap | +2,298 | +1.17% |
| oracle | +2,124 | +1.05% |
| intraweek | +1,460 | +0.70% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_conv | -434 | -0.20% |
| snake_abs_exit_conv | -434 | -0.20% |
| snake_abs | -444 | -0.21% |
| snake_abs_exit | -601 | -0.28% |
| snake_anaconda | -1,106 | -0.54% |
| snake_viper_tick | -1,925 | -0.94% |
| snake_viper_wild | -1,996 | -0.95% |

Average per day so far: unified Rs +622, snake_abs_exit_conv Rs +583, snake_abs_exit Rs +572, benchmark Rs +483, snake_abs_conv Rs +453, snake_abs Rs +441, intraweek Rs +399, snake_viper_wild Rs +352, intramonth Rs +334, random_hold Rs +215, snake_viper_tick Rs +204, oracle Rs +140, snake_anaconda Rs +118, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -43, gold Rs -215, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.