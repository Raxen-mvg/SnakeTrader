# Paper trading report

Updated 2026-11-06 11:31 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 214,732 | +7.37% | 0 | - | 236 |
| benchmark | 214,519 | +7.26% | 0 | - | 237 |
| intraweek | 211,375 | +5.69% | 25 | 48% | 2,757 |
| snake_abs_exit_conv | 209,311 | +4.66% | 1 | 100% | 255 |
| snake_abs_exit | 209,099 | +4.55% | 1 | 100% | 260 |
| intramonth | 206,777 | +3.39% | 0 | - | 235 |
| snake_abs | 206,268 | +3.13% | 1 | 100% | 255 |
| snake_abs_conv | 206,100 | +3.05% | 1 | 100% | 255 |
| oracle | 204,813 | +2.41% | 0 | - | 233 |
| random_hold | 203,192 | +1.60% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 196,657 | -1.67% | 3 | 33% | 374 |
| snake_viper_wild | 195,388 | -2.31% | 3 | 33% | 702 |
| benchmark_smallcap | 194,664 | -2.67% | 0 | - | 237 |
| snake_viper_tick | 192,081 | -3.96% | 2 | 0% | 532 |
| gold | 189,815 | -5.09% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 187,326 (-6.34%).

Profit on 2026-11-06:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,957 | +0.93% |
| benchmark | +750 | +0.35% |
| oracle | +741 | +0.36% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| random_hold | -1,131 | -0.55% |
| intramonth | -1,172 | -0.56% |
| unified | -1,252 | -0.58% |
| benchmark_smallcap | -4,024 | -2.02% |
| gold | -4,406 | -2.27% |
| snake_abs | -5,420 | -2.56% |
| snake_abs_conv | -5,445 | -2.57% |
| snake_abs_exit_conv | -5,493 | -2.56% |
| snake_abs_exit | -5,560 | -2.59% |
| snake_anaconda | -5,822 | -2.88% |
| snake_viper_tick | -9,057 | -4.50% |
| snake_viper_wild | -9,268 | -4.53% |

Average per day so far: unified Rs +508, benchmark Rs +501, intraweek Rs +392, snake_abs_exit_conv Rs +358, snake_abs_exit Rs +350, snake_abs_conv Rs +235, intramonth Rs +234, snake_abs Rs +232, oracle Rs +166, random_hold Rs +110, nifty_calls Rs +63, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -139, benchmark_smallcap Rs -213, snake_viper_wild Rs -220, gold Rs -351, snake_nonews Rs -411, snake Rs -434, snake_viper_tick Rs -440

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.