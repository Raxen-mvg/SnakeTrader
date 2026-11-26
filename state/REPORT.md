# Paper trading report

Updated 2026-11-26 13:20 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,803 | +12.90% | 0 | - | 237 |
| unified | 223,474 | +11.74% | 0 | - | 236 |
| oracle | 213,418 | +6.71% | 0 | - | 233 |
| intramonth | 210,687 | +5.34% | 0 | - | 235 |
| random_hold | 209,528 | +4.76% | 13 | 69% | 1,037 |
| intraweek | 208,074 | +4.04% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 200,717 | +0.36% | 0 | - | 237 |
| snake_abs_exit | 200,234 | +0.12% | 2 | 50% | 345 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs_exit_conv | 199,666 | -0.17% | 2 | 50% | 345 |
| snake_abs | 198,080 | -0.96% | 1 | 100% | 255 |
| snake_abs_conv | 197,877 | -1.06% | 1 | 100% | 255 |
| snake_viper_wild | 192,110 | -3.94% | 16 | 50% | 2,827 |
| snake_anaconda | 191,776 | -4.11% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake_viper_tick | 188,847 | -5.58% | 15 | 47% | 2,625 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,125 | -16.94% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,798 (-5.60%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark_smallcap | +1,906 | +0.96% |
| gold | +1,529 | +0.93% |
| intraweek | +1,331 | +0.64% |
| benchmark | +780 | +0.35% |
| random_hold | +35 | +0.02% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -377 | -0.18% |
| unified | -626 | -0.28% |
| intramonth | -1,006 | -0.47% |
| snake_abs_exit | -2,022 | -1.00% |
| snake_abs | -2,070 | -1.03% |
| snake_abs_conv | -2,095 | -1.05% |
| snake_abs_exit_conv | -2,310 | -1.14% |
| snake_anaconda | -2,777 | -1.43% |
| snake_viper_tick | -5,330 | -2.75% |
| snake_viper_wild | -5,434 | -2.75% |

Average per day so far: benchmark Rs +629, unified Rs +573, oracle Rs +327, intramonth Rs +261, random_hold Rs +232, intraweek Rs +197, nifty_calls Rs +45, benchmark_smallcap Rs +19, snake_abs_exit Rs +6, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_abs_exit_conv Rs -9, snake_abs Rs -49, snake_abs_conv Rs -56, snake_anaconda Rs -228, snake_viper_wild Rs -239, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -372, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.