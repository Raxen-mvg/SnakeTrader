# Paper trading report

Updated 2026-11-09 15:30 IST. Model picks as of 2026-11-03. Each strategy started with Rs 200,000 of fake money. Costs are Zerodha's published charges. Goal: +10% by 2026-10-31 (tracked, not traded on).

| Strategy | Equity (Rs) | Return | Closed trades | Win rate | Costs paid (Rs) |
|:---|---:|---:|---:|---:|---:|
| unified | 219,747 | +9.87% | 0 | - | 236 |
| benchmark | 218,092 | +9.05% | 0 | - | 237 |
| intraweek | 214,542 | +7.27% | 30 | 53% | 3,302 |
| snake_abs_exit | 211,984 | +5.99% | 2 | 50% | 308 |
| snake_abs_exit_conv | 211,909 | +5.95% | 2 | 50% | 330 |
| intramonth | 210,609 | +5.30% | 0 | - | 235 |
| oracle | 209,919 | +4.96% | 0 | - | 233 |
| snake_abs | 209,647 | +4.82% | 1 | 100% | 255 |
| snake_abs_conv | 209,477 | +4.74% | 1 | 100% | 255 |
| random_hold | 204,961 | +2.48% | 9 | 67% | 709 |
| nifty_calls | 201,836 | +0.92% | 3 | 33% | 202 |
| intraday | 200,000 | +0.00% | 0 | - | 0 |
| gold_trend | 200,000 | +0.00% | 0 | - | 0 |
| statarb | 200,000 | +0.00% | 0 | - | 0 |
| snake_anaconda | 199,466 | -0.27% | 3 | 33% | 374 |
| benchmark_smallcap | 198,172 | -0.91% | 0 | - | 237 |
| snake_viper_wild | 197,430 | -1.28% | 7 | 57% | 1,332 |
| snake_viper_tick | 194,077 | -2.96% | 6 | 50% | 1,154 |
| gold | 192,133 | -3.93% | 0 | - | 237 |
| snake_nonews | 188,910 | -5.54% | 6 | 17% | 515 |
| snake | 187,855 | -6.07% | 6 | 17% | 518 |

Combined allocator (virtual): Rs 190,363 (-4.82%).

Profit on 2026-11-09:

| Strategy | Rs | % |
|:---|---:|---:|
| snake_abs_conv | +4,250 | +2.07% |
| snake_abs | +4,228 | +2.06% |
| intraweek | +4,179 | +1.99% |
| unified | +4,137 | +1.92% |
| oracle | +4,092 | +1.99% |
| snake_abs_exit | +3,672 | +1.76% |
| snake_anaconda | +3,639 | +1.86% |
| snake_abs_exit_conv | +3,487 | +1.67% |
| intramonth | +3,006 | +1.45% |
| snake_viper_wild | +1,393 | +0.71% |
| benchmark_smallcap | +1,379 | +0.70% |
| snake_viper_tick | +1,367 | +0.71% |
| gold | +1,085 | +0.57% |
| random_hold | +1,054 | +0.52% |
| benchmark | +604 | +0.28% |
| intraday | +0 | +0.00% |
| nifty_calls | +0 | +0.00% |
| snake | +0 | +0.00% |
| statarb | +0 | +0.00% |
| gold_trend | +0 | +0.00% |
| snake_nonews | +0 | +0.00% |

Average per day so far: unified Rs +658, benchmark Rs +603, intraweek Rs +485, snake_abs_exit Rs +444, snake_abs_exit_conv Rs +441, intramonth Rs +354, snake_abs_conv Rs +351, snake_abs Rs +345, oracle Rs +331, random_hold Rs +165, nifty_calls Rs +61, gold_trend Rs +0, intraday Rs +0, statarb Rs +0, snake_anaconda Rs -21, benchmark_smallcap Rs -70, snake_viper_wild Rs -117, gold Rs -262, snake_viper_tick Rs -312, snake_nonews Rs -396, snake Rs -419

Option results are SIMULATED (Black-Scholes on the real Nifty level), not real option prices.