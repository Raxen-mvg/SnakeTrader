# Paper trading report

Updated 2026-11-26 11:50 IST. Model picks as of 2026-11-23. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 225,734 | +12.87% | 0 | - | 237 |
| unified | 223,166 | +11.58% | 0 | - | 236 |
| oracle | 213,148 | +6.57% | 0 | - | 233 |
| intramonth | 210,390 | +5.20% | 0 | - | 235 |
| random_hold | 209,854 | +4.93% | 13 | 69% | 1,037 |
| intraweek | 208,624 | +4.31% | 40 | 55% | 4,400 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| snake_abs_exit | 201,138 | +0.57% | 2 | 50% | 345 |
| snake_abs_exit_conv | 200,632 | +0.32% | 2 | 50% | 345 |
| benchmark_smallcap | 200,571 | +0.29% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_abs | 198,907 | -0.55% | 1 | 100% | 255 |
| snake_abs_conv | 198,718 | -0.64% | 1 | 100% | 255 |
| snake_anaconda | 192,794 | -3.60% | 3 | 33% | 374 |
| snake_viper_wild | 192,407 | -3.80% | 16 | 50% | 2,827 |
| snake_viper_tick | 189,139 | -5.43% | 15 | 47% | 2,625 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |
| gold | 166,142 | -16.93% | 0 | - | 237 |

Combined allocator (virtual): Rs 188,826 (-5.59%).

Profit on 2026-11-26:

| Strategy | Rs | % |
|:---|---:|---:|
| intraweek | +1,881 | +0.91% |
| benchmark_smallcap | +1,760 | +0.89% |
| gold | +1,545 | +0.94% |
| benchmark | +711 | +0.32% |
| random_hold | +362 | +0.17% |
| nifty_calls | +0 | +0.00% |
| statarb | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| oracle | -647 | -0.30% |
| unified | -934 | -0.42% |
| snake_abs_exit | -1,118 | -0.55% |
| snake_abs | -1,243 | -0.62% |
| snake_abs_conv | -1,254 | -0.63% |
| intramonth | -1,303 | -0.62% |
| snake_abs_exit_conv | -1,344 | -0.67% |
| snake_anaconda | -1,759 | -0.90% |
| snake_viper_tick | -5,038 | -2.60% |
| snake_viper_wild | -5,136 | -2.60% |

Average per day so far: benchmark Rs +628, unified Rs +565, oracle Rs +321, intramonth Rs +253, random_hold Rs +240, intraweek Rs +210, nifty_calls Rs +45, snake_abs_exit Rs +30, snake_abs_exit_conv Rs +17, benchmark_smallcap Rs +15, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_abs Rs -28, snake_abs_conv Rs -34, snake_anaconda Rs -200, snake_viper_wild Rs -230, snake_nonews Rs -284, snake Rs -304, snake_viper_tick Rs -362, gold Rs -826

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.