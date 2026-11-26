# Paper trading report

Updated 2026-11-26 14:09 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,382 | +12.69% | 0 | - | 237 |
| unified | 223,311 | +11.66% | 0 | - | 236 |
| oracle | 213,046 | +6.52% | 0 | - | 233 |
| intramonth | 210,535 | +5.27% | 0 | - | 235 |
| random_hold | 209,359 | +4.68% | 13 | 69% | 1,037 |
| intraweek | 207,939 | +3.97% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,369 | +0.18% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit | 199,842 | -0.08% | 2 | 50% | 345 |
| snake_abs_exit_conv | 199,311 | -0.34% | 2 | 50% | 345 |
| snake_abs | 197,584 | -1.21% | 1 | 100% | 255 |
| snake_abs_conv | 197,377 | -1.31% | 1 | 100% | 255 |
| snake_viper_wild | 192,345 | -3.83% | 16 | 50% | 2,827 |
| snake_anaconda | 191,286 | -4.36% | 3 | 33% | 374 |
| snake_viper_tick | 189,077 | -5.46% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,224 | -16.89% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,579 (-5.71%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,628 | +0.99% |
| benchmark_smallcap | +1,558 | +0.78% |
| intraweek | +1,196 | +0.58% |
| benchmark | +360 | +0.16% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| random_hold | -133 | -0.06% |
| oracle | -750 | -0.35% |
| unified | -789 | -0.35% |
| intramonth | -1,158 | -0.55% |
| snake_abs_exit | -2,413 | -1.19% |
| snake_abs | -2,566 | -1.28% |
| snake_abs_conv | -2,595 | -1.30% |
| snake_abs_exit_conv | -2,664 | -1.32% |
| snake_anaconda | -3,267 | -1.68% |
| snake_viper_tick | -5,099 | -2.63% |
| snake_viper_wild | -5,199 | -2.63% |

Average per day so far: benchmark Rs +619, unified Rs +569, oracle Rs +318, intramonth Rs +257, random_hold Rs +228, intraweek Rs +194, nifty_calls Rs +45, benchmark_smallcap Rs +10, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_abs_exit Rs -4, snake_abs_exit_conv Rs -18, snake_abs Rs -62, snake_abs_conv Rs -69, snake_viper_wild Rs -232, snake_anaconda Rs -242, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -364, gold Rs -824

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.