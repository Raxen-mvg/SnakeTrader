# Paper trading report

Updated 2026-11-27 15:10 IST. Model picks as of 2026-11-25. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 223,485 | +11.74% | 0 | - | 236 |
| benchmark | 223,432 | +11.72% | 0 | - | 237 |
| oracle | 211,875 | +5.94% | 0 | - | 233 |
| random_hold | 211,115 | +5.56% | 13 | 69% | 1,037 |
| intramonth | 211,065 | +5.53% | 0 | - | 235 |
| intraweek | 207,825 | +3.91% | 40 | 55% | 4,400 |
| snake_abs_exit_conv | 206,355 | +3.18% | 2 | 50% | 345 |
| snake_abs_exit | 204,104 | +2.05% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,569 | +0.78% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 199,450 | -0.28% | 1 | 100% | 255 |
| snake_abs_conv | 199,261 | -0.37% | 1 | 100% | 255 |
| snake_anaconda | 193,006 | -3.50% | 3 | 33% | 374 |
| snake_viper_wild | 192,567 | -3.72% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,296 | -5.35% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 170,959 | -14.52% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,945 (-5.53%).

Profit on 2026-11-27:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +5,958 | +2.97% |
| gold | +4,965 | +2.99% |
| snake_abs_exit | +3,027 | +1.50% |
| random_hold | +2,521 | +1.21% |
| snake_abs | +898 | +0.45% |
| snake_abs_conv | +894 | +0.45% |
| intraweek | +776 | +0.38% |
| benchmark_smallcap | +729 | +0.36% |
| snake_anaconda | +710 | +0.37% |
| intramonth | +532 | +0.25% |
| unified | +407 | +0.18% |
| snake_viper_wild | +362 | +0.19% |
| snake_viper_tick | +355 | +0.19% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -360 | -0.17% |
| benchmark | -2,555 | -1.13% |

Average per day so far: unified Rs +559, benchmark Rs +558, oracle Rs +283, random_hold Rs +265, intramonth Rs +263, intraweek Rs +186, snake_abs_exit_conv Rs +163, snake_abs_exit Rs +105, nifty_calls Rs +44, benchmark_smallcap Rs +41, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -14, snake_abs_conv Rs -19, snake_anaconda Rs -189, snake_viper_wild Rs -219, snake_nonews Rs -277, snake Rs -296, snake_viper_tick Rs -345, gold Rs -691

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.