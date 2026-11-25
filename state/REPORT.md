# Paper trading report

Updated 2026-11-25 14:30 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,579 | +12.29% | 0 | - | 237 |
| unified | 224,255 | +12.13% | 0 | - | 236 |
| oracle | 212,580 | +6.29% | 0 | - | 233 |
| intramonth | 211,746 | +5.87% | 0 | - | 235 |
| random_hold | 209,607 | +4.80% | 12 | 75% | 1,009 |
| intraweek | 206,958 | +3.48% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,246 | +0.62% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,902 | +0.45% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,651 | -0.17% | 1 | 100% | 255 |
| snake_abs_conv | 199,449 | -0.28% | 1 | 100% | 255 |
| benchmark_smallcap | 198,755 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 197,039 | -1.48% | 16 | 50% | 2,827 |
| snake_viper_tick | 193,683 | -3.16% | 15 | 47% | 2,625 |
| snake_anaconda | 192,985 | -3.51% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,106 | -17.45% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,779 (-5.61%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,106 | +1.40% |
| random_hold | +1,181 | +0.57% |
| oracle | +238 | +0.11% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| unified | -30 | -0.01% |
| benchmark_smallcap | -224 | -0.11% |
| intramonth | -1,005 | -0.47% |
| snake_viper_tick | -4,009 | -2.03% |
| snake_viper_wild | -4,085 | -2.03% |
| gold | -4,324 | -2.55% |
| intraweek | -4,661 | -2.20% |
| snake_anaconda | -5,718 | -2.88% |
| snake_abs | -5,810 | -2.83% |
| snake_abs_conv | -5,854 | -2.85% |
| snake_abs_exit_conv | -6,144 | -2.97% |
| snake_abs_exit | -6,249 | -3.01% |

Average per day so far: benchmark Rs +614, unified Rs +606, oracle Rs +315, intramonth Rs +294, random_hold Rs +240, intraweek Rs +174, nifty_calls Rs +46, snake_abs_exit Rs +34, snake_abs_exit_conv Rs +24, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -9, snake_abs_conv Rs -15, benchmark_smallcap Rs -35, snake_viper_wild Rs -93, snake_anaconda Rs -200, snake_viper_tick Rs -218, snake_nonews Rs -292, snake Rs -311, gold Rs -872

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.