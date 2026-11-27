# Paper trading report

Updated 2026-11-27 14:19 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,120 | +12.06% | 0 | - | 237 |
| unified | 223,643 | +11.82% | 0 | - | 236 |
| oracle | 212,181 | +6.09% | 0 | - | 233 |
| random_hold | 211,201 | +5.60% | 13 | 69% | 1,037 |
| intramonth | 210,936 | +5.47% | 0 | - | 235 |
| intraweek | 208,217 | +4.11% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,517 | +3.26% | 2 | 50% | 345 |
| snake_abs_exit | 204,309 | +2.15% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,659 | +0.83% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,683 | -0.16% | 1 | 100% | 255 |
| snake_abs_conv | 199,496 | -0.25% | 1 | 100% | 255 |
| snake_anaconda | 193,122 | -3.44% | 3 | 33% | 374 |
| snake_viper_wild | 192,342 | -3.83% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,075 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,663 | -14.67% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,081 (-5.46%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +6,120 | +3.05% |
| gold | +4,669 | +2.81% |
| snake_abs_exit | +3,232 | +1.61% |
| random_hold | +2,607 | +1.25% |
| intraweek | +1,168 | +0.56% |
| snake_abs | +1,130 | +0.57% |
| snake_abs_conv | +1,129 | +0.57% |
| snake_anaconda | +825 | +0.43% |
| benchmark_smallcap | +818 | +0.41% |
| unified | +564 | +0.25% |
| intramonth | +402 | +0.19% |
| snake_viper_wild | +136 | +0.07% |
| snake_viper_tick | +134 | +0.07% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -54 | -0.03% |
| benchmark | -1,867 | -0.83% |

Average per day so far: benchmark Rs +574, unified Rs +563, oracle Rs +290, random_hold Rs +267, intramonth Rs +260, intraweek Rs +196, snake_abs_exit_conv Rs +167, snake_abs_exit Rs +110, nifty_calls Rs +44, benchmark_smallcap Rs +44, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -8, snake_abs_conv Rs -13, snake_anaconda Rs -186, snake_viper_wild Rs -225, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -352, gold Rs -699

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.