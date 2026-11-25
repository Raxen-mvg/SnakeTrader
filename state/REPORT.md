# Paper trading report

Updated 2026-11-25 10:13 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,318 | +12.66% | 0 | - | 236 |
| benchmark | 224,510 | +12.26% | 0 | - | 237 |
| intramonth | 212,940 | +6.47% | 0 | - | 235 |
| oracle | 212,897 | +6.45% | 0 | - | 233 |
| random_hold | 209,572 | +4.79% | 12 | 75% | 1,009 |
| intraweek | 207,850 | +3.92% | 40 | 55% | 4,400 |
| snake_abs_exit | 202,009 | +1.00% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,341 | +0.67% | 2 | 50% | 345 |
| snake_abs | 200,915 | +0.46% | 1 | 100% | 255 |
| snake_abs_conv | 200,726 | +0.36% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,361 | -0.32% | 0 | - | 237 |
| snake_viper_wild | 197,956 | -1.02% | 16 | 50% | 2,827 |
| snake_viper_tick | 194,591 | -2.71% | 15 | 47% | 2,625 |
| snake_anaconda | 193,678 | -3.16% | 3 | 33% | 374 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,517 | -17.24% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,419 (-5.29%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,037 | +1.37% |
| random_hold | +1,145 | +0.55% |
| unified | +1,032 | +0.46% |
| oracle | +554 | +0.26% |
| benchmark_smallcap | +381 | +0.19% |
| intramonth | +189 | +0.09% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_viper_tick | -3,102 | -1.57% |
| snake_viper_wild | -3,168 | -1.57% |
| intraweek | -3,769 | -1.78% |
| gold | -3,913 | -2.31% |
| snake_abs | -4,546 | -2.21% |
| snake_abs_conv | -4,577 | -2.23% |
| snake_anaconda | -5,025 | -2.53% |
| snake_abs_exit | -5,486 | -2.64% |
| snake_abs_exit_conv | -5,704 | -2.75% |

Average per day so far: unified Rs +633, benchmark Rs +613, intramonth Rs +324, oracle Rs +322, random_hold Rs +239, intraweek Rs +196, snake_abs_exit Rs +54, nifty_calls Rs +46, snake_abs_exit_conv Rs +36, snake_abs Rs +24, snake_abs_conv Rs +20, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -18, snake_viper_wild Rs -64, snake_anaconda Rs -181, snake_viper_tick Rs -187, snake_nonews Rs -292, snake Rs -311, gold Rs -862

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.