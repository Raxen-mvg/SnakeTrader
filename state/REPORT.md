# Paper trading report

Updated 2026-11-23 11:38 IST. Model picks as of 2026-11-20. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 224,485 | +12.24% | 0 | - | 236 |
| benchmark | 223,439 | +11.72% | 0 | - | 237 |
| intraweek | 213,063 | +6.53% | 40 | 55% | 4,400 |
| intramonth | 212,564 | +6.28% | 0 | - | 235 |
| oracle | 211,435 | +5.72% | 0 | - | 233 |
| random_hold | 210,181 | +5.09% | 12 | 75% | 1,009 |
| snake_abs_exit | 207,851 | +3.92% | 2 | 50% | 345 |
| snake_abs_exit_conv | 206,793 | +3.40% | 2 | 50% | 345 |
| snake_abs | 205,420 | +2.71% | 1 | 100% | 255 |
| snake_abs_conv | 205,256 | +2.63% | 1 | 100% | 255 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_wild | 201,580 | +0.79% | 16 | 50% | 2,827 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,798 | -0.10% | 0 | - | 237 |
| snake_anaconda | 198,732 | -0.63% | 3 | 33% | 374 |
| snake_viper_tick | 198,139 | -0.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 169,907 | -15.05% | 0 | - | 237 |

Combined allocator (virtual): Rs 190,644 (-4.68%).

Profit on 2026-11-23:

| Strategy | Rs | % |
|:---|---:|---:|
| gold | +1,858 | +1.10% |
| snake_abs_exit_conv | +176 | +0.09% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| intraday | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake_abs | -500 | -0.24% |
| snake_abs_conv | -527 | -0.26% |
| random_hold | -578 | -0.27% |
| snake_abs_exit | -711 | -0.34% |
| oracle | -1,043 | -0.49% |
| benchmark_smallcap | -1,110 | -0.55% |
| snake_anaconda | -1,174 | -0.59% |
| snake_viper_tick | -1,233 | -0.62% |
| snake_viper_wild | -1,249 | -0.62% |
| unified | -1,697 | -0.75% |
| benchmark | -1,698 | -0.75% |
| intramonth | -2,440 | -1.14% |
| intraweek | -2,650 | -1.23% |

Average per day so far: unified Rs +628, benchmark Rs +601, intraweek Rs +335, intramonth Rs +322, oracle Rs +293, random_hold Rs +261, snake_abs_exit Rs +218, snake_abs_exit_conv Rs +189, snake_abs Rs +146, snake_abs_conv Rs +146, snake_viper_wild Rs +51, nifty_calls Rs +47, intraday Rs +0, gold_trend Rs +0, statarb Rs +0, benchmark_smallcap Rs -6, snake_anaconda Rs -37, snake_viper_tick Rs -66, snake_nonews Rs -300, snake Rs -320, gold Rs -772

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.