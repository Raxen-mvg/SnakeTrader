# Paper trading report

Updated 2026-11-25 10:49 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,459 | +12.73% | 0 | - | 237 |
| unified | 225,250 | +12.62% | 0 | - | 236 |
| intramonth | 212,980 | +6.49% | 0 | - | 235 |
| oracle | 212,017 | +6.01% | 0 | - | 233 |
| random_hold | 209,688 | +4.84% | 12 | 75% | 1,009 |
| intraweek | 207,945 | +3.97% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,285 | +1.14% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,797 | +0.90% | 2 | 50% | 345 |
| snake_abs | 201,262 | +0.63% | 1 | 100% | 255 |
| snake_abs_conv | 201,073 | +0.54% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,641 | -0.18% | 0 | - | 237 |
| snake_viper_wild | 195,474 | -2.26% | 16 | 50% | 2,827 |
| snake_anaconda | 193,618 | -3.19% | 3 | 33% | 374 |
| snake_viper_tick | 192,151 | -3.92% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,764 | -17.12% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,351 (-5.32%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,986 | +1.80% |
| random_hold | +1,262 | +0.61% |
| unified | +965 | +0.43% |
| benchmark_smallcap | +661 | +0.33% |
| intramonth | +228 | +0.11% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -325 | -0.15% |
| gold | -3,666 | -2.16% |
| intraweek | -3,674 | -1.74% |
| snake_abs | -4,198 | -2.04% |
| snake_abs_conv | -4,230 | -2.06% |
| snake_anaconda | -5,085 | -2.56% |
| snake_abs_exit | -5,210 | -2.51% |
| snake_abs_exit_conv | -5,249 | -2.54% |
| snake_viper_tick | -5,541 | -2.80% |
| snake_viper_wild | -5,650 | -2.81% |

Average per day so far: benchmark Rs +636, unified Rs +631, intramonth Rs +324, oracle Rs +300, random_hold Rs +242, intraweek Rs +199, snake_abs_exit Rs +62, snake_abs_exit_conv Rs +49, nifty_calls Rs +46, snake_abs Rs +33, snake_abs_conv Rs +29, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -10, snake_viper_wild Rs -141, snake_anaconda Rs -182, snake_viper_tick Rs -271, snake_nonews Rs -292, snake Rs -311, gold Rs -856

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.