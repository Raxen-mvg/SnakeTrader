# Paper trading report

Updated 2026-11-27 13:01 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,128 | +12.06% | 0 | - | 237 |
| unified | 223,352 | +11.68% | 0 | - | 236 |
| oracle | 211,894 | +5.95% | 0 | - | 233 |
| intramonth | 210,896 | +5.45% | 0 | - | 235 |
| random_hold | 210,781 | +5.39% | 13 | 69% | 1,037 |
| intraweek | 208,464 | +4.23% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,576 | +2.29% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,136 | +2.07% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,535 | +0.77% | 0 | - | 237 |
| snake_abs | 200,268 | +0.13% | 1 | 100% | 255 |
| snake_abs_conv | 200,085 | +0.04% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,643 | -3.18% | 3 | 33% | 374 |
| snake_viper_wild | 192,140 | -3.93% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,877 | -5.56% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,693 | -15.15% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,901 (-5.55%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,739 | +1.87% |
| gold | +3,699 | +2.23% |
| snake_abs_exit | +3,498 | +1.74% |
| random_hold | +2,187 | +1.05% |
| snake_abs_conv | +1,718 | +0.87% |
| snake_abs | +1,716 | +0.86% |
| intraweek | +1,415 | +0.68% |
| snake_anaconda | +1,347 | +0.70% |
| benchmark_smallcap | +695 | +0.35% |
| intramonth | +362 | +0.17% |
| unified | +274 | +0.12% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -64 | -0.03% |
| snake_viper_wild | -66 | -0.03% |
| oracle | -341 | -0.16% |
| benchmark | -1,859 | -0.82% |

Average per day so far: benchmark Rs +574, unified Rs +556, oracle Rs +283, intramonth Rs +259, random_hold Rs +257, intraweek Rs +202, snake_abs_exit Rs +117, snake_abs_exit_conv Rs +106, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +7, snake_abs_conv Rs +2, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -172, snake_viper_wild Rs -231, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -359, gold Rs -722

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.