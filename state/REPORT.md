# Paper trading report

Updated 2026-11-26 15:01 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,948 | +12.97% | 0 | - | 237 |
| unified | 223,029 | +11.52% | 0 | - | 236 |
| oracle | 212,312 | +6.16% | 0 | - | 233 |
| intramonth | 210,446 | +5.22% | 0 | - | 235 |
| random_hold | 208,826 | +4.41% | 13 | 69% | 1,037 |
| intraweek | 207,384 | +3.69% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,022 | +0.51% | 2 | 50% | 345 |
| benchmark_smallcap | 200,930 | +0.47% | 0 | - | 237 |
| snake_abs_exit_conv | 200,283 | +0.14% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,587 | -0.71% | 1 | 100% | 255 |
| snake_abs_conv | 198,391 | -0.81% | 1 | 100% | 255 |
| snake_viper_wild | 192,364 | -3.82% | 16 | 50% | 2,827 |
| snake_anaconda | 192,199 | -3.90% | 3 | 33% | 374 |
| snake_viper_tick | 189,096 | -5.45% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,109 | -16.95% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,378 (-5.81%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +2,119 | +1.07% |
| gold | +1,512 | +0.92% |
| benchmark | +926 | +0.41% |
| intraweek | +641 | +0.31% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -667 | -0.32% |
| unified | -1,070 | -0.48% |
| snake_abs_exit | -1,234 | -0.61% |
| intramonth | -1,248 | -0.59% |
| oracle | -1,484 | -0.69% |
| snake_abs | -1,563 | -0.78% |
| snake_abs_conv | -1,581 | -0.79% |
| snake_abs_exit_conv | -1,692 | -0.84% |
| snake_anaconda | -2,354 | -1.21% |
| snake_viper_tick | -5,081 | -2.62% |
| snake_viper_wild | -5,179 | -2.62% |

Average per day so far: benchmark Rs +633, unified Rs +562, oracle Rs +300, intramonth Rs +255, random_hold Rs +215, intraweek Rs +180, nifty_calls Rs +45, snake_abs_exit Rs +27, benchmark_smallcap Rs +25, snake_abs_exit_conv Rs +7, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -36, snake_abs_conv Rs -42, snake_anaconda Rs -217, snake_viper_wild Rs -231, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -363, gold Rs -827

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.