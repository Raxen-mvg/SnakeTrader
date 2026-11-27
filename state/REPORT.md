# Paper trading report

Updated 2026-11-27 11:52 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,258 | +12.13% | 0 | - | 237 |
| unified | 221,799 | +10.90% | 0 | - | 236 |
| oracle | 211,768 | +5.88% | 0 | - | 233 |
| random_hold | 210,158 | +5.08% | 13 | 69% | 1,037 |
| intramonth | 210,100 | +5.05% | 0 | - | 235 |
| intraweek | 207,754 | +3.88% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,269 | +2.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,994 | +2.00% | 2 | 50% | 345 |
| benchmark_smallcap | 201,849 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,585 | +0.29% | 1 | 100% | 255 |
| snake_abs_conv | 200,409 | +0.20% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,134 | -2.93% | 3 | 33% | 374 |
| snake_viper_wild | 192,524 | -3.74% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,253 | -5.37% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,322 (-5.84%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,191 | +2.08% |
| snake_abs_exit_conv | +3,597 | +1.79% |
| gold | +3,239 | +1.95% |
| snake_abs_conv | +2,043 | +1.03% |
| snake_abs | +2,033 | +1.02% |
| snake_anaconda | +1,837 | +0.95% |
| random_hold | +1,564 | +0.75% |
| benchmark_smallcap | +1,009 | +0.50% |
| intraweek | +705 | +0.34% |
| snake_viper_wild | +318 | +0.17% |
| snake_viper_tick | +312 | +0.17% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -433 | -0.21% |
| oracle | -468 | -0.22% |
| unified | -1,280 | -0.57% |
| benchmark | -1,729 | -0.77% |

Average per day so far: benchmark Rs +578, unified Rs +519, oracle Rs +280, random_hold Rs +242, intramonth Rs +240, intraweek Rs +185, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +102, benchmark_smallcap Rs +49, nifty_calls Rs +44, snake_abs Rs +15, snake_abs_conv Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -159, snake_viper_wild Rs -220, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -347, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.