# Paper trading report

Updated 2026-11-16 14:04 IST. Model picks as of 2026-11-13. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,504 | +10.25% | 0 | - | 236 |
| benchmark | 219,668 | +9.83% | 0 | - | 237 |
| snake_abs_exit | 213,421 | +6.71% | 2 | 50% | 345 |
| snake_abs_exit_conv | 212,183 | +6.09% | 2 | 50% | 345 |
| oracle | 211,355 | +5.68% | 0 | - | 233 |
| intramonth | 211,224 | +5.61% | 0 | - | 235 |
| intraweek | 211,179 | +5.59% | 35 | 54% | 3,851 |
| snake_abs | 209,568 | +4.78% | 1 | 100% | 255 |
| snake_abs_conv | 209,408 | +4.70% | 1 | 100% | 255 |
| random_hold | 207,659 | +3.83% | 10 | 70% | 733 |
| snake_viper_wild | 205,554 | +2.78% | 14 | 50% | 2,496 |
| snake_anaconda | 203,929 | +1.96% | 3 | 33% | 374 |
| snake_viper_tick | 202,039 | +1.02% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,224 | +0.11% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 181,316 | -9.34% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,351 (-4.82%).

Profit on 2026-11-16:

| Strategy | Rs | % |
|:---|---:|---:|
| unified | +1,484 | +0.68% |
| intramonth | +1,167 | +0.56% |
| snake_viper_wild | +797 | +0.39% |
| snake_viper_tick | +784 | +0.39% |
| random_hold | +433 | +0.21% |
| benchmark | +329 | +0.15% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_anaconda | -963 | -0.47% |
| oracle | -1,743 | -0.82% |
| benchmark_smallcap | -2,646 | -1.30% |
| gold | -2,680 | -1.46% |
| snake_abs_conv | -2,959 | -1.39% |
| snake_abs | -2,972 | -1.40% |
| snake_abs_exit | -3,564 | -1.64% |
| snake_abs_exit_conv | -4,198 | -1.94% |
| intraweek | -4,966 | -2.30% |

Average per day so far: unified Rs +603, benchmark Rs +578, snake_abs_exit Rs +433, snake_abs_exit_conv Rs +393, oracle Rs +334, intramonth Rs +330, intraweek Rs +329, snake_abs_conv Rs +303, snake_abs Rs +299, random_hold Rs +225, snake_viper_wild Rs +214, snake_anaconda Rs +135, snake_viper_tick Rs +89, nifty_calls Rs +54, benchmark_smallcap Rs +7, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -347, snake Rs -368, gold Rs -550

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.