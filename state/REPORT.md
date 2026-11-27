# Paper trading report

Updated 2026-11-27 11:58 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 224,411 | +12.21% | 0 | - | 237 |
| unified | 222,528 | +11.26% | 0 | - | 236 |
| oracle | 211,703 | +5.85% | 0 | - | 233 |
| intramonth | 210,475 | +5.24% | 0 | - | 235 |
| random_hold | 210,188 | +5.09% | 13 | 69% | 1,037 |
| intraweek | 207,785 | +3.89% | 40 | 55% | 4,400 |
| snake_abs_exit | 205,267 | +2.63% | 2 | 50% | 345 |
| snake_abs_exit_conv | 204,309 | +2.15% | 2 | 50% | 345 |
| benchmark_smallcap | 201,860 | +0.93% | 0 | - | 237 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs | 200,586 | +0.29% | 1 | 100% | 255 |
| snake_abs_conv | 200,410 | +0.20% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 194,020 | -2.99% | 3 | 33% | 374 |
| snake_viper_wild | 192,610 | -3.69% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,338 | -5.33% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,233 | -15.38% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,509 (-5.75%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit | +4,190 | +2.08% |
| snake_abs_exit_conv | +3,912 | +1.95% |
| gold | +3,239 | +1.95% |
| snake_abs_conv | +2,043 | +1.03% |
| snake_abs | +2,034 | +1.02% |
| snake_anaconda | +1,724 | +0.90% |
| random_hold | +1,594 | +0.76% |
| benchmark_smallcap | +1,020 | +0.51% |
| intraweek | +736 | +0.36% |
| snake_viper_wild | +405 | +0.21% |
| snake_viper_tick | +397 | +0.21% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| intramonth | -58 | -0.03% |
| oracle | -533 | -0.25% |
| unified | -551 | -0.25% |
| benchmark | -1,576 | -0.70% |

Average per day so far: benchmark Rs +581, unified Rs +536, oracle Rs +279, intramonth Rs +249, random_hold Rs +243, intraweek Rs +185, snake_abs_exit Rs +135, snake_abs_exit_conv Rs +110, benchmark_smallcap Rs +49, nifty_calls Rs +44, snake_abs Rs +15, snake_abs_conv Rs +11, gold_trend Rs +0, statarb Rs +0, intraday Rs +0, snake_anaconda Rs -162, snake_viper_wild Rs -217, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -344, gold Rs -733

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.