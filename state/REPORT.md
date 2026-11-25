# Paper trading report

Updated 2026-11-25 10:35 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,084 | +12.54% | 0 | - | 237 |
| unified | 225,073 | +12.54% | 0 | - | 236 |
| intramonth | 212,745 | +6.37% | 0 | - | 235 |
| oracle | 212,148 | +6.07% | 0 | - | 233 |
| random_hold | 209,096 | +4.55% | 12 | 75% | 1,009 |
| intraweek | 207,602 | +3.80% | 40 | 55% | 4,400 |
| snake_abs_exit | 201,875 | +0.94% | 2 | 50% | 345 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit_conv | 201,283 | +0.64% | 2 | 50% | 345 |
| snake_abs | 200,994 | +0.50% | 1 | 100% | 255 |
| snake_abs_conv | 200,804 | +0.40% | 1 | 100% | 255 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| benchmark_smallcap | 199,181 | -0.41% | 0 | - | 237 |
| snake_viper_wild | 195,470 | -2.27% | 16 | 50% | 2,827 |
| snake_anaconda | 193,336 | -3.33% | 3 | 33% | 374 |
| snake_viper_tick | 192,146 | -3.93% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 165,501 | -17.25% | 0 | - | 237 |

Combined allocator (virtual): Rs 189,110 (-5.44%).

Profit on 2026-11-25:

| Strategy | Rs | % |
|:---|---:|---:|
| benchmark | +3,611 | +1.63% |
| unified | +788 | +0.35% |
| random_hold | +669 | +0.32% |
| benchmark_smallcap | +202 | +0.10% |
| intraday | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| intramonth | -7 | -0.00% |
| oracle | -195 | -0.09% |
| gold | -3,929 | -2.32% |
| intraweek | -4,017 | -1.90% |
| snake_abs | -4,466 | -2.17% |
| snake_abs_conv | -4,499 | -2.19% |
| snake_anaconda | -5,367 | -2.70% |
| snake_viper_tick | -5,546 | -2.81% |
| snake_abs_exit | -5,620 | -2.71% |
| snake_viper_wild | -5,655 | -2.81% |
| snake_abs_exit_conv | -5,763 | -2.78% |

Average per day so far: benchmark Rs +627, unified Rs +627, intramonth Rs +319, oracle Rs +304, random_hold Rs +227, intraweek Rs +190, snake_abs_exit Rs +51, nifty_calls Rs +46, snake_abs_exit_conv Rs +35, snake_abs Rs +26, snake_abs_conv Rs +22, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, benchmark_smallcap Rs -23, snake_viper_wild Rs -142, snake_anaconda Rs -190, snake_viper_tick Rs -271, snake_nonews Rs -292, snake Rs -311, gold Rs -862

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.