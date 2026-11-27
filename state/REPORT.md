# Paper trading report

Updated 2026-11-27 12:37 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,204 | +12.10% | 0 | - | 237 |
| unified | 223,438 | +11.72% | 0 | - | 236 |
| oracle | 212,130 | +6.07% | 0 | - | 233 |
| intramonth | 211,017 | +5.51% | 0 | - | 235 |
| random_hold | 210,380 | +5.19% | 13 | 69% | 1,037 |
| intraweek | 208,120 | +4.06% | 40 | 55% | 4,400 |
| snake_abs_exit | 204,966 | +2.48% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,656 | +1.83% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,659 | +0.83% | 0 | - | 237 |
| snake_abs | 200,493 | +0.25% | 1 | 100% | 255 |
| snake_abs_conv | 200,314 | +0.16% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 193,911 | -3.04% | 3 | 33% | 374 |
| snake_viper_wild | 192,399 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,131 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,874 | -15.06% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,887 (-5.56%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +3,889 | +1.93% |
| gold | +3,880 | +2.34% |
| snake_abs_exit_conv | +3,259 | +1.63% |
| snake_abs_conv | +1,947 | +0.98% |
| snake_abs | +1,941 | +0.98% |
| random_hold | +1,786 | +0.86% |
| snake_anaconda | +1,615 | +0.84% |
| intraweek | +1,072 | +0.52% |
| benchmark_smallcap | +818 | +0.41% |
| intramonth | +483 | +0.23% |
| unified | +359 | +0.16% |
| snake_viper_wild | +194 | +0.10% |
| snake_viper_tick | +190 | +0.10% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -106 | -0.05% |
| benchmark | -1,782 | -0.79% |

Average per day so far: benchmark Rs +576, unified Rs +558, oracle Rs +289, intramonth Rs +262, random_hold Rs +247, intraweek Rs +193, snake_abs_exit Rs +127, snake_abs_exit_conv Rs +94, nifty_calls Rs +44, benchmark_smallcap Rs +44, snake_abs Rs +12, snake_abs_conv Rs +8, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -165, snake_viper_wild Rs -224, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -351, gold Rs -717

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.