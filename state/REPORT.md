# Paper trading report

Updated 2026-11-27 12:07 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,472 | +12.24% | 0 | - | 237 |
| unified | 223,403 | +11.70% | 0 | - | 236 |
| oracle | 211,970 | +5.99% | 0 | - | 233 |
| intramonth | 211,095 | +5.55% | 0 | - | 235 |
| random_hold | 210,091 | +5.05% | 13 | 69% | 1,037 |
| intraweek | 207,761 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,734 | +2.37% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,569 | +1.78% | 2 | 50% | 345 |
| benchmark_smallcap | 201,961 | +0.98% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,319 | +0.16% | 1 | 100% | 255 |
| snake_abs_conv | 200,141 | +0.07% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,746 | -3.13% | 3 | 33% | 374 |
| snake_viper_wild | 192,399 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,131 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,331 | -15.33% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,802 (-5.60%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,657 | +1.82% |
| gold | +3,337 | +2.01% |
| snake_abs_exit_conv | +3,172 | +1.58% |
| snake_abs_conv | +1,774 | +0.89% |
| snake_abs | +1,767 | +0.89% |
| random_hold | +1,497 | +0.72% |
| snake_anaconda | +1,450 | +0.75% |
| benchmark_smallcap | +1,121 | +0.56% |
| intraweek | +713 | +0.34% |
| intramonth | +561 | +0.27% |
| unified | +324 | +0.14% |
| snake_viper_wild | +194 | +0.10% |
| snake_viper_tick | +190 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -265 | -0.12% |
| benchmark | -1,515 | -0.67% |

Average per day so far: benchmark Rs +583, unified Rs +557, oracle Rs +285, intramonth Rs +264, random_hold Rs +240, intraweek Rs +185, snake_abs_exit Rs +121, snake_abs_exit_conv Rs +92, benchmark_smallcap Rs +52, nifty_calls Rs +44, snake_abs Rs +8, snake_abs_conv Rs +4, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -169, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -730

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.