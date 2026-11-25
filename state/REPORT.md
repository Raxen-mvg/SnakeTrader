# Paper trading report

Updated 2026-11-25 09:21 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 225,555 | +12.78% | 0 | - | 236 |
| benchmark | 224,357 | +12.18% | 0 | - | 237 |
| intramonth | 213,192 | +6.60% | 0 | - | 235 |
| oracle | 212,992 | +6.50% | 0 | - | 233 |
| intraweek | 212,024 | +6.01% | 40 | 55% | 4,400 |
| random_hold | 209,700 | +4.85% | 12 | 75% | 1,009 |
| snake_abs_exit | 206,081 | +3.04% | 2 | 50% | 345 |
| snake_abs_exit_conv | 205,456 | +2.73% | 2 | 50% | 345 |
| snake_abs | 204,868 | +2.43% | 1 | 100% | 255 |
| snake_abs_conv | 204,701 | +2.35% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 200,471 | +0.24% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,686 | -0.16% | 0 | - | 237 |
| snake_anaconda | 197,658 | -1.17% | 3 | 33% | 374 |
| snake_viper_tick | 197,053 | -1.47% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,060 | -16.97% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,680 (-4.66%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +2,884 | +1.30% |
| random_hold | +1,273 | +0.61% |
| unified | +1,270 | +0.57% |
| benchmark_smallcap | +706 | +0.35% |
| oracle | +649 | +0.31% |
| intramonth | +440 | +0.21% |
| intraweek | +405 | +0.19% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -593 | -0.29% |
| snake_abs_conv | -601 | -0.29% |
| snake_viper_tick | -639 | -0.32% |
| snake_viper_wild | -653 | -0.33% |
| snake_anaconda | -1,046 | -0.53% |
| snake_abs_exit | -1,414 | -0.68% |
| snake_abs_exit_conv | -1,590 | -0.77% |
| gold | -3,370 | -1.99% |

Average per day so far: unified Rs +639, benchmark Rs +609, intramonth Rs +330, oracle Rs +325, intraweek Rs +301, random_hold Rs +242, snake_abs_exit Rs +164, snake_abs_exit_conv Rs +147, snake_abs Rs +128, snake_abs_conv Rs +127, nifty_calls Rs +46, snake_viper_wild Rs +15, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -9, snake_anaconda Rs -67, snake_viper_tick Rs -102, snake_nonews Rs -292, snake Rs -311, gold Rs -849

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.