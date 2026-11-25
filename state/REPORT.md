# Paper trading report

Updated 2026-11-25 15:04 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,977 | +12.49% | 0 | - | 237 |
| unified | 224,401 | +12.20% | 0 | - | 236 |
| oracle | 213,388 | +6.69% | 0 | - | 233 |
| intramonth | 211,953 | +5.98% | 0 | - | 235 |
| random_hold | 209,598 | +4.80% | 12 | 75% | 1,009 |
| intraweek | 207,121 | +3.56% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,590 | +1.29% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,284 | +1.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,586 | +0.29% | 1 | 100% | 255 |
| snake_abs_conv | 200,408 | +0.20% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,058 | -0.47% | 0 | - | 237 |
| snake_viper_wild | 197,615 | -1.19% | 16 | 50% | 2,827 |
| snake_anaconda | 194,593 | -2.70% | 3 | 33% | 374 |
| snake_viper_tick | 194,247 | -2.88% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,860 | -17.57% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,196 (-5.40%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,504 | +1.58% |
| random_hold | +1,172 | +0.56% |
| oracle | +1,046 | +0.49% |
| unified | +116 | +0.05% |
| benchmark_smallcap | +78 | +0.04% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -799 | -0.38% |
| snake_viper_tick | -3,445 | -1.74% |
| snake_viper_wild | -3,509 | -1.75% |
| snake_anaconda | -4,111 | -2.07% |
| intraweek | -4,498 | -2.13% |
| gold | -4,570 | -2.70% |
| snake_abs_exit_conv | -4,761 | -2.30% |
| snake_abs | -4,875 | -2.37% |
| snake_abs_conv | -4,894 | -2.38% |
| snake_abs_exit | -4,905 | -2.36% |

Average per day so far: benchmark Rs +624, unified Rs +610, oracle Rs +335, intramonth Rs +299, random_hold Rs +240, intraweek Rs +178, snake_abs_exit Rs +70, snake_abs_exit_conv Rs +62, nifty_calls Rs +46, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -26, snake_viper_wild Rs -75, snake_anaconda Rs -154, snake_viper_tick Rs -198, snake_nonews Rs -292, snake Rs -311, gold Rs -879

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.