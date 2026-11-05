# Paper trading report

Updated 2026-11-05 10:18 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 218,744 | +9.37% | 0 | - | 236 |
| snake_abs_exit_conv | 215,605 | +7.80% | 1 | 100% | 255 |
| snake_abs_exit | 215,344 | +7.67% | 1 | 100% | 260 |
| benchmark | 212,607 | +6.30% | 0 | - | 237 |
| snake_abs | 212,479 | +6.24% | 1 | 100% | 255 |
| snake_abs_conv | 212,328 | +6.16% | 1 | 100% | 255 |
| intraweek | 211,171 | +5.58% | 25 | 48% | 2,757 |
| intramonth | 210,502 | +5.25% | 0 | - | 235 |
| random_hold | 206,790 | +3.40% | 8 | 62% | 649 |
| snake_viper_wild | 206,462 | +3.23% | 3 | 33% | 702 |
| oracle | 204,462 | +2.23% | 0 | - | 233 |
| snake_viper_tick | 202,925 | +1.46% | 2 | 0% | 532 |
| snake_anaconda | 202,646 | +1.32% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,652 | -0.17% | 0 | - | 237 |
| gold | 195,224 | -2.39% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,732 (-4.63%).

Profit on 2026-11-05:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +4,305 | +2.01% |
| benchmark | +3,848 | +1.84% |
| gold | +3,831 | +2.00% |
| intramonth | +3,486 | +1.68% |
| random_hold | +3,481 | +1.71% |
| benchmark_smallcap | +2,982 | +1.52% |
| oracle | +2,670 | +1.32% |
| intraweek | +1,473 | +0.70% |
| snake_abs_exit_conv | +590 | +0.27% |
| snake_abs | +576 | +0.27% |
| snake_abs_conv | +570 | +0.27% |
| snake_abs_exit | +443 | +0.21% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_anaconda | -1,174 | -0.58% |
| snake_viper_tick | -2,475 | -1.21% |
| snake_viper_wild | -2,568 | -1.23% |

Average per day so far: unified Rs +669, snake_abs_exit_conv Rs +624, snake_abs_exit Rs +614, snake_abs_conv Rs +493, snake_abs Rs +480, benchmark Rs +450, intraweek Rs +399, intramonth Rs +375, snake_viper_wild Rs +323, random_hold Rs +243, snake_viper_tick Rs +172, oracle Rs +159, snake_anaconda Rs +115, nifty_calls Rs +66, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, benchmark_smallcap Rs -15, gold Rs -171, snake_nonews Rs -427, snake Rs -450

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.