# Paper trading report

Updated 2026-11-26 14:05 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,099 | +12.55% | 0 | - | 237 |
| unified | 223,244 | +11.62% | 0 | - | 236 |
| oracle | 212,907 | +6.45% | 0 | - | 233 |
| intramonth | 210,474 | +5.24% | 0 | - | 235 |
| random_hold | 209,349 | +4.67% | 13 | 69% | 1,037 |
| intraweek | 207,625 | +3.81% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,123 | +0.06% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,988 | -0.01% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,416 | -0.29% | 2 | 50% | 345 |
| snake_abs | 197,791 | -1.10% | 1 | 100% | 255 |
| snake_abs_conv | 197,584 | -1.21% | 1 | 100% | 255 |
| snake_viper_wild | 192,345 | -3.83% | 16 | 50% | 2,827 |
| snake_anaconda | 191,490 | -4.25% | 3 | 33% | 374 |
| snake_viper_tick | 189,077 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,498 (-5.75%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,463 | +0.89% |
| benchmark_smallcap | +1,312 | +0.66% |
| intraweek | +882 | +0.43% |
| benchmark | +76 | +0.03% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -144 | -0.07% |
| unified | -856 | -0.38% |
| oracle | -889 | -0.42% |
| intramonth | -1,219 | -0.58% |
| snake_abs_exit | -2,268 | -1.12% |
| snake_abs | -2,359 | -1.18% |
| snake_abs_conv | -2,388 | -1.19% |
| snake_abs_exit_conv | -2,559 | -1.27% |
| snake_anaconda | -3,063 | -1.57% |
| snake_viper_tick | -5,099 | -2.63% |
| snake_viper_wild | -5,199 | -2.63% |

Average per day so far: benchmark Rs +612, unified Rs +567, oracle Rs +315, intramonth Rs +255, random_hold Rs +228, intraweek Rs +186, nifty_calls Rs +45, benchmark_smallcap Rs +3, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -0, snake_abs_exit_conv Rs -15, snake_abs Rs -57, snake_abs_conv Rs -64, snake_viper_wild Rs -232, snake_anaconda Rs -236, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -828

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.