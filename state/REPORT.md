# Paper trading report

Updated 2026-11-26 09:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,724 | +12.36% | 0 | - | 237 |
| unified | 223,813 | +11.91% | 0 | - | 236 |
| oracle | 213,677 | +6.84% | 0 | - | 233 |
| intramonth | 211,355 | +5.68% | 0 | - | 235 |
| random_hold | 210,299 | +5.15% | 13 | 69% | 1,037 |
| intraweek | 207,715 | +3.86% | 40 | 55% | 4,400 |
| snake_abs_exit | 203,650 | +1.82% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,049 | +1.52% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,853 | +0.43% | 1 | 100% | 255 |
| snake_abs_conv | 200,681 | +0.34% | 1 | 100% | 255 |
| benchmark_smallcap | 200,392 | +0.20% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_wild | 196,218 | -1.89% | 16 | 50% | 2,827 |
| snake_anaconda | 195,150 | -2.42% | 3 | 33% | 374 |
| snake_viper_tick | 192,880 | -3.56% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,178 | -16.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,313 (-5.34%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +2,581 | +1.57% |
| benchmark_smallcap | +1,581 | +0.80% |
| snake_abs_exit | +1,395 | +0.69% |
| snake_abs_exit_conv | +1,073 | +0.53% |
| intraweek | +972 | +0.47% |
| random_hold | +806 | +0.39% |
| snake_abs_conv | +709 | +0.35% |
| snake_abs | +704 | +0.35% |
| snake_anaconda | +597 | +0.31% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -118 | -0.06% |
| unified | -287 | -0.13% |
| benchmark | -298 | -0.13% |
| intramonth | -338 | -0.16% |
| snake_viper_tick | -1,297 | -0.67% |
| snake_viper_wild | -1,325 | -0.67% |

Average per day so far: benchmark Rs +603, unified Rs +581, oracle Rs +334, intramonth Rs +277, random_hold Rs +251, intraweek Rs +188, snake_abs_exit Rs +96, snake_abs_exit_conv Rs +80, nifty_calls Rs +45, snake_abs Rs +22, snake_abs_conv Rs +18, benchmark_smallcap Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_viper_wild Rs -115, snake_anaconda Rs -135, snake_viper_tick Rs -237, snake_nonews Rs -284, snake Rs -304, gold Rs -801

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.