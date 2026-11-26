# Paper trading report

Updated 2026-11-26 12:15 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 226,232 | +13.12% | 0 | - | 237 |
| unified | 223,160 | +11.58% | 0 | - | 236 |
| oracle | 212,998 | +6.50% | 0 | - | 233 |
| intramonth | 210,364 | +5.18% | 0 | - | 235 |
| random_hold | 209,808 | +4.90% | 13 | 69% | 1,037 |
| intraweek | 208,399 | +4.20% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,885 | +0.44% | 0 | - | 237 |
| snake_abs_exit | 200,862 | +0.43% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,299 | +0.15% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,583 | -0.71% | 1 | 100% | 255 |
| snake_abs_conv | 198,388 | -0.81% | 1 | 100% | 255 |
| snake_anaconda | 192,429 | -3.79% | 3 | 33% | 374 |
| snake_viper_wild | 192,287 | -3.86% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,021 | -5.49% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,895 | -17.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,764 (-5.62%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,074 | +1.04% |
| intraweek | +1,656 | +0.80% |
| gold | +1,299 | +0.79% |
| benchmark | +1,209 | +0.54% |
| random_hold | +315 | +0.15% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -797 | -0.37% |
| unified | -940 | -0.42% |
| intramonth | -1,329 | -0.63% |
| snake_abs_exit | -1,394 | -0.69% |
| snake_abs | -1,566 | -0.78% |
| snake_abs_conv | -1,584 | -0.79% |
| snake_abs_exit_conv | -1,676 | -0.83% |
| snake_anaconda | -2,124 | -1.09% |
| snake_viper_tick | -5,156 | -2.65% |
| snake_viper_wild | -5,256 | -2.66% |

Average per day so far: benchmark Rs +640, unified Rs +565, oracle Rs +317, intramonth Rs +253, random_hold Rs +239, intraweek Rs +205, nifty_calls Rs +45, benchmark_smallcap Rs +24, snake_abs_exit Rs +23, snake_abs_exit_conv Rs +8, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -36, snake_abs_conv Rs -42, snake_anaconda Rs -210, snake_viper_wild Rs -234, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -366, gold Rs -832

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.