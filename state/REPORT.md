# Paper trading report

Updated 2026-11-25 15:01 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,954 | +12.48% | 0 | - | 237 |
| unified | 224,477 | +12.24% | 0 | - | 236 |
| oracle | 213,499 | +6.75% | 0 | - | 233 |
| intramonth | 212,029 | +6.01% | 0 | - | 235 |
| random_hold | 209,681 | +4.84% | 12 | 75% | 1,009 |
| intraweek | 207,329 | +3.66% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,382 | +1.19% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,125 | +1.06% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,427 | +0.21% | 1 | 100% | 255 |
| snake_abs_conv | 200,249 | +0.12% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,159 | -0.42% | 0 | - | 237 |
| snake_viper_wild | 197,615 | -1.19% | 16 | 50% | 2,827 |
| snake_anaconda | 194,437 | -2.78% | 3 | 33% | 374 |
| snake_viper_tick | 194,247 | -2.88% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,794 | -17.60% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,245 (-5.38%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,481 | +1.57% |
| random_hold | +1,254 | +0.60% |
| oracle | +1,157 | +0.55% |
| unified | +192 | +0.09% |
| benchmark_smallcap | +179 | +0.09% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -722 | -0.34% |
| snake_viper_tick | -3,445 | -1.74% |
| snake_viper_wild | -3,509 | -1.75% |
| snake_anaconda | -4,267 | -2.15% |
| intraweek | -4,290 | -2.03% |
| gold | -4,636 | -2.74% |
| snake_abs_exit_conv | -4,921 | -2.38% |
| snake_abs | -5,033 | -2.45% |
| snake_abs_conv | -5,054 | -2.46% |
| snake_abs_exit | -5,112 | -2.46% |

Average per day so far: benchmark Rs +624, unified Rs +612, oracle Rs +337, intramonth Rs +301, random_hold Rs +242, intraweek Rs +183, snake_abs_exit Rs +64, snake_abs_exit_conv Rs +57, nifty_calls Rs +46, snake_abs Rs +11, snake_abs_conv Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -23, snake_viper_wild Rs -75, snake_anaconda Rs -159, snake_viper_tick Rs -198, snake_nonews Rs -292, snake Rs -311, gold Rs -880

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.