# Paper trading report

Updated 2026-11-25 13:55 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,584 | +12.29% | 0 | - | 236 |
| benchmark | 224,197 | +12.10% | 0 | - | 237 |
| oracle | 212,437 | +6.22% | 0 | - | 233 |
| intramonth | 212,150 | +6.08% | 0 | - | 235 |
| random_hold | 209,496 | +4.75% | 12 | 75% | 1,009 |
| intraweek | 207,421 | +3.71% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,563 | +0.78% | 2 | 50% | 345 |
| snake_abs_exit_conv | 201,315 | +0.66% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,880 | -0.06% | 1 | 100% | 255 |
| snake_abs_conv | 199,686 | -0.16% | 1 | 100% | 255 |
| benchmark_smallcap | 198,755 | -0.62% | 0 | - | 237 |
| snake_viper_wild | 197,370 | -1.31% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,008 | -3.00% | 15 | 47% | 2,625 |
| snake_anaconda | 193,422 | -3.29% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,777 | -17.61% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,947 (-5.53%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,723 | +1.23% |
| random_hold | +1,070 | +0.51% |
| unified | +298 | +0.13% |
| oracle | +95 | +0.04% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| benchmark_smallcap | -224 | -0.11% |
| intramonth | -601 | -0.28% |
| snake_viper_tick | -3,685 | -1.86% |
| snake_viper_wild | -3,754 | -1.87% |
| intraweek | -4,198 | -1.98% |
| gold | -4,653 | -2.75% |
| snake_anaconda | -5,282 | -2.66% |
| snake_abs | -5,581 | -2.72% |
| snake_abs_conv | -5,616 | -2.74% |
| snake_abs_exit_conv | -5,731 | -2.77% |
| snake_abs_exit | -5,932 | -2.86% |

Average per day so far: unified Rs +615, benchmark Rs +605, oracle Rs +311, intramonth Rs +304, random_hold Rs +237, intraweek Rs +186, nifty_calls Rs +46, snake_abs_exit Rs +42, snake_abs_exit_conv Rs +36, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_abs Rs -3, snake_abs_conv Rs -8, benchmark_smallcap Rs -35, snake_viper_wild Rs -82, snake_anaconda Rs -188, snake_viper_tick Rs -207, snake_nonews Rs -292, snake Rs -311, gold Rs -881

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.