# Paper trading report

Updated 2026-11-27 11:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,587 | +12.29% | 0 | - | 237 |
| unified | 222,520 | +11.26% | 0 | - | 236 |
| oracle | 212,255 | +6.13% | 0 | - | 233 |
| intramonth | 210,312 | +5.16% | 0 | - | 235 |
| random_hold | 210,061 | +5.03% | 13 | 69% | 1,037 |
| intraweek | 207,657 | +3.83% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,363 | +2.68% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,117 | +2.06% | 2 | 50% | 345 |
| benchmark_smallcap | 202,096 | +1.05% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,993 | +0.50% | 1 | 100% | 255 |
| snake_abs_conv | 200,817 | +0.41% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,562 | -2.72% | 3 | 33% | 374 |
| snake_viper_wild | 193,359 | -3.32% | 16 | 50% | 2,827 |
| snake_viper_tick | 190,071 | -4.96% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,582 (-5.71%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,286 | +2.13% |
| snake_abs_exit_conv | +3,720 | +1.86% |
| gold | +3,239 | +1.95% |
| snake_abs_conv | +2,451 | +1.24% |
| snake_abs | +2,441 | +1.23% |
| snake_anaconda | +2,266 | +1.18% |
| random_hold | +1,467 | +0.70% |
| benchmark_smallcap | +1,256 | +0.62% |
| snake_viper_wild | +1,154 | +0.60% |
| snake_viper_tick | +1,130 | +0.60% |
| intraweek | +609 | +0.29% |
| oracle | +19 | +0.01% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -221 | -0.10% |
| unified | -558 | -0.25% |
| benchmark | -1,400 | -0.62% |

Average per day so far: benchmark Rs +585, unified Rs +536, oracle Rs +292, intramonth Rs +246, random_hold Rs +240, intraweek Rs +182, snake_abs_exit Rs +138, snake_abs_exit_conv Rs +106, benchmark_smallcap Rs +55, nifty_calls Rs +44, snake_abs Rs +25, snake_abs_conv Rs +21, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -147, snake_viper_wild Rs -195, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -320, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.