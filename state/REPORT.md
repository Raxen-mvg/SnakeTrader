# Paper trading report

Updated 2026-11-25 15:07 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,076 | +12.54% | 0 | - | 237 |
| unified | 224,052 | +12.03% | 0 | - | 236 |
| oracle | 213,592 | +6.80% | 0 | - | 233 |
| intramonth | 211,568 | +5.78% | 0 | - | 235 |
| random_hold | 209,444 | +4.72% | 12 | 75% | 1,009 |
| intraweek | 206,966 | +3.48% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,336 | +1.17% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,036 | +1.02% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,307 | +0.15% | 1 | 100% | 255 |
| snake_abs_conv | 200,130 | +0.07% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,013 | -0.49% | 0 | - | 237 |
| snake_viper_wild | 197,490 | -1.25% | 16 | 50% | 2,827 |
| snake_anaconda | 194,604 | -2.70% | 3 | 33% | 374 |
| snake_viper_tick | 194,125 | -2.94% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,040 | -17.48% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,054 (-5.47%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,603 | +1.63% |
| oracle | +1,249 | +0.59% |
| random_hold | +1,018 | +0.49% |
| benchmark_smallcap | +34 | +0.02% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| unified | -234 | -0.10% |
| intramonth | -1,184 | -0.56% |
| snake_viper_tick | -3,567 | -1.80% |
| snake_viper_wild | -3,634 | -1.81% |
| snake_anaconda | -4,099 | -2.06% |
| gold | -4,389 | -2.59% |
| intraweek | -4,653 | -2.20% |
| snake_abs_exit_conv | -5,009 | -2.42% |
| snake_abs | -5,154 | -2.51% |
| snake_abs_exit | -5,159 | -2.49% |
| snake_abs_conv | -5,172 | -2.52% |

Average per day so far: benchmark Rs +627, unified Rs +601, oracle Rs +340, intramonth Rs +289, random_hold Rs +236, intraweek Rs +174, snake_abs_exit Rs +63, snake_abs_exit_conv Rs +55, nifty_calls Rs +46, snake_abs Rs +8, snake_abs_conv Rs +4, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -27, snake_viper_wild Rs -78, snake_anaconda Rs -154, snake_viper_tick Rs -203, snake_nonews Rs -292, snake Rs -311, gold Rs -874

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.