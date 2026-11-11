# Paper trading report

Updated 2026-11-11 12:43 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 220,578 | +10.29% | 0 | - | 237 |
| unified | 220,479 | +10.24% | 0 | - | 236 |
| snake_abs_exit_conv | 217,573 | +8.79% | 2 | 50% | 345 |
| snake_abs_exit | 216,478 | +8.24% | 2 | 50% | 345 |
| intraweek | 213,881 | +6.94% | 30 | 53% | 3,302 |
| snake_abs | 213,704 | +6.85% | 1 | 100% | 255 |
| snake_abs_conv | 213,552 | +6.78% | 1 | 100% | 255 |
| oracle | 211,975 | +5.99% | 0 | - | 233 |
| intramonth | 211,421 | +5.71% | 0 | - | 235 |
| random_hold | 206,842 | +3.42% | 9 | 67% | 709 |
| snake_viper_wild | 204,908 | +2.45% | 10 | 50% | 1,825 |
| snake_anaconda | 204,392 | +2.20% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_viper_tick | 201,414 | +0.71% | 9 | 44% | 1,639 |
| benchmark_smallcap | 201,367 | +0.68% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 190,046 | -4.98% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,346 (-4.33%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +7,478 | +3.79% |
| snake_viper_tick | +7,337 | +3.78% |
| snake_abs_exit_conv | +5,664 | +2.67% |
| snake_anaconda | +4,926 | +2.47% |
| snake_abs_exit | +4,494 | +2.12% |
| snake_abs_conv | +4,075 | +1.95% |
| snake_abs | +4,057 | +1.94% |
| benchmark_smallcap | +3,195 | +1.61% |
| benchmark | +2,486 | +1.14% |
| oracle | +2,056 | +0.98% |
| random_hold | +1,881 | +0.92% |
| intramonth | +812 | +0.39% |
| unified | +732 | +0.33% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -660 | -0.31% |
| gold | -2,088 | -1.09% |

Average per day so far: benchmark Rs +664, unified Rs +661, snake_abs_exit_conv Rs +628, snake_abs_exit Rs +588, snake_abs_conv Rs +484, snake_abs Rs +473, intraweek Rs +448, oracle Rs +386, intramonth Rs +368, random_hold Rs +221, snake_viper_wild Rs +213, snake_anaconda Rs +169, snake_viper_tick Rs +71, nifty_calls Rs +59, benchmark_smallcap Rs +51, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -321, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.