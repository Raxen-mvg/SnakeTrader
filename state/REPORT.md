# Paper trading report

Updated 2026-11-11 13:22 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 220,630 | +10.31% | 0 | - | 236 |
| benchmark | 220,601 | +10.30% | 0 | - | 237 |
| snake_abs_exit_conv | 218,441 | +9.22% | 2 | 50% | 345 |
| snake_abs_exit | 217,415 | +8.71% | 2 | 50% | 345 |
| snake_abs | 214,786 | +7.39% | 1 | 100% | 255 |
| snake_abs_conv | 214,636 | +7.32% | 1 | 100% | 255 |
| intraweek | 213,574 | +6.79% | 30 | 53% | 3,302 |
| oracle | 212,040 | +6.02% | 0 | - | 233 |
| intramonth | 211,674 | +5.84% | 0 | - | 235 |
| random_hold | 207,095 | +3.55% | 9 | 67% | 709 |
| snake_viper_wild | 205,934 | +2.97% | 10 | 50% | 1,825 |
| snake_anaconda | 205,293 | +2.65% | 3 | 33% | 374 |
| snake_viper_tick | 202,417 | +1.21% | 9 | 44% | 1,639 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| benchmark_smallcap | 201,333 | +0.67% | 0 | - | 237 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| gold | 189,947 | -5.03% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 191,481 (-4.26%).

Profit on 2026-11-11:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_viper_wild | +8,503 | +4.31% |
| snake_viper_tick | +8,340 | +4.30% |
| snake_abs_exit_conv | +6,532 | +3.08% |
| snake_anaconda | +5,827 | +2.92% |
| snake_abs_exit | +5,431 | +2.56% |
| snake_abs_conv | +5,159 | +2.46% |
| snake_abs | +5,140 | +2.45% |
| benchmark_smallcap | +3,161 | +1.59% |
| benchmark | +2,509 | +1.15% |
| random_hold | +2,134 | +1.04% |
| oracle | +2,121 | +1.01% |
| intramonth | +1,064 | +0.51% |
| unified | +883 | +0.40% |
| nifty_calls | +0 | +0.00% |
| intraday | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| statarb | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |
| snake | +0 | +0.00% |
| intraweek | -967 | -0.45% |
| gold | -2,187 | -1.14% |

Average per day so far: unified Rs +665, benchmark Rs +665, snake_abs_exit_conv Rs +659, snake_abs_exit Rs +622, snake_abs_conv Rs +523, snake_abs Rs +510, intraweek Rs +438, oracle Rs +388, intramonth Rs +377, snake_viper_wild Rs +258, random_hold Rs +229, snake_anaconda Rs +204, snake_viper_tick Rs +121, nifty_calls Rs +59, benchmark_smallcap Rs +49, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, gold Rs -324, snake_nonews Rs -382, snake Rs -405

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.