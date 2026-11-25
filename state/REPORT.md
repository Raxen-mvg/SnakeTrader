# Paper trading report

Updated 2026-11-25 09:42 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,797 | +12.90% | 0 | - | 236 |
| benchmark | 224,755 | +12.38% | 0 | - | 237 |
| intramonth | 213,564 | +6.78% | 0 | - | 235 |
| oracle | 213,007 | +6.50% | 0 | - | 233 |
| intraweek | 211,599 | +5.80% | 40 | 55% | 4,400 |
| random_hold | 210,138 | +5.07% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,281 | +1.64% | 2 | 50% | 345 |
| snake_abs_exit_conv | 202,750 | +1.38% | 2 | 50% | 345 |
| snake_abs | 202,045 | +1.02% | 1 | 100% | 255 |
| snake_abs_conv | 201,862 | +0.93% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,753 | -0.12% | 0 | - | 237 |
| snake_viper_wild | 199,252 | -0.37% | 16 | 50% | 2,827 |
| snake_viper_tick | 195,860 | -2.07% | 15 | 47% | 2,625 |
| snake_anaconda | 195,075 | -2.46% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,386 | -17.31% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,311 (-4.84%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,282 | +1.48% |
| random_hold | +1,712 | +0.82% |
| unified | +1,512 | +0.67% |
| intramonth | +812 | +0.38% |
| benchmark_smallcap | +773 | +0.39% |
| oracle | +665 | +0.31% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intraweek | -20 | -0.01% |
| snake_viper_tick | -1,833 | -0.93% |
| snake_viper_wild | -1,872 | -0.93% |
| snake_abs | -3,416 | -1.66% |
| snake_abs_conv | -3,440 | -1.68% |
| snake_anaconda | -3,628 | -1.83% |
| gold | -4,044 | -2.39% |
| snake_abs_exit | -4,214 | -2.03% |
| snake_abs_exit_conv | -4,296 | -2.08% |

Average per day so far: unified Rs +645, benchmark Rs +619, intramonth Rs +339, oracle Rs +325, intraweek Rs +290, random_hold Rs +253, snake_abs_exit Rs +89, snake_abs_exit_conv Rs +74, snake_abs Rs +54, snake_abs_conv Rs +50, nifty_calls Rs +46, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -7, snake_viper_wild Rs -23, snake_anaconda Rs -141, snake_viper_tick Rs -143, snake_nonews Rs -292, snake Rs -311, gold Rs -865

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.