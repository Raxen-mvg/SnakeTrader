# Paper trading report

Updated 2026-11-27 13:07 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,181 | +12.09% | 0 | - | 237 |
| unified | 223,384 | +11.69% | 0 | - | 236 |
| oracle | 211,879 | +5.94% | 0 | - | 233 |
| intramonth | 210,920 | +5.46% | 0 | - | 235 |
| random_hold | 210,909 | +5.45% | 13 | 69% | 1,037 |
| intraweek | 208,562 | +4.28% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,621 | +2.31% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,449 | +2.22% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,535 | +0.77% | 0 | - | 237 |
| snake_abs | 200,353 | +0.18% | 1 | 100% | 255 |
| snake_abs_conv | 200,170 | +0.09% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,726 | -3.14% | 3 | 33% | 374 |
| snake_viper_wild | 192,140 | -3.93% | 16 | 50% | 2,827 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,877 | -5.56% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,660 | -15.17% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,940 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +4,052 | +2.02% |
| gold | +3,666 | +2.21% |
| snake_abs_exit | +3,544 | +1.76% |
| random_hold | +2,315 | +1.11% |
| snake_abs_conv | +1,803 | +0.91% |
| snake_abs | +1,801 | +0.91% |
| intraweek | +1,513 | +0.73% |
| snake_anaconda | +1,429 | +0.74% |
| benchmark_smallcap | +695 | +0.35% |
| intramonth | +387 | +0.18% |
| unified | +305 | +0.14% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_viper_tick | -64 | -0.03% |
| snake_viper_wild | -66 | -0.03% |
| oracle | -356 | -0.17% |
| benchmark | -1,805 | -0.80% |

Average per day so far: benchmark Rs +576, unified Rs +557, oracle Rs +283, intramonth Rs +260, random_hold Rs +260, intraweek Rs +204, snake_abs_exit Rs +118, snake_abs_exit_conv Rs +114, nifty_calls Rs +44, benchmark_smallcap Rs +40, snake_abs Rs +9, snake_abs_conv Rs +4, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -170, snake_viper_wild Rs -231, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -359, gold Rs -722

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.