# Paper trading report

Updated 2026-11-25 11:34 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,933 | +12.97% | 0 | - | 237 |
| unified | 225,244 | +12.62% | 0 | - | 236 |
| intramonth | 213,016 | +6.51% | 0 | - | 235 |
| oracle | 211,889 | +5.95% | 0 | - | 233 |
| random_hold | 210,361 | +5.18% | 12 | 75% | 1,009 |
| intraweek | 208,252 | +4.13% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,264 | +1.13% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,669 | +0.83% | 2 | 50% | 345 |
| snake_abs | 201,403 | +0.70% | 1 | 100% | 255 |
| snake_abs_conv | 201,207 | +0.60% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,618 | -0.19% | 0 | - | 237 |
| snake_viper_wild | 196,343 | -1.83% | 16 | 50% | 2,827 |
| snake_anaconda | 193,743 | -3.13% | 3 | 33% | 374 |
| snake_viper_tick | 193,002 | -3.50% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,498 | -17.75% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,472 (-5.26%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,460 | +2.01% |
| random_hold | +1,935 | +0.93% |
| unified | +959 | +0.43% |
| benchmark_smallcap | +639 | +0.32% |
| intramonth | +264 | +0.12% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -453 | -0.21% |
| intraweek | -3,367 | -1.59% |
| snake_abs | -4,058 | -1.98% |
| snake_abs_conv | -4,096 | -2.00% |
| snake_viper_tick | -4,691 | -2.37% |
| snake_viper_wild | -4,781 | -2.38% |
| gold | -4,932 | -2.91% |
| snake_anaconda | -4,960 | -2.50% |
| snake_abs_exit | -5,231 | -2.52% |
| snake_abs_exit_conv | -5,377 | -2.60% |

Average per day so far: benchmark Rs +648, unified Rs +631, intramonth Rs +325, oracle Rs +297, random_hold Rs +259, intraweek Rs +206, snake_abs_exit Rs +61, nifty_calls Rs +46, snake_abs_exit_conv Rs +45, snake_abs Rs +37, snake_abs_conv Rs +33, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -11, snake_viper_wild Rs -114, snake_anaconda Rs -179, snake_viper_tick Rs -241, snake_nonews Rs -292, snake Rs -311, gold Rs -888

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.