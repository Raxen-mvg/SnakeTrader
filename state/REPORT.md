# Paper trading report

Updated 2026-11-27 09:42 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,711 | +12.86% | 0 | - | 237 |
| unified | 223,557 | +11.78% | 0 | - | 236 |
| oracle | 212,737 | +6.37% | 0 | - | 233 |
| intramonth | 211,269 | +5.63% | 0 | - | 235 |
| random_hold | 209,641 | +4.82% | 13 | 69% | 1,037 |
| intraweek | 207,636 | +3.82% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,679 | +2.34% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,763 | +1.88% | 2 | 50% | 345 |
| benchmark_smallcap | 202,163 | +1.08% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,555 | +0.28% | 1 | 100% | 255 |
| snake_abs_conv | 200,376 | +0.19% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,391 | -2.80% | 3 | 33% | 374 |
| snake_viper_wild | 192,988 | -3.51% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,707 | -5.15% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 168,016 | -15.99% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,932 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,602 | +1.79% |
| snake_abs_exit_conv | +3,366 | +1.68% |
| snake_anaconda | +2,095 | +1.09% |
| gold | +2,022 | +1.22% |
| snake_abs_conv | +2,010 | +1.01% |
| snake_abs | +2,003 | +1.01% |
| benchmark_smallcap | +1,323 | +0.66% |
| random_hold | +1,047 | +0.50% |
| snake_viper_wild | +782 | +0.41% |
| snake_viper_tick | +766 | +0.41% |
| intramonth | +736 | +0.35% |
| intraweek | +588 | +0.28% |
| oracle | +501 | +0.24% |
| unified | +478 | +0.21% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark | -275 | -0.12% |

Average per day so far: benchmark Rs +612, unified Rs +561, oracle Rs +303, intramonth Rs +268, random_hold Rs +230, intraweek Rs +182, snake_abs_exit Rs +120, snake_abs_exit_conv Rs +96, benchmark_smallcap Rs +57, nifty_calls Rs +44, snake_abs Rs +14, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -152, snake_viper_wild Rs -206, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -332, gold Rs -762

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.