# Paper trading report

Updated 2026-11-27 12:28 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| unified | 223,491 | +11.75% | 0 | - | 236 |
| oracle | 212,106 | +6.05% | 0 | - | 233 |
| intramonth | 211,142 | +5.57% | 0 | - | 235 |
| random_hold | 210,398 | +5.20% | 13 | 69% | 1,037 |
| intraweek | 208,079 | +4.04% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,984 | +2.49% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,770 | +1.89% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,513 | +0.76% | 0 | - | 237 |
| snake_abs | 200,611 | +0.30% | 1 | 100% | 255 |
| snake_abs_conv | 200,436 | +0.22% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,034 | -2.98% | 3 | 33% | 374 |
| snake_viper_wild | 192,471 | -3.76% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,202 | -5.40% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,430 | -15.29% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,894 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,907 | +1.94% |
| gold | +3,436 | +2.07% |
| snake_abs_exit_conv | +3,373 | +1.68% |
| snake_abs_conv | +2,069 | +1.04% |
| snake_abs | +2,058 | +1.04% |
| random_hold | +1,804 | +0.86% |
| snake_anaconda | +1,738 | +0.90% |
| intraweek | +1,031 | +0.50% |
| benchmark_smallcap | +673 | +0.34% |
| intramonth | +609 | +0.29% |
| unified | +413 | +0.18% |
| snake_viper_wild | +266 | +0.14% |
| snake_viper_tick | +261 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -130 | -0.06% |
| benchmark | -1,637 | -0.72% |

Average per day so far: benchmark Rs +580, unified Rs +559, oracle Rs +288, intramonth Rs +265, random_hold Rs +248, intraweek Rs +192, snake_abs_exit Rs +128, snake_abs_exit_conv Rs +97, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -161, snake_viper_wild Rs -221, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -348, gold Rs -728

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.