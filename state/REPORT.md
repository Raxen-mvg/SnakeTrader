# Paper trading report

Updated 2026-11-12 11:19 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 222,741 | +11.37% | 0 | - | 236 |
| benchmark | 220,655 | +10.33% | 0 | - | 237 |
| snake_abs_exit_conv | 219,584 | +9.79% | 2 | 50% | 345 |
| snake_abs_exit | 218,681 | +9.34% | 2 | 50% | 345 |
| snake_abs | 216,384 | +8.19% | 1 | 100% | 255 |
| snake_abs_conv | 216,225 | +8.11% | 1 | 100% | 255 |
| intraweek | 215,095 | +7.55% | 30 | 53% | 3,302 |
| oracle | 214,102 | +7.05% | 0 | - | 233 |
| intramonth | 213,030 | +6.51% | 0 | - | 235 |
| snake_viper_wild | 208,278 | +4.14% | 10 | 50% | 1,825 |
| random_hold | 208,009 | +4.00% | 10 | 70% | 733 |
| snake_anaconda | 207,160 | +3.58% | 3 | 33% | 374 |
| snake_viper_tick | 204,712 | +2.36% | 9 | 44% | 1,639 |
| benchmark_smallcap | 203,463 | +1.73% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 186,347 | -6.83% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,907 (-3.55%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +3,037 | +1.49% |
| unified | +2,927 | +1.33% |
| snake_abs_conv | +2,767 | +1.30% |
| snake_abs | +2,759 | +1.29% |
| benchmark_smallcap | +2,657 | +1.32% |
| snake_abs_exit | +2,519 | +1.17% |
| snake_abs_exit_conv | +2,433 | +1.12% |
| oracle | +2,099 | +0.99% |
| intramonth | +2,033 | +0.96% |
| intraweek | +1,962 | +0.92% |
| snake_viper_wild | +1,537 | +0.74% |
| snake_viper_tick | +1,503 | +0.74% |
| benchmark | +1,392 | +0.64% |
| random_hold | +898 | +0.43% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,239 | -1.71% |

Average per day so far: unified Rs +711, snake_abs_exit_conv Rs +675, benchmark Rs +645, snake_abs_exit Rs +644, snake_abs_conv Rs +559, snake_abs Rs +546, intraweek Rs +472, oracle Rs +441, intramonth Rs +407, snake_viper_wild Rs +345, snake_anaconda Rs +265, random_hold Rs +250, snake_viper_tick Rs +224, benchmark_smallcap Rs +124, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -427

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.