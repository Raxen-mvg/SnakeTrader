# Paper trading report

Updated 2026-11-25 09:28 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,724 | +12.86% | 0 | - | 236 |
| benchmark | 224,549 | +12.27% | 0 | - | 237 |
| intramonth | 213,366 | +6.68% | 0 | - | 235 |
| oracle | 212,773 | +6.39% | 0 | - | 233 |
| intraweek | 211,847 | +5.92% | 40 | 55% | 4,400 |
| random_hold | 209,407 | +4.70% | 12 | 75% | 1,009 |
| snake_abs_exit | 203,765 | +1.88% | 2 | 50% | 345 |
| snake_abs_exit_conv | 203,115 | +1.56% | 2 | 50% | 345 |
| snake_abs | 202,676 | +1.34% | 1 | 100% | 255 |
| snake_abs_conv | 202,493 | +1.25% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,164 | +0.08% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,786 | -0.11% | 0 | - | 237 |
| snake_viper_tick | 196,753 | -1.62% | 15 | 47% | 2,625 |
| snake_anaconda | 195,497 | -2.25% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,566 | -17.22% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,269 (-4.87%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,075 | +1.39% |
| unified | +1,439 | +0.64% |
| random_hold | +981 | +0.47% |
| benchmark_smallcap | +807 | +0.41% |
| intramonth | +615 | +0.29% |
| oracle | +431 | +0.20% |
| intraweek | +228 | +0.11% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -940 | -0.47% |
| snake_viper_wild | -960 | -0.48% |
| snake_abs | -2,785 | -1.35% |
| snake_abs_conv | -2,810 | -1.37% |
| snake_anaconda | -3,206 | -1.61% |
| snake_abs_exit | -3,730 | -1.80% |
| gold | -3,863 | -2.28% |
| snake_abs_exit_conv | -3,930 | -1.90% |

Average per day so far: unified Rs +643, benchmark Rs +614, intramonth Rs +334, oracle Rs +319, intraweek Rs +296, random_hold Rs +235, snake_abs_exit Rs +102, snake_abs_exit_conv Rs +84, snake_abs Rs +70, snake_abs_conv Rs +67, nifty_calls Rs +46, snake_viper_wild Rs +5, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_viper_tick Rs -112, snake_anaconda Rs -129, snake_nonews Rs -292, snake Rs -311, gold Rs -861

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.