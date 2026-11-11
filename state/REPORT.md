# Paper trading report

Updated 2026-11-11 09:34 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| benchmark | 221,075 | +10.54% | 0 | - | 237 |
| unified | 220,752 | +10.38% | 0 | - | 236 |
| snake_abs_exit_conv | 215,731 | +7.87% | 2 | 50% | 345 |
| intraweek | 214,811 | +7.41% | 30 | 53% | 3,302 |
| snake_abs_exit | 214,540 | +7.27% | 2 | 50% | 345 |
| snake_abs | 212,915 | +6.46% | 1 | 100% | 255 |
| snake_abs_conv | 212,754 | +6.38% | 1 | 100% | 255 |
| oracle | 211,283 | +5.64% | 0 | - | 233 |
| intramonth | 211,236 | +5.62% | 0 | - | 235 |
| random_hold | 205,940 | +2.97% | 9 | 67% | 709 |
| snake_anaconda | 202,572 | +1.29% | 3 | 33% | 374 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,053 | +0.53% | 0 | - | 237 |
| snake_viper_wild | 200,821 | +0.41% | 10 | 50% | 1,825 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_viper_tick | 197,409 | -1.29% | 9 | 44% | 1,639 |
| gold | 189,404 | -5.30% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,260 (-4.37%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_exit_conv | +3,822 | +1.80% |
| snake_viper_wild | +3,391 | +1.72% |
| snake_viper_tick | +3,333 | +1.72% |
| snake_abs_conv | +3,276 | +1.56% |
| snake_abs | +3,268 | +1.56% |
| snake_anaconda | +3,106 | +1.56% |
| benchmark | +2,983 | +1.37% |
| benchmark_smallcap | +2,881 | +1.45% |
| snake_abs_exit | +2,556 | +1.21% |
| oracle | +1,365 | +0.65% |
| unified | +1,006 | +0.46% |
| random_hold | +980 | +0.48% |
| intramonth | +627 | +0.30% |
| intraweek | +269 | +0.12% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| gold | -2,729 | -1.42% |

Average per day so far: benchmark Rs +680, unified Rs +669, snake_abs_exit_conv Rs +562, snake_abs_exit Rs +519, intraweek Rs +478, snake_abs_conv Rs +455, snake_abs Rs +445, oracle Rs +364, intramonth Rs +362, random_hold Rs +192, snake_anaconda Rs +99, nifty_calls Rs +59, benchmark_smallcap Rs +39, snake_viper_wild Rs +36, statarb Rs +0, gold_trend Rs +0, intraday Rs +0, snake_viper_tick Rs -130, gold Rs -342, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.