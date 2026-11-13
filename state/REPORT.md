# Paper trading report

Updated 2026-11-13 12:23 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,207 | +10.10% | 0 | - | 236 |
| benchmark | 219,041 | +9.52% | 0 | - | 237 |
| snake_abs_exit_conv | 216,419 | +8.21% | 2 | 50% | 345 |
| snake_abs_exit | 216,352 | +8.18% | 2 | 50% | 345 |
| intraweek | 215,727 | +7.86% | 30 | 53% | 3,302 |
| oracle | 213,118 | +6.56% | 0 | - | 233 |
| snake_abs | 212,618 | +6.31% | 1 | 100% | 255 |
| snake_abs_conv | 212,447 | +6.22% | 1 | 100% | 255 |
| intramonth | 210,705 | +5.35% | 0 | - | 235 |
| random_hold | 207,009 | +3.50% | 10 | 70% | 733 |
| snake_viper_wild | 205,532 | +2.77% | 14 | 50% | 2,496 |
| snake_anaconda | 204,834 | +2.42% | 3 | 33% | 374 |
| benchmark_smallcap | 202,578 | +1.29% | 0 | - | 237 |
| snake_viper_tick | 202,016 | +1.01% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 183,650 | -8.18% | 0 | - | 237 |

Combined allocator (virtual): Rs 191,717 (-4.14%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,069 | +0.50% |
| snake_viper_wild | +239 | +0.12% |
| snake_viper_tick | +234 | +0.12% |
| oracle | +2 | +0.00% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| unified | -490 | -0.22% |
| benchmark_smallcap | -628 | -0.31% |
| intramonth | -888 | -0.42% |
| random_hold | -1,045 | -0.50% |
| snake_abs_exit | -1,091 | -0.50% |
| snake_anaconda | -1,094 | -0.53% |
| benchmark | -1,507 | -0.68% |
| gold | -1,660 | -0.90% |
| snake_abs_exit_conv | -2,255 | -1.03% |
| snake_abs_conv | -3,088 | -1.43% |
| snake_abs | -3,093 | -1.43% |

Average per day so far: unified Rs +612, benchmark Rs +577, snake_abs_exit_conv Rs +547, snake_abs_exit Rs +545, intraweek Rs +477, snake_abs_conv Rs +415, snake_abs Rs +407, oracle Rs +398, intramonth Rs +324, snake_viper_wild Rs +221, random_hold Rs +212, snake_anaconda Rs +173, snake_viper_tick Rs +92, benchmark_smallcap Rs +89, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -495

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.