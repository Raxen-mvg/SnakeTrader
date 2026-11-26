# Paper trading report

Updated 2026-11-26 15:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,926 | +12.96% | 0 | - | 237 |
| unified | 223,105 | +11.55% | 0 | - | 236 |
| oracle | 212,298 | +6.15% | 0 | - | 233 |
| intramonth | 210,550 | +5.28% | 0 | - | 235 |
| random_hold | 208,513 | +4.26% | 13 | 69% | 1,037 |
| intraweek | 206,993 | +3.50% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,529 | +0.77% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,960 | +0.48% | 2 | 50% | 345 |
| benchmark_smallcap | 200,829 | +0.41% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,074 | -0.46% | 1 | 100% | 255 |
| snake_abs_conv | 198,891 | -0.55% | 1 | 100% | 255 |
| snake_anaconda | 192,872 | -3.56% | 3 | 33% | 374 |
| snake_viper_wild | 192,652 | -3.67% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,378 | -5.31% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,158 | -16.92% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,355 (-5.82%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,018 | +1.01% |
| gold | +1,562 | +0.95% |
| benchmark | +903 | +0.40% |
| intraweek | +249 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs_exit | -726 | -0.36% |
| random_hold | -980 | -0.47% |
| unified | -995 | -0.44% |
| snake_abs_exit_conv | -1,015 | -0.50% |
| snake_abs | -1,076 | -0.54% |
| snake_abs_conv | -1,081 | -0.54% |
| intramonth | -1,143 | -0.54% |
| oracle | -1,498 | -0.70% |
| snake_anaconda | -1,681 | -0.86% |
| snake_viper_tick | -4,799 | -2.47% |
| snake_viper_wild | -4,891 | -2.48% |

Average per day so far: benchmark Rs +632, unified Rs +564, oracle Rs +300, intramonth Rs +257, random_hold Rs +208, intraweek Rs +171, nifty_calls Rs +45, snake_abs_exit Rs +40, snake_abs_exit_conv Rs +25, benchmark_smallcap Rs +22, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -24, snake_abs_conv Rs -29, snake_anaconda Rs -198, snake_viper_wild Rs -223, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -354, gold Rs -825

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.