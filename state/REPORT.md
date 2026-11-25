# Paper trading report

Updated 2026-11-25 11:27 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,956 | +12.98% | 0 | - | 237 |
| unified | 225,010 | +12.51% | 0 | - | 236 |
| intramonth | 212,828 | +6.41% | 0 | - | 235 |
| oracle | 211,816 | +5.91% | 0 | - | 233 |
| random_hold | 210,273 | +5.14% | 12 | 75% | 1,009 |
| intraweek | 208,346 | +4.17% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,080 | +1.04% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,547 | +0.77% | 2 | 50% | 345 |
| snake_abs | 201,486 | +0.74% | 1 | 100% | 255 |
| snake_abs_conv | 201,290 | +0.65% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,517 | -0.24% | 0 | - | 237 |
| snake_viper_wild | 196,022 | -1.99% | 16 | 50% | 2,827 |
| snake_anaconda | 193,637 | -3.18% | 3 | 33% | 374 |
| snake_viper_tick | 192,687 | -3.66% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 164,514 | -17.74% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,385 (-5.31%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +4,483 | +2.02% |
| random_hold | +1,846 | +0.89% |
| unified | +725 | +0.32% |
| benchmark_smallcap | +538 | +0.27% |
| intramonth | +76 | +0.04% |
| snake | +0 | +0.00% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| statarb | +0 | +0.00% |
| oracle | -526 | -0.25% |
| intraweek | -3,273 | -1.55% |
| snake_abs | -3,975 | -1.94% |
| snake_abs_conv | -4,012 | -1.95% |
| gold | -4,916 | -2.90% |
| snake_viper_tick | -5,006 | -2.53% |
| snake_anaconda | -5,067 | -2.55% |
| snake_viper_wild | -5,103 | -2.54% |
| snake_abs_exit | -5,414 | -2.61% |
| snake_abs_exit_conv | -5,499 | -2.66% |

Average per day so far: benchmark Rs +649, unified Rs +625, intramonth Rs +321, oracle Rs +295, random_hold Rs +257, intraweek Rs +209, snake_abs_exit Rs +56, nifty_calls Rs +46, snake_abs_exit_conv Rs +42, snake_abs Rs +39, snake_abs_conv Rs +35, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -13, snake_viper_wild Rs -124, snake_anaconda Rs -182, snake_viper_tick Rs -252, snake_nonews Rs -292, snake Rs -311, gold Rs -887

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.