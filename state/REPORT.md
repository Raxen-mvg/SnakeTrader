# Paper trading report

Updated 2026-11-12 14:06 IST. Model picks as of 2026-11-11. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,784 | +10.39% | 0 | - | 236 |
| benchmark | 220,249 | +10.12% | 0 | - | 237 |
| snake_abs_exit_conv | 218,665 | +9.33% | 2 | 50% | 345 |
| snake_abs_exit | 217,616 | +8.81% | 2 | 50% | 345 |
| snake_abs | 215,802 | +7.90% | 1 | 100% | 255 |
| snake_abs_conv | 215,626 | +7.81% | 1 | 100% | 255 |
| intraweek | 214,383 | +7.19% | 30 | 53% | 3,302 |
| oracle | 212,805 | +6.40% | 0 | - | 233 |
| intramonth | 211,408 | +5.70% | 0 | - | 235 |
| random_hold | 207,902 | +3.95% | 10 | 70% | 733 |
| snake_viper_wild | 207,142 | +3.57% | 10 | 50% | 1,825 |
| snake_anaconda | 206,416 | +3.21% | 3 | 33% | 374 |
| snake_viper_tick | 203,598 | +1.80% | 9 | 44% | 1,639 |
| benchmark_smallcap | 202,791 | +1.40% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 185,771 | -7.11% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,899 (-4.05%).

Profit on 2026-11-12:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_anaconda | +2,293 | +1.12% |
| snake_abs | +2,177 | +1.02% |
| snake_abs_conv | +2,168 | +1.02% |
| benchmark_smallcap | +1,984 | +0.99% |
| snake_abs_exit_conv | +1,513 | +0.70% |
| snake_abs_exit | +1,454 | +0.67% |
| intraweek | +1,250 | +0.59% |
| benchmark | +987 | +0.45% |
| unified | +970 | +0.44% |
| oracle | +803 | +0.38% |
| random_hold | +791 | +0.38% |
| intramonth | +411 | +0.20% |
| snake_viper_wild | +400 | +0.19% |
| snake_viper_tick | +389 | +0.19% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -3,814 | -2.01% |

Average per day so far: unified Rs +650, snake_abs_exit_conv Rs +644, benchmark Rs +633, snake_abs_exit Rs +607, snake_abs_conv Rs +539, snake_abs Rs +527, intraweek Rs +449, oracle Rs +400, intramonth Rs +356, snake_viper_wild Rs +298, random_hold Rs +247, snake_anaconda Rs +238, snake_viper_tick Rs +171, benchmark_smallcap Rs +100, nifty_calls Rs +57, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -370, snake Rs -392, gold Rs -445

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.