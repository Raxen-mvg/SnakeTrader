# Paper trading report

Updated 2026-11-27 11:55 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,350 | +12.18% | 0 | - | 237 |
| unified | 221,664 | +10.83% | 0 | - | 236 |
| oracle | 211,743 | +5.87% | 0 | - | 233 |
| random_hold | 210,208 | +5.10% | 13 | 69% | 1,037 |
| intramonth | 209,993 | +5.00% | 0 | - | 235 |
| intraweek | 207,837 | +3.92% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,295 | +2.65% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,992 | +2.00% | 2 | 50% | 345 |
| benchmark_smallcap | 201,872 | +0.94% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,606 | +0.30% | 1 | 100% | 255 |
| snake_abs_conv | 200,430 | +0.21% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,156 | -2.92% | 3 | 33% | 374 |
| snake_viper_wild | 192,567 | -3.72% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,296 | -5.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,183 | -15.41% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,296 (-5.85%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,217 | +2.10% |
| snake_abs_exit_conv | +3,595 | +1.79% |
| gold | +3,189 | +1.92% |
| snake_abs_conv | +2,064 | +1.04% |
| snake_abs | +2,054 | +1.03% |
| snake_anaconda | +1,859 | +0.97% |
| random_hold | +1,614 | +0.77% |
| benchmark_smallcap | +1,031 | +0.51% |
| intraweek | +788 | +0.38% |
| snake_viper_wild | +362 | +0.19% |
| snake_viper_tick | +355 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| oracle | -492 | -0.23% |
| intramonth | -540 | -0.26% |
| unified | -1,415 | -0.63% |
| benchmark | -1,637 | -0.72% |

Average per day so far: benchmark Rs +580, unified Rs +516, oracle Rs +280, random_hold Rs +243, intramonth Rs +238, intraweek Rs +187, snake_abs_exit Rs +136, snake_abs_exit_conv Rs +102, benchmark_smallcap Rs +49, nifty_calls Rs +44, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -158, snake_viper_wild Rs -219, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -345, gold Rs -734

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.