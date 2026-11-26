# Paper trading report

Updated 2026-11-26 13:17 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,566 | +12.78% | 0 | - | 237 |
| unified | 223,429 | +11.71% | 0 | - | 236 |
| oracle | 213,224 | +6.61% | 0 | - | 233 |
| intramonth | 210,610 | +5.30% | 0 | - | 235 |
| random_hold | 209,955 | +4.98% | 13 | 69% | 1,037 |
| intraweek | 208,575 | +4.29% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,560 | +0.28% | 0 | - | 237 |
| snake_abs_exit | 200,023 | +0.01% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,499 | -0.25% | 2 | 50% | 345 |
| snake_abs | 197,870 | -1.06% | 1 | 100% | 255 |
| snake_abs_conv | 197,666 | -1.17% | 1 | 100% | 255 |
| snake_viper_wild | 192,062 | -3.97% | 16 | 50% | 2,827 |
| snake_anaconda | 191,535 | -4.23% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,800 | -5.60% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,224 | -16.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,830 (-5.59%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,832 | +0.89% |
| benchmark_smallcap | +1,749 | +0.88% |
| gold | +1,628 | +0.99% |
| benchmark | +543 | +0.24% |
| random_hold | +462 | +0.22% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -571 | -0.27% |
| unified | -670 | -0.30% |
| intramonth | -1,083 | -0.51% |
| snake_abs_exit | -2,233 | -1.10% |
| snake_abs | -2,280 | -1.14% |
| snake_abs_conv | -2,306 | -1.15% |
| snake_abs_exit_conv | -2,477 | -1.23% |
| snake_anaconda | -3,018 | -1.55% |
| snake_viper_tick | -5,377 | -2.77% |
| snake_viper_wild | -5,482 | -2.77% |

Average per day so far: benchmark Rs +624, unified Rs +571, oracle Rs +323, intramonth Rs +259, random_hold Rs +243, intraweek Rs +209, nifty_calls Rs +45, benchmark_smallcap Rs +15, snake_abs_exit Rs +1, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -13, snake_abs Rs -55, snake_abs_conv Rs -61, snake_anaconda Rs -235, snake_viper_wild Rs -241, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -373, gold Rs -824

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.