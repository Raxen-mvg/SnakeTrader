# Paper trading report

Updated 2026-11-27 09:31 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,336 | +12.67% | 0 | - | 237 |
| unified | 223,473 | +11.74% | 0 | - | 236 |
| oracle | 212,603 | +6.30% | 0 | - | 233 |
| intramonth | 211,075 | +5.54% | 0 | - | 235 |
| random_hold | 209,510 | +4.75% | 13 | 69% | 1,037 |
| intraweek | 207,656 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,910 | +1.46% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,082 | +1.04% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,401 | +0.70% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,349 | -0.33% | 1 | 100% | 255 |
| snake_abs_conv | 199,159 | -0.42% | 1 | 100% | 255 |
| snake_anaconda | 192,967 | -3.52% | 3 | 33% | 374 |
| snake_viper_wild | 191,865 | -4.07% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,607 | -5.70% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 167,983 | -16.01% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,771 (-5.61%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,989 | +1.20% |
| snake_abs_exit | +1,833 | +0.91% |
| snake_abs_exit_conv | +1,685 | +0.84% |
| random_hold | +916 | +0.44% |
| snake_abs | +797 | +0.40% |
| snake_abs_conv | +793 | +0.40% |
| snake_anaconda | +671 | +0.35% |
| intraweek | +608 | +0.29% |
| benchmark_smallcap | +560 | +0.28% |
| intramonth | +541 | +0.26% |
| unified | +395 | +0.18% |
| oracle | +367 | +0.17% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -334 | -0.18% |
| snake_viper_wild | -341 | -0.18% |
| benchmark | -650 | -0.29% |

Average per day so far: benchmark Rs +603, unified Rs +559, oracle Rs +300, intramonth Rs +264, random_hold Rs +226, intraweek Rs +182, snake_abs_exit Rs +75, snake_abs_exit_conv Rs +53, nifty_calls Rs +44, benchmark_smallcap Rs +37, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -16, snake_abs_conv Rs -22, snake_anaconda Rs -190, snake_viper_wild Rs -239, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -368, gold Rs -762

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.