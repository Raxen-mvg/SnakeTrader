# Paper trading report

Updated 2026-11-04 12:04 IST. Model picks as of 2026-10-30. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 213,813 | +6.91% | 0 | - | 236 |
| snake_abs_exit_conv | 209,208 | +4.60% | 1 | 100% | 255 |
| snake_abs_exit | 209,075 | +4.54% | 1 | 100% | 260 |
| intraweek | 208,441 | +4.22% | 25 | 48% | 2,757 |
| benchmark | 207,374 | +3.69% | 0 | - | 237 |
| snake_viper_wild | 206,860 | +3.43% | 3 | 33% | 702 |
| snake_abs | 206,118 | +3.06% | 1 | 100% | 255 |
| intramonth | 206,064 | +3.03% | 0 | - | 235 |
| snake_abs_conv | 205,966 | +2.98% | 1 | 100% | 255 |
| snake_viper_tick | 203,256 | +1.63% | 2 | 0% | 532 |
| random_hold | 202,601 | +1.30% | 8 | 62% | 649 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| oracle | 201,014 | +0.51% | 0 | - | 233 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 198,037 | -0.98% | 3 | 33% | 361 |
| benchmark_smallcap | 194,899 | -2.55% | 0 | - | 237 |
| gold | 190,506 | -4.75% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 189,050 (-5.48%).

Profit on 2026-11-04:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +5,228 | +2.82% |
| snake_abs_exit | +5,060 | +2.48% |
| snake_abs_exit_conv | +4,870 | +2.38% |
| snake_abs_conv | +4,825 | +2.40% |
| snake_abs | +4,809 | +2.39% |
| snake_anaconda | +4,213 | +2.17% |
| intraweek | +3,356 | +1.64% |
| random_hold | +2,133 | +1.06% |
| intramonth | +2,093 | +1.03% |
| benchmark_smallcap | +1,962 | +1.02% |
| unified | +1,812 | +0.85% |
| oracle | +1,024 | +0.51% |
| benchmark | +673 | +0.33% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,911 | -1.89% |
| snake_viper_wild | -4,033 | -1.91% |

Average per day so far: unified Rs +512, snake_abs_exit_conv Rs +384, snake_abs_exit Rs +378, snake_viper_wild Rs +361, intraweek Rs +313, benchmark Rs +273, snake_abs_conv Rs +249, snake_abs Rs +245, intramonth Rs +225, snake_viper_tick Rs +203, random_hold Rs +96, nifty_calls Rs +68, oracle Rs +38, statarb Rs +0, intraday Rs +0, gold_trend Rs +0, snake_anaconda Rs -89, benchmark_smallcap Rs -222, gold Rs -352, snake_nonews Rs -444, snake Rs -467

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.