# Paper trading report

Updated 2026-11-13 10:07 IST. Model picks as of 2026-11-12. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 221,062 | +10.53% | 0 | - | 236 |
| benchmark | 220,104 | +10.05% | 0 | - | 237 |
| snake_abs_exit_conv | 217,559 | +8.78% | 2 | 50% | 345 |
| snake_abs_exit | 216,921 | +8.46% | 2 | 50% | 345 |
| intraweek | 215,211 | +7.61% | 30 | 53% | 3,302 |
| oracle | 214,187 | +7.09% | 0 | - | 233 |
| snake_abs | 213,670 | +6.83% | 1 | 100% | 255 |
| snake_abs_conv | 213,510 | +6.75% | 1 | 100% | 255 |
| intramonth | 211,686 | +5.84% | 0 | - | 235 |
| random_hold | 207,624 | +3.81% | 10 | 70% | 733 |
| snake_viper_wild | 205,677 | +2.84% | 14 | 50% | 2,496 |
| snake_anaconda | 205,385 | +2.69% | 3 | 33% | 374 |
| benchmark_smallcap | 203,822 | +1.91% | 0 | - | 237 |
| snake_viper_tick | 202,160 | +1.08% | 13 | 46% | 2,299 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 184,209 | -7.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 192,216 (-3.89%).

Profit on 2026-11-13:

| Strategy | Rs | % |
|:---|---:|---:|
| oracle | +1,072 | +0.50% |
| benchmark_smallcap | +617 | +0.30% |
| intraweek | +553 | +0.26% |
| snake_viper_wild | +384 | +0.19% |
| snake_viper_tick | +379 | +0.19% |
| unified | +365 | +0.17% |
| intramonth | +93 | +0.04% |
| snake_nonews | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| random_hold | -430 | -0.21% |
| benchmark | -444 | -0.20% |
| snake_abs_exit | -522 | -0.24% |
| snake_anaconda | -542 | -0.26% |
| gold | -1,101 | -0.59% |
| snake_abs_exit_conv | -1,115 | -0.51% |
| snake_abs_conv | -2,025 | -0.94% |
| snake_abs | -2,041 | -0.95% |

Average per day so far: unified Rs +638, benchmark Rs +609, snake_abs_exit_conv Rs +585, snake_abs_exit Rs +564, intraweek Rs +461, snake_abs_conv Rs +450, snake_abs Rs +441, oracle Rs +430, intramonth Rs +354, random_hold Rs +231, snake_viper_wild Rs +227, snake_anaconda Rs +192, benchmark_smallcap Rs +132, snake_viper_tick Rs +98, nifty_calls Rs +56, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_nonews Rs -358, snake Rs -380, gold Rs -479

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.